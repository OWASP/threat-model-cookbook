# OWASP Threat Model Cookbook Project

This project is about creating and publishing threat model examples. They can be in the form of code, graphical or textual representations. The models will use diverse technologies, methodologies and techniques.

You can learn from those models, use them a base to start your own, or contribute and expand some of the models. Thus making this a collaborative cookbook of threat models.

https://owasp.org/www-project-threat-model-cookbook/

https://twitter.com/OWASP_tmcb

## Disclaimer
Examples provided in this repository are not representations of secure systems, but rather insecure systems that are easy to model. Most of them are made up systems that doesn't exist in reality. Any resemblance to real life systems is purely coincidental.

## Contributing
We are welcoming PRs containing examples to add to the cookbook. If you want to add new threat models, create more versions based of existing drafts, feel free to directly submit a PR.

Here's some guidelines on how our file structure works:
* Top-level directories are the type of threat models. Example: `Flow Diagram`.
* If your threat model has 1 or 2 files, you can put the files directly in that directory. If they have more, please create a folder with the name of your system to be modeled.
* The name of the system needs to be using dashes and alphanumeric characters only. No spaces.
* The files needs to have a specific extension depending on the format: `system-name.tool` and `system-name.tool.exportfiletype`. As examples, we have the code file `cryptowallet.plantuml` and the output to an image file generated from that code as `cryptowallet.plantuml.svg`. Refer to the README.md in each top-level folder for a list of tools and their file extension matches.
* If you have multiple representation of the same system using the same tool, we suggest you add `altN-` at the start of the file where `N` is a number.
* If you have multiple versions of the same system using the same tool, you could also show progression over time by adding `vN-` at the start.

If this sounds complicated and you just want to contribute, you can still submit a PR and we'll refactor it for you. We might have more automation and outside references in the future so we want to keep a strict file structure.

If you'd like to discuss about the structure of the project, feel free to join the discussion on [OWASP Slack](https://owasp.slack.com/messages/threatmodel-cookbook/).

## Licenses

All models in form of textual or graphical representations are under CC-BY 4.0

All models as code are under Apache License 2.0

