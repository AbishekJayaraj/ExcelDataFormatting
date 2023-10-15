import re
import pandas as pd
import shutil  # for copying the file

# Set the file names
input_file = r"C:\Users\DELL\Desktop\AbiFiles\PlantsDataset\PlantList.xlsx"
output_file = r"C:\Users\DELL\Desktop\AbiFiles\PlantsDataset\PlantList.xlsx"
backup_file = r"C:\Users\DELL\Desktop\AbiFiles\PlantsDataset\PlantList_backup.xlsx"

# Make a copy of the input file as a backup
shutil.copy(input_file, backup_file)

# Read the data from the input file
df = pd.read_excel(input_file)

# Define a function to remove brackets and their contents, as well as the comma
def remove_brackets_and_comma(text):
    # Remove text within brackets
    text = re.sub(r'\([^)]*\)', '', text)
    # Remove the comma and any following text (if present)
    text = text.split(',')[0]
    return text

# Apply the function to the specified column, 'PlantName' in this case
df['PlantName'] = df['PlantName'].apply(remove_brackets_and_comma)

# Save the modified data to the output file
df.to_excel(output_file, index=False, engine='openpyxl')
