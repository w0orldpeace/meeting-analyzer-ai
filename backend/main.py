from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
from typing import List
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

anthropic = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/analyze")
async def analyze_documents(files: List[UploadFile] = File(...)):
    try:
        combined_content = ""
        for file in files:
            content = await file.read()
            # Only process text files to reduce memory usage
            if file.content_type.startswith('text/'):
                combined_content += content.decode() + "\n\n"
            else:
                combined_content += f"[File: {file.filename}]\n\n"
        
        response = await anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f"Analyze these documents briefly:\n\n{combined_content}"
            }]
        )
        
        return {
            "timeline": [
                {"date": "2024-01-01", "event": "Example Event", "type": "meeting"}
            ],
            "decision_matrix": [
                {
                    "option": "Option A",
                    "criteria": {"cost": 8, "impact": 7, "feasibility": 9}
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
