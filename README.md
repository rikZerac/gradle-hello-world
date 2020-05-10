#Gradle hello world

Sample project to test and build a Java web app using a specific version of [Gradle](https://guides.gradle.org/building-java-web-applications/) 
in [Jenkins in Docker](https://github.com/jenkinsci/docker/blob/master/README.md)

The Java web app is made of one servlet exposing a `GET` ReST endpoint returning a *"hello, world"* message

##Prerequisites

- **Access to [project repository](https://github.com/rikZerac/gradle-hello-world)** 
- **Docker** stable release installed

##Contents

The project is hosted on a [GitHub repository](https://github.com/rikZerac/gradle-hello-world) and contains:

- the [main](https://github.com/rikZerac/gradle-hello-world/tree/master/src/main/java/org/gradle/examples/web) 
and [test](https://github.com/rikZerac/gradle-hello-world/tree/master/src/test/java/org/gradle/examples/web) sources of the Java web app.
The unit test is implemented with *JUnit* and *Mockito*

- a `build.gradle` build system for Gradle written in a Groovy DSL to unit test, build and run the app in an embedded Jetty servlet container

- the `Jenkinsfile` of a declarative pipeline
to automate test and build execution in a *Multibranch Pipeline* job on a Jenkins agent

- a `Dockerfile` with the recipe to build an image of a Jenkins master on an *Alpine Linux OS* with Gradle installed under `PATH` for the `jenkins` user

##Usage
With a shell opened at the **root of the project**:

1. **build a Docker image** using the provided `Dockerfile` and eventually choosing a global Gradle version for `jenkins` user

    ```docker build -t <IMAGE_NAME>:<IMAGE_TAG>  --build-arg gradlever=<GRADLE_VERSION> .```

    If not specified `gradlever` defaults to 6.4

2. **run a detached Docker container** on the created image that launch and expose a Jenkins master on `localhost:8080`

     ```docker run --name <CONTAINER_NAME> -d -p 8080:8080 -p 50000:50000 -v <DOCKER_HOST_JENKINS_HOME>:/var/jenkins_home <IMAGE_NAME>:<IMAGE_TAG>```
     
3. **browse `localhost:8080`** to land on Jenkins initial login page
 
4. **get the generated password to login** for the required initial setup by inspecting container logs:

    ```docker logs <CONTAINER_ID>```

    `<CONTAINER_ID>` is printed on shell stdout by the previous `docker run` command

5. **login and follow the initial setup** steps proposed by Jenkins GUI, *installing the suggested set of plugins*. this includes the declarative pipeline 
plugins required to parse and execute the `Jenkinsfile` of the project

6. **create a new *Multibranch Pipeline* job** by clicking on `New Item` entry on the left menu of Jenkins dashboard and setting 
[https://github.com/rikZerac/gradle-hello-world.git](https://github.com/rikZerac/gradle-hello-world.git) as GitHub branch source

7. *run the created job* which execute `clean`, `test` and `build` gradle tasks through a *Gradle wrapper* which downloads a project specific Gradle
    version(*4.10.3*) if not present in the job workspace und use it to run the tasks. Test reports are visible by browsing
    `build/reports/tests/test/index.html` inside the job workspace. **The built app war is archived** (with job execution fingerprint) and thus can be downloaded 
    from the build summary page  
 
8. hopefully do not find too many bugs =D