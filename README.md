# 🤖 AI-Powered Resume Ranker

This project ranks resumes based on how well they match a given Job Description using Natural Language Processing (NLP).

## 🔍 Features
- Upload resumes (.pdf or .docx)
- Paste job description
- Ranks resumes using TF-IDF + Cosine Similarity
- Interactive Streamlit UI

## 🛠️ Tech Stack
- Python
- PyMuPDF, docx2txt
- Scikit-learn (TF-IDF)
- Streamlit
- NLP + Cosine Similarity

## 🧠 How It Works
1. Extract text from uploaded resumes
2. Process JD and resume text with TF-IDF
3. Compute similarity scores
4. Display ranked results

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Live Demo
### link :- https://resume-ranker-ak.streamlit.app/
## Author : Karthik Aljapur
