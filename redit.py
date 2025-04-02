import csv

# File paths
input_file = '/home/wm0395/BTP/Dataset/metadata.csv'
output_file = '/home/wm0395/BTP/Dataset/speechdata.txt'

# Read and modify the CSV
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='|')
    writer = csv.writer(outfile, delimiter='|')
    
    for row in reader:
        if row[0].startswith('class'):
            row[0] = f"DUMMY1/{row[0]}.wav"
        writer.writerow(row)

print(f"Modified CSV saved to {output_file}")