from utils import read_input

def day01_challenge1(verbose=False):
    data = read_input('day01')

    start = 50
    total = 0

    for datum in data:
        direction = datum[0]
        num = int(datum[1:])
        num = num if direction == 'R' else -1*num

        start += num

        while start < 0:
            start = 99 + 1 + start
        while start > 99:
            start = start - 99 - 1

        if start == 0:
            total += 1

        if verbose:
            print(f"The dial is rotated {datum} to point at {start}. Total: {total}")

    if verbose:
        print(f"Final: {total}")
    return total

class Tick:
    def __init__(self, number):
        self.number = number
        self.next = None
        self.previous = None

    def setPrevious(self, previous):
        self.previous = previous

    def setNext(self, next):
        self.next = next

    def __repr__(self):
        next_num = self.next.number if self.next != None else "None"
        prev_num = self.previous.number if self.previous != None else "None"
        return f"Number: {self.number}, next: {next_num}, prev: {prev_num}"


def day01_challenge2(verbose = False):

    zero = Tick(0)
    previous_tick = zero
    for i in range(1,100):
        new_tick = Tick(i)
        if i == 50:
            start = new_tick
        new_tick.setPrevious(previous_tick)
        previous_tick.setNext(new_tick)

        previous_tick = new_tick

    zero.setPrevious(previous_tick)
    previous_tick.setNext(zero)

    data = read_input('day01')

    total = 0

    for datum in data:
        direction = datum[0]
        num = int(datum[1:])
        
        for i in range(num):
            if direction == 'L':
                start = start.previous
            else:
                start = start.next

            if start.number == 0:
                total += 1

    if verbose:
        print(f"Total: {total}")
    return total
