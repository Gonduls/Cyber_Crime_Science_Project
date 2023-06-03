import sys


# detect the 10 most used passwords from a text file given as input from command line and print them out in order of most used to least used
most_used = {}
with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        if line in most_used:
            most_used[line] += 1
        else:
            most_used[line] = 1

most_used = sorted(most_used.items(), key=lambda x: x[1], reverse=True)
for i in range(10):
    print(most_used[i][0], most_used[i][1])