# Risk Assessment Training Curriculum

This curriculum provides a structured path through talks and resources related to **Risk Assessment**.

## Suggested Learning Path

```mermaid
  A[Risk Assessment Overview]
  C0[Penetration Testing]
  C1[Vulnerability Scanning]
  C2[Social Engineering]
  C3[DAST]
  A --> C0
  C0 --> C1
  C1 --> C2
  C2 --> C3
  C3 --> Z[Apply Knowledge]
```

## How to Use This Curriculum

1. Watch the talks in the suggested order when present. If no order is present, skim titles and start with fundamentals.
2. Take notes. Capture core concepts, critical vocabulary, tools, and practical takeaways.
3. Practice. Recreate demos in a lab. Build a small asset to apply the idea.
4. Review. Summarize key points and write one paragraph on how to apply them at work.
5. Connect. Compare notes with peers, then refine your personal checklist.

## Available Talks

### SecKC Submission
- Speaker: Dave Hull --
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=mJIce8H6eJ8
- Key Takeaways:
  - This talk is about red teaming, why you should add it to your security program, what it is and what it isn't. The speaker will share some highlights and lessons learned from his own experiences gained during "force on force" engagements in Microsoft's Office 365 and share some practical insights for trying to make it work in other organizations.

### SecKC Submission
- Speaker: Ryan Preston
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=iWDyzwcSZSs
- Key Takeaways:
  - The second in a series of talks explaining and demonstrating modern attacks on Active Directory. During this presentation I will further cover Bloodhound and various other tools used in the reconnaissance phase of pentesting Active Directory.

### SecKC Submission
- Speaker: Ryan Moore
- Recorded: 2018
- Key Takeaways:
  - A demo and overview of the tools needed to start hacking servers (aka popping shells) and an introduction to some of the better, free hacking lab resources out there, including HackTheBox, VulnHub, and ImmersiveLabs.

### SecKC Submission
- Speaker: Daniel Lawson
- Recorded: 2018
- Watch: https:///www.youtube.com/watch?v=1ZqJBLaPuz4
- Key Takeaways:
  - I’ve been developing a tool for the past year that makes handling large scopes far easier. It uses a database backend for managing discovery, network mapping, domain mapping, ports, services, and credentials. It allows you to quickly find the low hanging fruit and focus on the deep diving that turns up the juicy vulnerabilities.

### SecKC Submission
- Speaker: Aaron Gulick (v01dnet)
- Recorded: 2019
- Key Takeaways:
  - Pentesting of Corperate Systems: Statistics & Findings

### SecKC Submission
- Speaker: Joel Kershner
- Recorded: 2019
- Key Takeaways:
  - Geographic information systems is a way to corre

### SecKC Submission
- Speaker: Dispareo, Mark Bayley
- Recorded: 2019
- Key Takeaways:
  - For those who are new to InfoSec or Pentesting this will teach them how to install Kali on a VM. This will be required for for the following month's "Hack your First Box"

### SecKC Submission
- Speaker: Dispareo (Mark Bayley), SysAaron
- Recorded: 2019
- Watch: https:///www.youtube.com/watch?v=OtwvBpJ6vjI
- Key Takeaways:
  - This will be a walk through workshop of a boot2root VM. Most people learn by doing, so this will help them run the commands themselves and become familiar with the actual commands and scripting part. This will take a VM downloaded from VulnHub, and walk through on the big projector how to hack into a box, beginning from Nmap and ending with cat root.txt. This will be a very easy box, and the participants will follow along and run commands themselves.

### SecKC Submission
- Speaker: awsmhacks
- Recorded: 2019
- Key Takeaways:
  - It's been about a year since the Attacking AD series and I wanted to provide some updates on what Attacking AD looks like in 2019. Then OF COURSE I'll have some new attacks I'm betting you aren't prepared for. Let's pwn some sh!t

### SecKC Submission
- Speaker: Andy Nelson
- Recorded: 2019
- Watch: https:///www.youtube.com/watch?v=EhdOzIkukwk
- Key Takeaways:
  - Software engineers commonly test our code as part of the development lifecycle. Part of that testing includes testing the inputs of our applications. However, most of the time our inputs are a set of pseudo random inputs. Fuzz testing takes input testing to another level by removing the well-defined input and replacing it with truly random inputs. Targeting an asset with random inputs allow the attacker to find new attack vectors. Creating a bug by finding memory related errors, race conditions or any undefined behavior, gives an attacker the ability to exploit the system in ways you might not have thought of. In this talk, I will give an overview of fuzz testing, how it can be used to find vulnerabilities and demonstrate how it is done. If you want to learn how to do some security vulnerability testing, this talk is for you.

### A Primer on USB HID Attacks
- Key Takeaways:
  - HID puts the Universal in “USB.” HID attack vectors have been explored for years and are a useful tool for on-site penetration tests and for testing access to USB enabled embedded and IoT devices. Kris will give a brief explanation of the method, point to some of his favorite tools, and provide a demonstration of basic attacks that make use of USB HID gadgets.

### Attacking Active D - A Hacking Series
- Key Takeaways:
  - This will be the first in a series of talks explaining and demonstrating modern attacks on Active Directory. During this presentation I will further cover Powershell Empire, picking up after davehull's presentation, and its functionality to a pentester. This will set the stage for the next few talks where we will learn about crackmapexec, responder, ntlmrelayx, Inveigh, and Bloodhound. Finally we will explore new tools that put all this together like DeathStar, AngryPuppy, Dogspawn, and GoFetch that automate domain takeovers.

## Milestones and Self check

- I can convert scan findings into tickets with risk ranks.
- I can scope a pentest with rules of engagement and success criteria.
- I can outline a phishing campaign and success metrics.

## Supplemental Learning and Adjacent Topics

- Run a basic web scan in a lab and triage the findings
- Draft a lightweight pentest rules of engagement note
- Outline a phishing simulation plan

