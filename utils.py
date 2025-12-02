def read_input(day='day01'):
    data = []
    with open(f'./{day}/input.txt') as f:
        data = [str(line.strip()) for line in f]

    return data
