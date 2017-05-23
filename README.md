# Purpose #

This repository holds the Swagger definition of the Knowledge Beacon API: https://github.com/NCATS-Tangerine/translator-knowledge-beacon/blob/develop/api/knowledge-beacon-api.yaml

Swagger API documents can be used to generate both client and server code as described below.  

# Swagger generated server #

Spring Boot Server 

## Overview ##

This project contains the Knowledge Beacon Application Programming Interface (KBAPI). 

The KBAPI is formally specified as an OpenAPI ("Swagger") specification, as archived in the 'api' subfolder.   A "Knowledge Beacon Workflow" document is also provided.

The [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project can be used to generate client and server libraries/applications to use the API. 

On Mac OSX machines, Homebrew can be used to install the swagger-codegen tool:

	brew install swagger-codegen

which downloads the JAR and installs an executable wrapper on your PATH.

Alternately, the swagger-codegene Java JAR should be downloaded and a "SWAGGER_CODEGEN_PATH" environmental variable set to point to the folder containing the jar.

Some sample scripts are given in the scripts subfolder to wrap this tool to facilitate the creation of some clients and servers (the '.sh' is a Linux bash shell version; the '.bat' is a Windows version)

* generateJavaClient.sh - generates a Java client library
* generateSpringBootServer.sh - generates a Java Spring Boot Server stub implementation

See the swagger-codegen web site for more language and framework implementation options for stub generation.  For proper execution, these scripts should be executed directly inside the 'scripts' folder.

## Building a Web Server using the API ##

The 'generateSpringBootServer' script (re-)generates a Java Spring Boot server code tree under 'server' subfolder in the root folder. Usage:

	cd scripts
	./generateSpringBootServer.sh api/knowledge-beacon_1.0.6.yaml  # use the .bat file for MS Windows  

The resulting code base is put in a 'server' subfolder may be directly built with Maven into an executable Java JAR file:

	mvn package

where the resulting JAR is placed into the 'target' subdirectory.  Alternately, the project may be converted to a Gradle project by simply running the 'gradle init' function inside the root project folder.

## Running the Web Server ##

Start your server as an simple java application, something like

	java -jar target/knowledge-beacon-server-1.0.6.jar

(for the Maven generated version) or

	java -jar build/libs/knowledge-beacon-server-1.0.6.jar

(for the Gradle generated version).

You can view the api documentation in swagger-ui by pointing to
  
	http://localhost:8080/api

Change default port value in application.properties

## Building a Client Library using the API ##

The 'generateJavaClient' script (re-)generates a Java Spring Boot server code tree under 'client' folder in the project. Usage:

	cd scripts
	./generateJavaClient.sh api/knowledge-beacon_1.0.6.yaml   # use the .bat file for MS Windows

The resulting code base is put in a 'server' subfolder may be directly built with Maven into an executable Java JAR file:
