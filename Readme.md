# Persona – Customizable AI Friend

## Overview

Persona is a customizable AI friendship chatbot inspired by the idea of long-term conversational memory found in modern AI assistants. Rather than simply answering questions, Persona is designed to build a lasting friendship by remembering important details about the user and adapting its personality to match individual preferences.

This project is a **demo/prototype** that explores personalized AI companionship. It is **not a copy of ChatGPT**, but instead demonstrates how conversational memory and personality customization can be combined into a friendship-focused AI experience.

---

## Features

### Personality Customization

Before chatting, users answer a short questionnaire to define how their AI friend should behave.

The AI can be customized based on:

* Support style
* Honesty style
* Humor style
* Energy level
* Conversation style
* Friend role (Best Friend, Mentor, Study Buddy, Emotional Support, Motivator)

With the available options, Persona can create **3,600 unique personality combinations**, making every AI friend feel different.

---

### Long-Term Memory

Persona remembers meaningful information shared by the user, including:

* Name
* Nickname
* Age
* Education
* School/College
* Profession
* Goals
* Hobbies
* Favourite things
* Pets
* Relationships
* Permanent preferences
* Nicknames the user gives the AI
* Important life events

Instead of storing rigid key-value pairs, memories are stored as natural language statements with an importance score, making them easier to retrieve and more human-like.

Example:

User:

> My pet cat is Lilly.

Stored Memory:

> The user has a pet cat named Lilly.

Importance:

> 0.95

---

### Conversation Memory

Persona can:

* Remember previous conversations
* Create separate chat histories
* Generate chat titles automatically
* Recall important information during future conversations

---

### Memory Management

Users can:

* View saved memories
* Edit memories
* Delete memories

---

### AI Responses

Persona generates replies based on:

* User personality preferences
* Stored long-term memories
* Current conversation context

This allows conversations to become more personal over time.

---

### Text-to-Speech

Every AI response can be played aloud using browser-based Text-to-Speech, making conversations feel more interactive.

---

## Tech Stack

### Backend

* Python
* Flask
* SQLite

### AI

* Ollama
* Large Language Model (LLM)

### Frontend

* HTML
* CSS
* JavaScript

---

## Future Improvements

* Multi-user authentication
* Semantic memory retrieval (RAG)
* Vector database support
* Voice input
* AI avatar
* Emotion detection
* Better long-term memory ranking
* Memory summarization
* Mobile application

---

## Purpose

This project was built as a demonstration of how personalized conversational AI can go beyond question answering by focusing on friendship, memory, and personality.

## Installation

### 1. Clone the repository

```bash
git https://github.com/sayoojsk28/PERSONA.git
```

### 2. Create a virtual environment (Optional but recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Create a .env file

Create a .env file in the project's root directory and add:

SECRET_KEY=your_secret_key_here

You can use any random secret string, for example:

SECRET_KEY=my_super_secret_key_123

### 5. Install and start Ollama

Download and install Ollama from:

https://ollama.com/download

Then pull the model used by the project (replace with your model if different):

```bash
ollama pull llama3.2:latest
```

Start the Ollama server if it isn't already running:

```bash
ollama serve
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

```
http://127.0.0.1:5000
```



It serves as a proof of concept for customizable AI companions rather than a replacement for existing general-purpose AI assistants.
