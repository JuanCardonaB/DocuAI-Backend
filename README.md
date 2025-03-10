# 🚀 DocuAI - Backend (FastAPI + Ollama)

## 📌 Description

**DocuAI** is a **FastAPI**-based backend that uses **Ollama** to answer questions about text documents. It allows users to upload files (PDF, TXT) and make queries based on their content, leveraging AI models to generate precise responses.

## 🏗️ Project Structure

```
📂 docuai-backend/
│── 📂 app/
│   │── 📂 routes/              # API Routes
│   │   │── example.py        # Endpoints
│   │── 📂 services/         # Business Logic
│   │   │── example_service.py  # Integrations with modules
│   │── 📂 models/           # Pydantic Models
│   │   │── request_models.py  # Input Models
│   │   │── response_models.py # Output Models
│   │── 📂 utils/            # Utility Functions
│   │   │── example.py     # Handling data app
│   │── main.py              # FastAPI Entry Point
│── 📂 config/               # Environment Configuration
│   │── config.py            # Variable Loading
│── .env                     # Environment Variables
│── requirements.txt         # Dependencies
│── README.md                # Documentation
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

<!-- ```bash
git clone https://github.com/your-user/docuai-backend.git
cd docuai-backend
``` -->

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the project root:

<!-- ```ini
OLLAMA_MODEL=mistral
``` -->

### 5️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

💡 **DocuAI** - An intelligent backend for document processing 🚀
