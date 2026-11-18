questions = [
    ["Which command shows hidden files?", "ls -a"],
    ["Which command shows the content of a file?", "cat"],
    ["Which command creates a file?", "touch"],
    ["Which command searches for text inside a file?", "grep"],
]

def ask(question, answer):
    print(question)
    user_answer = input("> ").strip().lower()
    is_correct = user_answer == answer
    if is_correct:
        print("Correct")
    else:
        print("Wrong")
    return is_correct


count = 0
for question, answer in questions:
    if ask(question, answer):
        count += 1

total = len(questions)
percentage = round(count / total * 100)
print(f"Score: {count}/{total} ({percentage}%)")

if percentage >= 75:
    print("Well done")
else:
    print("Keep studying")