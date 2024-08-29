word = "paralelepipedo"
vocals = ["a", "e", "i", "o", "u"]
count = 0
result = dict()


for letter in word:
    if letter in vocals:
        count += 1
        continue
    else:
        result.update({count: letter})
        count += 1

print(result)
