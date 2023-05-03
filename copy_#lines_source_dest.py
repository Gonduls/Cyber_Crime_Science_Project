import sys

if len(sys.argv) != 4:
    print("Usage: python3 copy_#lines_source_dest.py <#lines> <inputfile> <outputfile>")
    exit

print(sys.argv[1], sys.argv[2], sys.argv[3])
num = int(sys.argv[1])


inp = open(sys.argv[2], 'r')
outp = open(sys.argv[3], 'w')
for line in inp:
    outp.write(line)
    num -= 1
    if num == 0:
        break
inp.close()
outp.close()