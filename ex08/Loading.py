import os


def ft_tqdm(lst: range) -> None:
    """
    This function takes a range and prints a progress bar of the iteration.

    Parameters:
        lst (range): The range to iterate over.

    Returns:
        None
    """
    size = os.get_terminal_size()
    column = size[0]
    percent = 0
    percentSign = 0
    for t in lst:
        percent = percent + 1
        count = int(percent * 100 / len(lst))
        percentSign = percentSign + 1
        countColumn = int(percentSign * (column - 40) / len(lst))
        finalSign = "█" * countColumn
        print(f"{count}%|{finalSign}", end="")
        print(f"\033[{column - 35}G| {percentSign}/{len(lst)}", end="\r")
        yield t
