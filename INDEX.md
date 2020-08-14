# OWASP Threat Model Cookbook Index

Global view of example systems, with their overall description, that are represented in this project.


## BLANK
A generic model with generic name that doesn't represent a particular system. Useful to introduce a methodology without leading people into a particular architecture.

[![BLANK Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/BLANK/BLANK.py.svg "BLANK Flow Diagram")](./Flow%20Diagram/BLANK)

[![BLANK Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/BLANK.plantuml.svg "BLANK Attack Tree")](./Attack%20Tree/BLANK.plantuml)

[![BLANK Template](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Template/BLANK-draw.io.onepager.xml.svg "BLANK Template")](./Template/BLANK)



## app-y-ness
A mobile application to manage tenants of an apartment complex and sells various products that the landlord brews and grows. Tenants can use the mobile app to pay rent, buy products and receive fire n' surf alerts.

[![app-y-ness Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/app-y-ness/app-y-ness.py.svg "app-y-ness Flow Diagram")](./Flow%20Diagram/app-y-ness)


## cryptocurrency-wallet
A desktop application based on Electron that handle cryptocurrency operations with the Blockchain. The model also includes related components such as a Cryptocurrency Exchange web site and a trading bot in python.

[![cryptocurrency-wallet Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/cryptocurrency-wallet/cryptowallet.vsdx.svg "cryptocurrency-wallet Flow Diagram")](./Flow%20Diagram/cryptocurrency-wallet)

[![cryptocurrency-wallet Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/cryptowallet.plantuml.svg "cryptocurrency-wallet Attack Tree")](./Attack%20Tree/cryptowallet.plantuml)


## generic-cms
A simple web content management system with generic name components. Has a web server, a database and a CDN.

[![generic-cms Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/generic-cms/generic-cms.py.svg "generic-cms Flow Diagram")](./Flow%20Diagram/generic-cms)

[![generic-cms Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/generic-cms.plantuml.svg "generic-cms Attack Tree")](./Attack%20Tree/generic-cms.plantuml)


## iot-device
An internet of things device such as a lightbulb that is controlled with a mobile app, a python script or a cloud API. A website provides the cloud integration user interface and the IoT device exposes a local network API.

[![iot-device Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/iot-device/iot-device.vsdx.svg "iot-device Flow Diagram")](./Flow%20Diagram/iot-device)

[![iot-device Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/iot-device/iot-device.part1.plantuml.svg "iot-device Attack Tree")](./Attack%20Tree/iot-device)

[![iot-device Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/iot-device/iot-device.part2.plantuml.svg "iot-device Attack Tree")](./Attack%20Tree/iot-device)


## jetscout
A rental scooter equipped with a jet engine and tracking system that relies on IoT smart components. It receives voice commands and has a seat with a smart scale on it to know when the rider is sitting or has felt. It tracks health data from smart sensors and store it into the cloud for insurance purpose (totally not for reselling it). It has also a remote API that can control its jet engine.

[![jetscout Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/jetscout/alt5-jetscout.jpg "jetscout Flow Diagram")](./Flow%20Diagram/jetscout)

[![jetscout Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/jetscout/alt11-jetscout.jpg "jetscout Flow Diagram")](./Flow%20Diagram/jetscout)

[![jetscout Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/jetscout/jetscout.jpg "jetscout Attack Tree")](./Attack%20Tree/jetscout)


## online-battleroyale-game
A multiplayer video game client and server that has a lobby for matchmaking and provide statistics about the matches and players. Player accounts are stored in a central database and Customer Support staff can access it for moderation purposes.

[![online-battleroyale-game Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/online-battleroyale-game/onlinegame.py.svg "online-battleroyale-game Flow Diagram")](./Flow%20Diagram/online-battleroyale-game)

[![online-battleroyale-game Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/online-battleroyale-game/onlinegame.plantuml.svg "online-battleroyale-game Attack Tree")](./Attack%20Tree/online-battleroyale-game)


## physicalsafe
A textbook example of a physical safe that a bad actor wants to open.

[![physicalsafe Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/physicalsafe.plantuml.svg "physicalsafe Attack Tree")](./Attack%20Tree/physicalsafe.plantuml)


## renting-car-startup
A startup ecosystem based on mobile applications and APIs that manage peer to peer car rentals. A customer can use a mobile app to unlock and start the car. The owner of the car has its own mobile app to manage rentals. It has AI linked to its APIs and supports augmented reality features. The APIs also allows to change radio stations which are stored in the cloud on a flat file for legacy reasons.

[![renting-car-startup Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/renting-car-startup/rentingcar.py.svg "renting-car-startup Flow Diagram")](./Flow%20Diagram/renting-car-startup)

[![renting-car-startup Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/rentingcar.plantuml.svg "renting-car-startup Attack Tree")](./Attack%20Tree/rentingcar.plantuml)


## scouter
A shared scooter company (competitor of jetscout) that uses a vending machine to distribute tickets for renting their fleet of shared electric scooters. They use drones to track customers.

[![scouter Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/scouter/scouter.jpg "scouter Flow Diagram")](./Flow%20Diagram/scouter)

[![scouter Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/scouter/scouter.jpg "scouter Attack Tree")](./Attack%20Tree/scouter)


## sokify
An online hipster store platform that allows people to see pictures of socks on social medias and buy them. Its main components are a mobile application and an API, which connect to a legacy inventory management system that still sends fax.

[![sokify Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/sokify/alt1-sokify.jpg "sokify Flow Diagram")](./Flow%20Diagram/sokify)

[![sokify Attack Tree](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Attack%20Tree/sokify/sokify.plantuml.svg "sokify Attack Tree")](./Attack%20Tree/sokify)


## webapp-threat-dragon
A sample model of a web application, with a queue-decoupled background process. The OWASP Threat Dragon PDF example contains a report with details about elements with a description of threats and theirs mitigation.

[![webapp-threat-dragon Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/Flow%20Diagram/webapp-threat-dragon/webapp-threat-dragon.json.png "webapp-threat-dragon Flow Diagram")](./Flow%20Diagram/webapp-threat-dragon)


## 3-Tier-Web-App
This fictitious application exposes a Web UI on the internet and has a Web API and Database hosted on a public cloud provider. This is a full example using the IriusRisk threat modeling tool from ContinuumSecurity.

[![3-Tier-Web-App Flow Diagram](https://raw.githubusercontent.com/OWASP/threat-model-cookbook/master/IriusRisk/3-Tier-Web-App/Dataflow%20Diagram.png "3-Tier-Web-App Flow Diagram")](./IriusRisk/3-Tier-Web-App)

