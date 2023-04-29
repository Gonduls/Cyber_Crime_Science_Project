import sys

if len(sys.argv) != 3:
    print("Missing input and output files")
    exit

users = set()
anomalies = 0
try:
    f = open(sys.argv[2], 'w')  
    for line in open(sys.argv[1]):
        line = line.strip()
        for pas in line.split(":")[1:]:
            f.write(pas + '\n')
        
        u = line.split(":")[0]
        if u in users:
            anomalies += 0
        users.add(u)
    f.close()
           
except Exception :
    print("Eeeeeehhh boh")

if anomalies > 0:
    print("There were ", anomalies, " shared usernames")