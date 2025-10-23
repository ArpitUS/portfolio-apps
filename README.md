# Portfolio Apps

This repository contains a collection of **AI**, **Automation**, and **Digital Twin** microservices developed using **Python**, **Go**, and **cloud-native technologies**.  
Each app is fully containerized with **Docker**, automatically built and published via **GitHub Actions**, and deployed to **Render Cloud**.

---

## Live Deployments

| # | App Name | Description | Stack | Live URL |
|---|-----------|--------------|--------|-----------|
| 1 | **TwinViz 3D Builder** | Digital Twin Visualizer for AEC professionals | FastAPI | [twinviz-3d-builder.onrender.com](https://twinviz-3d-builder.onrender.com) |
| 2 | **AI Interview Coach** | AI-based mock interview system | FastAPI | [ai-interview-coach.onrender.com](https://ai-interview-coach.onrender.com) |
| 3 | **Auto Flow Engine** | Workflow automation engine for SMEs | Go | [auto-flow-engine.onrender.com/health](https://auto-flow-engine.onrender.com/health) |
| 4 | **Career Copilot AI** | Personalized AI career assistant | FastAPI | [career-copilot-ai.onrender.com](https://career-copilot-ai.onrender.com) |
| 5 | **Habitwise AI** | Smart habit tracking system | FastAPI | [habitwise-ai.onrender.com](https://habitwise-ai.onrender.com) |
| 6 | **Freelance Finance Tracker** | Finance and invoicing tracker for freelancers | FastAPI | [freelance-finance-tracker.onrender.com](https://freelance-finance-tracker.onrender.com) |
| 7 | **Agro Watch IoT** | IoT-powered farm monitoring system | Go | [agro-watch-iot.onrender.com/health](https://agro-watch-iot.onrender.com/health) |
| 8 | **FitManager App** | Gym management app with AI features | FastAPI | [fitmanager-app.onrender.com](https://fitmanager-app.onrender.com) |
| 9 | **SmartNotes AI** | AI note generator and summarizer | FastAPI | [smartnotes-ai.onrender.com](https://smartnotes-ai.onrender.com) |
| 10 | **Idea Validator AI** | Startup idea validation and research tool | FastAPI | [idea-validator-ai.onrender.com](https://idea-validator-ai.onrender.com) |

---

## Overview

The **Portfolio Apps** super-repo demonstrates:

- Multi-language microservice architecture (Python + Go)
- Containerized deployments with **Docker**
- Continuous Integration via **GitHub Actions**
- Continuous Deployment via **Render Cloud Deploy Hooks**
- Lightweight, cloud-ready apps for AI and Digital Twin workflows

---

## Tech Stack

| Layer | Technologies |
|--------|---------------|
| **Languages** | Go (1.23.4), Python (3.11) |
| **Frameworks** | FastAPI, Gorilla Mux |
| **Containerization** | Docker (multi-stage builds) |
| **Registry** | GitHub Container Registry (GHCR) |
| **Hosting** | Render Cloud (Oregon Region) |
| **CI/CD** | GitHub Actions (Build → Push → Deploy) |
| **Architecture** | Monorepo with matrix-based pipelines |

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/ArpitUS/portfolio-apps.git
cd portfolio-apps
```
