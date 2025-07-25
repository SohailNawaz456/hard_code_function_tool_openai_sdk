# 🧠 General Agent with Tool Calling (USD to PKR)

This project demonstrates a basic AI agent framework using a custom `function_tool` that allows the agent to answer queries like **"What is 1 USD to PKR?"**. The agent uses a built-in Python function decorated with `@function_tool`.

---

## 📦 Features

- Agent class with instructions
- Tool function: `usd_to_pkr`
- Runner class for executing queries
- `.env` integration for API keys
- Clean and extendable agent-tool structure

---

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name


Create and activate a virtual environment:


python -m venv .venv
source .venv/bin/activate  # on Windows use: .venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Add your .env file:
Create a .env file with your Gemini API key:

GEMINI_API_KEY=your_api_key_here
🚀 How to Run
Run your tool-enabled agent with the following command:


uv run tool.py
Sample output:

mathematica

Today 1 USD = 280 PKR
🧪 Project Structure

project-root/
│
├── agents/
│   └── __init__.py  # Contains Agent, Runner, function_tool, etc.
│
├── main.py          # Loads config using API key and model
├── tool.py          # Main script with agent and function tool
├── .env             # Contains your GEMINI_API_KEY
├── requirements.txt
└── README.md        # This file
👨‍💻 Author
Sohail Nawaz

LinkedIn
GitHub: SohailNawaz456

📜 License
This project is for educational and development purposes. You may extend or modify it freely.


---

Let me know if you'd like this content saved to a real `README.md` file, or if you want me to upload it to your 
