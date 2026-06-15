#!/bin/bash
source .venv/bin/activate && pip install -r requirements.txt -q && uvicorn app.main:app --reload
