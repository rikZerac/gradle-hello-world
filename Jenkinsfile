/*
Abstract the underline OS
Used a closure instead of a function in order to
have a first class object in the scope of pipeline model class run method
*/
Closure<Void> shell = {
    if (isUnix()){
        sh it
    } else {
        bat it
    }
}

pipeline{
    agent any
    stages {
        stage('Test'){
            steps {
                script{
                    //switch to a project specific Gradle version
                    shell 'gradle wrapper --gradle-version=4.10.3 '
                    shell 'gradlew clean test'
                }
            }
        }
        stage('Build'){
            steps {
                script{
                    shell 'gradlew build'
                }
            }
        }
        stage('Deploy'){
            steps {
                archiveArtifacts artifacts: 'build/libs/gradle-hello-world.war', fingerprint: true
            }
        }
    }
}