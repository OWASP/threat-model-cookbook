Examples of flow diagrams using different tools to create them.

Can be of various sub-types such as 
* Data Flow Diagram
* Connection Flow Diagram
* Process Flow Diagram

Tool | File match |
:--- | :---
| [pytm](https://github.com/izar/pytm/): A Pythonic framework for threat modeling | `*.py` |
| [Threat Dragon](https://owasp.org/www-project-threat-dragon/): The OWASP threat modelling tool | `*.json` |
| [Graphviz](https://graphviz.gitlab.io/) DOT | `*.dot` |
| Microsoft Visio | `*.vsdx` |
| Physical world paper or whiteboard | `*.jpg` |

Currently pytm is generating the dot and then Graphviz is used to create outputs.

Threat Dragon is an OWASP project. It is both an online threat modelling web application and a desktop application. It includes system diagramming as well as a rule engine to auto-generate threats.

Files starting with `altN-` are alternate version of the same system being modeled by a different person.
