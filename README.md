# Speculative Speculative Decoding

**Research Paper:** [https://arxiv.org/pdf/2603.03251v3](https://arxiv.org/pdf/2603.03251v3)

## The Mission
The inefficiency of autoregressive decoding in natural language processing (NLP) models leads to slow response times, limiting the usability of advanced AI systems in real-time applications such as conversational AI, language translation, and content generation.

## Architecture
The solution involves creating a high-performance, scalable NLP inference system leveraging the Speculative Speculative Decoding (SSD) algorithm to accelerate model response times. The architecture includes a backend service for SSD-based inference (Python, PyTorch/TensorFlow), a frontend for user interaction (React.js), an ML microservice for SSD optimization, and containerized deployment using Docker and Kubernetes for scalability.

## Services

### Backend
- Framework: FastAPI
- Endpoints:
  - `/health`: Health check endpoint
  - `/inference`: Endpoint for SSD-based inference

### Frontend
- Framework: React.js
- Basic setup with a welcome page

### ML Microservice
- Framework: Flask
- Endpoints:
  - `/optimize`: Endpoint for SSD optimization
  - `/health`: Health check endpoint

## Deployment
- Dockerized services
- Multi-service orchestration using Docker Compose

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Steps
1. Clone the repository.
2. Run `docker-compose up --build` to start all services.
3. Access the frontend at `http://localhost:3000`.
4. Access the backend API at `http://localhost:8000/docs`.
5. Access the ML service at `http://localhost:5000/health`.
