#!/bin/bash
# Created by Lance Hannestad
# STAR Informatics/Delphinai Corporation, Port Moody, BC, Canada
#
# This script takes a yaml or json file as an input. To run this script, do:
#	./generateJavaClient.sh ../api/knowledge-beacon.yaml
#
#  Note that if an executable swagger JAR is not on your PATH
#  (e.g. like a HomeBrew installed copy on a Mac OSX system), then
#  the SWAGGER_CODEGEN_PATH environment variable should point to the folder
#  where a downloaded copy of the swagger-codegen-cli.jar is located.
#
if [ -z $SWAGGER_CODEGEN_PATH ]; then
	# current directory is default if no path given?
	SWAGGER_CODEGEN_PATH="."
	echo "Swagger Codegen JAR path set to '$SWAGGER_CODEGEN_PATH'"
fi

SWAGGER_CODEGEN_EXEC=`which swagger-codegen`
if [ ! -e $SWAGGER_CODEGEN_EXEC ]; then
	SWAGGER_CODEGEN_EXEC=java -jar $SWAGGER_CODEGEN_PATH/swagger-codegen-cli.jar
fi

echo "Swagger Codegen executable is '$SWAGGER_CODEGEN_EXEC'"


if [ "$#" -lt 1 ]; then
	echo "generateJavaClient.sh <path to specification file>"
else
	$SWAGGER_CODEGEN_EXEC generate	\
	-i $1						\
	-l java						\
	-o ../client					\
	-c javaClientGenerateOptions.json			\
	--skip-overwrite
fi
