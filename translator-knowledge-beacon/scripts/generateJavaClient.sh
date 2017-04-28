#!/bin/bash
# Created by Lance Hannestad
# STAR Informatics/Delphinai Corporation, Port Moody, BC, Canada
#
# This script takes a yaml or json file as an input. To run this script, do:
#	./generateJavaClient.sh ../api/knowledge-beacon_1.0.6.yaml
#
#  Note that the SWAGGER_CODEGEN_PATH environment variable should point
#  to the folder where your downloaded swagger-codegen-cli.jar is located.
#
if [ -z $SWAGGER_CODEGEN_PATH ]; then
	# current directory is default if no path given?
	SWAGGER_CODEGEN_PATH="."
	echo "Swagger Codegen JAR path set to '$SWAGGER_CODEGEN_PATH'"
fi

SWAGGER_CLI=`which swagger-codegen-cli`
if [ ! -e $SWAGGER_CLI ]; then
	SWAGGER_CLI=java -jar $SWAGGER_CODEGEN_PATH/swagger-codegen-cli.jar
fi

echo "Swagger CLI executable is '$SWAGGER_EXEC'"


if [ "$#" -lt 1 ]; then
	echo "generateJavaClient.sh <path to specification file>"
else
	$SWAGGER_EXEC generate	\
	-i $1						\
	-l java						\
	-o ../client					\
	-c javaClientGenerateOptions.json			\
	--skip-overwrite
fi
