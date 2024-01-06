import pandas as pd
import sys

def clean_csv(input_filename, output_filename):
    # Read the CSV file
    df = pd.read_csv(input_filename, encoding='latin1')

    # Clean the data
    df = df.applymap(lambda x: x.encode('unicode_escape').decode('utf-8') if isinstance(x, str) else x)

    # Write the cleaned data to the new CSV file
    df.to_csv(output_filename, index=False, encoding='utf-8')

# Get the input and output filenames from the command line arguments
input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Call the function
clean_csv(input_filename, output_filename)
