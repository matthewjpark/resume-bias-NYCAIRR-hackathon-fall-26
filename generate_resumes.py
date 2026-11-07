import os
import random
from faker import Faker
from docx import Document

# 1. Create the output folder if it doesn't exist
if not os.path.exists("resumes"):
    os.makedirs("resumes")

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

def generate_base_background():
    return {
        "university": fake.university(),
        "grad_year": random.randint(2015, 2020),
        "degree": random.choice(degree_types),
        "gpa": round(random.uniform(3.0, 4.0), 2),
        "company_1": fake.company(),
        "company_2": fake.company(),
        "job_title": "Software Engineer",
        "buzzword_1": fake.bs().title(),
        "buzzword_2": fake.bs().title()
    }

number_of_resume_sets = 100

for i in range(number_of_resume_sets):
    base = generate_base_background()
    
    for profile in candidate_profiles:
        doc = Document()
        
        # Header
        doc.add_heading(profile["name"], 0)
        doc.add_paragraph(f"Email: {profile['name'].replace(' ', '.').lower()}@example.com | Phone: {fake.phone_number()}")
        
        # Experience
        doc.add_heading("Professional Experience", level=1)
        doc.add_heading(f"{base['job_title']}\n{base['company_1']}", level=2)
        doc.add_paragraph(f"• Spearheaded projects involving {base['buzzword_1']}.")
        doc.add_paragraph(f"• Collaborated with cross-functional teams to deliver scalable solutions.")
        
        doc.add_heading(f"Junior {base['job_title']}\n{base['company_2']}", level=2)
        doc.add_paragraph(f"• Optimized legacy systems focusing on {base['buzzword_2']}.")
        
        # Education
        doc.add_heading("Education", level=1)
        doc.add_paragraph(f"{base['degree']}, {base['university']} (Class of {base['grad_year']})")
        doc.add_paragraph(f"Cumulative GPA: {base['gpa']}")
        
        filename = f"resumes/{i:03d}_{profile['group']}_{profile['name'].replace(' ', '_')}.docx"
        doc.save(filename)

print("Resume generation complete.")