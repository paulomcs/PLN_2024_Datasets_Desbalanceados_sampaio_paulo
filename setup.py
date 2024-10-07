import csv
import json
import random

# Load configuration from config.json
with open('./config.json') as f:
    config = json.load(f)

# Define the input and output file paths
fake_csv_path = './Database/Fake.csv'
true_csv_path = './Database/True.csv'
output_csv_path = './Database/Mixed.csv'

# Load the CSV files
with open(fake_csv_path, 'r') as f:
    fake_reader = csv.reader(f)
    fake_data = list(fake_reader)

with open(true_csv_path, 'r') as f:
    true_reader = csv.reader(f)
    true_data = list(true_reader)

# Calculate the number of rows to take from each file based on the unbalanced ratio
num_fake_rows = int(len(fake_data) * config['unbalanced_ratio'])
num_true_rows = len(true_data) - num_fake_rows

# Select a random subset of rows from each file
fake_subset = random.sample(fake_data, num_fake_rows)
true_subset = random.sample(true_data, num_true_rows)

# Combine the subsets and shuffle the result
mixed_data = fake_subset + true_subset
random.shuffle(mixed_data)

# Write the mixed data to the output CSV file
with open(output_csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(mixed_data)