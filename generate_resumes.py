import os
import random
from faker import Faker
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

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

styles = getSampleStyleSheet()

# Custom visual tweaking for a polished look
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Title'],
    fontSize=18,
    leading=22,
    alignment=0,
    textColor=colors.HexColor('#1A2530')
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontSize=12,
    leading=15,
    textColor=colors.HexColor('#2C3E50'),
    spaceBefore=10,
    spaceAfter=4
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#333333')
)

bullet_style = ParagraphStyle(
    'BulletCustom',
    parent=styles['Normal'],
    fontSize=9.5,
    leading=13.5,
    leftIndent=12,
    spaceBefore=2,
    textColor=colors.HexColor('#222222')
)

number_of_resume_sets = 100

for i in range(number_of_resume_sets):
    base = generate_base_background()
    
    for profile in candidate_profiles:
        filename = f"resumes/{i:03d}_{profile['group']}_{profile['name'].replace(' ', '_')}.pdf"
        
        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )
        
        story = []
        
        # Candidate Header
        story.append(Paragraph(f"<b>{profile['name']}</b>", title_style))
        contact_info = f"Email: {profile['name'].replace(' ', '.').lower()}@example.com | Phone: {base['phone']} | Location: New York, NY"
        story.append(Paragraph(contact_info, body_style))
        story.append(Spacer(1, 8))
        
        # Technical Skills Section
        story.append(Paragraph("<b>TECHNICAL SKILLS</b>", section_heading))
        story.append(Paragraph(f"<b>Languages & Tools:</b> {base['skills']}", body_style))
        story.append(Spacer(1, 6))
        
        # Professional Experience Section
        story.append(Paragraph("<b>PROFESSIONAL EXPERIENCE</b>", section_heading))
        
        # Job 1
        job1_header = f"<b>Software Engineer</b> | {base['company_1']}"
        story.append(Paragraph(f"{job1_header} <font color='#666666'>({base['comp1_dates']})</font>", body_style))
        story.append(Paragraph(f"• {base['comp1_bullet_1']}", bullet_style))
        story.append(Paragraph(f"• {base['comp1_bullet_2']}", bullet_style))
        story.append(Paragraph(f"• {base['comp1_bullet_3']}", bullet_style))
        story.append(Spacer(1, 6))
        
        # Job 2
        job2_header = f"<b>Junior Software Engineer</b> | {base['company_2']}"
        story.append(Paragraph(f"{job2_header} <font color='#666666'>({base['comp2_dates']})</font>", body_style))
        story.append(Paragraph(f"• {base['comp2_bullet_1']}", bullet_style))
        story.append(Paragraph(f"• {base['comp2_bullet_2']}", bullet_style))
        story.append(Spacer(1, 8))
        
        # Education Section
        story.append(Paragraph("<b>EDUCATION</b>", section_heading))
        story.append(Paragraph(f"<b>{base['university']}</b> — {base['degree']} (Class of {base['grad_year']})", body_style))
        story.append(Paragraph(f"Cumulative GPA: {base['gpa']} / 4.00", body_style))
        
        # Build PDF file
        doc.build(story)

print("Detailed PDF resume generation complete.")