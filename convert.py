import pandas as pd

csv = input("What is your csv file name? ")
if csv[-4:] != ".csv":
    csv += ".csv"

try:
    table = pd.read_csv(csv, header=None, names=["FileName", "Rating"])
except:
    print("No CSV file found")
    exit()

rows = []
for filename, rating in zip(table["FileName"], table["Rating"]):
    try:
        rating = float(rating)
        parts = filename[:-4].split("_")

        if parts[1] == "base":
            rows.append({
                "FileName": filename,
                "Rating": rating,
                "Race": "NA",
                "Gender": "NA",
                "GPA": float(parts[3]),
                "Graduating Year": int(parts[5]),
                "Set": parts[0],
                "Name": "NA",
            })
        else:
            rows.append({
                "FileName": filename,
                "Rating": rating,
                "Race": parts[1],
                "Gender": parts[2],
                "GPA": float(parts[-2]),
                "Graduating Year": int(parts[-1]),
                "Set": parts[0],
                "Name": "_".join(parts[3:-2]),
            })
    except:
        print(f"Error for {filename}")

out = pd.DataFrame(rows)
out.to_csv(f"output-{csv}", index=False)
print(f"Done and ready to run py analyze.py with output-{csv}")
