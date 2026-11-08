import os
from openai import OpenAI
from api_key import get_openai_key
import csv

client = OpenAI(
    api_key=get_openai_key(),
)
list_to_export = []
resume_directory_str = "resumes_test"
directory = os.fsencode(resume_directory_str)
for filepath in os.listdir(directory):
    filename = os.fsdecode(filepath)
    file = client.files.create(file=open(resume_directory_str + "\\"  + filename, "rb"), purpose="user_data")
    response = client.responses.create(
        model="gpt-6-luna",
        instructions="You rank resumes for a software engineering position. Give a rating from 0 (worst) to 100. Only output a single number.",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_id": file.id,
                    }
                ],
            }
        ],
        #text={"verbosity": "low"},
    )
    print(response.output_text)
    split_title = filename.split("_")
    rating_metadata = [filename, response.output_text, split_title[1], split_title[2], split_title[4], split_title[3]]
    list_to_export.append(rating_metadata)

with open("responses.csv", "a") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(list_to_export)
