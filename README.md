# Dockerized Flask App 🚀

## 📌 Overview

A simple Flask-based web application containerized using Docker. This project demonstrates how to package and run applications in containers.

## 🏗 Architecture

User → Docker Container → Flask App

## ⚙️ Tech Stack

* Python (Flask)
* Docker

## 🚀 Features

* Lightweight containerized app
* Health check endpoint
* Easy deployment

## ▶️ How to Run

### Build Image

```bash
docker build -t dockerized-app .
```

### Run Container

```bash
docker run -d -p 5000:5000 dockerized-app
```

### Access App

* http://localhost:5000
* http://localhost:5000/health

## 📈 Future Improvements

* Add Docker Compose
* Add Nginx reverse proxy
* Deploy to Kubernetes
