# 98 -> 98/25 -> 3 quarters
# remaining_cents -> 98 % 25

# remaining_cents/10 -> num dimes
# remaining_cents = remaining_cents % 10

# remaining_cents//5 -> num nickels
# remaining_cents -> remaining_cents % 5

# remaining pennies --> remaining_cents


# print(int(98/25)) # or 98//25 to get integer 
# print(98 % 25)

# 3 q, 2 d, 0 nickles, 3 p
def genCoinChange(coinInput):
    outputObj = {}
    outputObj['q'] = coinInput//25
    remaining = coinInput % 25
    outputObj['d'] = remaining//10
    remaining = remaining % 10
    outputObj['n'] = remaining//5
    remaining = remaining % 5
    outputObj['p'] = remaining
    return outputObj


# def genCoinChange(coinInput):
#     outputObj = {}
#     quarters = coinInput//25
#     remaining = coinInput % 25
#     dimes = remaining//10
#     remaining = remaining % 10
#     nickles = remaining//5
#     remaining = remaining % 5
#     pennies = remaining
#     outputObj['q'] = quarters
#     outputObj['d'] = dimes
#     outputObj['nickles'] = nickles
#     outputObj['p'] = pennies
#     return outputObj


print(genCoinChange(84))