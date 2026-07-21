# 🚀 KaziFlow Agent

KaziFlow Agent is a production-oriented AI workflow orchestration platform that enables users to build, manage, and execute intelligent workflows powered by Large Language Models (LLMs).

The platform combines FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and OpenRouter to create scalable AI workflows composed of intelligent agents that collaborate to solve real-world business tasks.

---

# Features

- User Authentication (JWT)
- Project Management
- Workflow Management
- AI Agent Management
- Workflow Execution Engine
- Shared Execution Context
- OpenRouter AI Integration
- Prompt Builder Architecture
- Provider Abstraction Layer
- Execution Metrics
- PostgreSQL Database
- Alembic Database Migrations
- Docker Support

---

# Technology Stack

## Backend

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic v2
- Uvicorn

## Authentication

- JWT
- Argon2 Password Hashing

## AI

- OpenRouter
- OpenAI GPT-4.1 Mini
- Provider Abstraction Layer
- Prompt Builder

## DevOps

- Docker
- Git
- GitHub

---

# Architecture

```
               +----------------------+
               |      FastAPI API     |
               +----------+-----------+
                          |
              Authentication Layer
                          |
                Service Layer
                          |
          +---------------+--------------+
          |                              |
     Workflow Engine               Database
          |                              |
    Agent Executor               PostgreSQL
          |
    Prompt Builder
          |
  OpenRouter Provider
          |
      GPT-4.1 Mini
```

---

# Current Capabilities

✅ User Registration

✅ JWT Authentication

✅ Project CRUD

✅ Workflow CRUD

✅ Agent CRUD

✅ Workflow Execution

✅ AI-powered Agent Responses

✅ Execution Context

✅ Execution Metrics

---

# Example Workflow Execution

Input

```
Create an onboarding checklist for a new software engineer joining a fintech company.
```

Output

```
Certainly! Here's a comprehensive onboarding checklist...

• Pre-arrival
• Day 1
• Week 1
• Weeks 2–4
• Ongoing Learning
...
```

---

# Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── auth/
│   ├── core/
│   ├── database/
│   ├── engine/
│   ├── models/
│   ├── prompts/
│   ├── providers/
│   ├── routes/
│   ├── schemas/
│   └── services/
│
├── alembic/
├── docker/
└── docs/
```

---

# Running the Project

Clone the repository

```bash
git clone https://github.com/G1thub001/KaziFlow-Agent.git
```

Navigate into the backend

```bash
cd backend
```

Install dependencies

```bash
uv sync
```

Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=...
SECRET_KEY=...
OPENROUTER_API_KEY=...
MODEL_NAME=openai/gpt-4.1-mini
```

Run database migrations

```bash
alembic upgrade head
```

Start the server

```bash
uv run uvicorn app.main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# Roadmap

## Completed

- Authentication
- Project Management
- Workflow Management
- Agent Management
- AI Workflow Execution
- OpenRouter Integration
- Prompt Architecture
- Execution Metrics

## In Progress

- Multi-Agent Collaboration
- Agent Memory
- Agent Roles
- Conversation History
- Tool Calling

## Planned

- LangGraph-style Workflow Graphs
- Parallel Agent Execution
- Streaming Responses
- RAG Integration
- Vector Database
- Knowledge Base
- Scheduler
- Web Dashboard

---

# Author

**Brian Sing'ombe Kibagendi**

Control Systems Engineer

AI • Cybersecurity • Data Science • Intelligent Automation

---

# License

MIT License