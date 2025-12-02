from utils import read_input


def does_object_repeat(id: str, split_size: int, verbose: bool) -> bool:
    parts = [id[i:i+split_size] for i in range(0, len(id), split_size)]
    verbose and print(f"split: {split_size}, parts: {parts}")

    obj = {}
    for part in parts:
        if part.startswith('0'):
            verbose and print(f"Starts with 0, auto False")
            return False
        if part not in obj:
            obj[part] = 1
        else:
            obj[part] = obj[part] + 1
    obj_size = len(obj)

    return obj_size == 1


def contains_duplicate(id: str, verbose: bool) -> bool:
    length = len(id)

    num_splits = [i for i in range(1, length)]
    verbose and print(f"leng: {length} ")
    for split in num_splits:
        split_calc = len(id)/split
        if int(split_calc) != split_calc:
            continue
        repeats = does_object_repeat(id, split, verbose)
        if repeats:
            return True

    return False


def challenge01(verbose=False):
    data = read_input('day02')
    data = data[0].split(',')

    total = 0
    for datum in data:
        split_datum = datum.split('-')
        high = int(split_datum[1])
        low = int(split_datum[0])

        for id in range(low, high+1):
            if contains_duplicate(str(id), verbose=verbose):
                total += id

    print(f"Total is: {total}")
        

def challenge02():
    pass
