import sys
from zxcvbn import zxcvbn
import numpy as np


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

        
f = open('bruteforces.txt', 'w')
for line in open(sys.argv[1]):
    pswAmount += 1
    if pswAmount % 1000 == 0:
        print(pswAmount, end = ' ')
    if pswAmount % 10000 == 0:
        print()
    password = line.strip()

    pswLengths.append(len(password))
    try:
        
        res = zxcvbn(password, ['vpn', 'VPN', 'fortinet']) #, dictionary[pswAmount - 1]

        pattern_list = res["sequence"]
        pswPatternsAmount.append(len(pattern_list))
        patternNames = []
        for pat in pattern_list:
            pat_name = pat['pattern']
            patternNames.append(pat_name)
            pswPatternsFrequency[pat_name] += 1

        patternNames = tuple(patternNames)
        
        if patternNames == ('bruteforce',):
            f.write(password)
        if patternNames not in pswPatternsSetFrequency:
            pswPatternsSetFrequency[patternNames] = 0
        
        pswPatternsSetFrequency[patternNames] += 1
        

    except Exception:
        print(f"Password \"{password}\" raised an exception")

print("Total number of passwords: ", pswAmount)

print(f"Avarage psw length = {np.average(pswLengths)}")
print(f"Avarage psw patterns = {np.average(pswPatternsAmount)}")
print(f"Avarage bruteforce pattern token length = {np.average(pswBruteforceLengths)}")
for key, value in pswPatternsFrequency.items():
    print(f"{key} total amount: {value}")

print()

results = []
for key, value in pswPatternsSetFrequency.items():
    results.append((value, key))

results.sort(reverse=True)
for k, v in results:
    print(k, v)