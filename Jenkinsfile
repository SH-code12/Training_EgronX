pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/SH-code12/Training_EgronX'
            }
        }
        stage('Build Docker image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t shahdelnassag/jenkins_Training.'
                }
            }
        }
        stage('Run Docker container') {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh 'docker stop jenkins-con || true'
                    sh 'docker rm jenkins-con || true'
                    // Run Docker container
                    sh 'docker run -d --name jenkins-con -p 5050:90 shahdelnassag/jenkins_Training'
                }
            }
        }
        stage('Push Docker image') {
            steps {
                script {
                    // Log in to Docker Hub using token
                    sh 'echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin'
                    // Tag the Docker image
                    sh 'docker tag shahdelnassag/jenkins_Training shahdelnassag/jenkins_Training:v1.0.0'
                    // Push the Docker image
                    sh 'docker push shahdelnassag/jenkins_Training:v1.0.0'
                }
            }
        }
    }
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}