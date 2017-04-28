#!/bin/bash
# Created by Lance Hannestad
# STAR Informatics/Delphinai Corporation, Port Moody, BC, Canada

# This script takes a yaml or json file as an input. To run this script, do:
#	./generateJavaClient.sh ../api/knowledge-beacon_1.0.6.yaml

if [ "$#" -lt 1 ]; then
	echo "generateJavaClient.sh <path to specification file>"
else
	java -jar swagger-codegen-cli.jar generate	\
	-i $1						\
	-l java						\
	-o ../client					\
	-c javaClientGenerateOptions.json			\
	--skip-overwrite
fi
