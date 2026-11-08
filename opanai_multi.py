from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import csv
import threading

from openai import OpenAI
from api_key import get_openai_key

MAX_CONCURRENT_RESUMES = 6
resume_directory = Path("resumes_test")
instructions = (
    "You rank resumes for a software engineering position. "
    "Give a rating from 0 (worst) to 100. Only output a single number."
)


client_local = threading.local()


def get_client():
    if not hasattr(client_local, "client"):
        client_local.client = OpenAI(api_key=get_openai_key())
    return client_local.client


def rate_resume(resume_path):
    client = get_client()
    with resume_path.open("rb") as resume_file:
        uploaded_file = client.files.create(file=resume_file, purpose="user_data")

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=instructions,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_id": uploaded_file.id,
                    }
                ],
            }
        ],
    )
    return [resume_path.name, response.output_text]

resume_paths = sorted(path for path in resume_directory.iterdir() if path.is_file())
with open("responses.csv", "a", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_RESUMES) as executor:
        futures = [executor.submit(rate_resume, path) for path in resume_paths]
        for future in as_completed(futures):
            result = future.result()
            print(result[1], flush=True)
            csv_writer.writerow(result)
