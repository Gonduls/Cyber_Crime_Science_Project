# Purpose: extract unique passwords from files in a folder and write them to new files in a new folder
# a minimum number of unique passwords can be specified, if a file has less lines than that it is not copied
# Usage: python3 cleanFiles.py <folder_with_files> <min_number_of_lines>
# Output: a new folder with the same files as the input folder, but with unique passwords and with a minimum number of lines, named <input_folder>_clean

import os
import sys
import threading

#grab path from command line
path = sys.argv[1]
new_path = path + '_clean'

# if no min number of lines is given, set it to 1
if len(sys.argv) < 3:
    min_lines = 1
else:
    # grab min number of lines from command line
    min_lines = int(sys.argv[2])
    

# create a path for the new folder
if not os.path.exists(new_path):
    os.mkdir(new_path)

# get the list of the files in the first folder
passwordsFiles = os.listdir(path)

# function that reads all lines of a file and stores them in a set
# if len(set) > min_lines writes all of the lines them to a new file in new_path
def cleanFile(file):
    lines = set()
    for line in open(path + "/" + file, "r"):
        lines.add(line.strip())
    
    if len(lines) > min_lines:
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