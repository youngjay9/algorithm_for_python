import random


def getValue():
    d1 = {'point': 1, 'minValue': 1, 'maxValue': 1}
    d2 = {'point': 5, 'minValue': 2, 'maxValue': 1000}
    d3 = {'point': 10, 'minValue': 1001, 'maxValue': 5000}
    d4 = {'point': 100, 'minValue': 5001, 'maxValue': 10000}
    d5 = {'point': 1000, 'minValue': 10001, 'maxValue': 30000}

    all_list = []

    all_list.append(d1)
    all_list.append(d2)
    all_list.append(d3)
    all_list.append(d4)
    all_list.append(d5)

    value = random.randint(1, 10000)

    for l in all_list:
        if l.get('minValue') <= value <= l.get('maxValue'):
            print(f'point:{l.get("point")}')
            break


def main():
    getValue()


main()
