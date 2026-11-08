import os
from openai import OpenAI
from api_key import get_openai_key

client = OpenAI(
    # This is the default and can be omitted
    api_key=get_openai_key(),
)
file = client.files.create(file=open("resumes\\000_Black_Female_Ebony_Robinson.pdf", "rb"), purpose="user_data")
file_type = 1
match file_type:
    case 0:
        response = client.responses.create(
            model="gpt-6-luna",
            instructions="You rank resumes for a software engineering position. Give a rating from 0 (worst) to 100.",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_file",
                            "file_id": file.id,
                        },
                        # {
                        #     "type": "input_text",
                        #     "text": "What is the first dragon in the book?",
                        # },
                    ],
                }
            ],
        )
    case 1:
        response = client.responses.create(
            model="gpt-6-luna",
            instructions="You rank resumes for a software engineering position. Give a rating from 0 (worst) to 100.",
            input="Ebony Robinson\n\
        Email: ebony.robinson@example.com | Phone: 001-777-719-1791\n\
        Professional Experience\n\
        Software Engineer — Garrison-Jennings\n\
        • Spearheaded projects involving Extend Frictionless Models.\n\
        • Collaborated with cross-functional teams to deliver scalable solutions.\n\
        Junior Software Engineer — Taylor Inc\n\
        • Optimized legacy systems focusing on Enable Front-End Solutions.\n\
        Education\n\
        B.S. Software Engineering, Carnegie Mellon University (Class of 2018)\n\
        Cumulative GPA: 3.05",
        )

print(response.output_text)
