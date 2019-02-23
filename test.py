black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (9, 120, 236)
row = {}
we = 0
while we < 10:
    if we % 2 == 0:
        row[we * 20] = red
    else:
        row[we * 20] = green
    we += 1

for key, item in row.items():
    if item == blue:
        if key == 20 or key == 60 or key == 100 or key == 140 or key == 180:
            if key + 20 > mouse[0] > key and 20 + 20 > mouse[1] > 20:
                if click[2] == 1:
                    row[key] = green
                    count -= 1
                    greenb -= 1

        elif key == 0 or key == 40 or key == 80 or key == 120 or key == 160:
            if key + 20 > mouse[0] > key and 20 + 20 > mouse[1] > 20:
                if click[2] == 1:
                    row[key] = red
                    count -= 1
                    redb -= 1


row = []
column = []
def myround(x, base=20):
    return int(base * round(float(x)/base))

we = 100
while we > 0:
    num = random.randint(0, 100)
    row.append(myround(num))
    we -= 1
we = 100
while we > 0:
    num = random.randint(0, 100)
    column.append(myround(num))
    we -= 1