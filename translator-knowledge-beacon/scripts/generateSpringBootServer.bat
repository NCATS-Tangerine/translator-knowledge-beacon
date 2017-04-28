@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  Adapted by Richard Bruskiewich from Lance Hannestad bash script
@rem  STAR Informatics/Delphinai Corporation, Port Moody, BC, Canada
@rem
@rem  This script takes a yaml or json file as an input. To run this script, do:
@rem
@rem  cd scripts
@rem  ./generateSpringBootServer.bat ..\api\knowledge-beacon.yaml
@rem
@rem  Note that the SWAGGER_CODEGEN_PATH environment variable should point
@rem  to the folder where your downloaded swagger-codegen-cli.jar is located.
@rem
@rem ##########################################################################

if "%SWAGGER_CODEGEN_PATH%" == "" set SWAGGER_CODEGEN_PATH=.

if "%1" == "" goto fail

java -jar %SWAGGER_CODEGEN_PATH%\swagger-codegen-cli.jar generate -i %1	-l spring -o ..\server -c springBootServerGenerateOptions.json --skip-overwrite

goto end

:fail
echo "generateSpringBootServer.bat <path to specification file>"
goto end

:end
