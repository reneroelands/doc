# FINETECH preparation

## Abbreviations

| Abbreviation | Definition | Remarks |
|--------------|------------|---------|
| MES | Manufacturing Execution System | [ wiki](https://en.wikipedia.org/wiki/Manufacturing_execution_system)
| SCADA | Supervisory control and data acquisition | [wiki](https://en.wikipedia.org/wiki/SCADA) |
| REST | Representational state transfer | [wiki](https://en.wikipedia.org/wiki/Representational_state_transfer) |
| gPRS | Google Remote Procedure Call | [wiki](https://en.wikipedia.org/wiki/GRPC) |
| MQTT | MQ Telemetry Transport | [wiki](https://en.wikipedia.org/wiki/MQTT) |
| ATAM | e Architecture Tradeoff Analysis Method | [link](https://resources.sei.cmu.edu/asset_files/TechnicalReport/2000_005_001_13706.pdf) |
| CAFCR | Customer Objectives, Application, Functional, Conceptual and Realization | [link](https://www.gaudisite.nl/ArchitecturalReasoningBook.pdf) |
| CMMI | Capability Maturity Model Integration | [wiki](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration) |
|VCSEL | Vertical Cavity Surface Emitting Laser | [wike](https://en.wikipedia.org/wiki/Vertical-cavity_surface-emitting_laser) |
| SECS | SEMI Equipment Communications Standard / GEM Generic Equipment Model | [wiki](https://en.wikipedia.org/wiki/SECS/GEM)
| MOEMS | Micro-opto-mechanical systems | [wiki](https://en.wikipedia.org/wiki/Microoptoelectromechanical_systems) |
| IGBT | Insulated-gate bipolar transistor | [wiki](https://en.wikipedia.org/wiki/Insulated-gate_bipolar_transistor) |

| Concept | Definition | Remarks |
|---|----------|---------|
| Eutectic bonding | wafer bonding technique | [wiki](https://en.wikipedia.org/wiki/Eutectic_bonding) |
## People

| ID | Role | Department | Company |
|----|------|---|----|
[Arnoud de Geus](https://intranet.sioux.eu/nl/tijdlijn/arnoud-de-geus/133/profile) | Director New Business Development | General management | Sioux Group  |
[Tatiana Ungureanu](https://intranet.sioux.eu/nl/tijdlijn/tatiana-ungureanu/306/profile) | Project manager | Project Management | STN |
[Klaus Gruber](https://intranet.sioux.eu/nl/tijdlijn/klaus-gruber/938/profile) | Development Manager | 	Development Manager | STG |
| [Jan Hendriks](https://intranet.sioux.eu/nl/tijdlijn/jan-hendriks/776/profile) | 	Senior Software Architect | System Control Software | STN |
| [Joost van Riel](https://intranet.sioux.eu/nl/tijdlijn/joost-riel-van/353/profile) | Software Architect | System Control Software | STN |
| [Rene Roelands](https://intranet.sioux.eu/nl/tijdlijn/rene-roelands/1669/profile) | 	System architect | Mechatronic System Design | STN |
| Carlotta Baumann | General manager | | Finetech GmbH​ |
| [Matthäus Banach](https://www.linkedin.com/in/matth%C3%A4us-banach-29193ab7/) | Development manager / CTO | |  Finetech GmbH​ |
| Marcus Bolzhauser | consultant | what kind ?| [Bolzhauser AG?](https://bolzhauser.de/) |
| Michael Koch | SW department manager | SW department  | Finetech GmbH​ |
| [Dr. Sylvio Schneider](https://www.linkedin.com/in/dr-sylvio-schneider-a86289bb/) | SW team lead | SW department | Finetech GmbH​ |
| Michael Steinberg | Sales director | - | Finetech GmbH​ |
| [Sascha Lohse](https://www.linkedin.com/in/sascha-lohse-2a51779a/) | Head of product management | Product managment | Finetech GmbH​ |
| Georg Pauls | - | - | Finetech GmbH​ |
| Hartmut Grasnick | Aristotech? | - | Finetech GmbH​ |
| [Martin Rogge](https://www.linkedin.com/in/martin-rogge-62996681/) | Product manager | Product management | Finetech GmbH​ |



## Introduction
Finetech is the leading equipment manufacturer for sub-micron die bonding & advanced SMD rework.

[Finetech](https://www.finetech.de/)

Brief information about Finetech company

### General company information

- Turnover: €25 million, number of employees: 180
- Products:
    - Machines for micro assembly
    - Manual, semi and fully automatic die bonders for highly accurate placement, assembly and packaging

- Applications:
    - Bonding of laser bars, diodes, VCSEL/PD assembly

    - Multi-stage construction of opto-electromechanical assemblies (MEMS/MOEMS) for products, e.g. B. the communications industry and medical technology.

### Software development overview

- approx. 6 employees

- Tasks: Day-to-day business, such as bugs and improvements, as well as integration and development projects

- Programming of the machine control and operation in Delphi

- Microcontroller programming in C++

- Hardware integration using manufacturer DLLs

- Interface programming: CAN bus, EtherCat, Ethernet, USB3

From [email](https://siouxeu.sharepoint.com/sites/FinetechLead/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FFinetechLead%2FShared%20Documents%2FProject%20Request%20Info%2FFW%20Finetech%20%2D%20Info%2Emsg&parent=%2Fsites%2FFinetechLead%2FShared%20Documents%2FProject%20Request%20Info)

## Project-relevant object of consideration

Software, such as structure, architecture, development process, development environment
- The systems consist of hardware for execution and a Windows computer with complex control software

- The control software is written in Delphi as a monolith and comprises approx. 7 million LoC for the user interface and the entire control process (1.1 million LoC developed in-house)

- Versioning of the software is done with SVN

- The interfaces to the hardware are CAN bus and Ethernet

- The systems are self-sufficient and cannot be controlled externally or send data to a central infrastructure; MK: TeamViewer; MBo: Updates on demand, controlled from outside

- There is no integration into current production control systems (SCADA, MES); MK: ProcessExchange, MES approaches available and SECS/GEM

The software is characterized by the fact that machine functions can be parameterized by the customer and processes (which are implemented in the competition through programming) can be adapted by the customer or changed with reasonable effort.

#### Software Delphi:

- Can only work with the Windows operating system (Linux compiler possible in principle)
- Use of REST and gRPC possible
- HTTPS can be used with a certificate
- Use of MQTT (interface for IoT) does not work (planned according to the roadmap)
- Repeated uncertainty about the future of the language
- Finding new employees is very difficult

## Goals (consulting phase)

### Overall project goal

The existing solution should be checked for the following requirements:
- The machines must be able to be integrated into networked environments.
- Machine2machine communication must be possible.
- For maintenance reasons, it is necessary to be able to access the machines from the outside or, in the case of predictive maintenance, continuously monitor data.
- Machine can be addressed via tablet.
- The solutions must work worldwide.
- New services must be feasible with the resulting data.
- The architecture must be sustainable. This also applies to the corresponding programming languages.
- The productivity of software development must be "state of the art".

and create solutions with recommendations for action. (Effort estimation, cost planning, resource planning, risk assessment, schedule & probability of success)

### sub-goals

- Current and potential analysis of the software and software development.
- Concrete statement as to which approach to optimizing the software/development (and possibly related areas) is suggested and how you could support the improvement.
- Proposal of concrete quick wins improvements (visible improvement) that have immediate benefits and can be delivered quickly after project start.
- Specific statement on the potential for increasing overall productivity as part of a consulting project (duration 3 months).
- Best practice in mechanical engineering (high product complexity, high variety, high development effort.
- Concrete statement on the work packages that are required to achieve the indicated goals and sub-goals (roadmap) including estimate of effort / required skills.
- Presentation of the procedure in the event of a possible replacement of the current software.

### Other Project Requirements

-  Min. 1 consultant who develops the analysis and the procedural concept should also accompany the implementation in a follow-up project so that we can get an idea of ​​the people involved from the first contact.
- Experience in medium-sized companies, mechanical engineering, special machine construction (high complexity, small quantities, high number of variants)

## Product

### principle 

What is the principle?
- half mirror

### Product line R&D
__FINEPLACER__ lambda 2
- modular
- flexible
- field upgradable
- programmable
- all systems have same software 
- specific to photonics?

__FINEPLACER__ sigma
- lab systeem with larger working area

__FINEPLACER__ pico 2
- modular
- field configurable
- IPM software
- 

__FINEPLACER__ femto 2
- fully-automated die bonder with a placement accuracy of 0.3 µm @ 3 sigma that offers unrivaled flexibility for prototyping & production environments.

__FINEPLACER__ femto _blu_
= automated micro assembly cell with a placement accuracy of 2.0 µm @ 3 Sigma and ultra-low bonding force capability for photonic applications.

### product line High Yield
__FINEPLACER__ femto 2 / blu

__FINEXT6003__ 
- fully automatic large area production die bonder with true multi-chip, multi placement capability for high volume manufacturing.

### product line SMD rework

__FINEPLACER__ pico rs
- enhanced hot air rework station for assembly and rework of all types of SMD components.

__FINEPLACER__ core _plus_
- universal hot air rework station for electronic components and assemblies


## Customers
- Fraunhofer
- Ferdinand Braun Institut
- Ultra Communications, Inc.
- BMK Electronic Services
- High Frequency Technology, Hamburg University of Technology

## Presentation Sioux

[link sharepoint](https://siouxeu.sharepoint.com/:p:/r/sites/FinetechLead/_layouts/15/Doc.aspx?sourcedoc=%7BBED5E0FE-E736-4606-94A3-FAD8AD8BDCFD%7D&file=Projectrequest%20Finetech.pptx&action=edit&mobileredirect=true)

### Comments
slide 5:
- what is Sioux policy on size of customers? 
- what are the products that are interesting to Sioux?

slide 6:
- What does "Bad changeability" mean?
- What is wrong with the electronics?
- What is Elmo EtherCAT?

Slide 7:
- consultancy phase is more SW architect work, why is a system architect required?
- How much experience does Sioux have with code refactoring?

## Quotations & estimations

[link sharepoint](https://siouxeu.sharepoint.com/sites/FinetechLead/Shared%20Documents/Forms/AllItems.aspx?OR=Teams%2DHL&CT=1663569597187&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMjA3MzEwMTAwNSIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&id=%2Fsites%2FFinetechLead%2FShared%20Documents%2FQuotation%20and%20estimations&viewid=621fc9f7%2Dc3d9%2D4621%2D815d%2Ddb47c0b7bb31)

General:
- Who made this quotation?
- Which specific product?


Page 4: 
- Are the "key stakeholders" identified?
- We are not using a formal approach to architectural assessment but we refer to them anyway?
- What is "model extraction for software legacy"? Reverse engineering?

In the quotation it is already stated that an evolutionary approach is preferred. Why invest time in a revolutionary approach?

Page 5:
- really? the deliverable is 90k powerpoint presentation? 
    The outcome of step 1 is a presentation.

Page 6:
- which interview templates are available?
- is an NDA in place?
- is the assessent of the SW processes something we normally do?

Page 7:
- Which CMMI level is Sioux?
- I don't understand what is written here. How are we going to report the assement of the software process and organization?

Page 8:
- NA 

## Search for info

Arend-Jan proposal to talk to:

- Agfa project (Makalu) bijpraten met Rob Pulles 
- ASML WTTR-2 (Wafer Takeover Testrig V2) bijpraten met Glenn Roumen 
- Mitutoyo LENS bijpraten met Rob Pulles 
- Raith Litho FUMO wafer handling bijpraten met Ronald Plak 
- Vanderlande SPO4 bijpraten met Edwin Thijssen 
 
## Preparation

What needs to be prepared?



## interviews for SIOUX/CMM capabilities

- Introduction SAXCS
    - [Rob Pulles](https://intranet.sioux.eu/nl/tijdlijn/rob-pulles/639/profile): 	System designer mechatronics
    - [sharepoint](https://siouxeu.sharepoint.com/sites/SAXCSAsset)

- WTTR
    - [Glenn Roumen](https://intranet.sioux.eu/nl/tijdlijn/glenn-roumen/1604/profile): 	System Engineer Mechatronics 

    - WTTR
        P:\0222\128\Product\Investigations\_CR PR\PIR - WTTR2 Summary.docx

    - [Loy Rovers](https://intranet.sioux.eu/nl/tijdlijn/loy-rovers/598/profile): Principal System Designer Mechatronics

- AGFA
    - [Rob Pulles](https://intranet.sioux.eu/nl/tijdlijn/rob-pulles/639/profile): 	System designer mechatronics
    - printers 
    - 0602.004
    - nieuw RTOS
    - configurability
 
 Mitutoyo
    - [Rob Pulles](https://intranet.sioux.eu/nl/tijdlijn/rob-pulles/639/profile): 	System designer mechatronics
    - 0748.001


- DBSE:
    - [Mark Otto](https://intranet.sioux.eu/nl/tijdlijn/mark-otto/613/profile):	Principal system designer software
    - [Bert Brals](): System Architect

    Holodeck
    - Sander van Deelen
    
- Raith Litho
    - [Ronald Plak](https://intranet.sioux.eu/nl/tijdlijn/ronald-plak/638/profile): System Architect

- Vanderlande SPO4
    - [Edwin Thijssen](https://intranet.sioux.eu/nl/tijdlijn/edwin-thijssen/554/profile): 	system architect

## Notes SAXCS
SACXS is:
- easy to use.
- poorly documented

# For sales pitch from Sioux website
Projects
- LITEQ
- UPSS 1.0 Stage with Air Bearing System
    - Laser-Induced Subsurface separation (ASM-PT)
- Canon
- MCI

- Eugene
    - Robert 

Solutions
- joost sannen

- organization
