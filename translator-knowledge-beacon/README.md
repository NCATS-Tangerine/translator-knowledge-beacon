# Swagger generated server #

Spring Boot Server 

## Overview ##

This project contains the Knowledge Beacon Application Programming Interface (KBAPI). The KBAPI is formally specified as an OpenAPI ("Swagger") specification, as archived in the 'api' subfolder. 

The [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project can be used to generate client and server libraries/applications to use the API. Some sample scripts are given in the scripts subfolder wrap this tool to facilitate the creation of some clients and servers:

* generateJavaClient.sh - generates a Java client library
* generateSpringBootServer.sh - generates a Java Spring Boot Server stub implementation

See the swagger-codegen web site for more language and framework implementation options for stub generation.

## Building a Web Server using the API ##

The 'generateSpringBootServer.sh' script (re-)generates a Java Spring Boot server code tree under 'src' (with Maven dependencies documented in the pom.xml file). Usage:

	scripts/generateSpringBootServer.sh api/knowledge-beacon_1.0.6.yaml   

The resulting code base is put in a 'server' subfolder may be directly built with Maven into an executable Java JAR file:

	mvn package

where the resulting JAR is placed into the 'target' subdirectory.

Alternately, the project may be converted to a Gradle project by simply running the 'gradle init' function inside the root project folder.

## Running the Web Server ##

Start your server as an simple java application, something like

	java -jar target/swagger-spring-1.0.0.jar 

(for the Maven generated version) or

	java -jar build/libs/swagger-spring-1.0.0.jar 

(for the Gradle generated version).

You can view the api documentation in swagger-ui by pointing to
  
	http://localhost:8080/api

Change default port value in application.properties
