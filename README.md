# Resume Bias

Resume Bias is an application where fake resumes are designed to test ChatGPT to check whether its model has bias toward certain genders or races.

## Set up

1. Clone the repository:
   ```bash
   git clone https://github.com/matthewjpark/resume-bias-NYCAIRR-hackathon-fall-26
   cd resume-bias-NYCAIRR-hackathon-fall-26
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file:
   ```env
   OPENAI_API_KEY=your-generated-key
   ```
4. Create resumes. Currently, there are premade candidates, degree types, and universities. You can edit these; the premade versions are the test we used. To create the resumes, run:
   ```bash
   python generate_resumes.py
   ```
5. Generate ratings with OpenAI
6. Analyze the results to see differences

## Team
Wesley Pang ([@github-handle](https://github.com/Wesley25Pang05))
Matthew Park ([@github-handle](https://github.com/matthewjpark))
Jean Gautier ([@github-handle](https://github.com/JeanLuc49))
