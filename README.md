# 🚀 Autonomous Insurance Claims Processing Agent

## 📌 Project Overview

The **Autonomous Insurance Claims Processing Agent** is an AI-powered backend application that automates the initial processing of **First Notice of Loss (FNOL)** documents.

The application accepts **TXT** and **PDF** FNOL documents, extracts key insurance claim information using **Google Gemini AI**, validates mandatory fields, classifies the claim according to business rules, and recommends the appropriate processing workflow.

To improve reliability, the application also includes a **rule-based extraction fallback** that is used if AI extraction fails.

---

# ✨ Features

- 📄 Upload FNOL documents in **TXT** or **PDF** format
- 🤖 AI-powered field extraction using **Google Gemini**
- 🔄 Rule-based fallback extractor
- ✅ Mandatory field validation
- 🚦 Intelligent claim routing
- 📝 Reasoning for routing decision
- 📂 Automatically saves processed claims as JSON
- 📚 Interactive Swagger API Documentation
- 📋 Structured logging using Python Logging

---

# 🏗️ System Architecture

```
                 Upload TXT/PDF
                        │
                        ▼
                 Read Document Text
                        │
                        ▼
              Google Gemini AI Extraction
                        │
         (Fallback to Rule-Based Extraction)
                        ▼
                Extract Claim Fields
                        │
                        ▼
             Validate Mandatory Fields
                        │
                        ▼
                Apply Routing Rules
                        │
                        ▼
              Save Processed Claim
                        │
                        ▼
                 Return JSON Response
```

---

# 📂 Project Structure

```
insurance-claims-agent/
│
├── app/
│   ├── ai_extractor.py
│   ├── config.py
│   ├── extractor.py
│   ├── main.py
│   ├── router.py
│   ├── schemas.py
│   ├── utils.py
│   └── validator.py
│
├── output/
│
├── sample_documents/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

---

# 🛠️ Technologies Used

- Python
- FastAPI
- Google Gemini AI
- Pydantic
- pdfplumber
- python-dotenv
- Uvicorn

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/insurance-claims-agent.git
```

Replace `your-username` with your GitHub username.

---

## 2. Navigate to the Project

```bash
cd insurance-claims-agent
```

---

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Configure Environment Variables

Create a file named **`.env`** in the project root.

Add your Google Gemini API key:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Example:

```text
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXX
```

---

# ▶️ Running the Application

Start the FastAPI server using:

```bash
python -m uvicorn app.main:app --reload
```

If the server starts successfully, you should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 Access the API

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

This opens the **Swagger UI**, where you can test the API interactively.

---

# 📤 API Endpoint

## POST `/process-claim`

Uploads an FNOL document and processes the insurance claim.

### Supported File Types

- TXT
- PDF

---

# 📥 Sample Response

```json
{
  "extractedFields": {
    "policy_number": "POL12345",
    "policyholder_name": "John Smith",
    "effective_dates": "01-Jan-2026 to 31-Dec-2026",
    "incident_date": "05-Jul-2026",
    "incident_time": "3:45 PM",
    "location": "Bangalore",
    "description": "Minor collision while parking.",
    "claimant": "John Smith",
    "third_parties": "None",
    "contact_details": "9876543210",
    "asset_type": "Car",
    "asset_id": "KA01AB1234",
    "estimated_damage": 15000,
    "claim_type": "Vehicle",
    "attachments": "Photos",
    "initial_estimate": 15000
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage is below ₹25,000."
}
```

---

# 🚦 Routing Rules

| Rule | Recommended Route |
|------|-------------------|
| Estimated Damage < ₹25,000 | Fast-track |
| Missing Mandatory Fields | Manual Review |
| Description contains **fraud**, **staged**, or **inconsistent** | Investigation Flag |
| Claim Type = Injury | Specialist Queue |
| Otherwise | Standard Processing |

---

# 🤖 AI Integration

This project uses **Google Gemini AI** to extract structured information from FNOL documents.

If AI extraction fails due to API or network issues, the application automatically switches to the built-in rule-based extractor.

This hybrid architecture improves both flexibility and reliability.

---

# 📂 Output

Each processed claim is automatically saved as a JSON file in the **output/** directory for auditing and traceability.

Example:

```
output/
│
├── claim_20260708_190001.json
├── claim_20260708_190452.json
└── claim_20260708_191025.json
```

---

# 📈 Future Enhancements

- OCR support for scanned PDF documents
- Database integration (PostgreSQL/MySQL)
- JWT Authentication
- Docker deployment
- Unit Testing using Pytest
- Cloud Deployment (AWS/Azure)
- Claim Confidence Score
- Dashboard for processed claims

---

# 👨‍💻 Author

**Pavitra Sadananda Vaidya**

---

# 📄 License

This project was developed as part of a placement assessment for educational purposes.
