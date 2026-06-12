# 💜 MINDWELL.AI | Mental Health Support Chatbot v1.0

MINDWELL.AI is an AI-powered conversational web application designed to provide accessible, 24/7 emotional support and mental wellness guidance. By analyzing text input, the system delivers empathetic responses and evidence-based coping strategies (such as CBT techniques) for users experiencing mild-to-moderate stress or anxiety, while integrating strict safety guardrails for high-distress scenarios.

⚠️ **CRITICAL DISCLAIMER:** This application is **not a replacement for professional therapy, clinical diagnosis, or medical treatment**. It functions strictly as a self-led emotional well-being tool.

---

## 🚀 Key Features

* **Empathetic AI Conversationalist:** Utilizes a trained classification and response generation pipeline to deliver context-aware, compassionate interactions.
* **Safety & Crisis Intercept:** Integrates a deterministic regex and keyword-matching layer to instantly detect self-harm or high-distress triggers.
* **Emergency Escalation Protocol:** Bypasses standard AI generation when a crisis is detected, instantly routing the user to official, localized helpline resources.
* **Modern Elite Interface:** Features a calming, responsive dark-themed UI designed to reduce visual stress and provide a clean, distraction-free user experience.
* **Character Engagement Verification:** Ensures inputs meet minimum length thresholds to provide stable, context-rich responses.

---

## 🛠️ Tech Stack & Architecture

* **Frontend:** HTML5, CSS3 (Calming Dark-Theme UI), Vanilla JavaScript
* **Backend Framework:** Flask (Python)
* **Machine Learning & NLP:** Scikit-learn, Joblib, NLTK / Transformers
* **Core Models Built With:** Text Classification / Vectorization Pipelines

---

## 📂 Project Structure

```text
MentalHealthBot/
├── models/
│   ├── intent_classifier.joblib
│   └── text_vectorizer.joblib
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── data/
│   └── wellness_responses.json
└── MentalHealthBot.py
