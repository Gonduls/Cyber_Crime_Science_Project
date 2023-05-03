from zxcvbn import matching, scoring


password = "vpn"
matches = matching.omnimatch(password)

for pattern in scoring.most_guessable_match_sequence(password, matches)["sequence"]:
    print(pattern)
