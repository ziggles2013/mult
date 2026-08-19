def task_01_multiplation_table():
    number = int(input("Pick a number: "))

    for i in  range(1, 11):
        answer = number * i
        print(f"{number} x {i} = {answer}")


def task_01_STRECH_full_grid():
    print("-----full multiplation table-----")

    for row in range(1, 11):
        for col in  range(1, 11):
            product = row * col
            print(f"{product:4}", end='')
        print()

