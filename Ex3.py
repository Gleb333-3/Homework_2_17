listt = [50, 32, 37, 104]

celsius = list(map(lambda temp: (temp-32) * 5/9, listt))
print(celsius)