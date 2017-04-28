##Server API Code##

This folder will contain the generated server application using the API.

If you delete the folder, it is generally suggested that you do NOT delete the build.gradle file (is useful for the Spring Boot server generated). 

Rather, simply run "gradle clean build"

If you changed the contents of the springBootServerGenerateOptions.json configuration file, then change the manifest main target in the build.gradle file to your particular application main class package.