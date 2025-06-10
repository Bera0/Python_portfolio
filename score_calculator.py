# Insert name and score

name = input("What is your name? : ")
language = int(input("Language score: "))
math = int(input("Math score: "))
english = int(input("English score: "))

# Calculate total and Average

total = language + math + english
average = total / 3

# Calculate Grade

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Results

print(f"{name}'s Test Result")
print(f"Total: {total}points")
print(f"Average: {average:.2f}points")
print(f"Grade: {grade}")
