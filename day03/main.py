from utils import read_input

def challenge1(verbose=False):
    data = read_input('day03')


    total = 0
    for datum in data:
        highest = "0"
        for i in range(len(datum)):
            for j in range(i+1, len(datum)):
                new_check = f"{datum[i]}{datum[j]}"
                if int(new_check) > int(highest):
                    highest = new_check
        print(f"For {datum} highest was: {highest}")
        total += int(highest)

    print(f"Total is: {total}")
    return total

def recur(curr: str, remaining: str, highest: str) -> str:

    for i, char in enumerate(remaining):
        new_check = curr+char
        if len(new_check) == 12:
            if int(new_check) > int(highest):
                highest = new_check
                continue
        else:
            check_bound = len(new_check)
            if check_bound != 0 and int(new_check) < int(highest[:check_bound]):
                continue
            value = recur(curr+char, remaining[i+1:], highest)
            if int(value) > int(highest):
                highest = value
    return highest


def challenge2(verbose=False):
    data = read_input('day03')

    total = 0
    for datum in data:
        highest = recur("", datum, "0".ljust(12,"0"))
        print(f"For Datum:{datum}, highest: {highest}")
        total += int(highest)
    
    print(f"Total is: {total}")
    return total
