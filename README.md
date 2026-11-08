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
   There are 16 preset names, 4 different races, and 2 genders for each race

   It then generates a random university, skills, grad year, gpa, phone number, email, degree, companies worked at with a brief description, a random second language from the 4 additional languages, and a neutral club

   Next, it creates a base resume with that info and also 16 unique ones with the names, zipcodes that are predominantly a certain race/soci-economic class, adds a certain ethnic langaue to each race, an ethnic or neurtral club (depending on race), and saves them to .txt files
    
5. Generate ratings with OpenAI
6. Analyze the results to see differences

## Team
Wesley Pang ([Github](https://github.com/Wesley25Pang05))
Matthew Park ([Github](https://github.com/matthewjpark))
Jean Gautier ([Github](https://github.com/JeanLuc49))
