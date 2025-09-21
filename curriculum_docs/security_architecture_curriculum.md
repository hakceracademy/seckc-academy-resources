# Security Architecture Training Curriculum

This curriculum provides a structured path through talks and resources related to **Security Architecture**.

## Suggested Learning Path

```mermaid
  A[Security Architecture Overview]
  C0[Network Design]
  C1[Identity and Access]
  C2[Cloud Security]
  C3[Endpoint Hygiene]
  C4[Cryptography]
  C5[Container Security]
  A --> C0
  C0 --> C1
  C1 --> C2
  C2 --> C3
  C3 --> C4
  C4 --> C5
  C5 --> Z[Apply Knowledge]
```

## How to Use This Curriculum

1. Watch the talks in the suggested order when present. If no order is present, skim titles and start with fundamentals.
2. Take notes. Capture core concepts, critical vocabulary, tools, and practical takeaways.
3. Practice. Recreate demos in a lab. Build a small asset to apply the idea.
4. Review. Summarize key points and write one paragraph on how to apply them at work.
5. Connect. Compare notes with peers, then refine your personal checklist.

## Available Talks

### SecKC Submission
- Speaker: Adam Smith ;) AKA Adam E. AKA twizler tw13zlr
- Recorded: 2015
- Key Takeaways:
  - A nifty tool to tunnel all of your network traffic via a remote SSH connection. The install is on your machine and no root access on the remote machine is required.

