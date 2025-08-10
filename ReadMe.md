# Training EgronX (DevOps Role)

## Table of content

- [Task 1](#task-1)

- [Task 2](#task-2)


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
| Run docker-compose(Multiple Contaniers) Nginx(WebServer) and MySQL(Web Server)

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

32. Open Nginx on [localhost:9090]

    <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/6b37f226-8b40-4c5e-ba2a-b37e97fac5c5" />

4. Open MySQl on [localhost:3360]

    <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/1b98e138-ebf5-49d7-b00c-5b9263be1c8f" />

5. Stop services:
```
    docker-compose down
```
