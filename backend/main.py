from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from anthropic import Anthropic
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Anthropic client
anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/analyze")
async def analyze_documents(files: List[UploadFile] = File(...)):
    try:
        # Process files and combine content
        combined_content = ""
        for file in files:
            content = await file.read()
            combined_content += content.decode() + "\n\n"
        
        # Get analysis from Claude
        response = await anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            messages=[{
                "role": "user",
                "content": f"Analyze these documents and create a timeline and decision matrix:\n\n{combined_content}"
            }]
        )
        
        # Parse and return results
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
