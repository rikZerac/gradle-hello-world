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
                  shell 'gradle clean test'
                }
            }
        }
        stage('Build'){
            steps {
                script{
                    shell 'gradle build'
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