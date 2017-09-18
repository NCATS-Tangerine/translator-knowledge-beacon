## Swagger Codegen Tutorial for Python Flask apps

This tutorial will guide you through using [swagger-codegen](https://github.com/swagger-api/swagger-codegen) to generate a Python Flask server project stub. This tutorial will be most complete for Linux users, OSX and Windows users may need to consult the Swagger documentation for further details.

You should use Python version 3.5, in your terminal run `python --version` to check that you are up to date.

**1. Download `swagger-codegen-cli.jar`.** The latest stable version can be downloaded directly from Maven.org (Java 7 runtime at minimum).
```
wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.3/swagger-codegen-cli-2.2.3.jar -O swagger-codegen-cli.jar
```
On OSX you can use brew:
```
brew install swagger-codegen
```
A more detailed explanation can be found at https://github.com/swagger-api/swagger-codegen#prerequisites

**2. Generate the server project stub.** The `-i` flag is for the yaml or json specification file, the `-l` flag is for the project language, and the `-o` flag sets the directory name that the project will be generated into.
```
java -jar swagger-codegen-cli.jar generate -i specification.json -l python-flask -o server
```
If we run this command, it will generate a project structure looking like the following. Much of what will be generated has been omitted for clarity.
```
.
├── server
│   ├── requirements.txt
│   ├── swagger_server
│   │   ├── controllers
│   │   ├── models
│   │   ├── swagger
│   │   │   └── swagger.yaml
│   │   └── test
└── swagger-codegen-cli.jar
```
Your project will require version 1.1.15 or newer of Connexion. If the version is set to 1.1.9 in `requirements.txt` then change it. (This should be automatic in the near future).
Official documentation can be found here: https://github.com/swagger-api/swagger-codegen/wiki/Server-stub-generator-HOWTO#python-flask-connexion

**3.  Implement your beacon.** Take a look in the `controllers` directory, you will see a number of files that contain a stub function call for each of the API calls. You can now fill these stubs out. Use the swagger generated model classes, contained in the `models` directory.

**4.  Running your beacon**. Install the requirements with `pip`, and then run the `swagger_server` module with python.
```
pip install -r requirements.txt
python -m swagger_server
```
Your server should now be running at http://localhost:8080.
