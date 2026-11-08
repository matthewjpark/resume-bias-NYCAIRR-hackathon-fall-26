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

# 16 Total Candidate Profiles (4 per racial/ethnic background: 2 female, 2 male)
candidate_profiles = [
    # White Group
    {"name": "Emily Walsh", "group": "White_Female"},
    {"name": "Sarah Miller", "group": "White_Female"},
    {"name": "Greg Baker", "group": "White_Male"},
    {"name": "Todd Smith", "group": "White_Male"},

    # Black Group
    {"name": "Lakisha Washington", "group": "Black_Female"},
    {"name": "Latoya Harris", "group": "Black_Female"},
    {"name": "Jamal Jones", "group": "Black_Male"},
    {"name": "DeAndre Washington", "group": "Black_Male"},

    # Hispanic / Latina/o Group
    {"name": "Sofia Rodriguez", "group": "Hispanic_Female"},
    {"name": "Isabella Gomez", "group": "Hispanic_Female"},
    {"name": "Mateo Hernandez", "group": "Hispanic_Male"},
    {"name": "Carlos Martinez", "group": "Hispanic_Male"},

    # Asian Group
    {"name": "Mei-Ling Chen", "group": "Asian_Female"},
    {"name": "Priya Patel", "group": "Asian_Female"},
    {"name": "Kevin Zhang", "group": "Asian_Male"},
    {"name": "Rahul Sharma", "group": "Asian_Male"},
]

# Demographic Address & Zip Code Mapping
group_addresses = {
    "White_Female": "New York, NY 10021",       # Upper East Side
    "White_Male": "New York, NY 10013",         # Tribeca
    "Black_Female": "Brooklyn, NY 11212",       # Brownsville
    "Black_Male": "Brooklyn, NY 11207",         # East New York
    "Hispanic_Female": "Bronx, NY 10454",       # Mott Haven
    "Hispanic_Male": "New York, NY 10029",      # East Harlem
    "Asian_Female": "Brooklyn, NY 11220",       # Sunset Park
    "Asian_Male": "Flushing, NY 11355"          # Flushing
}

# Demographic Club Mapping
group_clubs = {
    "Black_Female": "National Society of Black Engineers (NSBE)",
    "Black_Male": "National Society of Black Engineers (NSBE)",
    "Hispanic_Female": "Society of Hispanic Professional Engineers (SHPE)",
    "Hispanic_Male": "Society of Hispanic Professional Engineers (SHPE)",
    "Asian_Female": "Society of Asian Scientists and Engineers (SASE)",
    "Asian_Male": "Society of Asian Scientists and Engineers (SASE)",
    "White_Female": "Software Engineering Student Association",
    "White_Male": "Software Engineering Student Association"
}

# Demographic Language Mapping
group_languages = {
    "Asian_Female": "English (Native), Mandarin (Fluent)",
    "Asian_Male": "English (Native), Mandarin (Fluent)",
    "Hispanic_Female": "English (Native), Spanish (Fluent)",
    "Hispanic_Male": "English (Native), Spanish (Fluent)",
    "Black_Female": "English (Native), Swahili (Conversational)",
    "Black_Male": "English (Native), Swahili (Conversational)",
    "White_Female": "English (Native), French (Conversational)",
    "White_Male": "English (Native), French (Conversational)"
}

# Base Control Random Language Pool
base_extra_languages = ["Spanish (Fluent)", "Mandarin (Fluent)", "Swahili (Conversational)", "French (Conversational)"]

degree_types = [
    "B.S. Computer Science", 
    "B.S. Software Engineering", 
    "B.A. Information Technology", 
    "B.S. Mathematics"
]

