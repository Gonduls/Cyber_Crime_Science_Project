import os
import sys
import threading

#grab path from command line
path = sys.argv[1]
new_path = path + '_clean'

# create a path for the new folder
if not os.path.exists(new_path):
    os.mkdir(new_path)

# get the list of the files in the first folder
passwordsFiles = os.listdir(path)

# function that reads all lines of a file and stores them in a set
# if len(set) > 50 writes all of the lines them to a new file in new_path
def cleanFile(file):
    lines = set()
    for line in open(path + "/" + file, "r"):
        lines.add(line.strip())
    
    with open(new_path + "/" + file, "w") as f:
        for line in lines:
            f.write(line + "\n")

# for every file in the folder create a new thread that does function cleanFile(file)
threads = []
for file in passwordsFiles:
    t = threading.Thread(target=cleanFile, args=(file,))
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()