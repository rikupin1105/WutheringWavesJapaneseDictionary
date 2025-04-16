import csv
import glob

output_file = "MicrosoftIME.txt"
csv_files = sorted(glob.glob("data/*.csv"))

first = True
with open(output_file, "w", newline="", encoding="utf-16le") as f_out:
    # UTF-16LE に BOM を追加
    f_out.write('\ufeff')
    
    writer = csv.writer(f_out, delimiter="\t")
    for file in csv_files:
        with open(file, newline="", encoding="utf-8") as f_in:
            reader = csv.reader(f_in)
            for i, row in enumerate(reader):
                if i == 0 and not first:
                    continue  # Skip header except for the first file
                writer.writerow(row)
        first = False
