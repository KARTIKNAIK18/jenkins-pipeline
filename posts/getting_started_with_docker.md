# Getting Started with Docker 🐳

Docker makes it easier to build, ship, and run apps. Here's how to start:

## Why Docker?
- Isolate environments
- Reproducible builds
- Easier deployment

## Basic Commands

```bash
docker build -t my-app .
docker run -p 3000:3000 my-app
docker ps
docker stop <container_id>
