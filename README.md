# 🌐 Portfolio Apps Super Repository

Welcome to the **Portfolio Apps Super Repository** — a unified collection of full-stack, cloud-native, and AI-powered applications developed by **Arpit Srivastava**.  
Each project demonstrates expertise in **FastAPI**, **React/Vite**, **Golang**, **Docker**, and **Render Cloud**, combined with modern DevOps workflows and scalable architecture principles.

---

## 🧩 Projects Included

| Project | Description | Tech Stack | Deployment |
|----------|--------------|-------------|-------------|
| **TwinViz 3D Builder** | 3D visualization and digital-twin platform for architecture and city modeling. | FastAPI · Vite · Nginx · Docker · Render | 🌐 [twinviz-3d-builder.onrender.com](https://twinviz-3d-builder.onrender.com) |
| **FitManager App** | AI-assisted fitness tracker and performance planner. | React · Node.js · MongoDB | 🚧 Coming Soon |
| **SmartNotes AI** | AI-powered note summarization and tagging assistant. | FastAPI · LangChain · Pinecone | 🚧 Coming Soon |
| **Idea Validator AI** | Evaluates and scores startup ideas using AI reasoning. | Next.js · OpenAI API | 🚧 Coming Soon |
| **AgroWatch IoT** | IoT-based smart farming dashboard for real-time analytics. | Golang · MQTT · TimescaleDB | 🚧 Coming Soon |
| **HabitWise AI** | Personalized habit-tracking assistant powered by ML. | Python · Streamlit · SQLite | 🚧 Coming Soon |
| **AutoFlow Engine** | Lightweight workflow automation and job scheduling engine. | FastAPI · Celery · Redis | 🚧 Coming Soon |

---

## 🧱 Repository Structure

Each application is self-contained and can be deployed independently or orchestrated through Docker Compose.

```bash
📦 portfolio-apps/
├── twinviz-3d-builder/
│ ├── backend/ # FastAPI backend (Python)
│ ├── frontend/ # React + Vite frontend (served by Nginx)
│ ├── docker-compose.yml # Local orchestration
│ ├── render.yaml # Cloud deployment definition
│ └── README.md
├── fitmanager-app/
```

---

## 🚀 Deployment Workflow

Each app is **containerized**, **CI/CD enabled**, and deployable to **Render Cloud** or **any Docker-compatible platform**.

### ⚙️ Pipeline Overview

1. **Dockerized builds** for frontend & backend.  
2. **GitHub Actions** triggers automated builds and pushes to registry.  
3. **Render.yaml** defines Render service configuration.  
4. **Zero-downtime deployments** on every `main` branch update.  
5. **Reverse proxy routing** connects `/api` to the backend.

---

## 🧰 Tech Stack Summary

| Category | Tools & Frameworks |
|-----------|--------------------|
| **Frontend** | React, Vite, TailwindCSS, Nginx |
| **Backend** | FastAPI (Python), Golang |
| **Database** | PostgreSQL, MongoDB, SQLite |
| **DevOps** | Docker, Render Cloud, GitHub Actions |
| **AI / ML** | OpenAI API, LangChain, MLflow |
| **Messaging & Workers** | Redis, Celery, MQTT, Kafka |

---

## 🧩 Example App — TwinViz 3D Builder

**TwinViz** is a digital-twin visualization system designed to integrate architectural and spatial data for real-time exploration.

### ✳️ Features

- Upload and visualize 3D models or BIM datasets.  
- Generate contextual city-scale visualizations.  
- Access model metadata through REST API.  
- Deploy seamlessly via Render.

### ▶️ Local Development

```bash
cd twinviz-3d-builder
docker compose up --build

├── smartnotes-ai/
└── ...
```

### Access

- Frontend → [http://localhost:5173](http://localhost:5173)
- Backend → [http://localhost:8000](http://localhost:8000)

### 🧾 Recent Updates

- Added render.yaml for unified frontend + backend deployment.
- Fixed npm install crash (exit code 254) with optimized multi-stage Dockerfile.
- Added memory-safe Node build flags for Render.
- Integrated GitHub Actions for automated CI/CD.
- Improved documentation and local development instructions.

### 💡 Build & Deploy (Manual)

For local Docker or Render testing:

```bash
docker compose down --volumes --remove-orphans
docker system prune -af
docker compose build --no-cache
docker compose up
```

### 🧠 Roadmap

- Add live deployment badges for each app
- Integrate Terraform for infrastructure provisioning
- Add Playwright & Pytest E2E testing
- Expand IoT and AI-driven modules
- Add unified API gateway and observability layer

### 📜 License

- All projects in this repository are distributed under the MIT License, unless otherwise specified.

### 👨‍💻 Author

#### Arpit Srivastava

- Software Engineer · Digital Twin Developer · Cloud & DevOps Specialist
- GitHub: [ArpitUS/portfolio-apps](https://github.com/ArpitUS/portfolio-apps)
- LinkedIn: [Arpit Srivastava](https://www.linkedin.com/in/arpit-u-srivastava/)
- Portfolio (Coming Soon)