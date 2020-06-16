
#Outline required steps for completing election analysis

#Load required dedependencies
import csv
import os

# Assign a variable for the load-from path and file.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable for the save-to path and file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file's content as an object.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Print the header row
    headers=next(file_reader)
    print(headers)
    
    #for row in file_reader:
    #    print(row)

#2. Compile a list of all the participating candidates

#3. Summarize the numbers of votes each candiate received

#4. Calculate thte total number of votes cast

#ß#Calculate the percentage of the total votes each candidate received

##Calculate which candidate, if any, received the majority vote
##Open the election results and read the file.
## Assign a variable for the file to load and the path.
