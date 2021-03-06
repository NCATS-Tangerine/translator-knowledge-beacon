# Purpose #

## Overview ##

This project documents the Knowledge Beacon Application Programming Interface (KBAPI). 

Specifically, this repository holds the OpenAPI ("Swagger") definition of the [**KBAPI** specification](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/master/api/knowledge-beacon-api.yaml) archived in the 'api' subfolder.

Check out our [Knowledge Beacon Wiki](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/wiki) for additional documentation on the status of Knowledge Beacon API implementations and some additional notes on how to build your own.

This API was developed as an early research and development during the Feasibility Phase of the [Biomedical Knowledge Translator Consortium ("Translator")](https://ncats.nih.gov/translator), funded by the [National Center for Advancing Translational Sciences ("NCATS")](https://ncats.nih.gov) program of the US National Institutes of Health. In the "Development" phase of Translator, the concept of the Knowledge Beacon API has been supplanted by the [Translator Reasoner Application Programming Interface ("TRAPI")](https://github.com/NCATSTranslator/ReasonerAPI/) although Knowledge Beacons remain hosted online at https://kba.ncats.io as documented in our paper (citation below).

### Citation

Hannestad LM, Dančík V, Godden M, Suen IW, Huellas-Bruskiewicz KC, Good BM, et al. (2021) Knowledge Beacons: Web services for data harvesting of distributed biomedical knowledge. PLoS ONE 16(3): e0231916. https://doi.org/10.1371/journal.pone.0231916

# Knowledge Beacons Workflow

The **KBAPI** is primarily designed to support a simple knowledge discovery workflow. The endpoint are generally summarized in the following table:

Section | Endpoint |Description 
 --- | --- | --- 
Metadata | `/categories` | List of available concept categories
| | `/predicates` | List of available predicates
| | `/kmap` | Knowledge map of the beacon
Concepts | `/concepts` | Query concepts by keywords
| | `/concepts/{conceptId}` | Details about concept
| | `/exactmatches` | Retrieve equivalent concept identifiers
Statements | `/statements` | Query statements by concept id
| | `/statements/{statementId}` | Details about statements


The workflow captured by the **KBAPI** is generally as illustrated in the following diagram:

![Knowledge Beacon Application Programming Interface](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/master/docs/KBAPI_Workflow.png "Knowledge Beacon Workflow")

Aside from the concept and statement accessing endpoints, the **KBAPI** also provides access to the list of concept (*/categories*) and relationship (*/predicates*) data types used by the beacon. 

In fact, concept instances returned by various calls (*/concepts?keywords=..*, */concepts/{conceptId}* and the subject/object concepts in knowledge assertions returned by the */statements* endpoint) are specified by the API to be tagged by the semantic concept types (i.e. "gene", "drug", "disease", etc.) reported by the */categories* endpoint, which is assumed to be based on a semantic data type controlled vocabulary (originally based on the [UMLS Metamap concept categories](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt), but which is now compliant to eh NCATS Translator endorsed [Biolink Model](https://biolink.github.io/biolink-model/).

The **KBAPI** also provides endpoints (*/exactmatches*) to report CURIE identifiers which are deemed to globally identify the functionally equivalent (*sensa*-[SKOS exactMatch](http://www.w3.org/2004/02/skos/core#exactMatch) or [OWL sameAs](https://www.w3.org/2002/07/owl)).

# Knowledge Beacons in Action!

The pool of known active and proposed beacons is enumerated in a **[master YAML-formatted catalog of beacons](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/master/api/knowledge-beacon-list.yaml)**. The significant currently active ones are as follows:

* **Semantic Medline Database:** Implementation of a [Translator Knowledge Graph Beacon](https://github.com/NCATS-Tangerine/tkg-beacon) wrapping the June 2019 release of the [Semantic Medline Database](https://skr3.nlm.nih.gov/) concepts and relationships text-mined from PubMed abstracts. Beacon deployed at https://kba.ncats.io/beacon/semmedb.
* **Monarch Database "Biolink" Beacon:** Implementation of a [Translator Knowledge Graph Beacon](https://github.com/NCATS-Tangerine/tkg-beacon) wrapping the Monarch Biolink API of the [Monarch Initiative Biomedical Resource](https://monarchinitiative.org/). Beacon deployed at https://kba.ncats.io/beacon/biolink.
* [HMDB](http://www.hmdb.ca). Human Metabolome Database wrapped as a beacon ([beacon by Vlado Dancik, Broad](https://github.com/NCATS-Tangerine/HMDB-knowledge-beacon)). Beacon deployed at https://kba.ncats.io/beacon/hmdb.
* [Rhea Beacon](https://www.rhea-db.org/). Rhea biochemical reactions database. Beacon deployed at https://kba.ncats.io/beacon/rhea.
* [SMPDB Beacon](http://smpdb.ca). Small Molecular Pathways database. Beacon deployed at https://kba.ncats.io/beacon/smpdb.
* [nDex Beacon](https://github.com/NCATS-Tangerine/ndex-beacon): a Java wrapper accessing the [nDex biomedical graph archive](http://www.home.ndexbio.org/index/) biomedical network data exchange archive. Beacon deployed at https://kba.ncats.io/beacon/ndex.

Other beacon wrappers may be hosted in other repositories elsewhere (see the [catalog of beacons](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/master/api/knowledge-beacon-list.yaml)).

# Sample Usage of the API

A concept by keywords search on the Semantic Medline Database Knowledge Beacon Endpoint:

```
https://kba.ncats.io/beacon/semmeddb/concepts?keywords=hyperhomocysteinemia
```
gives the following result:

```json
[
  {
    "categories": [
      "disease or phenotypic feature"
    ],
    "description": null,
    "id": "UMLS:C0598608",
    "name": "Hyperhomocysteinemia"
  }
]
```

Taking the concept id (with additional constraints) may be used to search for knowledge statements that answer questions like "what could treat Hyperhomocysteinemia?"

```
https://kba.ncats.io/beacon/semmeddb/statements?s_keywords=vitamin&edge_label=treats&t=UMLS%3AC0598608&offset=1&size=5
```

gives the following result:

```json
[
  {
    "id": "UMLS:C0301532:treats:UMLS:C0598608",
    "object": {
      "categories": [
        "disease or phenotypic feature"
      ],
      "id": "UMLS:C0598608",
      "name": "Hyperhomocysteinemia"
    },
    "predicate": {
      "edge_label": "treats",
      "negated": true,
      "relation": "semmeddb:treats"
    },
    "subject": {
      "categories": [
        "chemical substance"
      ],
      "id": "UMLS:C0301532",
      "name": "Multivitamin preparation"
    }
  },
  {
    "id": "UMLS:C0087162:treats:UMLS:C0598608",
    "object": {
      "categories": [
        "disease or phenotypic feature"
      ],
      "id": "UMLS:C0598608",
      "name": "Hyperhomocysteinemia"
    },
    "predicate": {
      "edge_label": "treats",
      "negated": true,
      "relation": "semmeddb:treats"
    },
    "subject": {
      "categories": [
        "chemical substance"
      ],
      "id": "UMLS:C0087162",
      "name": "Vitamin B6"
    }
  },
  {
    "id": "UMLS:C0042890:treats:UMLS:C0598608",
    "object": {
      "categories": [
        "disease or phenotypic feature"
      ],
      "id": "UMLS:C0598608",
      "name": "Hyperhomocysteinemia"
    },
    "predicate": {
      "edge_label": "treats",
      "negated": true,
      "relation": "semmeddb:treats"
    },
    "subject": {
      "categories": [
        "chemical substance"
      ],
      "id": "UMLS:C0042890",
      "name": "Vitamins"
    }
  },
  {
    "id": "UMLS:C0042849:treats:UMLS:C0598608",
    "object": {
      "categories": [
        "disease or phenotypic feature"
      ],
      "id": "UMLS:C0598608",
      "name": "Hyperhomocysteinemia"
    },
    "predicate": {
      "edge_label": "treats",
      "negated": true,
      "relation": "semmeddb:treats"
    },
    "subject": {
      "categories": [
        "chemical substance"
      ],
      "id": "UMLS:C0042849",
      "name": "Vitamin B Complex"
    }
  },
  {
    "id": "UMLS:C0042845:treats:UMLS:C0598608",
    "object": {
      "categories": [
        "disease or phenotypic feature"
      ],
      "id": "UMLS:C0598608",
      "name": "Hyperhomocysteinemia"
    },
    "predicate": {
      "edge_label": "treats",
      "negated": true,
      "relation": "semmeddb:treats"
    },
    "subject": {
      "categories": [
        "chemical substance"
      ],
      "id": "UMLS:C0042845",
      "name": "Vitamin B 12"
    }
  }
]
```

suggesting that some B vitamins can help treat Hyperhomocysteinemia.


# Knowledge Beacon Aggregator #

REST clients may also access aggregate data obtained from a pool of Knowledge Beacons through an instance of the [Knowledge Beacon Aggregator](https://github.com/NCATS-Tangerine/beacon-aggregator), a public version for which is hosted online at **https://kba.ncats.io**. 

# Beacon Validation #

A [Knowledge Beacon Validator](https://github.com/NCATS-Tangerine/beacon-validator) was developed to check Beacon function.

# Knowledge Beacon Clients #

A basic [command line client (and associated Python client access library)](https://github.com/NCATS-Tangerine/beacon-aggregator-client) was developed for simple access to the [Knowledge Beacon Aggregator](https://github.com/NCATS-Tangerine/beacon-aggregator). The documentation for the client calls of the API are documented in relative detail [here](https://github.com/NCATS-Tangerine/beacon-aggregator-client/blob/master/README.md#documentation-for-api-endpoints).
