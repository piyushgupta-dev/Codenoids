# 🚀 Agentic AI Assistant

An intelligent AI Assistant built using **React**, **FastAPI**, **Ollama**, and **LangChain**. The application combines conversational AI with tool-calling capabilities, allowing users to perform calculations, fetch weather information, analyze GitHub profiles, generate code, and interact with multiple specialized tools through a single chat interface.

---

## ✨ Features

### 🤖 AI Chat Assistant

* Powered by Ollama (Qwen2.5)
* Natural language conversations
* General knowledge and technical assistance

### 🧮 Calculator Tool

* Solves mathematical expressions
* Supports arithmetic operations

### 🌤 Weather Information

* Retrieves weather details for cities
* Displays temperature, humidity, and conditions

### 👨‍💻 GitHub Profile Analyzer

* Fetches GitHub profile information
* Displays followers, repositories, and profile details

### 💻 Code Assistant

* React.js Development
* FastAPI Development
* Python Programming
* JavaScript Programming

### 📄 Resume Assistant

* Resume analysis support

### 🌐 Portfolio Assistant

* Portfolio building guidance

### 🔬 Research Assistant

* Research and information gathering support

### 📊 Sensor Dashboard

* Temperature Monitoring
* Humidity Monitoring
* AQI Monitoring
* Noise Monitoring
* Parking Occupancy Monitoring

### ⚙️ Intelligent Tool Routing

* Automatically detects user intent
* Routes queries to the appropriate tool
* Falls back to the LLM for general conversations

---

## 🏗️ Architecture

```text
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
Query Router
      │
      ▼
Tool Layer
      │
      ▼
Ollama (Qwen2.5)
```

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Tailwind CSS
* JavaScript

### Backend

* FastAPI
* Python

### AI Layer

* Ollama
* Qwen2.5
* LangChain

### APIs

* GitHub API
* Weather API

---

## 📂 Project Structure

```text
project/
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── router.py
│   ├── tools.py
│   └── .env
│
├── src/
│   ├── components/
│   │   └── chatbot.jsx
│   │
│   ├── features/
│   │
│   └── App.jsx
│
├── public/
│
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### Frontend Setup

```bash
npm install
npm run dev
```

### Backend Setup

```bash
cd backend

source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

### Ollama Setup

Install Ollama and pull the model:

```bash
ollama pull qwen2.5:1.5b
```

Verify:

```bash
ollama list
```

---

## 🧪 Example Queries

```text
What is Artificial Intelligence?

25*48

weather delhi

github torvalds

react login page code

resume review

portfolio builder

research machine learning
```

---

## 🎯 Future Improvements

* Conversation Memory
* PDF Analyzer
* Image Analyzer
* Voice Assistant
* Real-Time News Integration
* Authentication System
* Database Integration
* LangGraph Workflows

---

## 👨‍💻 Author

**Piyush Gupta**

B.Tech Computer Science Engineering

GitHub: https://github.com/piyushgupta-dev

LinkedIn: Add Your LinkedIn Profile Here

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
