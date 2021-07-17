# function reverseString(str){
#     var newString = ""
#     for(let i = str.length - 1; i >= 0; i--){
#         newString += str[i]
#     }
#     return newString
# }

# console.log(reverseString("hello"));


def reverseString(str):
    newString = ""
    for i in range(len(str)-1, -1, -1):
        newString += str[i]
    return newString


print(reverseString("hello"))

for i in range(10, 20, 1):
    if i % 2 == 0:
        print("even")
    else:
        print(i)

print("done")


goats[2] = "Mamba"
print(goats)

x = 55

if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")

goats = ["Lebron", "MJ", "Kobe", "AI", 23, False, True, 45.5]

for x in goats:
    print(x)

for i in range(0,len(goats),1):
    if goats[i] == "AI":
        goats[i] = "Iverson"
    print(goats[i])
