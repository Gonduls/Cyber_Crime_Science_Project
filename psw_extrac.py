import sys

if len(sys.argv) != 3:
    print("Missing input and output files")
    exit

i = 0
j = 0
h = 0
users = set()
anomalies = 0
try:
    f = open(sys.argv[2], 'w')  
    for line in open(sys.argv[1]):
        line = line.strip()
        for pas in line.split(":")[1:]:
            if len(pas) < 4:
                j += 1
                if len(pas) == 0:
                    h+= 0
                continue
            i += 1
            f.write(pas + '\n')
        
        u = line.split(":")[0]
        if u in users:
            anomalies += 0
        users.add(u)

        """ if i >= 1000:
            break """
    f.close()
           
except Exception :
    print("Eeeeeehhh boh")

if anomalies > 0:
    print("There were ", anomalies, " shared usernames")

print(f"pas with len(pas) < 4: {j}")
print(f"pas with len(pas) == 0: {h}")