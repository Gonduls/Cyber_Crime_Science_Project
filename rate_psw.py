# Description: This script takes a folder with password files and outputs the amount of passwords with each score
# At the end of the output file it also outputs the total amount of passwords for each score
# Usage: python3 rate_psw.py <path to folder with password files> <output file name>

from zxcvbn import zxcvbn
import sys
import os
import threading

# grab path from command line
path = sys.argv[1]

# grab output file name from command line
outputFile = sys.argv[2]

# get the list of the files in the first folder
passwordsFiles = os.listdir(path)

output_list = []

# function that reads all lines of a file and counts the scores amount of each password, then appends results to output_list
def countScore(file):
    scores = [0, 0, 0, 0, 0]
    lines = 0
    for line in open(path + "/" + file, "r"):
        lines += 1
        try:
            score = zxcvbn(line.strip())["score"]
        except:
            continue
        scores[score] += 1
    
    output_list.append((file, scores, lines))

# for file in passwordsFiles create a new thread that does function countScore(file)
threads = []
for file in passwordsFiles:
    t = threading.Thread(target=countScore, args=(file,))
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()

# sort the output_list by the amount of lines in each file
output_list.sort(key=lambda x: -x[2])
total_results = [0, 0, 0, 0, 0]

# write the results to the output file
with open(outputFile, "w") as f:
    for file, scores, lines in output_list:
        f.write(str(lines) + '\t' +file + ": " + str(scores) + "\n")
        for i in range(5):
            total_results[i] += scores[i]
    
    f.write("Total: " + str(total_results) + "\n")