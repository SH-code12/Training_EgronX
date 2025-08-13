# Training EgronX (DevOps Role)

[![Run Password Generator Container](https://github.com/SH-code12/Training_EgronX/actions/workflows/action.yaml/badge.svg)](https://github.com/SH-code12/Training_EgronX/actions/workflows/action.yaml)

## Password Generator
|A simple web application genetate paswords using flask

## Table of content

- [Task 1](#task-1)

- [Task 2](#task-2)

- [Docker](#docker)

- [Jenkins](#jenkins)

## Task 1 
| Install Unbuntu and Docker
- Clik For Ubuntu [Install Ubuntu](https://www.youtube.com/watch?v=mXyN1aJYefc)

```
# Check ubuntu version
    lsb_release -a

# install Docker
    sudo apt install docker.io docker-buildx

# Post installation steps: to run docker without sudo (you may need to restart/relogin for changes to take effect)
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker

# Check version
    docker -v
```
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/3b1678af-bac0-4397-a6c2-ef8ba6c36eee" />

## Task 2
| Run docker-compose(Multiple Contaniers) Make Nginx(WebServer) and MySQL(Web Server)

1. Start services
```
    docker-compose up -d
```
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/ef99a648-78ce-4228-b58c-fbf7de9cb26e" />

2. Check Running Contaniers & Created Images 
```
# Runinng Contaniers
    docker ps

# Created Images 
    docker images

```

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/708b7171-2b58-4e8d-9e9d-02b63a89b270" />

3. Open Nginx on [localhost:9090]

    <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/6b37f226-8b40-4c5e-ba2a-b37e97fac5c5" />

4. Open MySQl on [localhost:3360]

    <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/1b98e138-ebf5-49d7-b00c-5b9263be1c8f" />

5. Stop services:
```
    docker-compose down
```

## Docker
1. Build Image Using Docker
```
    docker build -t shahdelnassag/passwordgenerator:v1.0
```
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/a58097a2-5ebc-4ca8-b162-a5ce539152ea" />

2. Push Image on DockerHub

| [Docker Hub Image](https://hub.docker.com/repository/docker/shahdelnassag/passwordgenerator/general)
```
    docker push shahdelnassag/passwordgenerator:v1.0
```
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/77f8f1eb-bd59-4e62-82a3-c1e5fff2eb8a" />

3. Run docker-compose 

| Make Nginx Reverse Proxy For my app

| Follow Link --> localhost:90/ , Nginx reverse to app

```
    docker-compose up -d
```

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/6efe89b6-f046-473a-9615-a2ac99b96171" />

## Jenkins

```
# Update
    sudo apt update

# install java 
    sudo apt install openjdk-17-jdk -y

# check verstion
    java -version

#Add the Jenkins repository key and source
    curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

    echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

# install jenkins 
    sudo apt update
    sudo apt install jenkins -y

# Enable Jenkins
    sudo systemctl enable jenkins

# Start Jenkins
    sudo systemctl start jenkins

# Check Status
    sudo systemctl status jenkins

## Get admin password
    sudo cat /var/lib/jenkins/secrets/initialAdminPassword

## Add Jenkins to group 
    sudo usermod -aG docker jenkins
# Open it
    localhost:8080/



```
- Show Status

    <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/6640af8a-42a0-4f10-a62d-0e654d8ba892" />

- Build Pipeline

    <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/c57f9052-2474-44ff-a050-ff5246a27494" />

- Image Created By Jenkins

    <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/50e49d9d-f992-407a-bb6c-1f7e93ce2703" />

- Stop Jenkins
```
    sudo systemctl stop jenkins
```
