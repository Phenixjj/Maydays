pipeline {
    agent any
    environment {
        CI='true'
    }
    stages {
        stage('Build') {
            steps {
                cd maysdays
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh '.jenkins/scripts/test.sh'
            }
        }
    }
}