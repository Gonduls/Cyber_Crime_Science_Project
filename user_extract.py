# Extracts the usernames from the input file and writes them to the output file
# The input file must be in the format username:password1[:password2...]
# Usage: python3 user_extract.py <input_file> <output_file>

import sys

if len(sys.argv) != 3:
    print("Missing input and output files")
    exit

f = open(sys.argv[2], 'w')  
for line in open(sys.argv[1]):
    line = line.strip()
    
    u = line.split(":")[0]
    f.write(u + "\n")
f.close()