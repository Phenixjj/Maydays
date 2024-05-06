pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                dir('maydays') {
                    sh 'npm install'
                }
            }
        }
        stage('Test') {
            steps {
                dir('maydays') {
                    sh './jenkins/scripts/test.sh'
                }
                
            }
        }
    }
}