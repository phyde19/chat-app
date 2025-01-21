# Blue Pilot Setup

## Prerequisites

Before starting, ensure you have podman-compose installed:

```bash
pip install podman-compose
```

## Getting Started

### Starting the Application

From the project root directory, run:

```bash
podman-compose up -d --build
```

This command:
- Builds the container images (`--build`)
- Runs the containers in detached mode (`-d`)


> 🕒 Note! The first build will take longer since it needs to download base images and install dependencies


### Verify Running Containers

Check the status of your containers:

```bash
podman ps
```

This will show both the frontend and backend containers with their respective ports and status.

### Viewing Logs

To watch the logs from both services in real-time:

```bash
podman-compose logs -f
```

### Stopping the Application

To stop and remove the containers:

```bash
podman-compose down
```

### Ports
The frontend runs on port 3000 and the backend on port 8000 in development mode.

## Note on Dockerfile Structure

If you're wondering about the multiple stages in the docker files (i.e. dev -> prod or dev -> build -> prod in the frontend) - we use a multi-stage build approach. This corresponds to the `target: dev` in the docker-compose.yaml file. It means only run the `dev` stage! This makes the Dockerfiles longer but it separates development and production environments. This will be relevant when deploying to OpenShift where it helps creating smaller, more efficient images by including only what's needed to run the application.