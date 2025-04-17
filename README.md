# AI Meme Generator

A full-stack AI-powered meme generator that creates hilarious memes based on user input! It uses **React.js** on the frontend, **Spring Boot** on the backend, and **Python** with NLP to understand user text and generate memes from templates.

## Project Overview

The AI Meme Generator lets users type in a prompt, and it intelligently matches their input with meme templates using semantic similarity. Then it dynamically generates a meme with a relevant caption.

## How It Works

- Uses **NLP with NLTK** to process user input
- Leverages **cosine similarity** (`sklearn.metrics.pairwise.cosine_similarity`) to match input with the best meme template from the dataset
- Generates the final meme and returns it to the frontend using **Flask API**
- **Spring Boot** acts as the backend bridge managing the AI service calls
- Frontend displays the final meme using a clean **React.js UI**

##  Features

-  AI-based meme generation from user prompts
-  Dynamic template selection via cosine similarity
-  Natural language understanding using NLTK
-  Full-stack: React + Spring Boot + Python
-  Kaggle dataset integration (memes + captions)

#  Tech Stack

| Layer       | Tech Used                        |
|-------------|----------------------------------|
| Frontend    | React.js                         |
| Backend     | Spring Boot                      |
| AI / NLP    | Python, Flask, NLTK, Scikit-learn |
| Dataset     | [Imgflip Meme Caption Dataset](https://www.kaggle.com/datasets/abhishtagatya/imgflipscraped-memes-caption-dataset) |


## Dataset Info

- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/abhishtagatya/imgflipscraped-memes-caption-dataset)
- Place the files inside a local `data/` folder
- The dataset is **excluded** from GitHub using `.gitignore`


## How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/ai-meme-generator.git
cd ai-meme-generator
## 2. Start the Python Flask AI Server
cd backend
python app.py
## 3. Start the Spring Boot Server
# Inside the backend folder
./mvnw spring-boot:run
## 4. Start the React Frontend
cd frontend/reactUI
npm install
npm start
```

## project by - Khushi Kadyan
linkedin-https://www.linkedin.com/in/khushi-kadyan-03s12a2004r/

### SCREENSHOTS-
home page-
![Screenshot 2025-04-14 152006](https://github.com/user-attachments/assets/e7ac53dd-f60e-4819-a03e-24c2954a1538)

trending meme section-

![Screenshot 2025-04-14 152021](https://github.com/user-attachments/assets/ac0ed1b5-1325-4bdc-baf0-bfa9328450fc)

📌 Note
This project is for educational and fun purposes. Dataset is not included in the repo — please download it from Kaggle and place it in the local data/ directory before running.
