def generateAcronym(stringInput):
    acronym = ""
    if stringInput[0] != " ":
        acronym += stringInput[0].upper()
    for i in range(len(stringInput)):
        if stringInput[i-1] == " " and stringInput[i] != " ":
            acronym += stringInput[i].upper()
    print(acronym)
    return acronym


generateAcronym("        national      basketball        association")