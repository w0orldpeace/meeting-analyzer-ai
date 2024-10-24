# Meeting Analyzer AI

An AI-powered meeting management and decision support tool that analyzes meeting transcripts, emails, and documents to create timelines and decision matrices.

## Features

- Document upload and analysis
- Automated timeline generation
- Decision matrix creation
- AI-powered insights using Claude API

## Tech Stack

- Frontend: Next.js with Tailwind CSS
- Backend: FastAPI with Python
- AI: Claude API by Anthropic
- Deployment: Railway

## Local Development

### Prerequisites

- Node.js 16+
- Python 3.9+
- Anthropic API key

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/meeting-analyzer-ai.git
cd meeting-analyzer-ai
```

2. Install frontend dependencies
```bash
cd frontend
npm install
npm run dev
```

3. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

4. Set up environment variables
Create a `.env` file in the backend directory:
```
ANTHROPIC_API_KEY=your_api_key_here
```

## Deployment

This project is configured for deployment on Railway.app:

1. Fork this repository
2. Sign up on Railway.app
3. Create new project from GitHub
4. Add your ANTHROPIC_API_KEY in the Environment Variables
5. Deploy!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details
3. Add your ANTHROPIC_API_KEY in Vercel's environment variables
4. Deploy!

## Support

For support, please open an issue in this repository.
