# 🤖 My First AI App

A command-line (CLI) AI chat assistant powered by Google's **Gemini 2.5 Flash** model. This application implements a persistent loop to accept user messages, maintains session-based conversation history, and prints streaming-like model responses directly in your terminal.

---

## 🏗️ Technology Stack

- **Language**: Python 3
- **AI SDK**: Google Generative AI (`google-generativeai`)
- **Model**: `gemini-2.5-flash`
- **Utility**: `python-dotenv` (for secure environment variable handling)

---

## 🛠️ Project Structure

```text
my-first-ai-app/
├── app.py              # Main CLI application script
├── requirements.txt    # Required python dependencies
├── .gitignore          # Git exclusion specifications
└── README.md           # Documentation
```

---

## ⚙️ Configuration & Environment Setup

The application retrieves its credentials from environment variables.

1. Create a file named `.env` in the root of the project.
2. Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> [!TIP]
> You can acquire a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

---

## 🚀 Getting Started

### 1. Install Dependencies
Run the package installer to configure your environment:

```bash
pip install -r requirements.txt
```

### 2. Run the App
Launch the interactive CLI session:

```bash
python app.py
```

### 3. Usage & Navigation
- Type a query at the `You: ` prompt and press `Enter` to converse with Gemini.
- The assistant remembers previous exchanges in the active session.
- Type `exit` (case-insensitive) to close the application.
