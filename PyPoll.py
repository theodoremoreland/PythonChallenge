import os
import csv

csvpath = os.path.join("..", "PythonChallenge", "data", "election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Converts csv to list
    poll = list(csvreader)

    # List of unique names in "candidate" column
    candidates = []

    # Dictionary with candidate names as keys and how often their name occurrs in "poll" list as values
    votes = {}
    
    # Adds names to "candidates" list from candidate column only if that name isn't already in the list
    for every_row in poll:
        if every_row[2] in candidates:
            continue
        else:
            candidates.append(every_row[2])

    # Adds candidate names (as keys) to "votes" dictionary with the number of times that name is found (as values)
    for i in candidates:
        count = 0
        for every_row in poll:
            if i in every_row[2]:
                count += 1
        votes[i] = count

    total = sum(votes.values())
    most_votes = max(votes.values())

    header = (f"Election Results \n-------------------------\nTotal Votes: {total}\n-------------------------\n")
    body = []

    # Loops through "votes" dictionary then appends each key,value pair to "body" list (as a tuple)
    for x,y in votes.items():
        person = x
        per100 = (y / total) * 100
        net = y
        body.append((f"{person}: {round(per100, 3)}% ({net})\n"))
        if y == most_votes:
            winner = (f"Winner: {person}")
    tail = ("-------------------------\n" + winner)

# "*body" extracts each element of the "body" list such that the elements can be printed as strings and not list elements
print(header, *body, tail)

# Merges each element of "body" into one string that acknowledges each "\n" command
nwbody = "\n".join(body)
output = header + nwbody + tail

f = open('./output/PyPoll_Export.txt','w')
f.write(output)
f.close()
