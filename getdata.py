import pandas as pd

# Path to the Excel file
excel_file_path = "HINDALCO_1D.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Display the DataFrame
#print(df)

count = 0
for i in range(0,len(df.index)):

    first_row_loc = df.loc[i]["instrument"]
    count=count+1
    #print(first_row_loc)
print(count)
print(len(df.index))