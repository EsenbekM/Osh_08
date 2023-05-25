import re

# text = "Geeks - Знания гар гор гер  с гарантией! "

# result = re.match(r"Знания", text)
# print(result)

# result = re.search(r"Знания", text)
# print(result)

# result = re.findall(r"г[а-я]р", text)
# print(result)

# result = re.split(r" ", text)
# print(result)

# result = re.sub(r"г[а-я]р", r"haha", text)
# print(result)

# result = re.sub(r".", r":", text)
# print(result)

with open('Lesson_6/test_regs.txt', 'r', encoding="utf-8") as file:
    content = file.readlines()
    for line in content:
        print(re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", line))

    # nur_telecom = re.findall(r"\+996 (?:70\d|50\d)[\d ]{9}", content)
    # print(nur_telecom)

    # megacom = re.findall(r"\+996 (?:55\d|99\d|75\d)[\d ]{9}", content)
    # print(megacom)

    # beeline = re.findall(r"\+996 (?:22\d|77\d)[\d ]{9}", content)
    # print(beeline)

# email = input("Enter email: ")

# is_correct = re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", email)

# if is_correct:
#     print("Ok")
# else:
#     print("Wrong!")
