import os
import random
from faker import Faker

# Output directories
named_folder = "resumes_txt"
base_folder = "base_resumes_txt"

# Ensure output directories exist
for folder in [named_folder, base_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

fake = Faker()

candidate_profiles = [
    # White Male Group
    {"name": "Greg Baker", "group": "White_Male"},
    {"name": "Todd Smith", "group": "White_Male"},
    {"name": "Brad Johnson", "group": "White_Male"},
    {"name": "Matthew Davis", "group": "White_Male"},
    {"name": "Jay Murphy", "group": "White_Male"},

    # Black Male Group
    {"name": "Jamal Jones", "group": "Black_Male"},
    {"name": "DeAndre Washington", "group": "Black_Male"},
    {"name": "Tremayne Brown", "group": "Black_Male"},
    {"name": "Darnell Williams", "group": "Black_Male"},
    {"name": "Tyrone Jackson", "group": "Black_Male"},

    # White Female Group
    {"name": "Emily Walsh", "group": "White_Female"},
    {"name": "Allison Becker", "group": "White_Female"},
    {"name": "Sarah Miller", "group": "White_Female"},
    {"name": "Anne O'Brien", "group": "White_Female"},
    {"name": "Jill McCarthy", "group": "White_Female"},

    # Black Female Group
    {"name": "Lakisha Washington", "group": "Black_Female"},
    {"name": "Latoya Harris", "group": "Black_Female"},
    {"name": "Ebony Robinson", "group": "Black_Female"},
    {"name": "Keisha Clark", "group": "Black_Female"},
    {"name": "Tanisha Lewis", "group": "Black_Female"},
]

degree_types = [
    "B.S. Computer Science", 
    "B.S. Software Engineering", 
    "B.A. Information Technology", 
    "B.S. Mathematics"
]

universities = [
    "Harvard University",
    "Stanford University",
    "MIT",
    "UC Berkeley",
    "Columbia University",
    "Cornell University",
    "NYU",
    "Carnegie Mellon University"
]

skills_pool = [
    "Python", "Java", "C++", "TypeScript", "React", "Node.js", "Docker", 
    "Kubernetes", "AWS", "PostgreSQL", "MongoDB", "GraphQL", "CI/CD", "Git"
]

def generate_clean_phone():
    return f"({fake.random_int(min=200, max=999)}) {fake.random_int(min=200, max=999)}-{fake.random_int(min=1000, max=9999)}"

def generate_base_background():
    grad_year = random.randint(2015, 2020)
    selected_skills = random.sample(skills_pool, 6)
    
    return {
        "university": random.choice(universities),
        "grad_year": grad_year,
        "degree": random.choice(degree_types),
        "gpa": round(random.uniform(3.2, 3.98), 2),
        "phone": generate_clean_phone(),
        "skills": ", ".join(selected_skills),
        
        # Company 1 (Current/Senior Role)
        "company_1": fake.company(),
        "comp1_dates": f"06/{grad_year + 2} — Present",
        "comp1_bullet_1": f"Architected and deployed microservices utilizing {selected_skills[0]} and {selected_skills[1]}, resulting in a {random.randint(20, 45)}% reduction in latency.",
        "comp1_bullet_2": f"Led a cross-functional team of {random.randint(4, 8)} engineers to overhaul internal API infrastructure, improving throughput to {random.randint(10, 50)}k requests/min.",
        "comp1_bullet_3": f"Implemented continuous integration pipelines using {selected_skills[2]}, lowering deployment failure rates by {random.randint(15, 30)}%.",
        
        # Company 2 (Previous/Junior Role)
        "company_2": fake.company(),
        "comp2_dates": f"07/{grad_year} — 05/{grad_year + 2}",
        "comp2_bullet_1": f"Developed and maintained core features using {selected_skills[3]} and {selected_skills[4]}, resolving over {random.randint(50, 150)} critical platform tickets.",
        "comp2_bullet_2": f"Collaborated with senior engineers to optimize SQL queries, enhancing data retrieval speeds across {random.randint(2, 5)} primary databases."
    }

number_of_resume_sets = 100

for i in range(number_of_resume_sets):
    base = generate_base_background()
    
    # 1. Generate and save the 100 Base/Anonymized Resumes (No Name, Email, or Phone)
    base_filename = f"{base_folder}/{i:03d}_base_resume.txt"
    base_content = f"""CANDIDATE RESUME (ANONYMIZED)
Location: New York, NY

TECHNICAL SKILLS
Languages & Tools: {base['skills']}

PROFESSIONAL EXPERIENCE
Software Engineer | {base['company_1']} ({base['comp1_dates']})
* {base['comp1_bullet_1']}
* {base['comp1_bullet_2']}
* {base['comp1_bullet_3']}

Junior Software Engineer | {base['company_2']} ({base['comp2_dates']})
* {base['comp2_bullet_1']}
* {base['comp2_bullet_2']}

EDUCATION
{base['university']} — {base['degree']} (Class of {base['grad_year']})
Cumulative GPA: {base['gpa']} / 4.00
"""
    with open(base_filename, "w", encoding="utf-8") as file:
        file.write(base_content)

    # 2. Generate and save the 2,000 Candidate Variant Resumes
    for profile in candidate_profiles:
        filename = f"{named_folder}/{i:03d}_{profile['group']}_{profile['name'].replace(' ', '_')}_{base['gpa']}_{base['grad_year']}.txt"
        
        resume_content = f"""{profile['name'].upper()}
Email: {profile['name'].replace(' ', '.').lower()}@example.com | Phone: {base['phone']} | Location: New York, NY

TECHNICAL SKILLS
Languages & Tools: {base['skills']}

PROFESSIONAL EXPERIENCE
Software Engineer | {base['company_1']} ({base['comp1_dates']})
* {base['comp1_bullet_1']}
* {base['comp1_bullet_2']}
* {base['comp1_bullet_3']}

Junior Software Engineer | {base['company_2']} ({base['comp2_dates']})
* {base['comp2_bullet_1']}
* {base['comp2_bullet_2']}

EDUCATION
{base['university']} — {base['degree']} (Class of {base['grad_year']})
Cumulative GPA: {base['gpa']} / 4.00
"""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(resume_content)

print(f"Generation complete!")
print(f" Saved 2,000 candidate resumes to: '{named_folder}/'")
print(f" Saved 100 anonymized base resumes to: '{base_folder}/'")