# 🤖 AI FAQ Chatbot

## 📌 Project Overview

The AI FAQ Chatbot is an NLP-based chatbot developed as part of the CodeAlpha Internship - Task 2.

This project uses Natural Language Processing techniques to understand user queries and provide relevant answers from a predefined FAQ knowledge base. Unlike traditional rule-based chatbots, this chatbot uses semantic similarity to understand the meaning of questions and generate accurate responses even when the user asks questions in different ways.

---

## ✨ Features

* 🤖 AI-powered question understanding
* 🧠 NLP-based semantic similarity matching
* 💬 Interactive chatbot interface
* 🔍 Understands different variations of questions
* ⚡ Fast and relevant responses
* 🎨 User-friendly Gradio interface
* ❓ Handles unknown questions gracefully

---

## 🛠️ Technologies Used

* Python
* Gradio
* Sentence Transformers
* Natural Language Processing (NLP)
* Scikit-learn

---

## ⚙️ How It Works

1. The user enters a question through the chatbot interface.
2. The question is converted into a numerical representation using a Sentence Transformer model.
3. The chatbot compares the question with stored FAQ questions using similarity matching.
4. The most relevant question is identified.
5. The corresponding answer is displayed to the user.

---

## 📂 Project Structure

```
CodeAlpha_AI_FAQ_Chatbot
│
├── app.py
├── faq_data.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Usage

### 1. Clone the repository

```
https://github.com/gaganasrijag/CodeAlpha_FAQ_Chatbot
```

### 2. Install required libraries

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open the Gradio local URL in your browser and start asking questions.

---

## 👩‍💻 Author

Gagana Srija 
