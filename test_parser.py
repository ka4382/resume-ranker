from resume_parser import extract_resume_text

file_path = "sample_resumes/resume1.pdf"  # Pick any resume you placed
text = extract_resume_text(file_path)

print("\n📄 First 1000 characters of resume:\n")
print(text[:1000])  # Print first 1000 characters to check
