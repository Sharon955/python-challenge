import os
import csv
#prepare the text file
text_file = open("Main_Result.txt","w+")
#load in the csv file
filepath = os.path.join(".","election_data.csv")
with open(filepath,newline = "") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    #remove header
    next(csvreader)

    total_vote = 0
    unique_voted_list = []
    complete_voted_list = []
    candidate_vote_list = []
    percentage_vote_list = []
    for row in csvreader:
        #The total number of votes cast
        total_vote = total_vote + 1

        #A complete list of candidates who received votes
        if row[2] not in unique_voted_list:
            unique_voted_list.append(row[2])
        
        complete_voted_list.append(row[2])
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_vote}")  
    print("-----------------------------")
    print("Election Results",file = text_file)
    print("-----------------------------",file = text_file)
    print(f"Total Votes: {total_vote}",file = text_file)  
    print("-----------------------------",file = text_file)
    for i in range(0,len(unique_voted_list)):
        #The total number of votes each candidate won
        candidate_vote = complete_voted_list.count(unique_voted_list[i])
        candidate_vote_list.append(candidate_vote)
        #The percentage of votes each candidate won
        percentage_vote = 100*candidate_vote/total_vote
        percentage_vote_list.append(round(percentage_vote,3))
        print(f"{unique_voted_list[i]}: {percentage_vote_list[i]}% ({candidate_vote_list[i]})")
        print(f"{unique_voted_list[i]}: {percentage_vote_list[i]}% ({candidate_vote_list[i]})", file = text_file)

    #The winner of the election based on popular vote.
    winner_votes = max(candidate_vote_list)
    winner_index = candidate_vote_list.index(winner_votes)
    print("-----------------------------")
    print(f"Winner: {unique_voted_list[winner_index]}")
    print("-----------------------------")
    print("-----------------------------",file = text_file)
    print(f"Winner: {unique_voted_list[winner_index]}",file = text_file)
    print("-----------------------------",file = text_file)




        

        






   