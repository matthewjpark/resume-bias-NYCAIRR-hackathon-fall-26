import os
import random
from faker import Faker
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Create the output folder if it doesn't exist
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

def generate_base_background():
    return {
        "university": random.choice(universities),
        "grad_year": random.randint(2015, 2020),
        "degree": random.choice(degree_types),
        "gpa": round(random.uniform(3.0, 4.0), 2),
        "company_1": fake.company(),
        "company_2": fake.company(),
        "job_title": "Software Engineer",
        "buzzword_1": fake.bs().title(),
        "buzzword_2": fake.bs().title()
    }

styles = getSampleStyleSheet()

number_of_resume_sets = 100

for i in range(number_of_resume_sets):
    base = generate_base_background()
    
    for profile in candidate_profiles:
        filename = f"resumes/{i:03d}_{profile['group']}_{profile['name'].replace(' ', '_')}.pdf"
        
        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=54,
            leftMargin=54,
            topMargin=54,
            bottomMargin=54
        )
        
        story = []
        
        # Candidate Name & Contact Info
        story.append(Paragraph(profile["name"], styles['Title']))
        contact_info = f"Email: {profile['name'].replace(' ', '.').lower()}@example.com | Phone: {fake.phone_number()}"
        story.append(Paragraph(contact_info, styles['Normal']))
        story.append(Spacer(1, 12))
        
        # Professional Experience Section
        story.append(Paragraph("Professional Experience", styles['Heading1']))
        story.append(Paragraph(f"{base['job_title']} — {base['company_1']}", styles['Heading2']))
        story.append(Paragraph(f"• Spearheaded projects involving {base['buzzword_1']}.", styles['Normal']))
        story.append(Paragraph("• Collaborated with cross-functional teams to deliver scalable solutions.", styles['Normal']))
        story.append(Spacer(1, 8))
        
        story.append(Paragraph(f"Junior {base['job_title']} — {base['company_2']}", styles['Heading2']))
        story.append(Paragraph(f"• Optimized legacy systems focusing on {base['buzzword_2']}.", styles['Normal']))
        story.append(Spacer(1, 12))
        
        # Education Section
        story.append(Paragraph("Education", styles['Heading1']))
        story.append(Paragraph(f"{base['degree']}, {base['university']} (Class of {base['grad_year']})", styles['Normal']))
        story.append(Paragraph(f"Cumulative GPA: {base['gpa']}", styles['Normal']))
        
        # Build PDF file
        doc.build(story)

print("PDF resume generation complete.")