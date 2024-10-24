from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/analyze")
async def analyze_documents(files: List[UploadFile] = File(...)):
    try:
        # Simple document processing
        documents = []
        for file in files:
            content = await file.read()
            if file.content_type.startswith('text/'):
                documents.append({
                    'name': file.filename,
                    'content': content.decode()
                })
        
        # Mock analysis response
        return {
            "timeline": [
                {
                    "date": "2024-01-01",
                    "event": f"Processed {len(documents)} documents",
                    "type": "analysis"
                }
            ],
            "decision_matrix": [
                {
                    "option": "Document Analysis",
                    "criteria": {
                        "files_processed": len(documents),
                        "success": True
                    }
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
