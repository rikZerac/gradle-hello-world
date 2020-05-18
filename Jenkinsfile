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

String workDir

pipeline{
    agent any
    stages {
        stage('Test'){
            steps {
                script{
                    workDir = pwd()
                    //switch to a project specific Gradle version
                    shell "gradle wrapper --gradle-version=4.10.3"
                    shell "${workDir}/gradlew clean test"
                    junit 'build/test-results/**/*.xml'
                }
            }
        }
        stage('Build'){
            steps {
                script{
                    shell "${workDir}/gradlew build"
                }
            }
        }
        stage('Deploy'){
            steps {
                archiveArtifacts artifacts: 'build/libs/*.war', fingerprint: true
            }
        }
    }
}