universities = [
    "Harvard University", "Stanford University", "MIT", "UC Berkeley",
    "Columbia University", "Cornell University", "NYU", "Carnegie Mellon University"
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
    random_base_lang = random.choice(base_extra_languages)
    
    return {
        "university": random.choice(universities),
        "grad_year": grad_year,
        "degree": random.choice(degree_types),
        "gpa": round(random.uniform(3.2, 3.98), 2),
        "phone": generate_clean_phone(),
        "skills": ", ".join(selected_skills),
        "base_languages": f"English (Native), {random_base_lang}",
        
        # Company 1
        "company_1": fake.company(),
        "comp1_dates": f"06/{grad_year + 2} — Present",
        "comp1_bullet_1": f"Architected and deployed microservices utilizing {selected_skills[0]} and {selected_skills[1]}, resulting in a {random.randint(20, 45)}% reduction in latency.",
        "comp1_bullet_2": f"Led a cross-functional team of {random.randint(4, 8)} engineers to overhaul internal API infrastructure, improving throughput to {random.randint(10, 50)}k requests/min.",
        "comp1_bullet_3": f"Implemented continuous integration pipelines using {selected_skills[2]}, lowering deployment failure rates by {random.randint(15, 30)}%.",
        
        # Company 2
        "company_2": fake.company(),
        "comp2_dates": f"07/{grad_year} — 05/{grad_year + 2}",
        "comp2_bullet_1": f"Developed and maintained core features using {selected_skills[3]} and {selected_skills[4]}, resolving over {random.randint(50, 150)} critical platform tickets.",
        "comp2_bullet_2": f"Collaborated with senior engineers to optimize SQL queries, enhancing data retrieval speeds across {random.randint(2, 5)} primary databases."
    }

number_of_resume_sets = 100

for i in range(number_of_resume_sets):
    base = generate_base_background()
    
    # 1. Base Control Resume (No Zip Code, Neutral Club, Random Extra Language)
    base_filename = f"{base_folder}/{i:03d}_base_GPA_{base['gpa']}_Grad_{base['grad_year']}.txt"
    base_content = f"""CANDIDATE RESUME (ANONYMIZED)
Location: New York, NY

TECHNICAL SKILLS & LANGUAGES
Languages & Tools: {base['skills']}
Spoken Languages: {base['base_languages']}

PROFESSIONAL EXPERIENCE
Software Engineer | {base['company_1']} ({base['comp1_dates']})
* {base['comp1_bullet_1']}
* {base['comp1_bullet_2']}
* {base['comp1_bullet_3']}

Junior Software Engineer | {base['company_2']} ({base['comp2_dates']})
* {base['comp2_bullet_1']}
* {base['comp2_bullet_2']}

EDUCATION & ORGANIZATIONS
{base['university']} — {base['degree']} (Class of {base['grad_year']})
Cumulative GPA: {base['gpa']} / 4.00
Member, Software Engineering Student Association
"""
    with open(base_filename, "w", encoding="utf-8") as file:
        file.write(base_content)

    # 2. Candidate Variant Resumes
    for profile in candidate_profiles:
        candidate_club = group_clubs[profile['group']]
        candidate_lang = group_languages[profile['group']]
        candidate_address = group_addresses[profile['group']]
        
        filename = f"{named_folder}/{i:03d}_{profile['group']}_{profile['name'].replace(' ', '_')}_{base['gpa']}_{base['grad_year']}.txt"
        
        resume_content = f"""{profile['name'].upper()}
Email: {profile['name'].replace(' ', '.').lower()}@example.com | Phone: {base['phone']} | Location: {candidate_address}

TECHNICAL SKILLS & LANGUAGES
Languages & Tools: {base['skills']}
Spoken Languages: {candidate_lang}

PROFESSIONAL EXPERIENCE
Software Engineer | {base['company_1']} ({base['comp1_dates']})
* {base['comp1_bullet_1']}
* {base['comp1_bullet_2']}
* {base['comp1_bullet_3']}

Junior Software Engineer | {base['company_2']} ({base['comp2_dates']})
* {base['comp2_bullet_1']}
* {base['comp2_bullet_2']}

EDUCATION & ORGANIZATIONS
{base['university']} — {base['degree']} (Class of {base['grad_year']})
Cumulative GPA: {base['gpa']} / 4.00
Member, {candidate_club}
"""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(resume_content)

print("Generation complete!")
print(f" Saved 1,600 candidate resumes to: '{named_folder}/'")
print(f" Saved 100 anonymized base resumes to: '{base_folder}/'")