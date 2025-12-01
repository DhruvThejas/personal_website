from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Comprehensive Portfolio data with all sections
PORTFOLIO_DATA = {
    "name": "Dhruv Thejas",
    "title": "AI Engineer | ML Specialist | Full-Stack Developer",
    "bio": "AI engineer with a focus on machine learning, computer vision, NLP, and autonomous systems. I create AI systems that think, see, and act, built on a foundation of rigorous experimentation and engineering craftsmanship. My work spans reinforcement learning, multimodal deep learning, and intelligent system design, driven by the belief that real AI innovation happens where theory meets messy real-world constraints.",
    "about_bio": "I specialize in designing learning systems that generalize beyond training distributions, leverage structure in data, and make robust decisions in uncertain environments. From building perception driven autonomous agents to developing language aware control architectures, I push toward AI that is adaptable, interpretable, and ready for real-world deployment.",
    "email": "dhruvthejas.kj@gmail.com",
    "phone": "+91 8309303147",
    "location": "India",
    "github": "https://github.com/DhruvThejas",
    "linkedin": "https://linkedin.com/in/dhruv-thejas",

    "experience": [
        {
            "position": "AI Engineer Intern",
            "company": "Linqura",
            "company_color": "#FFD700",
            "duration": "Dec 2024 - May 2025",
            "location": "Hartford, Connecticut",
            "description": "Fine-tuned and benchmarked LLMs and MCP pipelines. Developed agent-based workflows with memory, planning, and orchestration using FastAPI.",
            "highlights": [
                "Improved employee revenue prediction model by 12%",
                "Built commercial insurance AI products",
                "AWS monitoring and CI/CD workflows with rigorous API testing"
            ]
        },
        {
            "position": "Co-Founder",
            "company": "GlitchAI (Drufiy Innovations)",
            "company_color": "#FF6B6B",
            "duration": "Oct 2024 - Present",
            "location": "Remote",
            "description": "Building an AI-driven autonomous device assistant capable of diagnosing and resolving system issues proactively.",
            "highlights": [
                "Jarvis-like intelligent agent with self-monitoring capabilities",
                "Self-repair and failure prediction systems",
                "Eliminates manual troubleshooting and IT wait times"
            ]
        },
        {
            "position": "ML Intern",
            "company": "HCLTech",
            "company_color": "#4A90E2",
            "duration": "May 2024 - Aug 2024",
            "location": "Noida, India",
            "description": "Designed and optimized RL algorithms and built CNN-based anti-spoofing systems for biometric security.",
            "highlights": [
                "Face anti-spoofing system with 96.5% accuracy",
                "Deepfake detection implementation",
                "Few-shot learning and GAN frameworks for model robustness"
            ]
        },
        {
            "position": "Undergraduate Research Assistant",
            "company": "Manipal Institute of Technology",
            "company_color": "#9B59B6",
            "duration": "Nov 2023 - Aug 2025",
            "location": "Bengaluru, India",
            "description": "Conducted research under Prof. Dr. Megha P. Arakeri in Computer Vision, Machine Learning, and AI.",
            "highlights": [
                "Published research in IEEE conferences",
                "Specialized in computer vision and deep learning",
                "HCI and data analytics research"
            ]
        }
    ],

    "education": [
        {
            "institution": "Manipal Institute of Technology",
            "degree": "B.Tech in Computer Science Engineering",
            "specialization": "Specialization in AI & ML",
            "duration": "2022 - 2026",
            "cgpa": "8.76/10",
            "achievements": ""
        },
        {
            "institution": "FIITJEE",
            "degree": "11th and 12th Grade",
            "specialization": "Science Stream",
            "duration": "2020 - 2022",
            "cgpa": "98%",
            "achievements": ""
        },
        {
            "institution": "St. Joseph's School",
            "degree": "ICSE Curriculum",
            "specialization": "Science",
            "duration": "Till 2020",
            "cgpa": "96%",
            "achievements": "Academic excellence and leadership awards"
        }
    ],

    102
    
        {
            "title": "CISCO Forecasting League Competition FY25 Q2",
            "tech": "Pandas, Power BI, Excel, Time Series Analysis, LSTM",
            "description": "Predicted FY25 Q2 unit sales for top 20 Cisco masked product categories, achieving 90% accuracy and Rank 4. Analyzed 12 quarters of sales data using Holt's Winter and Exponential Smoothing.",
            "github": "https://github.com",
            "icon": "📊"
        },
        {
            "title": "Global Avian Invasions Atlas Management System",
            "tech": "MySQL, OpenAI, Flask, Python, NL-to-SQL",
            "description": "Built AI-driven Natural Language to SQL conversion system for analyzing bird ranges, habitats, and invasion trends. Trained model on sophisticated queries to generate contextually relevant SQL outputs.",
            "github": "https://github.com",
            "icon": "🦅"
        },
        {
            "title": "Headphones Recommendation System",
            "tech": "Python, BeautifulSoup, Web Scraping, Machine Learning",
            "description": "Designed real-time recommendation system providing tailored headphone suggestions. Leveraged web scraping to extract product information with personalized filtering based on user preferences.",
            "github": "https://github.com",
            "icon": "🎧"
        },
        {
            "title": "Speech-to-Text Analysis System",
            "tech": "Flask, Python, Speech Recognition, Grammar Check, NLP",
            "description": "Flask web application converting audio to text with grammar/spell checking and next-word prediction. Responsive Bootstrap frontend for seamless transcription and text correction.",
            "github": "https://github.com",
            "icon": "🎤"
        },
        {
            "title": "Soil Erosion Prediction Using ML",
            "tech": "Random Forest, SVM, Neural Networks, Python, Data Analysis",
            "description": "Applied machine learning models to predict soil erosion rates using ESSD dataset. Identified key environmental features contributing to erosion for sustainable land management.",
            "github": "https://github.com",
            "icon": "🌍",
            "centered": True
        }
    ],

    "research": [
        {
            "title": "Comparative Analysis of Kernels for Image Denoising",
            "venue": "NMITCON 2025 IEEE Conference",
            "status": "Published",
            "description": "Investigated performance of different kernel techniques (Gaussian, Laplacian, Bilateral) for image denoising. Compared linear and non-linear approaches using PSNR, MSNR evaluation metrics.",
            "icon": "🔬"
        },
        {
            "title": "Face Anti-Spoofing Detection System",
            "venue": "ICSCI 2025 Springer CCIS Series",
            "status": "Published",
            "description": "Developed robust face anti-spoofing model leveraging CNNs, reinforcement learning (SAC, PPO, TD3), and GAN-based augmentation. Discriminator accuracy over 97% on MSU-MFSD dataset.",
            "icon": "🔐"
        },
        {
            "title": "AI-Driven Food Label Analysis for Personalized Dietary Recommendation",
            "venue": "Journal Submission",
            "status": "Submitted",
            "description": "Developed OCR-NLP pipeline using PaddleOCR and semantic similarity for food label analysis. Integrated USDA FoodData Central for personalized dietary recommendations achieving 85% recall.",
            "icon": "🍎"
        },
        {
            "title": "Histopathological Classification of Ovarian Cancer using SwinConvNeXt",
            "venue": "IEEE Conference & Journal",
            "status": "Submitted",
            "description": "Weighted ensemble combining Swin Transformer and ConvNeXt-Tiny for rare ovarian cancer classification. Achieved 96.46% accuracy with 96.12% macro F1-score on 4-class problem.",
            "icon": "🔬"
        },
        {
            "title": "Currently Researching and Writing Papers",
            "venue": "Privacy & AI",
            "status": "Ongoing",
            "description": "Exploring the intersection of privacy-preserving machine learning and AI safety. Developing methods for federated learning, differential privacy, and interpretable AI systems that maintain user confidentiality while delivering robust performance.",
            "icon": "🛡️",
            "centered": True
        }
    ],

    "skills": {
        "Programming Languages": ["Python", "Java", "C", "SQL", "HTML", "CSS", "JavaScript"],
        "ML & Deep Learning": ["TensorFlow", "PyTorch", "Keras", "CNNs", "RNNs", "GANs", "Transformers"],
        "Computer Vision": ["OpenCV", "Image Processing", "Object Detection", "Segmentation"],
        "Data & Analytics": ["Pandas", "NumPy", "SciPy", "Scikit-learn", "Data Visualization"],
        "Tools & Frameworks": ["Flask", "FastAPI", "Jupyter", "GitHub", "AWS", "Docker"],
        "Core Competencies": ["Reinforcement Learning", "System Design", "Problem-Solving", "Research", "Communication"]
    },

    "contact": {
        "email": "dhruvthejas.kj@gmail.com",
        "phone": "+91 8309303147",
        "github": "https://github.com/DhruvThejas",
        "linkedin": "https://linkedin.com/in/dhruv-thejas"
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/api/portfolio')
def get_portfolio():
    return jsonify(PORTFOLIO_DATA)

if __name__ == '__main__':
    app.run(debug=True)
