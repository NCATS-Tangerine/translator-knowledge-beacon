# Purpose #

## Overview ##

This project documents the Knowledge Beacon Application Programming Interface (KBAPI). 

Specifically, this repository holds the OpenAPI ("Swagger") definition of the KBAPI archived in the 'api' subfolder: https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/api/knowledge-beacon-api.yaml

These OpenAPI definitions can be directly used to generate both client and server code as described below. A "Knowledge Beacon Workflow" document discusses the use of the API.

# Knowledge Beacons in Action! #

An initial prototype web application client "Translator Knowledge.Bio" accessing Knowledge Beacons is implemented and running at **http://tkbio.ncats.io.**, the code for which is available **[here](https://github.com/NCATS-Tangerine/tkbio)**. 

The pool of known beacons is currently documented in a **[master YAML-formatted catalog of beacons](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/api/knowledge-beacon-list.yaml)**. REST clients may also access aggregate data via the API from all these registered beacons, through a [Knowledge Beacon Aggregator](https://github.com/NCATS-Tangerine/beacon-aggregator), a public version for which is hosted online at **https://kba.ncats.io**. 

Some of these KBAPI wrappers are locally published in other repositories within the NCATS-Tangerine organization, as follows:

* [Reference Beacon](https://github.com/NCATS-Tangerine/reference-beacon): a Java Spring Boot KBAPI accessing a Neo4j server containing Semantic Medline Database concepts and relationships textmined from PubMed abstracts
* [Monarch Database "Biolink" Beacon](https://github.com/NCATS-Tangerine/biolink-beacon): a Python KSAPI accessing the Biolink API of the [Monarch Initiative Biomedical Resource](https://monarchinitiative.org/)
* [nDex Beacon]9https://github.com/NCATS-Tangerine/ndex-beacon): a Java wrapper accessing the [nDex biomedical graph archive](http://www.home.ndexbio.org/index/) biomedical network data exchange archive.
* [StringDb Beacon](https://github.com/NCATS-Tangerine/stringdb-beacon) : a Python wrapper for the [STRING Protein-Protein interactions database](https://string-db.org/).

Other beacon wrappers (e.g. Wikidata) are hosted in other repositories elsewhere (see the [catalog of beacons](https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/api/knowledge-beacon-list.yaml)).

# Swagger generated server #

##Spring Boot Server## 

The [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project can be used to generate client and server libraries/applications to use the API. 

On Mac OSX machines, Homebrew can be used to install the swagger-codegen tool:

	brew install swagger-codegen

which downloads the JAR and installs an executable wrapper on your PATH.

Alternately, the swagger-codegene Java JAR should be downloaded and a "SWAGGER_CODEGEN_PATH" environmental variable set to point to the folder containing the jar.

Some sample scripts are given in the scripts subfolder to use for the creation of Java clients and servers (the '.sh' is a Linux bash shell version; the '.bat' is a Windows version)

* generateJavaClient.sh - generates a Java client library
* generateSpringBootServer.sh - generates a Java Spring Boot Server stub implementation

See the swagger-codegen web site for additional language and framework implementation options for stub generation.  For proper execution, these scripts should be executed directly inside the 'scripts' folder.

## Building a Web Server using the API ##

The 'generateSpringBootServer' script (re-)generates a Java Spring Boot server code tree under 'server' subfolder in the root folder. Usage:

	cd scripts
	./generateSpringBootServer.sh api/knowledge-beacon.yaml  # use the .bat file for MS Windows  

The resulting code base is put in a 'server' subfolder may be directly built with Maven into an executable Java JAR file:

	mvn package

where the resulting JAR is placed into the 'target' subdirectory.  Alternately, the project may be converted to a Gradle project by simply running the 'gradle init' function inside the root project folder.

## Running the Web Server ##

Start your server as an simple java application (where '*' is the version of the API, e.g. '1.0.12') as follows:

For a Maven generated version, type:

	java -jar target/knowledge-beacon-server-*.jar


Alternately, for the Gradle generated version, type:

	java -jar build/libs/knowledge-beacon-server-*.jar


You can view the api documentation online by pointing to
  
	http://localhost:8080/api

(where 'api' is the basepath in the OpenAPI document).  You can change default port value in **application.properties** under server/src/main/resources.

## Building a Client Library using the API ##

The 'generateJavaClient' script (re-)generates a Java client access code tree under 'client' folder in the project, as follows:

	cd scripts
	./generateJavaClient.sh api/knowledge-beacon_*.yaml   # use the .bat file for MS Windows

(where '*' is the version of the API, e.g. '1.0.12')  The resulting code base is put in a 'client' subfolder to be directly customized then built into an executable Java JAR file.
