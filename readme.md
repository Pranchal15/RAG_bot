# RAG Bot – Streamlit + vLLM

A lightweight Retrieval-Augmented Generation (RAG) chatbot powered by [vLLM](https://github.com/vllm-project/vllm) and [Streamlit](https://streamlit.io).  
It supports local inference with Mistral-7B and allows PDF-based question answering.

---

## 🚀 Live Demo

👉 [Try it out on Streamlit Cloud](https://pranchal15-rag-bot-streamlit-app-5kqfex.streamlit.app/)

> ⚠️ This is a work in progress. Feedback and contributions are welcome!

---

## 🛠️ Setup Instructions

### 1. Clone the repo and navigate to the folder
```bash
git clone https://github.com/Pranchal15/rag-bot-streamlit.git
cd rag-bot-streamlit
```

### 2. Create and activate a conda environment
```bash
conda create -n ragbot python=3.10
conda activate ragbot
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download model weights
This script downloads the Mistral-7B-Instruct weights.
```bash
python download_mistral.py
```

### 5. Start the vLLM API server
```bash
python -m vllm.entrypoints.openai.api_server \
  --model ./models/mistral \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192
```

### 6. Run the Streamlit app
```bash
streamlit run app.py
```

Make sure the vLLM server is running on `http://localhost:8000/v1`.

---

## 💡 Features

- 🔎 PDF ingestion and chunking using LangChain loaders
- 🤖 Local inference using vLLM with Mistral 7B
- 🧠 FAISS-based vector search
- 🎯 RAG pipeline with prompt templating
- 🧪 Simple UI with Streamlit

---

## 📬 Contributing

Found a bug or have a feature request?  
Feel free to [open an issue](https://github.com/Pranchal15/rag-bot-streamlit/issues) or submit a PR.

---
