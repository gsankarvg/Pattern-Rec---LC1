series_list = [
    [2, 4, 6, 8, 10],
    [3, 6, 12, 24, 48],
    [1, 1, 2, 3, 5, 8],
    [10, 20, 30, 55, 70],
    [100, 50, 25, 12.5, 6.25]
]


def is_ap(seq):
    common_difference = seq[1] - seq[0]
    for i in range(1, len(seq) - 1):
        if seq[i + 1] - seq[i] != common_difference:
            return False
    return True

def is_gp(seq):
    common_ratio = seq[1] / seq[0]
    for i in range(1, len(seq) - 1):
        if seq[i+1] / seq[i] != common_ratio:
            return False
    return True

def is_fibanocci(seq):
    for i in range(2, len(seq)-1):
        if seq[i] != seq[i-1] + seq[i-2]:
            return False
    return True


for series in series_list:
    print(f"series = {series}")
    print(f"arithmetic progression = {'Yes' if is_ap(series) else 'No'}")
    print(f"geometric progression = {'Yes' if is_gp(series) else 'No'}")
    print(f"fibanocci = {'Yes' if is_fibanocci(series) else 'No'}")
    print("----------------------------------")

