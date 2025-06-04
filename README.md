# 💬 AI Chatbot with Gemini API + FastAPI

This project is a smart AI-powered chatbot built using **FastAPI** (Python) and **Gemini AI (by Google)** for conversational responses. It offers both intelligent generative replies and instant FAQ-based fallback for known queries.

## ✨ Features

- 🤖 Gemini Pro AI-generated responses
- 📚 Predefined FAQ fallback for fast replies
- 💬 Frontend chat interface using HTML, CSS & JS
- ⏳ Typing indicator effect for a real feel
- 🔐 API Key managed via `.env` for security
- 🔁 Seamless frontend-backend integration


## 🗂️ Project Structure

chatbot_project/
├── main.py # FastAPI server & route definitions
├── chatbot.py # Gemini integration & fallback logic
├── data.py # Dictionary of predefined FAQs
├── .env # Gemini API key
├── templates/
│ └── index.html # Chatbot UI (frontend)
├── static/
│ ├── style.css # Styles for chat layout
│ └── script.js # JavaScript to handle chat
└── README.md # Project documentation


---

## ⚙️ Getting Started

### 1. 📦 Install Dependencies

```bash
pip install fastapi uvicorn python-dotenv google-generativeai


2. 🔑 Set Your Gemini API Key
Create a file named .env in the root folder:

GEMINI_API_KEY=your_gemini_api_key_here
💡 You can get your API key from https://makersuite.google.com/app/apikey

3. 🚀 Run the App
bash:
uvicorn main:app --reload
Visit: http://127.0.0.1:8000


🛠️ Built With

- FastAPI – Python web framework

- Google Generative AI (Gemini) – For generative responses

- HTML/CSS/JavaScript – Frontend user interface

- dotenv – Environment variable management


📈 Future Enhancements

💬 Store chat history using SQLite or MongoDB

🌐 Multi-language support

🔊 Text-to-speech/Voice chat

👤 User authentication and profiles

📱 Responsive mobile layout

🤝 Contribution
Feel free to fork this repo and contribute via pull requests!

🌟 Star this repo

🍴 Fork it

🛠️ Make your changes

📩 Submit a pull request

📄 License

MIT License © 2025 Rudra Mohan Mishra