### SecKC Submission
- Speaker: Caleb Christopher
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=30TLngOVwqQ
- Key Takeaways:
  - TL:DR: Learn what SPF, DKIM, and DMARC records are, what they do, why you should use them for EVERY domain you administer, and how to get started. In this talk, Caleb Christopher (cchristopher on Slack, if you couldn't guess) will discuss how to specify who is authorized to send email on behalf of a domain, how to provide for domain-based (not user-based) email non-repudiation, and how to specify for other mail servers what to do with messages that don't line up with your proof-of-identity requirements. Slide deck will be made public.

### SecKC Submission
- Speaker: rixon
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=sbjsg9H74DM
- Key Takeaways:
  - This month's tool talk will be on netcat, a simple but versatile network tool.

### SecKC Submission
- Speaker: Matty McFatty
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=sbN5Bz3v-uA
- Key Takeaways:
  - Qubes OS sounds cool, but it's a little intimidating to use it as your day-to-day OS. Let me show you around Qubes OS a little and take away some of the mystery. I'll show you the basics of using Qubes OS and discuss some of the pros and cons.

### SecKC Submission
- Speaker: Gared Seats
- Recorded: 2018
- Key Takeaways:
  - Have you ever wanted a lab or development setup, so you can try things, test things, figure out problems or just have a great time? This session covers the basics or setting up a great lab environment without breaking the bank. We know budgets are tight for businesses or home. This session will show you how to set up a quality build that will last a while for you. We’ll also go over some software recommendations and scenarios for how to use and deploy this system. (Bonus – an actual mobile lab system will be at the session so you can see it in person.)

### SecKC Submission
- Speaker: Ryan
- Recorded: 2018
- Watch: https:///www.youtube.com/watch?v=sdC31u3VUrk
- Key Takeaways:
  - Access management services are providing attackers insta-pwn capabilities. I'll demonstrate how devices meant to protect the network actually provide an avenue of attack. Apologies ahead of time, you might have to go back in to work tonight.

### SecKC Submission
- Speaker: Aaron J. Scantlin
- Recorded: 2018
- Key Takeaways:
  - Shared resources are ubiquitous today, primarily in the form of WiFi networks, public computers and cloud resources. While the latter is outside the scope of this talk, Aaron is going to discuss the chain of trust in shared computing and show you just how much risk is accepted when you utilize networks and computers that are outside your control.

### SecKC Submission
- Speaker: Caleb Christopher
- Recorded: 2019
- Key Takeaways:
  - -----BEGIN TALK DESCRIPTION----- MIIBBgKBgDI/ranPo8MDfguQfSzqg7mtNlUJLLBK7tlVALyk42agbLTSFcZbs9Yw t3nSe9yNzZB9ZVrL3O9GXkEb6xvj3dqrog+wWOeFCqNV7BuJNYYC/ef4vlnUFQdwyswbd7d198qjWBZ7MiZRXxX8qKRln+osTvsDYOMZk93k0cGZgyuJAoGAHkgFohgAnH93kDPjN4sHaT9WsmZ4ailbMtcnWuLizTRJ2sdGjNrpuwT1R+x1nlYHOeDUSOu6De0kQJX+HZuQCoha6THsdgcV297krN22FwsDZ1PItXLIr5oC7zcNQaDyAJOIv6BCufHQ0IR+L9b9esniMbF8yV0d7EVAaBJiyRk= -----END TALK DESCRIPTION-----

### SecKC Submission
- Speaker: Aaron Goldblatt
- Recorded: 2019
- Watch: https:///www.youtube.com/watch?v=HWuXfK_YjGA
- Key Takeaways:
  - Encrypting data in transit has to happen, even inside your perimeter. Using SSL/TLS certificates without massive cost overruns or outages requires managing this infrastructure. Here's how to get started.

### SecKC Submission
- Speaker: Sebastian McMillan
- Recorded: 2019
- Key Takeaways:
  - This is how to use the power of many open source projects to take hardware security to an entire new level. Leveraging the Linux kernel loading capabilities of Coreboot and the compartmentalization of Qubes OS, we move the root of trust from the OS to the firmware.

### SecKC Submission
- Speaker: Nate Johnson (aka. Caprico)
- Recorded: 2019
- Key Takeaways:
  - This talk is an overview of Docker, where you will discover what it is, its implementation and how it can be incorporated into security. Nate Johnson guides us through an introduction to Docker complete with a demonstration of how he found and assisted in taking down a botnet that utilized Docker. Walk away from this talk knowing how to effectively and securely use Docker to augment your security toolbox.

### SecKC Submission
- Speaker: Arden Meyer
- Recorded: 2019
- Key Takeaways:
  - A "choose your own adventure" style talk beginning with a high-level understanding of Steganography, drilling down into media options, then techniques, ending with an example of encoding & decoding messages.

### SecKC Submission
- Speaker: Aaron Crawford
- Recorded: 2019
- Watch: https:///www.youtube.com/watch?v=8inHqSeOdps
- Key Takeaways:
  - Too many vendors and influencers wax endlessly about Artificial Intelligence but what exactly is it? How does it apply to security? How can you get started doing your own research and applications? Discover from one of the leading independent researchers in the field how to quick start your path into artificial intelligence for security, complete with hands on examples. Go beyond the marketing buzzwords and word salad to learn how Artificial Intelligence can be used in security and how you can get started for under $100.

### SecKC Submission
- Speaker: Brent Stone
- Recorded: 2019
- Key Takeaways:
  - Brent will follow up his 2019 DEFCON talk "Reverse Engineering 17+ Cars in Under 10 Minutes" with more details about how to create tools that automate analysis of Industrial Control System (ICS) networks.

### SecKC - March 2020
- Speaker: @Brent Stone
- Recorded: 2020 03
- Watch: https:///www.youtube.com/watch?v=01v3e0wBGUQ

### SecKC - February 2021
- Speaker: @Brent Stone
- Recorded: 2021 02
- Watch: https:///www.youtube.com/watch?v=JkKerHFYHZo

### SecKC Submission
- Speaker: Sebastian McMillan
- Recorded: 2021
- Key Takeaways:
  - Chromebooks, love them or hate them, are becoming more and more relevant. Going from low end laptops that only have a web browser to high end machines with double digits of ram and massive storage running a full-fledged desktop OS, we'll be talking about the security model of Chromebooks and why they are highly locked down, but yet also quite possibly the most open mainstream platform.

### SecKC Submission
- Speaker: Brandon Winchester
- Recorded: 2021
- Key Takeaways:
  - Gitlab, or any automated pipeline process is 1/2 of the continuous integration pipeline. Despite everyone's loathing of tech buzz words, there's some gold in understanding and leaning on other people's lessons learned about CI/CD. Ill cover Docker as an introduction for those squeamish about it, and demonstrate how to leverage some process in practicing builds and delivery using pipeline automation to convince you why you'd want to do it.

### SecKC Submission
- Speaker: Joel kershner
- Recorded: 2021
- Key Takeaways:
  - A home lab is a crucial aspect of doing anything in technology. Cost to performance and energy efficiency is a key topic and so is automation and containers. Metal as a service (MAAS) is able to rapid deploy linux on physical hardware and automagically build out applications at scale with JUJU. Do you have a pile of raspberry pi’s then put them to work!

### SecKC Submission
- Speaker: hevnsnt
- Recorded: 2021
- Watch: https:///www.youtube.com/watch?v=7ExGddG-rmg
- Key Takeaways:
  - SecKC was pretty early in the Crypto Currency game with the introduction of SecKCoin (RIP). SecKCoin was a great introduction into how cryptocurrency works. This is an update to that talk, focused around what crypto currency is, how it works, and a brief introduction into the world of NFTs. WHY ARE PEOPLE BUYING JIFS FOR MILLIONS OF DOLLARS!? Well come and find out.

### SecKC Submission
- Speaker: Badge Pirates - Carl Fugate
- Recorded: 2021
- Key Takeaways:
  - So you have seen all the cool electronic badges and SAO's and are interested in making your own? This series of talks is for you. The process is broken up so you can focus on each step independently on your journey to having your first PCB's manufactured. The series begins with creating the artwork and understanding the limitations and constraints of designing art using a PCB. We will use all open source tools in this series including Inkscape (Vector Artwork Generation), SVG2Shenzen (Inkscape plugin for easily generating KiCAD footprints) and KiCAD as our Electronics Design Automation (EDA) platform.

### SecKC - June 2022
- Speaker: @Brent Stone
- Recorded: 2022 06

### SecKC Submission
- Speaker: Daniel Charboneau
- Recorded: 2022
- Watch: https:///www.youtube.com/watch?v=7FLkezsySgU
- Key Takeaways:
  - I will be speaking on the evolution of TEE's from Specific purpose to General compute. What the implications and future of the technology is... Soon General Compute TEE's will be in your phone, car, router, etc.

### SecKC - March 2023
- Speaker: @Brent Stone
- Recorded: 2023 03

### SecKC Submission
- Speaker: Jim McKibben
- Recorded: 2025
- Key Takeaways:
  - How to go about planning and building a Homelab that is responsive and in most cases already aware of external threats. This covers initial high over view build plan, but dives however deep into using an Open Source tool called CrowdSec to parse events and connect the parts of an existing network / home-lab to this perimeter maintainer. We will cover some lessons learned in getting this to work as well as integrating local and external CrowdSec installs under one main Engine to have a Multi-Server setup.

### SecKC Submission
- Speaker: Jack Sippel
- Recorded: 2025
- Key Takeaways:
  - TBD once we decide to do this

### SecKC Submission
- Speaker: Kevin Bennet

### SecKC Submission
- Speaker: Patrick Burns

### SecKC Submission
- Speaker: Joel Kershner

### SecKC Submission
- Speaker: Adam Ossenford
- Watch: https:///www.youtube.com/watch?v=FRHFHqkQikM

## Milestones and Self check

- I can whiteboard a zero trust flow for an app to a service.
- I can identify three high risk data flows and propose controls.
- I can evaluate a secret management approach and document tradeoffs.

## Supplemental Learning and Adjacent Topics

- Draw a zero trust reference for a small SaaS
- Map a cloud VPC baseline with guardrails
- Review key management patterns for app secrets

