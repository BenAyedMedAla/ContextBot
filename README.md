# 🌾 Agricultural Chatbot

An intelligent chatbot that uses Google’s **Gemini AI** to answer agriculture-related questions. It supports both direct Docker usage and local customization with easy deployment.

---

## 🚀 Features

* 🌐 Natural language Q\&A on agricultural topics
* 🤖 Powered by **LangChain** + **Google Generative AI (Gemini 2.0 Flash)**
* 🔐 Uses secure environment variable for your API key
* 🐳 Runs in **Docker** — no local setup required

---

## ✅ Quick Start

### Option 1: **Run Directly with Docker (No Build Required)**

> Ideal if you just want to test or use the chatbot without modifying the knowledge base.

Make sure you have Docker installed. You can [download Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows or Mac.

1. Get your Google API Key from [Google AI Studio](https://makersuite.google.com/app).
2. Replace `"your-api-key"` with your actual key and run:

```bash
docker run -p 5000:8000 -e API_KEY="your-api-key" alabenayed/agricultural-chatbot
```

> The chatbot will be available at: [http://localhost:5000/ask](http://localhost:5000/ask)


### Option 2: **Modify the `.txt` Knowledge Base**

> Use this if you want to change or extend the chatbot's knowledge.

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/agricultural-chatbot.git
cd agricultural-chatbot
```

2. Modify the `.txt` files in the knowledge base folder as needed.

3. Rebuild the Docker container:

```bash
docker build -t agricultural-chatbot .
docker run -p 5000:8000 -e API_KEY="your-api-key" agricultural-chatbot
```

---

## 📬 How to Ask a Question

You can interact with the chatbot in two ways:

* **From a frontend interface** (if included).
* **Using Postman or CURL**:

Send a POST request to:

```
http://localhost:5000/ask
```

With JSON body:

```json
{
  "messageText": "quand on cultive fraise ?"
}
```

---

## 🔍 Test Questions

Here are some sample questions to test different categories:

### 🌱 Cultures et Plantes

* Quels sont les besoins de la fraise au printemps ?
* Quelle est la meilleure période pour semer les carottes ?
* Le poireau craint-il l’excès d’eau ?

### 🐄 Élevage

* Quelle est la différence entre bovins viande et bovins lait ?
* Que faire pour prévenir la mammite chez les vaches ?

### 🧻 Maladies et Ravageurs

* Quels sont les symptômes de la rouille jaune sur le blé ?
* Comment lutter naturellement contre le mildiou de la tomate ?

### 💧 Irrigation et Sols

* Quels sont les différents types d’irrigation ?
* Comment améliorer un sol argileux pour les légumes ?

### ☁️ Climat et Météo

* Quelle culture choisir en zone semi-aride ?
* Quels outils permettent d’anticiper les aléas climatiques ?

### 🚜 Mécanisation

* Quel matériel est recommandé pour semer le blé ?
* À quoi sert le strip-till ?

### 💶 Économie et Réglementation

* Comment calculer la marge brute d’une culture ?
* Quelles aides agricoles sont disponibles via la PAC ?

---
