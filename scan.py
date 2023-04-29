import sys
import re

txt, num, mix = 0, 0, 0
max_txt, max_num, max_mix = "", "", ""
for i in range(1, len(sys.argv)):
    print(sys.argv[i])

    try:
        
        for line in open(sys.argv[i]):
            line = line.strip()
            # print(line)
            if str.isalpha(line):
                if(len(line) > len(max_txt)):
                    max_txt = line
                txt += 1
            elif str.isdecimal(line):
                if(len(line) > len(max_num)):
                    max_num = line
                num += 1
            else:
                if(len(line) > len(max_mix)):
                    max_mix = line
                mix += 1    
    except Exception :
        print()
    
print("All text =", txt, "\tMax all text =", max_txt)
print("All numbers =", num, "\tMax all numbers =", max_num)
print("Mix of them =", mix, "\tMax mix =", max_mix)

