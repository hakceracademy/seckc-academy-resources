# Threat Intelligence Training Curriculum

This curriculum provides a structured path through talks and resources related to **Threat Intelligence**.

## Suggested Learning Path

```mermaid
  A[Threat Intelligence Overview]
  C0[Internal Intelligence]
  C1[External Intelligence]
  C2[Contextual Intelligence]
  C3[Third and Fourth Party Risk]
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
- Speaker: Gared -
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=aIKbXo-vIGk
- Key Takeaways:
  - Quick Tool Talk about the wonderful search tool Shodan.

### SecKC Submission
- Speaker: joel kershner -
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=EH8eTD8yL4s
- Key Takeaways:
  - One of the key problems that the blue team faces is lack of timely coordination and communication on threats between organizations. TAXII and OTX are open and free platforms that allow automated threat sharing and dovetail into existing security sensors such as Snort,Suricata, Bro-IDS and others. Also domestic laws have changed allowing organizations to share information with less fear of potential legal liabilities.

### SecKC Submission
- Speaker: John Stauffacher
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=mm8Wlfh5Pcs
- Key Takeaways:
  - Ever think somebody could be a phishing victim, and not even have an email account? Let's walk through a recent case of a little old lady who ultimately lost her house, and a large sum of money in a phishing scam, all without ever having an email account. This talk will touch on a novel threat facing the soft target of the Real Estate industry, but could just as easily exist amongst day traders, or anybody transfering large sums of money, all via email.

### SecKC Submission
- Speaker: Greg Mathes
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=DRbRd8eZIik
- Key Takeaways:
  - The current state of threat intel in the enterprise is in shambles. Management doesn’t know the actual risks to the organization, IR teams are flying blind in incidents, and SOCs have no indication what they should be hunting for. For many years, it was believed that threat actor attribution was both impossible and provided little to no value to most enterprises. But by using threat intel platforms, organizations can provide context to its analysts through the analysis of an actor’s behaviors, motivations, and capabilities. This leads to all stakeholders being better informed of current risks in addition to better predicting the risks they will encounter tomorrow.

### SecKC Submission
- Speaker: James Liggett
- Recorded: 2019
- Key Takeaways:
  - "It is highly probably that you might have FancyBears or Cozybears are attempting to access your networks" A quick presentation reviews major changes in international environments that have led to some major changes in Russian cyber operations. This talk is based on an aggregation of open source data and open threat intelligence but is designed to help break out some of the APTs and make intelligence more understandable and more usable. After reviewing APT's tactics, techniques and procedures, some remediation strategies are presented for individuals and organizations, with the goal of stopping bad threat intelligence.

### SecKC Submission
- Speaker: James Liggett
- Recorded: 2019
- Key Takeaways:
  - We here threat data all the time about Advanced Persistent Threats, and there are so many funny names and numbers (APT10, CozyBear). It is hard to keep track and use any of the data in a meaningful way. This speech, created from aggregated open source data, details about APTs. What are APTs, how do they view the battlespace, what enablers and tools do they use. And some defense and response strategies.

### SecKC Submission
- Speaker: Ginsberg5150
- Recorded: 2019
- Key Takeaways:
  - A look into the modern OSINT scene. Start with basic search preferences and move into more advanced searches. Dont care if you learn anything. I still think its fun. :-)

### SecKC Submission
- Speaker: Alex Kloster
- Recorded: 2020
- Key Takeaways:
  - Extreme Privacy, and what it takes to disappear from the internet, combining disinformation and OSINT

### SecKC Submission
- Speaker: Jimmy the Red
- Recorded: 2020
- Key Takeaways:
  - Looking at creating and offensive use of Deepfake (image, video, speech). I will discuss disinformation, deepfakes, targets, growth, and how we, and truth, are fucked

### SecKC Submission
- Speaker: Josh Rickard
- Recorded: 2020
- Key Takeaways:
  - MITRE ATT&CK provides security teams with a framework to assist with detecting attacks and the techniques used by malicious actors. Currently, using MITRE ATT&CK generally entails an intensely manual processes since MITRE ATT&CK is strictly text-based. In order to build detections or create defense strategies using ATT&CK, security practitioners must have deep technical knowledge of attack phases (Tactics) as well as experience (and knowledge) in specific procedures (Techniques) used by attackers. Security teams can use ATT&CK to build defensive objectives (strategies) but lack the ability to make these objectives actionable. During this talk, I will discuss two open-source projects (pyattck & PSAttck) I have released to assist with making MITRE ATT&CK actionable. These open-source tools are focused towards security practitioners and enables them by providing additional information as it relates to MITRE ATT&CK techniques, actors, and tools. By enriching MITRE ATT&CK using multiple open-source projects, security professionals have access to potential commands, detections and queries related to attacker techniques as well as known targets, operations, and additional tools used by actors not included within ATT&CK's dataset. You also have access to additional names and data points which enables offensive teams when selecting tools and C2 infrastructure. Having access to this additional context, security professionals can now search their logs for potential commands related to a specific technique, retrieve potential detections & queries to assist with making MITRE ATT&CK actionable. By providing this additional (actionable) context, security teams can begin using ATT&CK on day one.

### SecKC Submission
- Speaker: Daniel Shimkus - d@n in discord server
- Recorded: 2022
- Key Takeaways:
  - A brief, 10 minute-ish news roundup of stories I found interesting in the months of December 2021-January 2022. Stories that will be discussed include recent iPhone vulnerabilities, nation-state cyber activity, and recent tech mergers and how they affect the industry.

### SecKC Submission
- Speaker: Aaron J. Scantlin
- Recorded: 2022
- Key Takeaways:
  - Some people use social media. Some people sign NDAs. Some people are dumb. When all three of these intersect, you get a lightning talk on OSINT.

### SecKC Submission
- Speaker: Aaron Smith
- Recorded: 2025
- Watch: https:///www.youtube.com/watch?v=qVKeN-t8nj4
- Key Takeaways:
  - Presenting on pre-encryption activity by rhysida. Could also speak a little on a novel pre-encryption technique seen from Akira as well basically my article here https://www.at-bay.com/threat-research/rhysida-evading-detection/

### SecKC Submission
- Speaker: Wayne Crowder
- Watch: https:///www.youtube.com/watch?v=iN83ZPs1cT0

### SecKC Submission
- Speaker: Tom Heffron

## Milestones and Self check

- I can write PIRs and derive three IOCs from one advisory.
- I can track a CVE across vendors and suggest detection ideas.
- I can brief stakeholders on one trend with suggested mitigations.

## Supplemental Learning and Adjacent Topics

- Translate one public advisory into IOCs and detection ideas
- Practice PIRs writing and source validation
- Correlate CVEs with vendor advisories

