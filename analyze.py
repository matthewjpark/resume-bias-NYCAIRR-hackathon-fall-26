import pandas as pd
from scipy import stats

csv = input("What is your csv file name? ")
if csv[-4:] != ".csv":
    csv += ".csv"
try:
    table = pd.read_csv(csv)
except:
    print("No CSV file found")
    exit()

table["Set"] = table["FileName"].str[:3]
isBase = table["FileName"].str.contains("base_resume")
base = table[table["FileName"].str.contains("base_resume")].set_index("Set")["Rating"]
table = table[~isBase].copy()
table["Adj"] = table["Rating"] - table["Set"].map(base)

race = table.groupby("Race").agg(
    count=("Rating", "count"),
    ratingMean=("Rating", "mean"),
    ratingMedian=("Rating", "median"),
    ratingSTD=("Rating", "std"),
    GPAMean=("GPA", "mean"),
    GPAMedian=("GPA", "median"),
    GPASTD=("GPA", "std"),
    gradMean=("Graduating Year", "mean"),
    gradMedian=("Graduating Year", "median"),
    gradSTD=("Graduating Year", "std"),
)

gender = table.groupby("Gender").agg(
    count=("Rating", "count"),
    ratingMean=("Rating", "mean"),
    ratingMedian=("Rating", "median"),
    ratingSTD=("Rating", "std"),
    GPAMean=("GPA", "mean"),
    GPAMedian=("GPA", "median"),
    GPASTD=("GPA", "std"),
    gradMean=("Graduating Year", "mean"),
    gradMedian=("Graduating Year", "median"),
    gradSTD=("Graduating Year", "std"),
)

raceP = table.pivot_table(index="Set", columns="Race", values="Rating", aggfunc="mean")
diff = (raceP["White"] - raceP["Black"]).dropna()
racePVAL = stats.ttest_1samp(diff, 0)

genderP = table.pivot_table(index="Set", columns="Gender", values="Rating", aggfunc="mean")
diff = (genderP["Male"] - genderP["Female"]).dropna()
genderPVAL = stats.ttest_1samp(diff, 0)

adjP = table.pivot_table(index="Set", columns="Race", values="Adj", aggfunc="mean")
blackP = stats.ttest_1samp(adjP["Black"].dropna(), 0)
whiteP = stats.ttest_1samp(adjP["White"].dropna(), 0)

adjP = table.pivot_table(index="Set", columns="Gender", values="Adj", aggfunc="mean")
maleP = stats.ttest_1samp(adjP["Male"].dropna(), 0)
femaleP = stats.ttest_1samp(adjP["Female"].dropna(), 0)

with open("table.txt", "w") as f:
    print(f"{race.round(2)}\n\n{gender.round(2)}\n", file=f)
    print(f"White vs Black: p = {racePVAL.pvalue}", file=f)
    print(f"Black vs Base: p = {blackP.pvalue}", file=f)
    print(f"White vs Base: p = {whiteP.pvalue}", file=f)

    print(f"Male vs Female: p = {genderPVAL.pvalue}", file=f)
    print(f"Male vs Base: p = {maleP.pvalue}", file=f)
    print(f"Female vs Base: p = {femaleP.pvalue}", file=f)
    print("Done")
