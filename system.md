# Crewmind - Tally AI Assistant

## 🧠 System Architecture

<img src="./assets/architecture.png" alt="System Architecture" width="800"/>


The system follows a modular hexagonal architecture. The React frontend communicates with a FastAPI backend through clearly defined ports and adapters. MongoDB stores question-response pairs, and an external LLM (e.g., Together.ai) handles dynamic responses.

---

## 💻 Application Screenshots

### 🗨️ Ask Assistant Page

<img src="./assets/ui-ask-1.png" alt="Ask Assistant UI" />

<img src="./assets/ui-ask-2.png" alt="Ask Assistant UI" />

*Above: The main interface where users can submit questions and receive responses in real-time.*

<img src="./assets/api-ask.png" alt="Ask Assistant API" />

*Above: A screenshot of the `POST /api/v1/ask` request via a test client showing the assistant’s response.*

---

### 🕓 History Page

<img src="./assets/ui-history.png" alt="History UI" />

*Above: Displays the full conversation history with past questions and AI responses.*

<img src="./assets/api-history.png" alt="History API" />

*Above: Raw JSON response from the `GET /api/v1/history` endpoint showing stored conversations with timestamps.*
