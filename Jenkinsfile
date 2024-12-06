pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'python3 test.py'
            }
        }
    }
}