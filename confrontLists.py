import os
import sys
import threading

#grab path1 and path2 from command line
path1 = sys.argv[1]
path2 = sys.argv[2]
# get the list of the files in the first folder
passwordsFiles = os.listdir(path1)
# get the list of the files in the second folder
dictionaries = os.listdir(path2)

hashes = set()
def readDict(dictionary):
    for line in open(path2 + "/" + dictionary, "r", encoding='latin-1'):
        hashes.add(hash(line.strip()))

# from the list of files in the second folder, read all lines of each file and store their hash in a set
threads = []
for dictionary in dictionaries:
    t = threading.Thread(target=readDict, args=(dictionary,))
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()
print('Lenght of all dictionaries combined', len(hashes))

file_lock = threading.Lock()
def addToVulnToDict(file):
    if file in ['general.txt', 'dict.txt']:
        return
    
    # correct holds all passwords that are in the correct file and will need to be reprinted there
    correct = []
    toAdd = []
    for line in open(path1 + "/" + file, "r"):
        if hash(line.strip()) in hashes:
            toAdd.append(line.strip())
        else:
            correct.append(line.strip())
    
    print(file, len(correct), len(toAdd))
    
    # replace all lines in the file with the correct ones
    with open(path1 + "/" + file, "w") as f:
        for line in correct:
            f.write(line + "\n")
    
    # add all the lines that were not correct to the dict.txt file
    with file_lock:
        with open(path1 + "/dict.txt", "a") as f:
            for line in toAdd:
                f.write(line + "\n")
    

# for file in passwordsFiles create a new thread that does function addToVulnToDict(file)
threads = []
for file in passwordsFiles:
    t = threading.Thread(target=addToVulnToDict, args=(file,))
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()