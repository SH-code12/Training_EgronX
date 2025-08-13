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
                sh 'docker build -t shahdelnassag/jenkins-training .'
            }
        }
        stage('Run Docker container') {
            steps {
                // Stop and remove any existing container first
                sh 'docker stop jenkins-con || true'
                sh 'docker rm jenkins-con || true'
                // Run the container
                sh 'docker run -d --name jenkins-con -p 5050:90 shahdelnassag/jenkins-training'
            }
        }
        stage('Push Docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USER', passwordVariable: 'DOCKER_HUB_PASS')]) {
                    sh 'echo $DOCKER_HUB_PASS | docker login -u $DOCKER_HUB_USER --password-stdin'
                    sh 'docker tag shahdelnassag/jenkins-training shahdelnassag/jenkins-training:v1.0.0'
                    sh 'docker push shahdelnassag/jenkins-training:v1.0.0'
                }
            }
        }
    }

    post {
        always {
            // Stop and remove the container after pipeline finishes
            sh 'docker stop jenkins-con || true'
            sh 'docker rm jenkins-con || true'
        }
    }
}
