import os
import re

def combine_yob_files(input_folder, output_file):
    yob_pattern = re.compile(r"yob(\d{4})\.txt$")

    with open(output_file, "w", encoding="utf-8") as outfile:
        for filename in sorted(os.listdir(input_folder)):
            match = yob_pattern.match(filename)
            if match:
                year = match.group(1)
                file_path = os.path.join(input_folder, filename)
                with open(file_path, "r", encoding="utf-8") as infile:
                    for line in infile:
                        line = line.strip()
                        if line:
                            outfile.write(f"{line},{year}\n")

if __name__ == "__main__":
    input_folder = r"C:\Users\mimii\Downloads\names"
    output_file = "all_yob.txt"
    combine_yob_files(input_folder, output_file)
    print("file written")
