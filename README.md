# KIM Workshop 2023 - Metadata hands-on session

Github's CI/CD integration is a powerfull tool to create data pipelines and automated workflows.

This is a demo repository for the creation of semantic web related data:
1. Automated RDF data generation from Python scripts (triple-generation.yml).
2. Automated generation and versioning of ontology specifications from markdown files (ontology-generation.yml).

Workflow 1 (/data) executes a Python script which generates RDF data out of an XML file. Workflow 2 (/ontology) generates an ontology specification out of a human readable markdown syntax. After the generation the newly created ontology is ready to publish in turtle format and is directly versioned within this workflow.
