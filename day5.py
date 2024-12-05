with open("data.txt") as f:
  data = f.read().splitlines()
  splindex = data.index("")
  rules = data[:splindex]
  books = data[splindex+1:]
  books = [book.split(",") for book in books]
new_rules =[]

for i in range(len(rules)):
  rules[i] = rules[i].split("|")

def page_checker(lst):
    patterns = []
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if i < j:
                patterns.append([lst[i], lst[j]])
            elif i > j:
                patterns.append([lst[j], lst[i]])
    for pattern in patterns:
        if not pattern in rules:
            return False
    return True

page_list = []
for book in books:
    if page_checker(book):
        page_list.append(int(book[len(book)//2]))

print(sum(page_list))





