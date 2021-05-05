# The Data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candiate won
# 5. The winner of the election based on popular vote

#AT SECTION 3.4.3

import csv
import os

# Assign a variable to load the file to a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to the save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform Analysis
    file_reader = csv.reader(election_data)
    # Read and print the headers
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file
    #for row in file_reader:
    #    print(row[0])

# Close the file
#election_data.close()

# Create a filename variable to a direct or indirect path to the file


with open(file_to_save,"w") as txt_file:

    txt_file.write("Counties in the Election\n--------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

#txt_file.close()