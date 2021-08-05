def generateAcronym(stringInput):
    acronym = ""
    if stringInput[0] != " ":
        acronym += stringInput[0]
    for i in range(len(stringInput)):
        if stringInput[i-1] == " " and stringInput[i] != " ":
            acronym += stringInput[i]
    print(acronym.upper())
    return acronym.upper()


generateAcronym("        national      basketball        association")


def acronym2(stringInput):
    y = stringInput.split()
    # print(y)
    result = ""
    for word in y:
        result += word[0]
    return result.upper()

print(acronym2("   national      basketball    association"))