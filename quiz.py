count = 0
print("Which command shows hidden files?")
answer = input("> ")

if answer.strip().lower() == "ls -a":
    print("Correct answer")
    count += 1
else:
    print("Wrong answer")

print("Which command shows the content of the file?")
answer = input("> ")

if answer.strip().lower() == "cat":
    print("Correct answer")
    count += 1
else:
    print("Wrong answer")

print("Which command creates a file?")
answer = input("> ")
 
if answer.strip().lower() == "touch":
     print("Correct answer")
     count += 1
else:
    print("Wrong answer") 

print(f"Score: {count}/3")  