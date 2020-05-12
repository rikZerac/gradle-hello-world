# Gradle hello world

Sample project to test and build a Java web app using a specific version of [Gradle][gradle-link] 
in [Jenkins in Docker][jenkins-docker-link]

The Java web app is made of one servlet exposing a `GET` ReST endpoint returning a *"hello, world"* message

## Prerequisites
 
- **Docker** stable release installed

## Contents

The project contains:

- the [main][main-sources-link] 
and [test][test-sources-link] sources of the Java web app.
The unit test is implemented with *JUnit* and *Mockito*

- a `build.gradle` build system for Gradle written in a Groovy DSL to unit test, build and run the app in an embedded Jetty servlet container

- the `Jenkinsfile` of a declarative pipeline
to automate test and build execution in a *Multibranch Pipeline* job on a Jenkins agent

- a `Dockerfile` with the recipe to build an image of a Jenkins master on an *Alpine Linux OS* with Gradle installed under `PATH` for the `jenkins` user

- a `plugins.txt` file listing a reference set of plugins to be preinstalled when building the Jenkins master Docker image, 
including declarative pipeline ones required to parse and execute the `Jenkinsfile`

- a simple [*Python 3* module][list-plugins-module-link] to list plugins installed on a Jenkins instance via `http`

## Usage
With a shell opened at the **root of the project**:

1. **build a Docker image** using the provided `Dockerfile`, eventually choosing Jenkins version and global Gradle version for `jenkins` user:

    ```docker build -t <IMAGE_NAME>:<IMAGE_TAG>  --build-arg gradleVer=<GRADLE_VERSION> --build-arg jenkinsVer=<JENKINS_VERSION> .```

    If not specified `jenkinsVer` defaults to **`2.235`** and `gradleVer` defaults to **`6.4`** 

2. **run a detached Docker container** on the created image that launch and expose a Jenkins master on `localhost:8080`

     ```docker run --name <CONTAINER_NAME> -d -p 8080:8080 -p 50000:50000 -v <DOCKER_HOST_JENKINS_HOME>:/var/jenkins_home <IMAGE_NAME>:<IMAGE_TAG>```
     
     Mounting a Docker host named volume on `/var/jenkins_home` allows to persist all data that the instance will produce when running(like *jobs* 
     and *workspaces*) so to backup and reuse them
     
3. **browse `localhost:8080`** to land on Jenkins dashboard as **anonymous** user
> The provided `Dockerfile` configures the Jenkins instance to have a **preinstalled set of plugins** read from [`plugins.txt`][plugins-txt-link] 
> and with **initial admin login and setup wizard disabled**. This is intended to have a recipe to provide preconfigured Jenkins instances
> on the fly, deciding a custom set of plugins in a declarative way through a bare and versionable text file which acts as a 'shopping list'.
> This approach is very comfortable for scenarios like spawning a Jenkins instance to develop and try a `Jenkinsfile` and provisioning 
> ready torun new fresh instances or replicas on demand. **Of course in the case of a Jenkins instance used to streamline production CI/CD, 
> it is required to secure it via the GUI (`Manage Jenkins`) or by removing initial set disabling in the `Dockerfile`**

4. **create a new *Multibranch Pipeline* job** by clicking on `New Item` entry on the left menu of Jenkins dashboard and setting 
[https://github.com/rikZerac/gradle-hello-world.git][github-link] as GitHub branch source

5. **run the created job** which execute `clean`, `test` and `build` gradle tasks through a *Gradle wrapper* which downloads a project specific Gradle
    version(*4.10.3*) if not present in the job workspace und use it to run the tasks. Test reports are visible by browsing
    `build/reports/tests/test/index.html` inside the job workspace. **The built app war is archived** (with job execution fingerprint) and thus can be downloaded 
    from the build summary page  
 
6. hopefully do not find too many bugs =D

[gradle-link]: https://guides.gradle.org/building-java-web-applications/
[jenkins-docker-link]: https://github.com/jenkinsci/docker/blob/master/README.md
[main-sources-link]: https://github.com/rikZerac/gradle-hello-world/tree/master/src/main/java/org/gradle/examples/web
[test-sources-link]: https://github.com/rikZerac/gradle-hello-world/tree/master/src/test/java/org/gradle/examples/web
[list-plugins-module-link]: https://github.com/rikZerac/gradle-hello-world/tree/master/list-jenkins-plugins
[plugins-txt-link]:  https://github.com/rikZerac/gradle-hello-world/blob/master/plugins.txt
[github-link]: https://github.com/rikZerac/gradle-hello-world.git