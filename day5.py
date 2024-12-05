with open("data.txt") as f:
  data = f.read().splitlines()
  splindex = data.index("")
  rules = data[:splindex]
  books = data[splindex+1:]
  books = [book.split(",") for book in books]

"""for part 2"""
flat_rules =[]

for i in range(len(rules)):
  rules[i] = rules[i].split("|")
  """this is for part 2"""
  for j in rules[i]:
      flat_rules += [j]

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

#part 1
broken_pages = []
page_list = []
for book in books:
    if page_checker(book):
        page_list.append(int(book[len(book)//2]))
    else:
        broken_pages.append(book)
#part 1
print(sum(page_list))

#part2
fixed_updates = []
for bp in broken_pages:
    """create a dummy page we can fill"""
    fixed_page = [1 for i in range(len(bp))]
    for i in range(len(bp)):
        """find index of each item in the flat rules. the length of this list can give us the correct index of the item """
        indexes = [index for index, value in enumerate(flat_rules) if value == bp[i] and not index % 2 and flat_rules[index +1] in bp]
        fixed_index = len(indexes)
        fixed_page[fixed_index] = bp[i]
    fixed_page = fixed_page[::-1]
    fixed_updates.append(int(fixed_page[len(fixed_page)//2]))

print(sum(fixed_updates))



