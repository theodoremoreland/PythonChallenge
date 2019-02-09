import os
import csv

csvpath = os.path.join("..", "python-challenge", "PyPoll", "election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #converts csv to list
    poll = list(csvreader)

    #list of unique names in "canidate" column
    canidates = []

    #dictionary with canidate names as keys and how often their name occurrs in "poll" list as values
    votes = {}
    
    #adds names to "canidates" list from canidate column only if that name isn't already in the list
    for every_row in poll:
        if every_row[2] in canidates:
            continue
        else:
            canidates.append(every_row[2])

    #adds candidate names (as keys) to "votes" dictionary with the number of times that name is found (as values)
    for i in canidates:
        count = 0
        for every_row in poll:
            if i in every_row[2]:
                count += 1
        votes[i] = count

    total = sum(votes.values())
    most_votes = max(votes.values())

    header = (f"Election Results \n-------------------------\nTotal Votes: {total}\n-------------------------\n")
    body = []

    #loops through "votes" dictionary then appends each key,value pair to "body" list (as a tuple)
    for x,y in votes.items():
        person = x
        per100 = (y / total) * 100
        net = y
        body.append((f"{person}: {round(per100, 3)}% ({net})\n"))
        if y == most_votes:
            winner = (f"Winner: {person}")
    tail = ("-------------------------\n" + winner)

#"*body" extracts each element of the "body" list such that the elements can be printed as strings and not list elements
print(header, *body, tail)
#merges each element of "body" into one string that acknowledges each "\n" command
nwbody = "\n".join(body)
output = header + nwbody + tail
f = open('PyPoll_Export.txt','w')
f.write(output)
f.close()
