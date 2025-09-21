# Security Operations Training Curriculum

This curriculum provides a structured path through talks and resources related to **Security Operations**.

## Suggested Learning Path

```mermaid
  A[Security Operations Overview]
  C0[Incident Response]
  C1[Threat Hunting]
  C2[SOC]
  C3[Forensics]
  C4[Vulnerability Management]
  C5[SIEM and SOAR]
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
- Speaker: Dave Hull
- Recorded: 2015
- Watch: https:///www.youtube.com/watch?v=cQmsT9D0kKI
- Key Takeaways:
  - Four years ago, I left the midwest for high adventure in the Pacific Northwest
  - casting my lot with the developer of the world's most popular operating system, or rather a devices and services company. Wait no, make that a "cloud first, mobile first" company based in Redmond, WA. My gig was IR at scale -- 100s of thousands of globally distributed systems. This trolk will be an honest look at Kansa -- an open source, PowerShell-based incident response framework, developed with the goal of executing IR at scale. We'll look at some data collected and analyzed for red-team engagements and see where Kansa shines and I'll talk about where it falls down, some work-arounds and I may briefly mention commercial solutions in both positive and negative lights.

### SecKC Submission
- Speaker: Blake Bryant or
- Recorded: 2015
- Watch: https:///www.youtube.com/watch?v=v8tEh-3gkxs
- Key Takeaways:
  - Based on over two years of thesis research resulting in the implementation of a “kill chain” framework within SIEM software. A novel “kill chain” model was developed, loosely based upon the Lockheed Martin Cyber Kill-Chain, and implemented within a commercial SIEM system through modifications to the existing SIEM database. These modifications resulted in a new log ontology capable of normalizing security sensor data in accordance with modern threat research. New SIEM correlation rules were developed using the novel log ontology and compared to existing vendor recommended correlation rules using the default normalization model. The novel log ontology produced promising results indicating improved detection rates, more descriptive security alarms, a lower number of false positives, and simplified SIEM correlation rule construction. These improvements were assessed to provide improved visibility and more efficient investigation processes to security analysts resulting in a reduction in the mean time required to detect , escalate, and resolve security incidents.

### SecKC Submission
- Speaker: Thomas Gardner
- Recorded: 2016
- Key Takeaways:
  - Curious about reverse engineering but still working on your Assembly skills? Have you ever received spam or phishing emails and wanted to know how to properly examine them? Wanna know what took out the Ukrainian power grid? Look no further! We'll go over what tools to use to analyze malicious documents and how to interpret analyses already out on the web. We'll also go over pertinent indicators to share with other teams/people Targeted at those interested in Digital Forensics and Incident Response

### SecKC Submission
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=Oj03Nzk4KiU
- Key Takeaways:
  - Placeholder... Technical walkthrough of how ransomware does its thing.

### SecKC Submission
- Speaker: Bill Swearingen
- Recorded: 2016
- Key Takeaways:
  - A walk-through of how-to (and why you should) to connect and use the SecKC VPN

### SecKC Submission
- Recorded: 2016
- Key Takeaways:
  - Do you have 15 minutes? Have you heard of Ansible? This talk will quickly cover the basics of Ansible configuration management system. Installation, directory structure, Ansible galaxy, vault, roles, templates, modules, ad-hoc cli, and perhaps even shell.

### SecKC Submission
- Speaker: Joe Piggeé Sr.
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=f6GJZCBDyyA
- Key Takeaways:
  - Security Information and Event Management What a SIEM IS NOT!!!! What is a SIEM? Why Do I need a SIEM,? SIEM - For the SMB-SOHO-DEVOPS-Enterprise-And even the @home!!!! In summary, from a business perspective share best practices for implementing SIEM technology, and highlighting some of the differences between many of the big players in the SIEM arena. The take aways will be: - Understanding of what SIEM is - What a SIEM can do - What to expect of a SIEM - How to get more for less, via a SIEM - Avoid COMMON pitfalls with the deployment and maintenance of a SIEM - Getting return on unseen value of the SIEM - The Power of Business Intelligence - Provide resources, information and discovery for insight for help and training - Common Use-Cases for compliance, and security awareness - SIEM deployment walk-thru, from start to finish

### SecKC Submission
- Speaker: Steven Dietz
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=WffQdXp22Ek
- Key Takeaways:
  - Demonstrate five core security tool utilities useful for both daily and specific Infosec use. These are commands or switches within almost every Windows install useful for forensics, protection or encryption. The utilities allow you to wipe drives, copy files with all metadata (MAC) content or file/folder inspection

### SecKC Submission
- Speaker: Matty McFatty
- Recorded: 2016
- Watch: https:///www.youtube.com/watch?v=hY1UahLSLAQ
- Key Takeaways:
  - I discovered an ATM skimmer while traveling in Bali. Of course, I had to take it home and take it apart.

### SecKC Submission
- Speaker: RSAXVC
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=-ee1N4MRhJE
- Key Takeaways:
  - I think one of my neighbors must have gotten a drone for christmas, because one recently up to my bedroom window. I found the same model at a hobby shop, bought one, took it home, backdoored it, documented it, cracked it, found how it escaped Mirai but just barely, and designed a $3 ESP8266-based microcontroller interdiction system to prevent video recording near my house.

### SecKC Submission
- Speaker: Joel Kershner
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=sjukFKiz_EI
- Key Takeaways:
  - Open Source Security Information Manager OSSIM is an open source SIEM which combines open source threat intel and best of breed open IDS and network along with Vulnerability assessment tools and asset management tools. Like most security focused linux distributions when you peel back the cool web gui you find layers upon layers of duct tape and baling wire but if you have a small or medium sized network its extremly useful.

### SecKC Submission
- Speaker: Aaron J. Scantlin
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=CpvPwO3LkdA
- Key Takeaways:
  - Think home network security monitoring is a costly and time-consuming effort? Think again! With about $50 and a few hours of your time, you can log network events just like your favorite three-letter agencies. This talk will go over the required hardware and software, go through the setup and configuration process process, and provide some starting ideas for events to alert on (with template scripts).

### SecKC Submission
- Speaker: rsaxvc
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=j9PoE-Ry3Vs
- Key Takeaways:
  - I'll show off a simple tool fr BLE hacking on the go, and own a few willing participants devices.

### SecKC Submission
- Speaker: Archwisp / Bryan C. Geraghty
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=js323csYbts
- Key Takeaways:
  - You saw Cory's 101 talk on reversing (https://www.youtube.com/watch?v=Fr7xC8_FHgs) and you wanted to learn more. So you picked up some books poked around a bit at some CTFs but still don't really understand what's going on. Well, that's about to change. In this talk, we're going to walk through how to solve the FLARE-ON CTF: IgniteMe reverse engineering challenge from September of 2017. Ultimately, you will learn the solution to the challenge, but the real goal of this talk is to teach you the background, techniques, and tools you would need to know in order to solve a challenge like this. This is going to be a really deep technical dive but we'll make sure to have lots of fun along the way!

### SecKC Submission
- Speaker: Dusty Evanoff
- Recorded: 2017
- Watch: https:///www.youtube.com/watch?v=aJuVp9ptFew
- Key Takeaways:
  - This is an introduction to Mimikatz for the uninitiated. I'll show you how to steal Windows passwords (and other secrets) like a boss as well as how to bypass common defenses. Then, we'll discuss how to minimize the damage caused by credential theft, and talk about how you can detect it on your own network.

### SecKC Submission
- Speaker: Alex Lauerman
- Recorded: 2018
- Key Takeaways:
  - If you scan for it, it will be there. Identifying vulnerabilities at scale is easy. We'll go through some of the techniques and challenges of finding vulnerabilities at scale. This talk should be useful to those tasked with protecting large networks. Attendees will also gain perspective on how easy it is for a real attackers, and why we are losing at securing the internet from large scale attacks like the mirai botnet.

### SecKC Submission
- Speaker: Sampson Chandler
- Recorded: 2018
- Key Takeaways:
  - A brief look into how cellphones talk to each other, how this can be attacked, how to protect yourself, and why this technology should be improved.

### SecKC Submission
- Speaker: Ryan Preston
- Recorded: 2018
- Watch: https:///www.youtube.com/watch?v=CgTfw_2W0yM
- Key Takeaways:
  - I'm inside your network. I've weaponized the(every) browser. If you use the internet, I've got you. There is a universal feature that lets me (and a lot of other people) inside your network without you ever knowing. You won't see it, you can't stop it. Harvesting credit cards and passwords was only the beginning, now I've got code execution _on_the_inside_.

### SecKC Submission
- Speaker: Katie Bratman and Shane Fonyi
- Recorded: 2018
- Key Takeaways:
  - As technology advances, more and more opportunities to interact with the digital world via the internet arises. Many people who use these devices, that are apart of the Internet of Things, do not often question the confidentiality or integrity of the devices they purchase. In a lot of cases, getting your internet-connected toaster compromised might only lead to burnt toast and minor scaring, but the same cannot be said for some other devices. Since the internet is for porn, it is only natural for devices to be created to support that philosophy. Our research into a couple of these devices, dubbed The Internet of Dongs, surfaced some interesting and scary results. Join us as we take a deep dive into the vast world of IoD and learn just how personal these devices can be. We will show just how simple it is to locate and compromise a bluetooth-connected device and how insecure your data could be.

### SecKC Submission
- Speaker: rixon
- Recorded: 2018
- Watch: https:///www.youtube.com/watch?v=Gbf2XjreVzU
- Key Takeaways:
  - This will be an introduction to car hacking.

### SecKC Submission
- Speaker: Matt Clemons / Cisco
- Recorded: 2018
- Watch: https:///www.youtube.com/watch?v=fRhtaYAQRtE
- Key Takeaways:
  - Labbing up some popular attack tools and defending against them. Gathering indicators of compromise and making them actionable.

### SecKC Submission
- Speaker: Parker Crook, Ben Holder
- Recorded: 2018
- Key Takeaways:
  - Never responded to email. removing

### SecKC Submission
- Speaker: Aaron Crawford
- Recorded: 2018
- Key Takeaways:
  - Are you taking every possible precaution to ensure that your security assessments don’t result in any damage? Have you ever had someone not trust you after learning what you do for a living? Can your actions during a security assessment cause lasting damage to a client? Does your job in security cause mental health troubles? If you’ve ever wondered about these and many more Aaron Crawford sits down and shares over twenty-three years of experience in the security industry with things you’ve never considered before. Addressing preplanning legal pitfalls all the way to mental aftercare that can easily be applied and should become a standard practice. Learn how to carefully plan a security assessment with several key steps that most professionals overlook to ensure the best care for your clients and yourself. These are the items that no one has ever discussed, until now. Prepare to step away with a more thorough and impactful tool-set for your security assessments. This brief talk and discussion will cover: 1. What can go wrong 2. What aren’t you considering 3. Client fallout from security assessment impacts 4. More than just vulnerabilities 5. Repercussions of a security assessment 6. What is trust? 7. Regaining trust of everyone and everything 8. How to make checklists 9. Getting legal help 10. Aftercare and how to take care of yourself 11. Summary and resources This talk can be 10 minutes or up to 45/50 minutes.

### SecKC Submission
- Speaker: Eric Evans aka ESquared
- Recorded: 2018
- Watch: https:///www.youtube.com/watch?v=tyV1N5fPpXY
- Key Takeaways:
  - How to install, configure, and maintain a local DNS server on your home/lab network. Using a raspberry pi and a little bit of knowledge to block ads, stop malware, and be aware of what is going on in your home network. Requires 0 DNS experience and just a little time.

### SecKC Submission
- Speaker: John Stauffacher
- Recorded: 2018
- Key Takeaways:
  - So...about that large cache of uhh data you have there: An interesting tale from the Trace3 IR team involving Google, a Filemaker Pro Database, a Mac Mini that hadn't been turned off in over 4yrs, a plastic surgeon, an insurance company and a whole treasure trove of Workers Compensation data ( which is *not* considered PHI - go figure). This is a fun one in that it is a prime example of everything you don't want to have happen with data that you are entrusted with. In this scenario our client was notified by one of it's clients that certain customers of theirs had found data pertaining to their workers compensation cases through a simple Google search. What started out as a simple investigation into "how did it get there" lead our team down some interesting rabbit holes, and oddball conversations with our clients legal team -- who just happened to be running point on this investigation. Share in our collective adventure as we set forth to educate, enlighten and hopefully amuse you.

### SecKC Submission
- Speaker: Bill Swearingen
- Recorded: 2018
- Key Takeaways:
  - PULL OVER! No it is a cardigan, but thanks for noticing! After getting a nasty speeding ticket, OG SecKC HA/KC/ER hevnsnt dedicated a month reverse engineering speed measurement devices and developed homebrew countermeasures. Come learn how police RF (X, K, KA) and Laser speed detection systems work and how to implement your own homebrew jamming countermeasures on the cheap, essentially making your vehicle invisible to law enforcement. This SecKC talk is bringing the hacking back, and is illegal in all 50 states. You better be able to think fast to keep up with this talk and prepare to get home in record time.

### SecKC Submission
- Speaker: Sampson Chandler
- Recorded: 2019
- Key Takeaways:
  - I will discuss basics of Incident Response including developing policies, plans, and general tips.

### SecKC Submission
- Speaker: awsmhacks
- Recorded: 2019
- Key Takeaways:
  - It has been a while since I covered attacks and techniques used to pwn Active Directory environments and I've got some new tricks up my sleeve (under my hood?). We'll briefly reminisce the attack theory, check out new features added to some of my favorite tools, AND, since you've all fixed the vulns i was using to steal passwords(see parts 1-4 on my github), take a look at the new-new i'm using to gobble up yo account credentials. Come see what the bad guys are up to in this follow-up and find out what happened to part 5 :)

### SecKC Submission
- Speaker: rsaxvc
- Recorded: 2019
- Key Takeaways:
  - Learn to locate ethereum mining rigs and other embedded devices using Shodan.io and shared SSH host public keys

### SecKC - February 2020
- Speaker: Matt Danda
- Recorded: 2020 02
- Watch: https:///www.youtube.com/watch?v=jkl5NJrRKgA

### SecKC - February 2020
- Speaker: Joel
- Recorded: 2020 02
- Watch: https:///www.youtube.com/watch?v=TIDas-CKpeU

### SecKC - February 2020
- Speaker: Aaron
- Recorded: 2020 02
- Watch: https:///www.youtube.com/watch?v=la1azEPMhbQ

### SecKC - March 2020
- Speaker: @ericsguillen
- Recorded: 2020 03
- Watch: https:///www.youtube.com/watch?v=01v3e0wBGUQ

### SecKC Submission
- Speaker: Eric Guillen aka geoda
- Recorded: 2020
- Key Takeaways:
  - (Description in progress...) Every year, SANS puts on a Holiday Hack Challenge around the holidays. This year was titled KringleCon 2: Turtle Doves. This was the first time I decided to actually sit down and give it a go. I will go over lessons learned from completing this challenge, the effort put in, and what it takes to get a Super Honorable Mention. There may be some spoilers from the challenge, so be warned. But know that all official answers have already been posted.

### SecKC - February 2021
- Speaker: Matt Danda
- Recorded: 2021 02
- Watch: https:///www.youtube.com/watch?v=jkl5NJrRKgA

### SecKC - February 2021
- Speaker: @asmodianx2000
- Recorded: 2021 02
- Watch: https:///www.youtube.com/watch?v=TIDas-CKpeU

### SecKC - February 2021
- Speaker: @sysaaron
- Recorded: 2021 02
- Watch: https:///www.youtube.com/watch?v=JkKerHFYHZo

### SecKC Submission
- Speaker: Justin Enloe
- Recorded: 2021
- Watch: https:///www.youtube.com/watch?v=UHObICrvpr0
- Key Takeaways:
  - Demonstrating the vulnerabilities of weak passwords, and human error, to gain network access and escalate privileges.

### SecKC - June 2022
- Speaker: Matt Danda
- Recorded: 2022 06
- Watch: https:///www.youtube.com/watch?v=jkl5NJrRKgA

### SecKC - June 2022
- Speaker: @asmodianx2000
- Recorded: 2022 06
- Watch: https:///www.youtube.com/watch?v=TIDas-CKpeU

### SecKC - June 2022
- Speaker: @sysaaron
- Recorded: 2022 06

### SecKC Submission
- Speaker: Dispareo and the KU Health System Cyber Team
- Recorded: 2022
- Key Takeaways:
  - This will be a one-hour capture the flag.

### SecKC Submission
- Speaker: MrARM
- Recorded: 2022
- Key Takeaways:
  - So, you have a flipper or want a flipper? I will show you some useful tricks you can do with it in addition to making the most of what it can do. I'll be teaching you how to install custom firmware to unlock the full potential of the flipper, as well as showing some ways that the flipper makes cloning devices trivial in comparison to prior hardware.

### SecKC - March 2023
- Speaker: @geoda
- Recorded: 2023 03

### SecKC - March 2023
- Speaker: Matt Danda
- Recorded: 2023 03
- Watch: https:///www.youtube.com/watch?v=jkl5NJrRKgA

### SecKC - March 2023
- Speaker: @asmodianx2000
- Recorded: 2023 03
- Watch: https:///www.youtube.com/watch?v=TIDas-CKpeU

### SecKC - March 2023
- Speaker: @sysaaron
- Recorded: 2023 03

### SecKC Submission
- Speaker: Zoe/Foehammer/Echo_419 (All the same person/speaker)
- Recorded: 2023
- Key Takeaways:
  - This talk will discuss the ONCD Background/Context, the different steps in the badge CTF, the different challenges, and overall lessons learned.

### SecKC Submission
- Speaker: John Tuckner
- Recorded: 2023
- Key Takeaways:
  - For the past year, I've been capturing information on the automations security operations teams are implementing in their organizations. In this presentation, I'll be sharing the results along with specific case studies.

### SecKC Submission
- Speaker: Isaiah
- Recorded: 2024
- Watch: https:///www.youtube.com/watch?v=cz0RIJQTKmc
- Key Takeaways:
  - Do you ever wonder what's running on the "security" cameras you can buy for $20 on Amazon? Check this shit out.

### SecKC Submission
- Speaker: Matt Elliott
- Recorded: 2024
- Key Takeaways:
  - Process injection and adjacent techniques have been evolving for more than a decade and are widely implemented in various malwares. Let's discuss the fundamentals and observe how it can help an attacker blend in... or stick out.

### SecKC Submission
- Speaker: Tom Pohl
- Recorded: 2025
- Key Takeaways:
  - In today's cybersecurity landscape, even the smallest misconfigurations can have catastrophic consequences. Join us in this deep dive into the world of Microsoft Certificate Authority (CA) misconfigurations, where we'll expose the hidden vulnerabilities that can turn a single compromised user account into a full domain admin nightmare. This session will guide you through real-world case studies and technical demonstrations, revealing how attackers exploit these common mistakes to gather sensitive network and user data, escalate privileges, and gain persistent access. You'll learn how these oversights occur, the tactics hackers use to exploit them, and most importantly, how your blue team can detect and prevent such attacks. Arm yourself with the knowledge to fortify your CA infrastructure and protect your organization.

### RunAs: A Double-Edged Sword
- Key Takeaways:
  - RunAs is a command that's been around since Windows 2000. It allows users and applications to run under a different user. Windows users have been using this for years to install software and run programs. But did you know that RunAs could be used maliciously? That attackers can use this to enumerate and attack your network? Join us as we dive into analyzing the RunAs command and how bad guys can use it to attack your network. We will discuss our research on how a simple command can be easy to use but difficult to eliminate.

### SecKC Submission
- Speaker: Leif Dreizler
- Watch: https:///www.youtube.com/watch?v=qgJlS9g0Opk

### SecKC Submission
- Speaker: Dusty Evanoff
- Watch: https:///www.youtube.com/watch?v=Qkw3caHTAek

### SecKC Submission
- Speaker: Aaron Crawford
- Watch: https:///www.youtube.com/watch?v=4S1oUno85Bs

### SecKC Submission
- Speaker: Cory Kennedy
- Watch: https:///www.youtube.com/watch?v=Fr7xC8_FHgs

### SecKC Submission
- Speaker: Chris Lamb

### SecKC Submission
- Speaker: Tyler Schunk
- Watch: https:///www.youtube.com/watch?v=O72bq7i8DII

### you can post about me if you want
- Key Takeaways:
  - This is a brief (10-15 minute) talk that revolves around a particularly interesting incident response event that occurred at the University of Missouri toward the end of May. We will discuss how the event began, the IR process, the resolution, and the major takeaways from the whole event.

## Milestones and Self check

- I can run through a detect triage contain recover exercise for one scenario.
- I can map two detections to ATT&CK and validate signal to noise.
- I can draft an incident comms template for exec, legal, and IT.

## Supplemental Learning and Adjacent Topics

- Walk through NIST 800 61 phases on a mock incident
- Create a quick SIEM rule to detection validation checklist
- Practice triage with public CTI reports

