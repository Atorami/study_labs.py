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


# elevator back to middle of the building after each lifting
def scene_3(data):
    scene_data = []
    for i in data[2]:
        floor_counter = 0
        middle_floor = 5
        for j in range(data[0]):
            start, finish = i
            floor_counter += abs(start - finish) + abs(middle_floor - finish)
        scene_data.append(round(floor_counter * data[1] / 1000, 2))

    return scene_data


def main():
    repeat_num = 1000
    floor_height = 2.8
    scene_input_data = [repeat_num, floor_height, [script_1(), script_2(), script_3()]]
    scene_1_data = scene_1(scene_input_data)
    scene_2_data = scene_2(scene_input_data)
    scene_3_data = scene_3(scene_input_data)
    scene_output_data = [scene_1_data, scene_2_data, scene_3_data]

    for i in range(len(scene_output_data)):
        print(f'Scene {i+1} :')
        average_val = 0
        for j in range(len(scene_output_data[i])):
            average_val += scene_output_data[i][j]
            print(f'Algorithm {j+1} : {scene_output_data[i][j]} km')
        print(f'Scene {i+1} average value : {round(average_val/3, 2)} km')


main()
