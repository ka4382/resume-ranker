from ranker import load_resumes, load_job_description, rank_resumes

# Paths
resume_folder = "sample_resumes"
jd_file = "job_description.txt"

# Load data
filenames, resumes = load_resumes(resume_folder)
jd = load_job_description(jd_file)

# Rank
scores = rank_resumes(resumes, jd)

# Display results
ranked = sorted(zip(filenames, scores), key=lambda x: x[1], reverse=True)

print("\n📊 Ranked Resumes (Top Matches First):\n")
for i, (name, score) in enumerate(ranked):
    print(f"{i+1}. {name} — Score: {score:.4f}")
