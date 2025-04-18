# 🎬 Movie Recommender System

An intelligent, content-based movie recommender that suggests similar movies based on your input — complete with poster images. Built using FastAPI, Streamlit, and sentence-transformers, this app is fully Dockerized for seamless local deployment.

## 🚀 Features

- 🎯 Recommends similar movies using NLP-based content similarity
- 🖼️ Displays movie posters alongside titles
- ⚡ Fast and responsive backend with FastAPI
- 💻 Simple, clean frontend with Streamlit
- 🐳 Fully containerized using Docker & Docker Compose

## ⚙️ Tech Stack

- **Preprocessing & ML**:  
  `pandas`, `numpy`, `scikit-learn`, `sentence-transformers`  
- **Backend**:  
  `FastAPI`, `Uvicorn`  
- **Frontend**:  
  `Streamlit`  
- **Containerization**:  
  `Docker`, `Docker Compose`

## 🧱 Project Structure

```text
├── backend/
│   ├── main.py              # FastAPI API for recommendations
│   ├── dockerfile           # Dockerfile for backend
│   ├── data/                # Preprocessed dataset and embeddings
│   └── requirements.txt
├── frontend/
│   ├── movie_ui.py          # Streamlit frontend app
│   ├── dockerfile           # Dockerfile for frontend
│   ├── .streamlit           # Streamlit customization
│   └── requirements.txt
├── docker-compose.yml       # Orchestrates backend and frontend
└── README.md
## 🐳 Running Locally with Docker

```bash
git clone https://github.com/akasssshhhhh/Movie_Recommender_system.git
cd Movie_Recommender_system 
docker-compose up --build

## 📚 What I Learned & Challenges Faced

-Implemented a full-stack content-based recommendation system
-Gained hands-on experience with sentence embeddings for similarity search
-Improved data cleaning skills — especially handling large datasets with many missing values
-Learned how to containerize backend and frontend apps for local deployment
