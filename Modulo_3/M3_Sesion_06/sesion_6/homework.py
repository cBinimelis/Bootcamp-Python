import random

print("-------------------------------PROMEDIO-------------------------------")
added_numbers = 0
random_numbers = random.sample(range(1, 1001), 100)

for number in random_numbers:
    added_numbers += number

print(f"El promedio es {added_numbers/100}.")


print("------------------------------NEGATIVOS------------------------------")
random_numbers = random.sample(range(-100, 1001), 100)
count = 0
for number in random_numbers:
    if number % 2 == 0:
        continue
    if number < 0:
        print(f"Se hicieron {count} iteraciónes, el primer negativo es: {number}.")
        break
    count += 1
