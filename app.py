from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Comprehensive Portfolio data with all sections
PORTFOLIO_DATA = {
    "name": "Dhruv Thejas",
    "title": "AI Engineer | ML Specialist | Full-Stack Developer",
    "bio": "Building intelligent systems at the intersection of AI and real-world applications. Expertise in LLMs, Computer Vision, and Reinforcement Learning.",
    "email": "dhruvthejas.kj@gmail.com",
    "phone": "+91 8309303147",
    "location": "India",
    "github": "https://github.com/DhruvThejas",
    "linkedin": "https://linkedin.com/in/dhruv-thejas",
    "resume_url": "https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/131687302/2c8fdcf7-d44e-4f40-97d4-6a3ca254c3dc/Dhruv_MS_Resume_v1.pdf",
    
    "experience": [
        {
            "title": "AI Engineer Intern",
            "company": "Linqura",
            "location": "Hartford, Connecticut",
            "period": "Dec 2024 - May 2025",
            "description": "Fine-tuned and benchmarked LLMs and MCP pipelines. Developed agent-based workflows with memory, planning, and orchestration using FastAPI.",
            "highlights": [
                "Improved employee revenue prediction model by 12%",
                "Built commercial insurance AI products",
                "AWS monitoring and CI/CD workflows",
                "FastAPI for testing and deployment"
            ]
        },
        {
            "title": "Co-Founder",
            "company": "GlitchAI (Drufiy Innovations)",
            "location": "Remote",
            "period": "Oct 2024 - Present",
            "description": "Building AI-driven autonomous device assistant for proactive system diagnostics and self-repair capabilities.",
            "highlights": [
                "Jarvis-like intelligent agent design",
                "Self-monitoring and failure prediction",
                "Autonomous system resolution",
                "LLM integration for natural interaction"
            ]
        },
        {
            "title": "ML Intern",
            "company": "HCLTech",
            "location": "Noida, India",
            "period": "May 2024 - Aug 2024",
            "description": "Designed and optimized RL algorithms and built CNN-based biometric security systems for face anti-spoofing.",
            "highlights": [
                "Face anti-spoofing system: 96.5% accuracy",
                "Deepfake detection implementation",
                "RL algorithms: SAC, PPO, TD3",
                "GAN-based data augmentation"
            ]
        },
        {
            "title": "Undergraduate Research Assistant",
            "company": "Manipal Institute of Technology",
            "location": "Bengaluru, India",
            "period": "Nov 2023 - Aug 2025",
            "description": "Research mentorship under Prof. Dr. Megha P. Arakeri in Computer Vision, AI, and Data Analytics.",
            "highlights": [
                "Published research papers in IEEE conferences",
                "Computer Vision research projects",
                "Data Analytics and ML research",
                "Senior position in IEEE council"
            ]
        }
    ],
    
    "education": [
        {
            "school": "Manipal Institute of Technology",
            "degree": "B.Tech in Computer Science",
            "specialization": "AI & ML Specialization",
            "period": "2022 - 2026",
            "cgpa": "8.76/10",
            "achievements": ["AI/ML Focus", "Strong academic record"]
        },
        {
            "school": "FIITJEE",
            "degree": "11th & 12th Grade",
            "period": "2020 - 2022",
            "score": "98%",
            "achievements": ["Top performer", "National scholarship"]
        },
        {
            "school": "St. Josephs School",
            "degree": "ICSE Curriculum",
            "period": "Till 10th",
            "score": "96%",
            "achievements": ["Honors", "Academic excellence"]
        }
    ],
    
    "projects": [
        {
            "title": "CISCO Forecasting League Competition",
            "period": "FY25 Q2 Prediction",
            "description": "Predicted FY25 Q2 unit sales for top 20 Cisco product categories with advanced time series analysis.",
            "achievement": "Rank 4 - 90% accuracy",
            "image_placeholder": "🎯",
            "tech": ["Python", "Pandas", "Power BI", "LSTM", "Time Series"],
            "github": "https://github.com/DhruvThejas"
        },
        {
            "title": "AI-Driven Food Label Analysis",
            "period": "2024-2025",
            "description": "OCR-NLP pipeline for food label analysis and personalized dietary recommendations using RAG.",
            "achievement": "85.09% recall - Journal Paper Submitted",
            "image_placeholder": "🥗",
            "tech": ["PaddleOCR", "YAKE", "RAG", "USDA API", "NLP"],
            "github": "https://github.com/DhruvThejas"
        },
        {
            "title": "Face Anti-Spoofing Detection System",
            "period": "2024-2025",
            "description": "Robust CNN and RL-based biometric security system for deepfake detection with GAN augmentation.",
            "achievement": "97% discriminator accuracy - ICSCI 2025 Conference",
            "image_placeholder": "🔐",
            "tech": ["TensorFlow", "PyTorch", "CNN", "GAN", "RL (SAC, PPO, TD3)"],
            "github": "https://github.com/DhruvThejas"
        },
        {
            "title": "Global Avian Invasions Atlas Management",
            "period": "2024",
            "description": "Natural Language to SQL conversion system for analyzing bird ranges, habitats, and invasion trends.",
            "achievement": "AI-powered wildlife database for ecological monitoring",
            "image_placeholder": "🦅",
            "tech": ["Flask", "MySQL", "OpenAI", "NLP", "SQL Generation"],
            "github": "https://github.com/DhruvThejas"
        },
        {
            "title": "Headphones Recommendation System",
            "period": "2024",
            "description": "Real-time recommendation system with web scraping and personalized filtering for headphones.",
            "achievement": "Multi-criteria filtering with user preferences",
            "image_placeholder": "🎧",
            "tech": ["Web Scraping", "BeautifulSoup", "Python", "Recommendation Engine"],
            "github": "https://github.com/DhruvThejas"
        },
        {
            "title": "Speech-to-Text Analysis System",
            "period": "2024",
            "description": "Flask-based application converting audio to text with grammar checking and word prediction.",
            "achievement": "Real-time transcription with writing assistance",
            "image_placeholder": "🎤",
            "tech": ["Flask", "Python", "Speech Recognition", "TextBlob", "LanguageTool"],
            "github": "https://github.com/DhruvThejas"
        }
    ],
    
    "research": [
        {
            "title": "Histopathological Classification of Rare Ovarian Cancer using SwinConvNeXt Ensemble",
            "venue": "Journal Submission In Progress",
            "status": "Ongoing",
            "achievement": "96.46% accuracy, 96.12% macro F1-score",
            "description": "Weighted ensemble combining Swin Transformer and ConvNeXt-Tiny for rare cancer classification.",
            "image_placeholder": "🔬",
            "tech": ["Swin Transformer", "ConvNeXt", "Medical Imaging", "Ensemble Learning"],
            "github": "https://github.com/DhruvThejas"
        },
        {
            "title": "Comparative Analysis of Kernels for Image Denoising",
            "venue": "NMITCON 2025 (IEEE Conference)",
            "status": "Published",
            "achievement": "Optimal filtering strategies identified and validated",
            "description": "Performance analysis of Gaussian, Laplacian, and Bilateral kernels under multiple noise models.",
            "image_placeholder": "🖼️",
            "tech": ["Image Processing", "Filter Design", "PSNR", "MSNR", "MAE"],
            "github": "https://github.com/DhruvThejas"
        },
        {
            "title": "Soil Erosion Prediction Using Machine Learning",
            "venue": "Earth System Science Data (ESSD)",
            "status": "Completed",
            "achievement": "Data-driven insights for sustainable land management",
            "description": "Applied ML models (Random Forest, SVM, Neural Networks) for soil erosion rate prediction.",
            "image_placeholder": "🌍",
            "tech": ["Random Forest", "SVM", "Neural Networks", "Environmental Data"],
            "github": "https://github.com/DhruvThejas"
        }
    ],
    
    "awards": [
        {
            "title": "Student of the Year 2020",
            "issuer": "The Times of India",
            "description": "Exceptional academic and extracurricular performance",
            "year": 2020
        },
        {
            "title": "Amazon ML Summer School 2025 Trainee",
            "issuer": "Amazon",
            "description": "Selected trainee for advanced ML & AI systems training",
            "year": 2025
        },
        {
            "title": "Rank 4 - CISCO Forecasting League",
            "issuer": "CISCO",
            "description": "FY25 Q2 prediction with 90% accuracy",
            "year": 2025
        }
    ],
    
    "skills": {
        "Programming": ["Python", "Java", "C", "SQL", "HTML", "CSS", "JavaScript"],
        "ML/DL Frameworks": ["TensorFlow", "PyTorch", "Keras", "Scikit-learn", "XGBoost"],
        "Computer Vision": ["OpenCV", "CNNs", "Image Processing", "Face Detection"],
        "Data Science": ["Pandas", "NumPy", "SciPy", "Power BI", "Excel"],
        "Tools & Platforms": ["Jupyter", "GitHub", "VSCode", "AWS", "FastAPI", "Flask"],
        "Core Skills": ["Problem-Solving", "Research", "Team Collaboration", "Communication"]
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/api/portfolio')
def get_portfolio():
    return jsonify(PORTFOLIO_DATA)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
