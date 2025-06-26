import os
from resume_parser import extract_resume_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_resumes(folder_path):
    resume_texts = []
    filenames = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            full_path = os.path.join(folder_path, filename)
            try:
                text = extract_resume_text(full_path)
                resume_texts.append(text)
                filenames.append(filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return filenames, resume_texts

def load_job_description(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        jd_text = f.read()
    return jd_text

def rank_resumes(resume_texts, jd_text):
    docs = resume_texts + [jd_text]  # Add JD as the last document
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(docs)

    jd_vector = tfidf_matrix[-1]  # Last vector = JD
    resume_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(jd_vector, resume_vectors).flatten()
    return similarities
