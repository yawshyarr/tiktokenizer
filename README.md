<div align="center">

<br/>

```
 _____     _              _
|_   _|__ | | _____ _ __ (_)_______ _ __
  | |/ _ \| |/ / _ \ '_ \| |_  / _ \ '__|
  | | (_) |   <  __/ | | | |/ /  __/ |
  |_|\___/|_|\_\___|_| |_|_/___\___|_|
```

### 🔢 Visual Token Explorer for GPT-2, GPT-4 & GPT-4o

<br/>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![Tiktoken](https://img.shields.io/badge/Tiktoken-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

<br/>

> **Tokenizer** is a lightweight web app that lets you visually explore how AI language models split text into tokens — with live stats, frequency charts, and support for multiple GPT encoding schemes.

<br/>

---

</div>

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Supported Encodings](#-supported-encodings)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [How Tokenization Works](#-how-tokenization-works)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **Visual Token Highlighting** | Each token rendered with a unique color — hover to inspect, click to pin |
| 🔢 **Token ID Display** | See the raw integer IDs assigned to each token |
| 📊 **Live Statistics** | Total tokens, unique tokens, character count, average token length |
| 📈 **Frequency Chart** | Top 8 most frequent tokens displayed in a bar chart |
| 🔄 **Multi-Model Support** | Switch between GPT-2, GPT-4, and GPT-4o encodings instantly |
| ⚡ **Real-Time Analysis** | Results update as you type — no page reloads |
| 🌑 **Dark UI** | Sleek dark interface with noise texture and smooth animations |

---

## 🎬 Demo

```
Input:  "Hello, how are you today?"

Tokens (cl100k / GPT-4):
┌────────┬────────┬────────┬────────┬────────┬─────────┐
│ Hello  │   ,    │  how   │  are   │  you   │ today?  │
└────────┴────────┴────────┴────────┴────────┴─────────┘

Token IDs:  [9906, 11, 1268, 527, 499, 3432, 30]

Stats:  7 tokens · 6 unique · 25 chars · avg length 3.4
```

---

## 🧩 Supported Encodings

| Model Key | Encoding | Used By |
|---|---|---|
| `gpt2` | `gpt2` | GPT-2 |
| `cl100k` | `cl100k_base` | GPT-3.5-turbo, GPT-4 |
| `o200k` | `o200k_base` | GPT-4o |

> Different models tokenize the same text differently — this tool lets you compare them instantly.

---

## 🛠️ Tech Stack

```
┌──────────────────────────────────────────┐
│               FRONTEND                    │
│  HTML · CSS · Vanilla JS                 │
│  Fonts: Syne (display) + DM Mono (code)  │
├──────────────────────────────────────────┤
│               BACKEND                    │
│  Flask (Python) · Tiktoken (OpenAI)      │
│  REST API · JSON responses               │
└──────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

---

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/tokenizer-app.git
cd tokenizer-app
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> **requirements.txt** contains:
> ```
> flask
> tiktoken
> ```

---

### 3. Run the App

```bash
python app.py
```

Open your browser and go to:

```
http://localhost:5000
```

No `.env` file, no API keys, no database needed! ✅

---

## 📡 API Reference

### `POST /tokenize`

Tokenizes the given text using the specified model encoding.

**Request Body:**

```json
{
  "text": "Hello world",
  "model": "cl100k"
}
```

**Model options:** `gpt2` · `cl100k` · `o200k`

**Response:**

```json
{
  "tokens": ["Hello", " world"],
  "ids": [9906, 1917],
  "stats": {
    "total": 2,
    "unique": 2,
    "chars": 11,
    "avg_len": 5.0,
    "top": [["Hello", 1], ["world", 1]]
  }
}
```

| Field | Type | Description |
|---|---|---|
| `tokens` | `string[]` | Human-readable token strings |
| `ids` | `int[]` | Integer token IDs |
| `stats.total` | `int` | Total number of tokens |
| `stats.unique` | `int` | Number of unique tokens |
| `stats.chars` | `int` | Total character count |
| `stats.avg_len` | `float` | Average characters per token |
| `stats.top` | `array` | Top 8 most frequent tokens |

---

## 📁 Project Structure

```
tokenizer-app/
├── app.py                  ← Flask server + /tokenize endpoint
├── requirements.txt        ← Python dependencies
├── README.md
└── static/
    └── index.html          ← Full frontend (HTML + CSS + JS)
```

---

## 🧠 How Tokenization Works

Large language models don't read text character by character — they read **tokens**.

A token is a chunk of text, typically 3–5 characters. The model converts your text into a sequence of integer token IDs, then processes those numbers.

```
"tokenization"  →  ["token", "ization"]  →  [4263, 2065]
```

**Why does it matter?**
- API costs are calculated per token
- Context windows are measured in tokens
- Different models use different tokenizers — same text, different token counts

This tool uses **tiktoken** (OpenAI's official tokenizer library) to give you exact, production-accurate token counts for each model.

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

Made with ❤️ yawshyarr ·
Give it a ⭐ if you found it useful!

</div>
