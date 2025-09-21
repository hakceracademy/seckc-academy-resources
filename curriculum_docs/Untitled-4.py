#!/usr/bin/env python3
# file: rebucket_transcripts.py
import argparse, csv, logging, os, shutil, sys, tempfile
from pathlib import Path

import pandas as pd

def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")

def slugify(s: str) -> str:
    s = (s or "").strip()
    s = s.replace("\\", "/")
    # Keep simple ASCII-ish slugs
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch in (" ", "_", "-", "/"):
            out.append("-")
        elif ch in (">",):
            out.append("/")
        else:
            out.append("-")
    slug = "".join(out)
    # collapse repeats and trim
    while "--" in slug:
        slug = slug.replace("--", "-")
    slug = slug.strip("-/ ")
    # enforce safe default
    return slug or "uncategorized"

def split_category(cat: str) -> Path:
    """
    Turn "Parent > Child" into Path("Parent/Child"), safely slugged.
    """
    raw = (cat or "").strip()
    if ">" in raw:
        parts = [slugify(p.strip()) for p in raw.split(">") if p.strip()]
        return Path(*[p for p in parts if p])
    return Path(slugify(raw)) if raw else Path("uncategorized")

def is_subpath(p: Path, root: Path) -> bool:
    try:
        p.resolve().relative_to(root.resolve())
        return True
    except Exception:
        return False

def move_file(src: Path, dst: Path, dry_run: bool) -> None:
    if dry_run:
        logging.info("[dry-run] move %s -> %s", src, dst)
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    logging.info("moved %s -> %s", src, dst)

def atomic_write_csv(df: pd.DataFrame, out_path: Path) -> None:
    tmp_fd, tmp_name = tempfile.mkstemp(prefix=".tmp_rebucket_", suffix=".csv", dir=str(out_path.parent))
    os.close(tmp_fd)
    tmp = Path(tmp_name)
    try:
        df.to_csv(tmp, index=False)
        tmp.replace(out_path)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except Exception:
                pass

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="webapp/seckc_academy_resources", help="Root directory of resources")
    ap.add_argument("--csv", default="SecKC_Academy_Source_Data.csv", help="CSV filename under --root")
    ap.add_argument("--transcripts_dir", default="transcripts", help="Transcripts dir under --root")
    ap.add_argument("--category_col", default="category", help="CSV column that holds category label")
    ap.add_argument("--path_col", default="transcript_path", help="CSV column that holds transcript path")
    ap.add_argument("--dry_run", action="store_true", help="Do not move or write, only log actions")
    ap.add_argument("--verbose", action="store_true", help="Verbose logging")
    args = ap.parse_args()

    setup_logging(args.verbose)

    root = Path(args.root).resolve()
    csv_path = (root / args.csv).resolve()
    troot = (root / args.transcripts_dir).resolve()

    if not csv_path.exists():
        logging.error("CSV not found: %s", csv_path)
        sys.exit(1)
    if not troot.exists():
        logging.error("Transcripts dir not found: %s", troot)
        sys.exit(1)

    df = pd.read_csv(csv_path, dtype=str).fillna("")
    for col in (args.category_col, args.path_col):
        if col not in df.columns:
            logging.error("CSV missing required column: %s", col)
            sys.exit(1)

    moves = 0
    updates = 0

    for idx, row in df.iterrows():
        category = str(row.get(args.category_col, "")).strip()
        rel_path = str(row.get(args.path_col, "")).strip()

        if not rel_path:
            continue

        # Resolve existing transcript path
        # Accept either absolute or relative; normalize into Path under troot.
        src = Path(rel_path)
        if not src.is_absolute():
            src = (root / rel_path).resolve()

        if not src.exists():
            # try assuming it is relative to transcripts dir
            alt = (troot / Path(rel_path).name).resolve()
            if alt.exists():
                src = alt
            else:
                logging.warning("transcript missing, skipping row %s: %s", idx, rel_path)
                continue

        if not is_subpath(src, root):
            logging.warning("refusing to move file outside root: %s", src)
            continue

        # Build destination under transcripts/<category...>/<filename>
        cat_dir = split_category(category)
        dst = (troot / cat_dir / src.name).resolve()

        # If already in the right place, just normalize the CSV path
        if src == dst:
            new_rel = dst.relative_to(root)
            if rel_path != str(new_rel):
                df.at[idx, args.path_col] = str(new_rel).replace("\\", "/")
                updates += 1
            continue

        # Move and update CSV path
        move_file(src, dst, dry_run=args.dry_run)
        moves += 1
        new_rel = dst.relative_to(root)
        df.at[idx, args.path_col] = str(new_rel).replace("\\", "/")
        updates += 1

    if args.dry_run:
        logging.info("[dry-run] planned moves: %d, planned CSV updates: %d", moves, updates)
        return

    atomic_write_csv(df, csv_path)
    logging.info("done. moved: %d, csv rows updated: %d", moves, updates)

if __name__ == "__main__":
    main()
