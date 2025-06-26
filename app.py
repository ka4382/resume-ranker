import streamlit as st
import os
from resume_parser import extract_resume_text
from ranker import rank_resumes

# ---- CONFIG ----
UPLOAD_FOLDER = "uploaded_resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---- UI ----
st.set_page_config(page_title="AI Resume Ranker", layout="wide")
st.title("🤖 AI-Powered Resume Ranker")
st.markdown("Upload resumes and paste a job description to see ranked matches!")

# ---- Upload Resumes ----
uploaded_files = st.file_uploader("Upload Resume PDFs", type=['pdf', 'docx'], accept_multiple_files=True)

# ---- Job Description ----
jd_text = st.text_area("Paste Job Description here:", height=200)

# ---- Button ----
if st.button("🔍 Rank Resumes"):

    if not uploaded_files or not jd_text:
        st.warning("Please upload at least one resume and paste a job description.")
    else:
        filenames = []
        resume_texts = []

        # Save + extract text from resumes
        for uploaded_file in uploaded_files:
            save_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.read())

            try:
                text = extract_resume_text(save_path)
                filenames.append(uploaded_file.name)
                resume_texts.append(text)
            except Exception as e:
                st.error(f"❌ Error reading {uploaded_file.name}: {e}")

        # Run ranking
        scores = rank_resumes(resume_texts, jd_text)
        ranked = sorted(zip(filenames, scores), key=lambda x: x[1], reverse=True)

        # Display results
        st.success("✅ Ranking Complete!")
        st.subheader("📊 Top Matching Resumes:")
        for i, (fname, score) in enumerate(ranked, 1):
            st.write(f"**{i}. {fname}** — Score: `{score:.4f}`")
