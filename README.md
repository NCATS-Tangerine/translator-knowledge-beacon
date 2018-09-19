# Purpose #

## Overview ##

This project documents the Knowledge Beacon Application Programming Interface (KBAPI). 

Specifically, this repository holds the OpenAPI ("Swagger") definition of the **KBAPI** archived in the 'api' subfolder: https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/api/knowledge-beacon-api.yaml

Check out our [Knowledge Beacon Wiki](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/wiki) for additional documentation on the status of Knowledge Beacon API implementations and some additional notes on how to build your own.

# Knowledge Beacons Workflow

The **KBAPI** is primarily designed to support a simple knowledge discovery workflow, as illustrated in following diagram:

![Knowledge Beacon Application Programming Interface](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/docs/KBAPI_Workflow.png "Knowledge Beacon Workflow")

Aside from the concept and statement accessing endpoints, the **KBAPI** also provides access to the list of concept (*/categories*) and relationship (*/predicates*) data types used by the beacon. 

In fact, concept instances returned by various calls (*/concepts?keywords=..*, */concepts/{conceptId}* and the subject/object concepts in knowledge assertions returned by the */statements* endpoint) are specified by the API to be tagged by the semantic concept types (i.e. "gene", "drug", "disease", etc.) reported by the */categories* endpoint, which is assumed to be based on a semantic data type controlled vocabulary (originally based on the [UMLS Metamap concept categories](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt), but which is now undergoing NCATS Translator curation to a richer ontology).

The **KBAPI** also provides endpoints (*/exactmatches*) to report CURIE identifiers which are deemed to globally identify the functionally equivalent (*sensa*-[SKOS exactMatch](http://www.w3.org/2004/02/skos/core#exactMatch) or [OWL sameAs](https://www.w3.org/2002/07/owl)).

# Knowledge Beacons in Action!

The pool of known beacons is currently documented in a **[master YAML-formatted catalog of beacons](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/api/knowledge-beacon-list.yaml)**. REST clients may also access aggregate data via the API from all these registered beacons, through a [Knowledge Beacon Aggregator](https://github.com/NCATS-Tangerine/beacon-aggregator), a public version for which is hosted online at **https://kba.ncats.io**. 

Some of these KBAPI wrappers are locally published in other repositories within the NCATS-Tangerine organization, as follows:

* [Semantic Medline Database Beacon](now uses code from https://github.com/NCATS-Tangerine/tkg-beacon). Implementation of the [Translator Knowledge Graph Beacon](https://github.com/NCATS-Tangerine/tkg-beacon) wrapping the [Semantic Medline Database](https://skr3.nlm.nih.gov/) concepts and relationships text-mined from PubMed abstracts. Beacon deployed at https://kba.ncats.io/beacon/rkb.(note, this beacon may soon be reconfigured to resolved as https://kba.ncats.io/beacon/semmeddb).
* [Monarch Database "Biolink" Beacon](now uses code from https://github.com/NCATS-Tangerine/tkg-beacon): Implementation of the [Translator Knowledge Graph Beacon](https://github.com/NCATS-Tangerine/tkg-beacon) wrapping the Monarch Biolink API of the [Monarch Initiative Biomedical Resource](https://monarchinitiative.org/). Beacon deployed at https://kba.ncats.io/beacon/biolink.
* [HMBD Database](http://www.hmdb.ca). Human Metabolome database wrapped as a beacon ([beacon by Vlado Dancik, Broad](https://github.com/NCATS-Tangerine/HMDB-knowledge-beacon)). Beacon deployed at https://translator.ncats.io/hmdb-knowledge-beacon.
* [nDex Beacon](https://github.com/NCATS-Tangerine/ndex-beacon): a Java wrapper accessing the [nDex biomedical graph archive](http://www.home.ndexbio.org/index/) biomedical network data exchange archive. NCATS prototype beacon deployed at https://kba.ncats.io/beacon/ndex.
* [RTX Knowledge Graph Beacon](). NCATS RTX team implementation of the [Translator Knowledge Graph Beacon](https://github.com/NCATS-Tangerine/tkg-beacon) wrapping the NCATS RTX reasoner compiled knowledge graph. Beacon deployed at https://kba.ncats.io/beacon/rtx. 
* [Biothings Explorer Beacon](http://biothings.io/explorer/). Beacon wrapping the Biothings Explorer resource accessing SmartAPI published resources. Beacon deployed at https://kba.ncats.io/beacon/biothings-explorer.
* [Rhea Beacon](https://www.rhea-db.org/). Rhea biochemical reactions database. Prototype beacon deployed at https://kba.ncats.io/beacon/rhea.

Other beacon wrappers are hosted in other repositories elsewhere (see the [catalog of beacons](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/api/knowledge-beacon-list.yaml)).

# Knowledge Clients

A simple web application client "Translator Knowledge.Bio" for visually browsing Knowledge Beacon Aggregator data is implemented and running at **http://tkbio.ncats.io.**, the code for which is available **[here](https://github.com/NCATS-Tangerine/tkbio)**. 
