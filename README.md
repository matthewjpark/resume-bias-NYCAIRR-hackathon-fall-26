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
   There are 20 preset names, 10 male, 10 female, and there are 5 typically black and 5 typically white names for each gender.

   It then generates a random university, skills, grad year, gpa, phone number, email, degree, companies worked at with a brief description.

   Next, it creates a base resume with that info and also 20 unique ones with the names and saves them to .txt files
    
5. Generate ratings with OpenAI
6. Analyze the results to see differences

## Team
Wesley Pang ([Github](https://github.com/Wesley25Pang05))
Matthew Park ([Github](https://github.com/matthewjpark))
Jean Gautier ([Github](https://github.com/JeanLuc49))


## How it works
generate_resumes.py randomly generates many resumes that are nearly identical, except with 
[insert updated file name here opanai_multi.py] sends the resume to the OpenAI API and returns a score from 0 to 100. The file name, along with the score, is stored in a csv file for analyze.py to then parse and analyze.