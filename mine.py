from zxcvbn import matching, scoring


passwords = ["Custom.outlook.Future89", "Custom.outlook.Buonanotte89"]
matches = matching.omnimatch(passwords[0])

for pattern in scoring.most_guessable_match_sequence(passwords[0], matches)["sequence"]:
    print(pattern)

print("*******************************************************************************************")
matches = matching.omnimatch(passwords[1])

for pattern in scoring.most_guessable_match_sequence(passwords[1], matches)["sequence"]:
    print(pattern)