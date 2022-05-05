import re
from pathlib import Path

pride_prejudice = {}
book_file_path = Path.cwd() / "pride_and_prejudice.txt"

regex_text = "[\W_]+"

temp = []
if book_file_path.exists():
    with book_file_path.open() as book:
        for line in book.readlines():
            if line != "\n":
                temp.append(line.strip())

book_string = ""
for entry in temp:
    book_string += entry.lower() + " "

book_string = re.sub(regex_text, " ", book_string)

word_list = re.split("\s", book_string)

for word in word_list:
    pride_prejudice[word] = 1

for word in word_list:
    pride_prejudice[word] += 1

max_word = max(pride_prejudice, key=pride_prejudice.get)
print(f'The most used word in Pride and Prejudice is: {max_word}\n'
      f'It is used {pride_prejudice[max_word]} times.')
