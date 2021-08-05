def parensValid(stri):
    counter = 0
    for p in range(len(stri)):
        if counter < 0:
            return False
        if stri[p] == "(":
            counter += 1
        elif stri[p] == ")":
            counter -= 1
    if counter == 0:
        return True
    else:
        return False

print(parensValid("y(3(p)p(3)r)s"))
print(parensValid("n(0(p)3"))
print(parensValid("(n) )b("))



def parensValid(st):
    openP = 0
    closeP = 0
    for p in st:
        if closeP > openP:
            return False
        if p == "(":
            openP += 1
        elif p == ")":
            closeP += 1
    if openP == closeP:
        return True
    else:
        return False


print(parensValid("y(3(p)p(3)r)s"))
print(parensValid("n(0(p)3"))
print(parensValid("(n) )b("))
