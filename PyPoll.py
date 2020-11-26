import os
import csv


def create_list_of_candidate_names(poll_data):
    """
    """

    candidates = []

    # Adds names to "candidates" list from candidate column only if that name isn't already in the list
    for row in poll_data:
        if row[2] not in candidates:
            candidates.append(row[2])
    
    return candidates


def tally_votes_per_candidate_for_each_candidate(poll_data, candidate_names):
    """
    """

    votes_per_candidate = {} # Dictionary with candidate names as keys and how often their name occurrs in "poll_data" list as values

    # Adds candidate names (as keys) to "votes_per_candidate" dictionary with the number of times that name is found (as values)
    for candidate in candidate_names:
        vote_count = 0
        for row in poll_data:
            if candidate in row[2]:
                vote_count += 1
        votes_per_candidate[candidate] = vote_count

    return votes_per_candidate


def create_header(votes_per_candidate):
    """
    """

    total_votes = sum(votes_per_candidate.values())
    header = f"\nElection Results \n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n"

    return header


def create_body(votes_per_candidate):
    """
    """
    total_votes = sum(votes_per_candidate.values())
    highest_vote_count = max(votes_per_candidate.values())
    body = []

    # Loops through "votes_per_candidate" dictionary then appends each key,value pair to "body" list (as a tuple)
    for candidate, vote_count in votes_per_candidate.items():
        percentage_of_total_votes = (vote_count / total_votes) * 100
        body.append((f"{candidate}: {round(percentage_of_total_votes, 3)}% ({vote_count})\n"))

    return body


def create_footer(votes_per_candidate):
    """
    """

    vote_counts = list(votes_per_candidate.values())
    candidate_names = list(votes_per_candidate.keys())
    index_of_highest_vote_count = vote_counts.index(max(vote_counts))
    winner = candidate_names[index_of_highest_vote_count]
    footer = f"-------------------------\n Winner: {winner}"

    return footer


def create_txt_file(header, body, footer):
    """
    """

    nwbody = "\n".join(body) # Merges each element of "body" into one string that acknowledges each "\n" command
    output = header + nwbody + footer

    f = open('./output/PyPoll_Export.txt','w')
    f.write(output)
    f.close()


def main():
    csvpath = os.path.join("..", "PythonChallenge", "data", "election_data.csv")

    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader) # Skips the first row/header of csv as to avoid incompatible data-types (e.g. objects & integers)
        
        poll_data = list(csvreader)
        candidate_names = create_list_of_candidate_names(poll_data)
        votes_per_candidate = tally_votes_per_candidate_for_each_candidate(poll_data, candidate_names)

        header = create_header(votes_per_candidate)
        body = create_body(votes_per_candidate)
        footer = create_footer(votes_per_candidate)

        print(header, *body, footer) # "*body" extracts each element of the "body" list such that the elements can be printed as strings and not list elements

        create_txt_file(header, body, footer)


main()