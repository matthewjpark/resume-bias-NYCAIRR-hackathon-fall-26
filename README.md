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
After generating the CSV from OpenAI, we need to parse the data into columns for analyze.py. To do this, run convert.py and input the name of your file. After the file is converted, it should be called output-fileName.csv. Then you will run analyze.py with the new csv to generate tables by race, gender, and the base. It will also generate p-values to determine significance (p < 0.05)
   ```bash
   python convert.py
   ```
   ```text
   What is your csv file name? fileName
   ```
   ```bash
   python analyze.py
   ```
   ```text
   What is your csv file name? output-fileName
   ```

## Team
Wesley Pang ([Github](https://github.com/Wesley25Pang05))
Matthew Park ([Github](https://github.com/matthewjpark))
Jean Gautier ([Github](https://github.com/JeanLuc49))


## How it works
generate_resumes.py randomly generates many resumes that are nearly identical, except with 
[insert updated file name here opanai_multi.py] sends the resume to the OpenAI API and returns a score from 0 to 100. The file name, along with the score, is stored in a csv file for analyze.py to then parse and analyze.
