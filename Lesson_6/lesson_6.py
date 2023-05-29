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

class Person:
    def __init__(self, full_name, email, file, color) -> None:
        self.full_name = full_name
        self.email = email
        self.file = file
        self.color = color




with open('Lesson_6/MOCK_DATA.txt', 'r', encoding="utf-8") as file:
    content = file.readlines()
    people = []
    for line in content:
        full_name = re.findall(r"^[A-Za-z'\-]+\s[A-Za-z'\-]+", line)[0]
        mail = re.findall(r"[a-zA-Z0-9]+@[-a-zA-Z0-9]+\.[a-zA-Z0-9]+", line)[0]
        file = re.findall(r"	\w+\.\w+", line)[0].replace("\t", '')
        color = re.findall(r"#\w+", line)[0].replace("\t", '')
        people.append(
            Person(full_name, mail, file, color)
        )
    
    with open('Lesson_6/fullname.txt', 'w', encoding="utf-8") as fillname_file:
        for i in people:
            fillname_file.write(i.full_name)
    with open('Lesson_6/mail.txt', 'w', encoding="utf-8") as Mail_file:
        for i in people:
            Mail_file.write(i.email)
    with open('Lesson_6/file.txt', 'w', encoding="utf-8") as file_file:
        for i in people:
            file_file.write(i.file)
    with open('Lesson_6/color.txt', 'w', encoding="utf-8") as color_file:
        for i in people:
            color_file.write(i.color)

    #     print(re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", line))

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
