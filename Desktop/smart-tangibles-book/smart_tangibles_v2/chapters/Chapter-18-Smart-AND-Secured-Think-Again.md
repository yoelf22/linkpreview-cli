### Chapter 18 - Smart AND Secured? Think Again

> ## <Add in context>
>
> <!--https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/--> smart products be made to be secured? Listing attack vectors, and strategies to improve safety, data security, and privacy of smart connected and IoT products.

---

#### [Part 1: Threats]

![A safe combination lock](../images/73dd11_d7c2e70fc657481181fe067d5cc421b7mv2.jpg)

Have the code? Are you the only one?

> _Smart tangibles present enhanced utility, but also increased security, privacy and safety challenges._

How smart tangibles are susceptible to both edges of this blade, is yet to be fully understood, as this stands at the core of differentiation for companies like Apple, and conversely, weaponized - rightfully or not - by governments in their trade wars.

## <!--Table of Contents-->

-   <!--Introduction-->

-   <!--A Brief Introduction: The OSI Model-->

-   <!--Cybersecurity and the OSI Model-->

-   <!--OSI Model Adaptation to IoT-->

-   <!--Notorious Smart Products Cyber Attacks-->

-   <!--Further Reading-->

#### What Seems to be the Trouble?

##### A brief introduction: The OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into several abstract layers, where each serves specific tasks and communicates with its adjacent layers, enabling interoperable network communication across heterogeneous systems.

![ISO 35.100 OSI model diagram](../images/73dd11_f66d8b412bf746a0a274305810e3179amv2.png)

Developed in the late 1970's this model was specifically adapted for client-server computer networks, and proved suitable for the internet era and the reality of widespread personal computers connecting to remote servers, and later to cloud services.

##### Cybersecurity and the OSI Model

The layered structure of the OSI model also serves as a useful framework for understanding cybersecurity risks.

Each layer - from physical hardware to application logic - can be a vector for attack, and mitigation strategies are often layered accordingly, from firewalling at the network level to authentication and encryption at the application layer.

![Common security threats](../images/73dd11_fb36776648c74780b8a699937dc96089mv2.jpg)

##### OSI Model Adaptation to IoT

Internet of Things (IoT) category of products introduces increased complexity as diversified hardware, connectivity, and interaction layers are introduced. This is captured in a slightly different OSI model, showing how devices, network infrastructure, protocols, and visualization tools interact in a layered stack - from raw hardware at the bottom to user-facing applications at the top.

![IoT adaptation of OSI model](../images/73dd11_ab5f118e689f4dabbe6f3314c6851089mv2.jpg)

Crucially, the IoT paradigm necessitates special attention to the hardware layer, as it consists of a vast variability of use cases, and to the application layer, as it is now split between the edge device and the web:

-   Inputs (keyboards and mice give way to other input devices)

-   Outputs (Screens vary wildly or are missing altogether)

-   Energy supply (the default AC mains give way to PoE, batteries, solar...)

-   Sensors and actuators (to some extent, the core purpose of this whole category)

-   Application (split between the device, the cloud, and web interface)

![Expanded layers of OSI for smart tangibles](../images/73dd11_afa31c462bdc4551aad428317fd0a357mv2.png)

Expanded layers of OSI for smart tangibles

##### Smart and (not) Secured: New Structures - New Threats

Looking at smart and IoT products and their version of OSI structure, it becomes clear that unique vulnerabilities emerge at the embodiments of the physical layer, as well as at the extension to the cloud and beyond.

##### Cyber attack vectors examples:

###### Physical Layer:

Tampering, side-channel attacks, sensor spoofing, power supply manipulation (battery draining, over-voltage), environmental sabotage (e.g., heat or vibration).

##### BrickerBot

- **What happened**: Malware known as BrickerBot forcibly disabled (“bricked”) IoT devices. It targeted poorly secured devices at the firmware/hardware level, executing malicious commands that destroyed storage and cut network access - aligning with physical-layer sabotage.

- **Smart elements exploited**:  by exploiting open Telnet services and weak/default credentials

- **Impact**: More than 2 million devices were bricked before it faded away in late 2017.

  ------

  

###### Data Link:

