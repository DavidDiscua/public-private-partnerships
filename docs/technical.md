# Technical overview

OCDS for PPPs is built on top of upon the [Open Contracting Data Standard](http://standard.open-contracting.org).

This provides a foundational model for:

* Publishing data about contracting processes as structured JSON;
* Converting between JSON and spreadsheet data representations;
* Publishing real-time releases from a contracting process;
* Publishing compiled records of a contracting process;

The basic OCDS schema has been [extended](/extensions/) with a range of additional building blocks and codelist values. 

The extended OCDS for PPPs schema provides all the elements covered by the World Bank PPP Disclosure Framework.

## The OCDS for PPPs Schema

To produce and validate OCDS for PPPs data, create an OCDS 1.1 file, and include the consolidated OCDS for PPPs extensions. 

TODO TODO TOD

A compiled OCDS for PPPs schema, with the extensions applied, is also  [available to download](LINK LINK LINK), and a [full reference table is provided](LINK LINK LINK).

## Who is this for?

The OCDS for PPPs, and this documentation, is designed for systems designers, seeking to:

* Build data collection processes for PPP disclosure;
* Integrate existing PPP disclosures from existing sytems;
* Export and publish PPP disclosures in a common format;
* Present and visualise PPP disclosures;

OCDS for PPPs provide a data model. Additional design work will be required to develop interfaces and workflows appropriate to the collection and dissemination of data on a case-by-case basis. 

The extended OCDS for PPPs schema and [reference documentation](reference.md) can be used as a 'checklist' to ensure that information is being captured on all the required aspects of the framework, and that information is published at the appropriate time. 

This documentation is **not** designed for individual PPP project managers. If you want to directly publish data on a PPP project to meet with World Bank Disclosure Framework requirements, we recommend seeking out appropriate tools that can implement OCDS for PPPs, or talking to vendors or developers about adding OCDS for PPPs support to your existing information management tools.

## How to use this documentation

First review:

* The [core Open Contracting Data Standard documentation](http://standard.open-contracting.org/latest/en/getting_started/);
* The [World Bank Framework for Disclosure in Public Private Partnerships](http://www.worldbank.org/en/topic/publicprivatepartnerships/brief/a-framework-for-disclosure-in-public-private-partnership-projects)

Then consult the [reference](reference.md) pages to see how each element from the PPP Disclosure Framework template can be captured using OCDS.

