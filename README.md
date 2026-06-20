# 🦜 LangChain & Gen AI Projects — Learning Journey

> From zero to building a live AI Chatbot with multi-turn memory — everything documented, every line written from scratch.

---

## 👋 What is this repo?

This is my **hands-on exploration of the Gen AI ecosystem** using LangChain.

No copy-paste tutorials. Every script was written, broken, debugged, and fixed by me while learning how LLMs, Chat Models, Embeddings, and Prompt Engineering actually work under the hood.

If you're starting your Gen AI journey — this repo is your free launchpad. 🚀

---

## 📁 Project Structure

```
gen-ai-projects/
│
├── 1.LLMS/
│   └── llm_demo.py                  # LLM basics using HuggingFace
│
├── 2.Chatmodels/
│   ├── 1_chatmodel_openai.py        # OpenAI GPT Chat Model
│   ├── 2_chatmodel_anthro.py        # Anthropic Claude Chat Model
│   ├── 3_chatmodel_google.py        # Google Gemini Chat Model
│   └── 4_chatmodel_hf_api.py        # HuggingFace Chat Model ✅ Free & Working
│
├── 3.Embeddedmodels/
│   ├── embedding_hf_local.py        # HuggingFace Local Embeddings
│   ├── openai_docs.py               # OpenAI Embeddings on Docs
│   └── openai.py                    # OpenAI Embeddings
│
├── chatbot.py                       # ✅ AI Chatbot with Streamlit UI
├── prompt_generator.py              # Dynamic Prompt Generator
├── prompt_template.json             # Saved Prompt Template
├── prompt_ui.py                     # Streamlit Prompt UI App
├── requirements.txt                 # Dependencies
├── .env.example                     # Environment variables template
└── README.md                        # You are here
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🦜 LangChain | LLM orchestration framework |
| 🤗 HuggingFace | Free LLMs and local embeddings |
| 🟢 OpenAI | GPT Chat Models |
| 🟣 Anthropic | Claude Chat Models |
| 🔵 Google | Gemini Chat Models |
| 🎈 Streamlit | UI for Chatbot and Prompt apps |
| 🐍 Python | Core language |

---

## ✅ Free Projects — No Paid API Needed

| File | What it does | Status |
|---|---|---|
| `llm_demo.py` | HuggingFace LLM basics | ✅ Working |
| `4_chatmodel_hf_api.py` | HuggingFace Chat Model | ✅ Working |
| `embedding_hf_local.py` | Local embeddings — no API cost | ✅ Working |
| `chatbot.py` | Full AI Chatbot with Streamlit UI | ✅ Working |
| `prompt_ui.py` | Dynamic Prompt Generator App | ✅ Working |

## 🔑 Requires Paid API Key

| File | What it does | Status |
|---|---|---|
| `1_chatmodel_openai.py` | OpenAI GPT Model | 🔑 Needs API Key |
| `2_chatmodel_anthro.py` | Anthropic Claude | 🔑 Needs API Key |
| `3_chatmodel_google.py` | Google Gemini | 🔑 Needs API Key |

---

## 🤖 AI Chatbot — Features

| Feature | Details |
|---|---|
| 🧠 Model | Qwen 2.5 72B via HuggingFace |
| 💬 Memory | Multi-turn conversation history |
| 💾 Save Chat | History saved as JSON |
| 📊 Stats | Real-time message count |
| 🎨 UI | Custom dark sidebar + clean Streamlit UI |
| 🗑️ Clear | Clear current or full history |

---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/AshishChaubey2003/gen-ai-projects.git
cd gen-ai-projects
```

### 2. Create virtual environment
```bash
python -m venv genenv
genenv\Scripts\activate        # Windows
source genenv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
```bash
copy .env.example .env
# Add your API keys in .env
```

### 5. Run AI Chatbot
```bash
streamlit run chatbot.py
```

### 6. Run Prompt UI App
```bash
streamlit run prompt_ui.py
```

---

## 🔑 Environment Variables

Create a `.env` file from `.env.example`:

```
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

👉 Get your **free** HuggingFace token here — https://huggingface.co/settings/tokens

---

## 📚 What I Learned

- ✅ How LLMs work and how to use them with LangChain
- ✅ Difference between LLMs and Chat Models — and when to use which
- ✅ How to integrate OpenAI, Anthropic, Google, and HuggingFace in one codebase
- ✅ What Embedding Models are and how semantic search works
- ✅ How to build a Streamlit Chatbot with multi-turn conversation memory
- ✅ How to save and reload chat history as JSON
- ✅ Prompt Engineering — static templates vs dynamic prompt generators
- ✅ How to build a live Prompt UI app with Streamlit

---

## 🗺️ What's Next

This repo is **Phase 0** of my Gen AI journey.

| Phase | Topic | Repo |
|---|---|---|
| ✅ Phase 0 | LangChain Basics — LLMs, Chat Models, Embeddings, Prompts | You are here |
| 🔄 Phase 1 | RAG Foundations — vector stores, retrieval chains | [RAG Journey →](https://github.com/AshishChaubey2003/Retreival-Argument-Generation) |
| ⏳ Phase 2 | Advanced RAG — hybrid search, Self-RAG, Corrective RAG | Coming soon |
| ⏳ Phase 3 | Agentic AI — LangGraph multi-agent pipelines | Coming soon |
| ⏳ Phase 4 | Production — LangSmith, monitoring, deployment | Coming soon |

---

## 🔗 Connect With Me

- 💼 [LinkedIn](https://linkedin.com/in/ashishchaubey2dec) — daily AI learning posts
- 💻 [GitHub](https://github.com/AshishChaubey2003) — all projects live here
- 📧 sashishchaubey1234@gmail.com

> 💼 **Open to work** — Python Backend / GenAI / LLM Engineer roles. B.Tech CSE 2025, immediate joiner, open to relocation across India.

---

> *"The best way to learn Gen AI is to build something with it every single day."* 🚀
