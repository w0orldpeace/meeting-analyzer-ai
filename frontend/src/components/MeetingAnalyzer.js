import React, { useState } from 'react';
import { Upload, FileText, Clock, Grid } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const MeetingAnalyzer = () => {
  const [files, setFiles] = useState([]);
  const [timelineData, setTimelineData] = useState([]);
  const [decisionMatrix, setDecisionMatrix] = useState([]);
  const [activeView, setActiveView] = useState('upload');

  const handleFileUpload = async (e) => {
    const uploadedFiles = Array.from(e.target.files);
    setFiles(uploadedFiles);
    
    const formData = new FormData();
    uploadedFiles.forEach(file => {
      formData.append('files', file);
    });

    try {
      const response = await fetch('/api/analyze', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Analysis failed');
      }

      const data = await response.json();
      setTimelineData(data.timeline);
      setDecisionMatrix(data.decision_matrix);
      setActiveView('timeline');
    } catch (error) {
      console.error('Error analyzing files:', error);
    }
  };

  return (
    <div className="max-w-6xl mx-auto p-6">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-4">Meeting Analysis Assistant</h1>
        <div className="flex space-x-4 mb-6">
          <button
            className={`px-4 py-2 rounded-lg flex items-center space-x-2 ${
              activeView === 'upload' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => setActiveView('upload')}
          >
            <Upload size={20} />
            <span>Upload</span>
          </button>
          <button
            className={`px-4 py-2 rounded-lg flex items-center space-x-2 ${
              activeView === 'timeline' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => setActiveView('timeline')}
          >
            <Clock size={20} />
            <span>Timeline</span>
          </button>
          <button
            className={`px-4 py-2 rounded-lg flex items-center space-x-2 ${
              activeView === 'matrix' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
            onClick={() => setActiveView('matrix')}
          >
            <Grid size={20} />
            <span>Decision Matrix</span>
          </button>
        </div>
      </div>

      {activeView === 'upload' && (
        <Card>
          <CardHeader>
            <CardTitle>Upload Documents</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
              <input
                type="file"
                multiple
                onChange={handleFileUpload}
                className="hidden"
                id="file-upload"
              />
              <label
                htmlFor="file-upload"
                className="cursor-pointer flex flex-col items-center"
              >
                <FileText size={48} className="text-gray-400 mb-4" />
                <span className="text-lg mb-2">Drop files here or click to upload</span>
                <span className="text-sm text-gray-500">
                  Support for PDF, DOC, and TXT files
                </span>
              </label>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default MeetingAnalyzer;
