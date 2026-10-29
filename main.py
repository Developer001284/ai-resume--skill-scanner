# AI Resume Skill Scanner - by Developer001284
# This tool scans resume text and extracts skills - perfect for hiring AI!

def scan_resume(resume_text):
    print("\n🔍 Scanning Resume with AI...\n")
    
    skills_db = ["python", "java", "ai", "machine learning", "github", "sql", "javascript", "react", "communication", "teamwork"]
    
    found_skills = []
    resume_lower = resume_text.lower()
    
    for skill in skills_db:
        if skill in resume_lower:
            found_skills.append(skill.title())
    
    print(f"✅ Found {len(found_skills)} Skills:")
    for skill in found_skills:
        print(f"   - {skill}")
    
    score = len(found_skills) * 10
    print(f"\n⭐ Resume Score: {score}/100")
    
    if score >= 50:
        print("🎉 Verdict: SHORTLISTED for Interview!")
    else:
        print("💡 Verdict: Add more technical skills")
