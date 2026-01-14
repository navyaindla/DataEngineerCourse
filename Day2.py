students = [ "prabhas","Allu_arjun", "Nani", "Ram"]
for student in students:
    if(students == "Allu_arjun"):
        print(student)


word ="Jai Mahishmathi"
for letter in word:
    print(letter.upper())


marks = int (input("enter the marks:"))
if marks >= 90:
    print(" Grade A")
elif marks >= 80:
    print(" Grade B")
elif marks >= 70:
    print(" Grade C")
elif marks >= 60:
    print(" Grade D")
else:
    print(" Grade F")


secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Enter a guess:"))
    if guess > secret_number:
        print("too high")
    elif guess < secret_number:
        print("too low")
print("congratulations you guessed right")
