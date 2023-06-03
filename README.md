# Cyber Crime Science Project

Contains the collection of files used to analyze data for the Cyber Crime Science project at Tu Delft.

These scripts were used to analyze the file fortinet-2021.txt. The file can be found in the [Seclist github repository](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/fortinet-2021.txt).

All scripts in this repository present a brief description of their purpose. The main pipeline followed to analyze the dataset consists in:
- [psw_extrac.py](./psw_extrac.py): Extracts passwords from the fortinet-2021.txt file into an output file
- [scan.py](./scan.py): Creates a folder where all passwords from an input file are divided into more files based on the sequences recognized by [zxcvbn](https://github.com/dwolfhub/zxcvbn-python)
- [addToDict_txt.py](./addToDict_txt.py): Takes as input two folders, one containing well known dictionaries (i.e. [RockYou.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz), ...) and the folder of passwords in sequences from [scan.py](./scan.py), and replaces passwords in "dict.txt" if found in the known dictionaries.
- [rate_psw.py](./rate_psw.py): counts the lines contained in each password file and assigns the sore given by [zxcvbn](https://github.com/dwolfhub/zxcvbn-python), then outputs all to a file

Use [cleanFiles.py](./cleanFiles.py) if you want to limit you research to files with unique passwords