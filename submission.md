# 🤖 Nexa Assistant – Fullstack AI Q&A System

A minimal fullstack assistant that allows users to ask questions and receive AI-generated responses. Built using Clean Hexagonal Architecture with FastAPI, MongoDB, and React (TypeScript).

---

## 🧱 Features

- ✅ Ask a question → Get an AI-generated answer
- ✅ Stores all Q&A pairs with timestamps
- ✅ View full conversation history
- ✅ Modern, typed, modular backend & frontend
- ✅ Clean architecture with separation of concerns
- ✅ Docker + Compose setup

---

## 🧰 Tech Stack

| Layer        | Tech                               |
|--------------|------------------------------------|
| **Frontend** | React (TypeScript), Axios, Vite    |
| **Backend**  | FastAPI, Motor (async Mongo), Pydantic |
| **AI**       | Together.ai API (can plug any LLM) |
| **Database** | MongoDB                            |
| **Infra**    | Docker, Docker Compose, dotenv     |
| **Testing**  | Pytest (backend)                   |

---

## 🚀 How to Run Locally

### 🔧 Prerequisites

- Node.js + npm
- Python 3.11+
- Docker + Docker Compose
- MongoDB (if running locally)

---

### 📦 Backend

```bash
# Clone the repo
git clone https://github.com/your-username/nexa-assistant.git
cd nexa-assistant/backend

# Create virtualenv and install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cd ../
# Create .env file
cp .env.example .env

# Run backend with docker
docker compose -f docker-compose.yml up --build
```

Or run locally with:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

### 🌐 Frontend

```bash
cd ../frontend

# Install deps
npm install

# Start dev server
npm run dev
```

Visit: [http://localhost:5173](http://localhost:5173)

---

## 🔗 API Endpoints

| Method | Endpoint         | Description                     |
|--------|------------------|---------------------------------|
| POST   | `/api/v1/ask`     | Submit question, get response   |
| GET    | `/api/v1/history` | Fetch all past Q&A conversations |

---

## 🧪 Run Tests

```bash
cd backend
pytest
```

---

## 💡 Improvements With More Time

- ✅ Add streaming/tokenized responses
- ✅ Full CI/CD pipeline (GitHub Actions)
- ✅ JWT authentication / auth service
- ✅ Admin panel (manage history, rate limits)
- ✅ Switchable LLM adapters via config
- ✅ Refine the UI to have a chat-like interface and clean UI

---

