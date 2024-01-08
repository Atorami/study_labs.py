import random


def script_1():
    start = random.randint(0, 10)
    finish = random.randint(0, 10)
    while start == finish:
        finish = random.randint(0, 10)

    return start, finish


def script_2():
    if random.random() < 0.7:
        start = random.randint(4, 10)
        finish = 0
        return start, finish
    return script_1()


def script_3():
    if random.random() < 0.7:
        start = 0
        finish = random.randint(1, 10)
        return start, finish
    return script_1()


def scene_1(data):
    scene_data = []

    for i in data[2]:
        floor_counter = 0
        last_floor = 0

        for j in range(data[0]):
            start, finish = i
            lift_back = abs(last_floor - start)
            lift_next = abs(start - finish)
            floor_counter += (lift_back + lift_next)
            last_floor = finish

        scene_data.append(round(floor_counter * data[1] / 1000, 2))
    return scene_data


def scene_2(data):
    scene_data = []

    for i in data[2]:
        floor_counter = 0
        for j in range(data[0]):
            start, finish = i
            floor_counter += start + abs(start - finish) + finish

        scene_data.append(round(floor_counter * data[1] / 1000, 2))

    return scene_data


def main():
    repeat_num = 1000
    floor_height = 2.8
    scenes_data = [repeat_num, floor_height, [script_1(), script_2(), script_3()]]

    scene_1(scenes_data)
    scene_2(scenes_data)

    print(scene_1(scenes_data))
    print(scene_2(scenes_data))


main()
