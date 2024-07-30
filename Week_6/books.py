import json


class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author


b1 = Books("Harry Potter", "Me")

json_str = json.dumps(
    {"title": b1.title, "author": b1.author}, indent=4, separators=(",", ":"))

print(json_str)
