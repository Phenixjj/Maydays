pipeline {
    agent any
    environment {
        CI='true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'cd maydays && npm install'
            }
        }
        stage('Test') {
            steps {
                sh '.jenkins/scripts/test.sh'
            }
        }
    }
}