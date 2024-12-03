def multextractor(str):
  """clunky code that extracts and multiplies integers from instructions"""
  str1 = ""
  str2 = ""
  for index, value in enumerate(str):
    if value.isnumeric():
      str1 += value
    elif not value.isnumeric() and not value == ",":
      break
    elif value == "," and str1:
      new_str = str[index+1:]
      for item in new_str:
        if not item.isnumeric() and not item == ")":
          break
        elif item.isnumeric():
          str2 += item
        elif item == ")" and str2:
            if len(str1) <= 3 and len(str2) <= 3:
                return int(str1) * int(str2)
    else:
        break

def computer(data):
  instructions = []
  for item in data:
    if item[0]== "(":
      item = item[1:]
      out = multextractor(item)
      # print(out)
      if out:
        instructions.append(out)
  return sum(instructions)


#part 1
with open("data.txt") as f:
  data = f.read()
data = data.split("mul")
print(computer(data))

#part 2
with open("data.txt") as f:
  data = f.read()
data = data.split("don't")
new_data = data[0]
for item in data:
  item = item.split("do")
  item = item[1:]
  item = "".join(item)
  new_data += item

new_data = new_data.split("mul")

print(computer((new_data)))









