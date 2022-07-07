# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
# from termios import OFDEL

# # Add a variable to load a file from a path.
file_to_load = os.path.join(".", "Resources", "election_results.csv")
# # Add a variable to save the file to a path.
file_to_save = os.path.join(".", "Analysis", "election_analysis.txt")
path = "C:/PS/election_results.csv"
# isFile=os.path.isfile(path)
# print(isFile)

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
# Initialize a list for candidate_options i.e the names of the candidates
candidate_options = []

# Initialize a dictionary for candidate votes which holds the key of candidate name and value of running total 
candidate_votes = {}

# Initialize a list for county_options i.e the names of the counties
county_options = []

# initialize a dictionary for counties which holds the key of county name and the value of running total of 
# votes cast in that county
county_votes = {}

# note to me, 
# # Change Dictionary Values in Python Using the dict. update() Method.
# up_dict = {"Python":500}
# print("Dictionary before updation:",dict)
# dict.update(up_dict)
# print("Dictionary after updation:",dict)

# 1: Fill the candidate names list, county names list, candidate votes dictionary and county votes dictionary.   I am hard-coding this but need to come back and do this 
# programatically.  Eventually I want to discover these values through code and add them dynamically, for now I'm hard-coding them because I haven't figured out
# how to do the dynamic option and am running out of time
candidate_options = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = {"Charles Casper Stockham" :0, "Diana DeGette":0,"Raymon Anthony Doane":0}
county_options = ["Arapahoe","Denver", "Jefferson" ]
county_votes = {"Arapahoe" :0, "Denver": 0 , "Jefferson": 0}


# Track the winning candidate, vote count and percentage.  Initialize the variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.  Initialize the variables
highest_turnout_county_name = ""
highest_turnout_county_votes = 0

# Read the csv file and convert it into a list of dictionaries

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            # print("Candidate name not in the candidate list, adding it")  -for debugging purposes
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
           # 4b: Add the existing county to the list of counties.
            # print("Count name not in the county list, adding it")  - for debugging purposes
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
        f"-------------------------\n")
   
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # Retrieve the county vote count and percentage
        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
          f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each county's voter count and percentage to the
        # terminal.
        # 6d: Print the county results to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
                       
        # 6f: Loop through the county_votes dictionary Write an if statement to determine the winning county and get its vote count.
        # Save the  highest_county_turnout_name, highest_county_turnout_votes values to the variables created above.
        
       
    # 7: Print the county with the largest turnout to the terminal.
     
    # 8: Save the county with the largest turnout to the text file.
 

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # #Print the current contents of the dictionaries and lists
    # print (candidate_options)
    # print (candidate_votes)
    # print(county_options)
    # print(county_votes)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
