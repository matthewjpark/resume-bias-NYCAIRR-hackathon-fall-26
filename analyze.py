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
isBase = table["FileName"].str.contains("_base_")
baseRows = table[isBase].copy()
base = table[table["FileName"].str.contains("_base_")].set_index("Set")["Rating"]
table = table[~isBase].copy()
table["Adj"] = table["Rating"] - table["Set"].map(base)

baseRows["Group"] = "Base"
baseTable = baseRows.groupby("Group").agg(
    count=("Rating", "count"),
    ratingMean=("Rating", "mean"),
    ratingMedian=("Rating", "median"),
    ratingSTD=("Rating", "std"),
)

race = table.groupby("Race").agg(
    count=("Rating", "count"),
    ratingMean=("Rating", "mean"),
    ratingMedian=("Rating", "median"),
    ratingSTD=("Rating", "std"),
)

gender = table.groupby("Gender").agg(
    count=("Rating", "count"),
    ratingMean=("Rating", "mean"),
    ratingMedian=("Rating", "median"),
    ratingSTD=("Rating", "std"),
)

adjP = table.pivot_table(index="Set", columns="Race", values="Adj", aggfunc="mean")
blackP = stats.ttest_1samp(adjP["Black"].dropna(), 0)
whiteP = stats.ttest_1samp(adjP["White"].dropna(), 0)
asianP = stats.ttest_1samp(adjP["Asian"].dropna(), 0)
hispanicP = stats.ttest_1samp(adjP["Hispanic"].dropna(), 0)

raceP = table.pivot_table(index="Set", columns="Race", values="Rating", aggfunc="mean")
diffB = stats.ttest_1samp((raceP["White"] - raceP["Black"]).dropna(), 0)
diffA = stats.ttest_1samp((raceP["White"] - raceP["Asian"]).dropna(), 0)
diffH = stats.ttest_1samp((raceP["White"] - raceP["Hispanic"]).dropna(), 0)

adjP = table.pivot_table(index="Set", columns="Gender", values="Adj", aggfunc="mean")
maleP = stats.ttest_1samp(adjP["Male"].dropna(), 0)
femaleP = stats.ttest_1samp(adjP["Female"].dropna(), 0)

raceP = table.pivot_table(index="Set", columns="Gender", values="Rating", aggfunc="mean")
diffR = stats.ttest_1samp((raceP["Male"] - raceP["Female"]).dropna(), 0)

with open("table.txt", "w") as f:
    print(f"{race.round(2)}\n\n{gender.round(2)}\n\n{baseTable.round(2)}\n", file=f)
    print(f"Black vs Base: p = {blackP.pvalue}", file=f)
    print(f"White vs Base: p = {whiteP.pvalue}", file=f)
    print(f"Asian vs Base: p = {asianP.pvalue}", file=f)
    print(f"Hispanics vs Base: p = {hispanicP.pvalue}", file=f)
    print(f"White vs Black: p = {diffB.pvalue}", file=f)
    print(f"White vs Asian: p = {diffA.pvalue}", file=f)
    print(f"White vs Hispanic: p = {diffH.pvalue}", file=f)
    print(f"Male vs Base: p = {maleP.pvalue}", file=f)
    print(f"Female vs Base: p = {femaleP.pvalue}", file=f)
    print(f"Male vs Female: p = {diffR.pvalue}", file=f)
