import copy
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

doyoung_before = set()
youngjong_before = set()
doyoung_before.add((x1, y1))
youngjong_before.add((x2, y2))
time_location = []
time = 0

while True:
    time += 1
    doyoung = set()
    youngjong = set()
    for tmp_x, tmp_y in doyoung_before:
        doyoung.add((tmp_x+1, tmp_y))
        doyoung.add((tmp_x-1, tmp_y))
        doyoung.add((tmp_x, tmp_y-1))
        doyoung.add((tmp_x, tmp_y+1))
    for tmp_x, tmp_y in youngjong_before:
        youngjong.add((tmp_x-1, tmp_y+1))
        youngjong.add((tmp_x+1, tmp_y+1))
        youngjong.add((tmp_x-1, tmp_y-1))
        youngjong.add((tmp_x+1, tmp_y-1))
    doyoung_before = copy.deepcopy(doyoung)
    youngjong_before = copy.deepcopy(youngjong)
    if list(doyoung & youngjong) != []:
        print(time)
        break
