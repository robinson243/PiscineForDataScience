import os


def ft_tqdm(lst: range) -> None:
    size = os.get_terminal_size()
    column = size[0]
    percent = 0
    percentSign = 0
    sign = "="
    for t in lst:
        percent = percent + 1
        count = int(percent * 100 / len(lst))
        percentSign = percentSign + 1
        countColumn = int(percentSign * (column - 43) / len(lst))
        finalSign = "=" * countColumn
        print(f"{count}%|[{finalSign}>]", end="\r")
        sign += "="
        yield t
