import sys
import os
from zxcvbn import zxcvbn
import numpy as np
from datetime import datetime

if(len(sys.argv) != 2):
    print("Missing input file")
    raise Exception

output_folder_name = '../' + datetime.now().strftime("%Y%m%d_%H:%M")[2:]+ '_' + sys.argv[1].split('/')[-1][:-4]
os.mkdir(output_folder_name)

def generateFileName(patterns : list[str]) -> str:
    result = '_'.join([pat[:4] for pat in patterns])
    return result + '.txt'

def addToFile(password: str, fname: str, fileDict: dict):
    if fname not in fileDict.keys():
        fileDict[fname] = open(output_folder_name + '/' + fname, 'w')
    fileDict[fname].write(password + '\n')

output = open(output_folder_name + '/general.txt', 'w')

pswAmount = 0
pswPatternsAmount = []
pswLengths = []
pswBruteforceLengths = []

pswPatternsFrequency = {
    'bruteforce': 0,
    'dictionary': 0,
    'repeat': 0,
    'spatial': 0,
    'sequence': 0,
    'regex': 0,
    'date': 0
}

pswPatternsSetFrequency = {}
pswPatternsFiles = {}


        
for line in open(sys.argv[1]):
    pswAmount += 1
    if pswAmount % 1000 == 0:
        print(pswAmount, end = ' ')
    if pswAmount % 10000 == 0:
        print()

    password = line.strip()

    pswLengths.append(len(password))
    try:
        res = zxcvbn(password, ['vpn', 'VPN', '2021', '2020'])

        pattern_list = res["sequence"]
        pswPatternsAmount.append(len(pattern_list))
        patternNames = []
        for pat in pattern_list:
            pat_name = pat['pattern']
            patternNames.append(pat_name)
            pswPatternsFrequency[pat_name] += 1
            if pat_name == 'bruteforce':
                pswBruteforceLengths.append(len(pat['token']))

        addToFile(password, generateFileName(patternNames), pswPatternsFiles)
        patternNames = tuple(patternNames)
        
        if patternNames not in pswPatternsSetFrequency:
            pswPatternsSetFrequency[patternNames] = 0
        pswPatternsSetFrequency[patternNames] += 1
        

    except Exception:
        print(f"Password \"{password}\" raised an exception")

output.write(f"Total number of passwords: {pswAmount}\n")

output.write(f"Avarage psw length = {np.average(pswLengths)}\n")
output.write(f"Avarage psw patterns = {np.average(pswPatternsAmount)}\n")
output.write(f"Avarage bruteforce pattern token length = {np.average(pswBruteforceLengths)}\n\n")
for key, value in pswPatternsFrequency.items():
    output.write(f"{key} total amount: {value}\n")

results = []
for key, value in pswPatternsSetFrequency.items():
    results.append((value, key))

results.sort(reverse=True)
for k, v in results:
    output.write(f"\n{k} - {v}")