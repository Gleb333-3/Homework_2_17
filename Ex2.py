listt = [2, -3, 56, -123, 345, -213, 9999, -3333]
list_positive = [number for number in listt if number > 0]
list_negative = [number for number in listt if number < 0]

print(list_positive, "\n", list_negative)