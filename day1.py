#LANGUAGE: Python

import numpy as np

with open("data.txt") as f:
    seats = f.read().split("\n")
    seats = [seat.split("   ") for seat in seats]
    seats = np.array(seats)
    seats = np.rot90(seats)
    seats = [[int(s) for s in seat] for seat in seats]
    seats = [sorted(seat) for seat in seats]

#part 1
difference = abs(np.subtract(seats[0], seats[1]))
print(difference)
print(sum(difference))

#part2
list1 = seats[1]
list2 = seats[0]
similarity_list = [list2.count(i)*i for i in list1]
similarity_score = sum(similarity_list)
print(similarity_score)


