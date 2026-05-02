# Katalis
Stock Market Sentiment Radar. A local, full-stack AI web application that analyzes financial news sentiment and classifies it as Positive, Negative, or Neutral for retail investors.

## Tech Stack
![Nuxt](https://img.shields.io/badge/Nuxt-00DC82?style=for-the-badge&logo=nuxt.js&logoColor=white)
![Vue](https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind%20CSS-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white)
![ECharts](https://img.shields.io/badge/Apache%20ECharts-AA0000?style=for-the-badge&logo=apacheecharts&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-0B5FFF?style=for-the-badge&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

## Overview
Katalis provides a clean, data-dense sentiment dashboard built for an enterprise financial aesthetic. The backend serves a local SQLite database and a pre-trained NLP model loaded at startup. The frontend consumes the API and renders a donut sentiment chart and a compact headline table.

## Architecture
- Frontend: Nuxt 3 (Vue 3 Composition API) + Tailwind CSS
- Backend: FastAPI + SQLAlchemy + SQLite
- NLP: Scikit-learn (TF-IDF + SVM or Naive Bayes), persisted with Joblib

## Features
- Donut sentiment visualization with subtle, professional styling
- Compact headline table for recent news
- REST API for news retrieval and sentiment classification
- Local-only SQLite storage and model loading

## Repository Structure
```
.
├── frontend
│   ├── app.vue
│   ├── components
│   └── assets
└── backend
		└── app
```

## Requirements
- Node.js 18+ and npm
- Python 3.10+

## Setup and Run
### 1) Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2) Frontend
```bash
cd frontend
npm install
npm run dev
```

## Endpoints
Base URL: http://localhost:8000

### GET /news
Returns a list of the latest news items.

### POST /news
Create a news item with sentiment label.

Example body:
```json
{
	"source": "IDX Market",
	"title": "Banking sector leads late-session rebound on liquidity news",
	"sentiment": "Positive"
}
```

### POST /sentiment
Classify sentiment for a list of texts.

Example body:
```json
{
	"texts": [
		"Rupiah menguat terhadap dolar AS setelah rilis data inflasi.",
		"Tekanan jual meningkat pada sektor komoditas."
	]
}
```

Example response:
```json
{
	"labels": ["Positive", "Negative"]
}
```

## Model Loading
The model file is expected at:
```
backend/app/models/sentiment_model.pkl
```
If the file is missing, the `/sentiment` endpoint responds with HTTP 503.

## Train a Local Model
Use the sample dataset or replace it with your own.

```bash
cd backend
python scripts/train_model.py
```

Training data path:
```
backend/data/sample_train.csv
```

## Seed the Database
Populate SQLite with sample headlines for the dashboard.

```bash
cd backend
python scripts/seed_db.py
```

Seed data path:
```
backend/data/sample_seed.csv
```

## Dev-only Seed Endpoint
Enable the endpoint by setting:
```
KATALIS_DEV_MODE=1
```

Then call:
```
POST /admin/seed
POST /admin/seed?reset=true
```

## UI/UX Notes
- Typography uses small, measured sizes (text-xs to text-lg).
- Card layout uses tight padding and subtle borders.
- No emojis are used in the UI.

## Development Tips
- If TypeScript types appear missing in Nuxt, run:
```bash
cd frontend
npx nuxi prepare
```

## License
Private. Update before publishing.
