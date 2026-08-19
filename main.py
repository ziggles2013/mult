def task_01_multiplation_table():
    number = int(input("Pick a number: "))

    for i in  range(1, 11):
        answer = number * i
        print(f"{number} x {i} = {answer}")

