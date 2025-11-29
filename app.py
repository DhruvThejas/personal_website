from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Portfolio data
PORTFOLIO_DATA = {
    "name": "Dhruv Thejas",
    "title": "AI Engineer | ML Specialist | Full-Stack Developer",
    "bio": "Passionate AI/ML Engineer with expertise in LLMs, Computer Vision, and Reinforcement Learning.",
    "email": "dhruvthejas.kj@gmail.com",
    "phone": "+91 8309303147",
    "location": "India",
    "github": "https://github.com/DhruvThejas",
    "linkedin": "https://linkedin.com/in/dhruv-thejas",
    "resume_url": "https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/131687302/2c8fdcf7-d44e-4f40-97d4-6a3ca254c3dc/Dhruv_MS_Resume_v1.pdf",
}

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/api/portfolio')
def get_portfolio():
    return jsonify(PORTFOLIO_DATA)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
