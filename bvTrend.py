#!/bin/python3

def generate():
    with open('data.txt', 'r') as data:
        old = None
        for line in data.readlines():
            pure = line.strip('\n').split(' ')[3:]
            old = pure if old is None else old
            trend = subtract(pure, old)
            write(trend)
            old = pure


def subtract(new, old):
    output = []
    for i in range(6):
        difference = int(new[i]) - int(old[i])
        output.append(difference)
    return output


def write(change):
    with open('trend.txt', 'a') as file:
        file.write(f'{change[0]}:{change[1]}:{change[2]}:{change[3]}:{change[4]}:{change[5]}\n')


if __name__ == '__main__':
    generate()
