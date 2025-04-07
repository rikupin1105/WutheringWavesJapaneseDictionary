import csv
import glob

output_file = "GoogleJapaneseIME.txt"
csv_files = sorted(glob.glob("data/*.csv"))

first = True
with open(output_file, "w", newline="", encoding="utf-8") as f_out:
    writer = csv.writer(f_out, delimiter="\t")
    for file in csv_files:
        with open(file, newline="", encoding="utf-8") as f_in:
            reader = csv.reader(f_in)
            for i, row in enumerate(reader):
                if i == 0 and not first:
                    continue  # Skip header except for the first file
                writer.writerow(row)
        first = False