Eavesdropping on unencrypted RF signals (e.g., BLE, Zigbee), MAC spoofing, jamming, replay attacks over local wireless protocols.

##### <u><span>Tesla Keyless Entry App Hijack (2016-2024)</span></u>

![Tesla keyless phone app](../images/73dd11_ea0db35779ca45fa9f62b75935d39866mv2.png)

Tesla keyless phone app. Source: [<u><span>Taslem</span></u>](https://talsem.com/blogs/tesla-tips/understanding-tesla-phone-key-functionality)

-   **What happened**: Security researchers exploited flaws in Tesla’s keyless entry system via the app’s Bluetooth Low Energy (BLE) connection. Using a relay attack, they tricked the vehicle into thinking the authorized phone was nearby and gained unauthorized access.

-   **Smart elements exploited**: Exploit used BLE signal relay to trick the vehicle into unlocking, targeting weaknesses in BLE communication (MAC spoofing, signal replay).

-   **Impact**: Demonstrated how over-the-air convenience features can become physical vulnerabilities.

------



##### <u><span>Flaws in Smart Locks (Various, 2016–2020)</span></u>

![](../images/73dd11_75c53ece672c485eab3f36c9c39c5783mv2.webp)

![](../images/73dd11_0ebf05f2a22746d48d15718ec5e72172mv2.webp)

- **What happened**: Bluetooth sniffing and weak BLE protocols exposed device control, a data link level failure.

- **Smart elements exploited**: BLE communication, cloud management interfaces, firmware updates.

- **Impact**: Erosion of consumer trust in smart home security products.

  ------

  

##### <u><span>Coffee Shop MAC Spoofing</span></u>

-   **What happened**: Owners learned from their Internet Service Provider (ISP) that the spoofers were using the coffee shop’s network to Nmap scans.

-   **Smart elements exploited**: Nmap scanning is a way to look for open ports on a network to gather information about the devices connected to that network.

------



#### Network Layer:

Address spoofing (e.g., IPv6-related), insecure mesh routing, location tracking via IP leaks, exposure from gateway misconfiguration.

------



##### <u><span>VPNFilter Botnet</span></u>

The VPNFilter malware infected over 500,000 home routers and NAS devices around the world. It could intercept and alter network traffic - corrupting packet routing and enabling espionage, with capabilities including address spoofing and network misconfiguration. 

------

​	

#### Transport Layer:

Exploitation of lightweight protocols (e.g., CoAP, MQTT) with limited handshake/authentication, man-in-the-middle (MITM) attacks on UDP-based communication.

##### <u><span>CoAP Amplification Attacks</span></u>

Research has revealed that IoT devices using **CoAP** (a UDP‑based protocol) can be weaponized for reflected DDoS. Attackers send tiny spoofed CoAP requests that trigger amplified responses, overloading targets - an exploit at the transport layer. CoAP-based DDoS attacks can involve tens to hundreds of thousands of compromised IoT devices, drawn from a global pool of over 580,000 known vulnerable endpoints. These attacks generate highly amplified traffic, often reaching volumes of several hundred gigabits per second. The resulting financial impact is comparable to other large-scale DDoS incidents, with potential losses exceeding $200,000 per attack depending on the target and duration.

------



#### Session Layer:

Session hijacking due to weak or absent session management in embedded systems, protocol downgrade attacks.  

------

##### <u><span>FireSheep / DroidSheep</span></u>

Tools like **FireSheep** (for desktop) and **DroidSheep** (on Android) captured session cookies over unsecured Wi‑Fi, allowing attackers to hijack logged-in sessions. This is a textbook session hijacking attack at the session layer. Launched in October 2010, FireSheep was downloaded by approximately **200,000 users worldwide** soon after release. Each person using it could target dozens of devices on the same network in public hotspots.

------



#### Presentation:

Malformed data injection in minimal-format environments, encoding exploits in constrained parsing modules.

------



##### <u><span>Ping of Death</span></u>

Although not strictly IoT-specific, the **ping-of-death** attack sends oversized ICMP packets that overflow buffer-handling routines in networking stacks. It exemplifies malformed-packet attacks - presentation-layer exploits.

------



### Application:

Unauthorized remote control, firmware over-the-air (FOTA) hijacking, malicious update injection, insecure API endpoints, data leakage from sensor payloads.

- It seems that this layer is more vulnerable than others, or at least easier to detect.

- Some Notorious cases:

  ##### <u><span>St. Jude Medical (Abbott) Pacemaker Vulnerabilities (2017)</span></u>


![Pacemaker by Abbott](../images/73dd11_7311678703c24264bfd879b9f98bb9f1mv2.jpg)

Hacked: Pacemaker by Abbott

Security researchers, followed by confirmation from the FDA, revealed that St. Jude’s pacemakers and defibrillators were vulnerable to remote hacking through their wireless telemetry systems. The core vulnerabilities lay in the firmware update mechanisms and remote monitoring features, which exposed insecure APIs and allowed unauthorized remote control. As a result, a major recall was issued, accompanied by a public awareness campaign that affected over 400,000 devices.

------



##### <u><span>Jeep Cherokee Hack by Charlie Miller and Chris Valasek (2015)</span></u>

![Andy Greenberg/WIRED](../images/73dd11_7317e138097c4bfbaa3d9aa83f98b148mv2.webp)

Andy Greenberg/WIRED

Researchers demonstrated that the Jeep Cherokee’s Uconnect system could be exploited to gain full remote access to vehicle functions by targeting application-layer commands. The attack leveraged cellular connectivity, software update channels, and the integration between the infotainment system and critical vehicle controls. In response to the severity of the threat, Fiat Chrysler issued a recall affecting 1.4 million vehicles.

------



##### <u><span>Mirai Botnet Attack on IoT Devices (2016)</span></u>

![screenshot of malware code](../images/73dd11_bc190e604fc449499f893c9e28f068efmv2.jpg)

Screenshot / Tech Crunch

The Mirai botnet attack exploited default login credentials in embedded, internet-facing devices to gain remote control at the application layer — a textbook case of poor security hygiene. These devices, often shipped with hardcoded or unchanged credentials, were easily hijacked and conscripted into a massive botnet. The resulting DDoS attack targeted DNS provider Dyn, disrupting major services like Twitter, Netflix, and Reddit, and also overwhelmed the security blog KrebsOnSecurity with a 620 Gbps traffic surge.

------



##### <u><span>Ring Doorbell Camera Hacks (2019)</span></u>

![Ring doorbell camera](../images/73dd11_af062bdbdf1b4eeb9bdadf598b4d5620mv2.jpg)

Ring doorbell camera / abc news

Attackers exploited weak passwords and the absence of two-factor authentication to hijack video feeds through the Ring app’s cloud APIs. This security gap allowed unauthorized access to users’ home camera systems, sparking public outrage. In response, Ring implemented mandatory 2FA and enhanced its security communication to rebuild user trust.

------



##### <u><span>Nest Thermostat Ransom Attack (2019)</span></u>

![Image / Trend Micro](../images/73dd11_73edc07654d44c53950872d0bb9e5147mv2.jpg)

Image / Trend Micro

Nest users fell victim to credential stuffing attacks, where hackers used previously breached usernames and passwords to gain unauthorized access to their online accounts. This allowed attackers to remotely manipulate smart home devices, such as thermostats. In response, Google urged users to adopt stronger passwords and enabled two-factor authentication to mitigate future risks.

Read about mitigation in Part 2: [<u><span>Smart Product Cyber Threat Mitigation</span></u>](https://www.theroadtlv.com/post/smart-and-secured-think-again-part2)

**_Are you, too, considering security and privacy of your connected product users?..._**

------



#### Read more:

- [<u><span>This is a part of the Hardware is Hard blog series. You can read it online here</span></u>](https://www.theroadtlv.com/post/product-management-for-the-physical-world-series).

- [<u><span>"Smart Tangibles", the book, is due 2026. You can read about it here</span></u>](https://www.theroadtlv.com/post/smart-tangibles).

  ------

  

#### Further reading:

-   [<u><span>Federal Trade Commission</span></u>](https://www.ftc.gov/business-guidance/resources/careful-connections-keeping-internet-things-secure) Careful Connections: Keeping the Internet of Things Secure

-   BrickerBot:

    -   [<u><span>The Daily Swig</span></u>](https://portswigger.net/daily-swig/iot-protocols-are-leaking-data-like-sieves?utm_source=chatgpt.com) IoT protocols are leaking data like sieves

    -   [<u><span>Wikipedia</span></u>](https://en.wikipedia.org/wiki/BrickerBot?utm_source=chatgpt.com) BrickerBot

-   VPN filter botnet

    -   [<u><span>Hacker News</span></u>](https://thehackernews.com/2018/05/vpnfilter-router-hacking.html) Researchers unearth a huge botnet army of 500,000 hacked routers

-   Coffee Shops MAC spoofing:

    -   [<u><span>Stack Exchange</span></u>](https://security.stackexchange.com/questions/261310/identification-of-a-laptop-using-a-spoofed-wifi-mac-address) MAC Address Spoofing: How It Works and How to Protect Yourself

-   Tesla hacks:

    -   [<u><span>The Guardian</span></u>](https://www.theguardian.com/technology/2016/sep/20/tesla-model-s-chinese-hack-remote-control-brakes), Sep 2016: Team of hackers take remote control of Tesla Model S from 12 miles away

    -   [<u><span>Auto Evolution</span></u>](https://www.autoevolution.com/news/researchers-discovered-that-teslas-are-easy-to-steal-despite-adopting-new-keyless-tech-234343.html), May 2024: Researchers Discover That Teslas Are Easy To Steal Despite Adopting New Keyless Tech

    -   [<u><span>The Byte</span></u>](https://futurism.com/the-byte/teslas-stolen-wifi-charging-research), Nov 2024: Teslas can be stolen by hijacking WiFi at charging stations, researchers find

-   St Jude pacemaker hack:

    -   [<u><span>American Heart Association Journals</span></u>](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.118.037331) Nov 2018: Pacemaker Recall Highlights Security Concerns for Implantable Devices

-   Jeep Cherokee Hack:

    -   [<u><span>Wired</span></u>](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/) Jul 2015: Hackers Remotely Kill a Jeep on the Highway - With Me in It

-   Mirai Botnet Attack:

    -   [<u><span>Tech Crunch</span></u>](https://techcrunch.com/2016/10/10/hackers-release-source-code-for-a-powerful-ddos-app-called-mirai/) Oct 2016: Hackers release source code for a powerful DDoS app called Mirai

-   Ring Doorbell Camera Hacks:

    -   [<u><span>ABC News</span></u>](https://abcnews.go.com/US/ring-security-camera-hacks-homeowners-subjected-racial-abuse/story?id=67679790), Dec 2019: Ring security camera hacks see homeowners subjected to racial abuse, ransom demands

-   Flaws in Smart Locks:

    -   [<u><span>The Verge</span></u>](https://www.theverge.com/circuitbreaker/2018/6/13/17461612/tapplock-smart-lock-hack-bluetooth-low-energy) Jul 2018: This fingerprint-verified padlock is extremely easy to hack

    -   [<u><span>BGR</span></u>](https://bgr.com/tech/researchers-find-smart-door-locks-are-easy-to-hack-surprising-no-one/) Aug 2016: Researchers find ‘smart’ door locks are easy to hack, surprising no one

-   Nest Thermostat Ransom Attack:

    -   [<u><span>Trend Micro</span></u>](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/hacker-compromised-family-s-wi-fi-taunted-family-with-thermostat-camera-for-24-hours) Sep 2019: Hacker Compromised Family’s Wi-Fi, Taunted Family With Thermostat, Camera for 24 Hours

-   US ban on Huawei

    -   [<u><span>U.S. Restrictions on Huawei Technologies: National Security, Foreign Policy, and Economic Interests</span></u>](https://www.congress.gov/crs-product/R47012#:~:text=In%20November%202021%2C%20Congress%20acted,from%20the%20Entity%20List%20(S.)

    -   [<u><span>Huawei Says US Sanctions Will Reduce Revenue by $30 Billion</span></u>](https://www.wired.com/story/huawei-says-us-sanctions-reduce-revenue-dollar30-billion/)

    -   [<u><span>UK defence firms warn staff against connecting phones to Chinese-made EVs amid espionage fears</span></u>](https://www.computing.co.uk/news/2025/security/uk-defence-firms-warn-staff-against-connecting-phones-to-chinese-made-evs-amid-espionage-fears)

