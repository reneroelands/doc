
# TOGAF

## Definitions

TOGAF: The open group architecture framework

## Architecture Principles

There are five criteria that distinguish a good set of principles:

- **Understandable**: the underlying tenets can be quickly grasped and understood by individuals throughout the organization. The intention of the principle is clear and unambiguous, so that violations, whether intentional or not, are minimized.
- **Robust**: enable good quality decisions about architectures and plans to be made, and enforceable policies and standards to be created. Each principle should be sufficiently definitive and precise to support consistent decision-making in complex, potentially controversial situations.
- **Complete**: every potentially important principle governing the management of information and technology for the organization is defined — the principles cover every situation perceived.
- **Consistent**: strict adherence to one principle may require a loose interpretation of another principle. The set of principles must be expressed in a way that allows a balance of interpretations. Principles should not be contradictory to the point where adhering to one principle would violate the spirit of another. Every word in a principle statement should be carefully chosen to allow consistent yet flexible interpretation.
- **Stable**: principles should be enduring, yet able to accommodate changes. An amendment process should be established for adding, removing, or altering principles after they are ratified initially.

## Stakeholder management

### Stakeholder identification

Look at who is impacted by the Enterprise Architecture project:

- Who gains and who loses from this change?
- Who controls change management of processes?
- Who designs new systems?
- Who will make the decisions?
- Who procures IT systems and who decides what to buy?
- Who controls resources?
- Who has specialist skills the project needs?
- Who has influence?

## Architecture Repository

How many companies have it?

## Architecture Patterns

- **Name** A meaningful and memorable way to refer to the pattern, typically a single word or short phrase.
- **Problem** A description of the problem indicating the intent in applying the pattern—the intended goals and objectives to be reached within the context and forces described below (perhaps with some indication of their priorities).
- **Context** The preconditions under which the pattern is applicable — a description of the initial state before the pattern is applied.
- **Forces**  A description of the relevant forces and constraints, and how they interact/conflict with each other and with the intended goals and objectives. The description should clarify the intricacies of the problem and make explicit the kinds of trade-offs that must be considered. (The need for such trade-offs is typically what makes the problem difficult, and generates the need for the pattern in the first place.) The notion of "forces" equates in many ways to the "qualities" that architects seek to
optimize, and the concerns they seek to address, in designing architectures. For example:

  - Security, robustness, reliability, fault-tolerance
  - Manageability
  - Efficiency, performance, throughput, bandwidth requirements, space
utilization
  - Scalability (incremental growth on-demand)
  - Extensibility, evolvability, maintainability
  - Modular ity, independence, re-usability, openness, composability (plug-and play), portability
  - Completeness and correctness
  - Ease-of-construction
  - Ease-of-use
  - etc., ...
- **Solution** A description, using text and/or graphics, of how to achieve the intended goals and objectives. The description should identify both the solution’s static structure and its dynamic behavior — the people and computing actors, and their collaborations. The description may include guidelines for implementing the solution. Variants or specializations of the solution may also be described.
- **Resulting Context** The post-conditions after the pattern has been applied. Implementing the solution normally requires trade-offs among competing forces.

### Architectural decision patterns

- Descriptive Decision Support: SysML, OPM, IDEF0, FFBD
- Prescriptive Qualitative Decision Support: ..
- Prescriptive Quantitative Decision Support: DSM

“In partitioning, choose the elements so that they are as independent as possible, that is, elements with low external complexity and high internal cohesion.”

## Interesting

Zachman Framework

| - | Why | How | What | Who | Where | When |
|---|-----|-----|------|-----|-------|------|
| ***Contextual*** | Goal list | Process list | Material list | Role list | Locations list | Event list  |
| ***Conceptual*** | Goal relationships | Process Model | Entity relationship model | Role relationship model | Location model | Event model |
| ***Logical*** | Rules diagram | Process diagram | Data model diagram | Role relationship diagram | Locations diagram | Event diagram |
| ***Physical*** | Rules spec | Process function spec | Data entity spec | Role spec | Location spec | Event spec |
| ***Detailed*** | Rules details | Process details | Data details | Role details | Location details | Event details |

There's a 6th line: usage
Enterprise Architecture Management Pattern Catalog