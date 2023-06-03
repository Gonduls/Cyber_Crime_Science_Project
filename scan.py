# Like fastScan.py, but also ouputs more statistics and uses a wordlist to check for dictionary words, sadly hardcoded
# It does the scan for every file specified in input

import sys
from zxcvbn import zxcvbn
import numpy as np


dict = open("../wordlists/forti_users_first_10000.txt", 'r') #, encoding='latin-1' for rock you
dictionary = [line.strip() for line in dict]
print(dictionary[0])

txt, num, mix = 0, 0, 0
max_txt, max_num, max_mix = "", "", ""

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

for i in range(1, len(sys.argv)):
    print(sys.argv[i])

        
    f = open('bruteforces.txt', 'w')
    for line in open(sys.argv[i]):
        pswAmount += 1
        if pswAmount % 1000 == 0:
            print(pswAmount)
        password = line.strip()

        pswLengths.append(len(password))
        try:
            """ if str.isalpha(password):
                if(len(password) > len(max_txt)):
                    max_txt = password
                txt += 1
            elif str.isdecimal(password):
                if(len(password) > len(max_num)):
                    max_num = password
                num += 1
            else:
                if(len(password) > len(max_mix)):
                    max_mix = password
                mix += 1    """ 
            
            res = zxcvbn(password) #, dictionary[pswAmount - 1]

            pattern_list = res["sequence"]
            pswPatternsAmount.append(len(pattern_list))
            patternNames = []
            for pat in pattern_list:
                pat_name = pat['pattern']
                patternNames.append(pat_name)
                pswPatternsFrequency[pat_name] += 1
                if pat_name == 'bruteforce':
                    f.write(f"{pat['token']} - {password}\n")
                    pswBruteforceLengths.append(len(pat['token']))

            patternNames = tuple(patternNames)
            
            if patternNames == ('bruteforce',):
                print(password)
            if patternNames not in pswPatternsSetFrequency:
                pswPatternsSetFrequency[patternNames] = 0
            
            pswPatternsSetFrequency[patternNames] += 1
            

        except Exception:
            print(f"Password \"{password}\" raised an exception")

print("Total number of passwords: ", pswAmount)
print()
""" print("All text =", txt, "\t\tMax all text =", max_txt)
print("All numbers =", num, "\tMax all numbers =", max_num)
print("Mix of them =", mix, "\tMax mix =", max_mix) 
print()"""

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