
num = int(input("Enter mood number 1 to 10: "))

if num <= 2:
    word = "really down"
elif num <= 4:
    word = "a bit low"
elif num <= 6:
    word = "so-so"
elif num <= 8:
    word = "pretty good"
else:
    word = "super happy"

print("Your feeling is:", word)