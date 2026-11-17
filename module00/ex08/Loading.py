import os


def ft_tqdm(lst: range) -> None:
    """
    This function takes a range and prints a progress bar of the iteration.

    Parameters:
        lst (range): The range to iterate over.

    Returns:
        None
    """
    if (len(lst) == 0):
        print("0it [00:00, ?it/s]")
    size = os.get_terminal_size()
    column = size[0]
    percent = 0
    percentSign = 0
    for t in lst:
        gap = len(f'{len(lst)}') * 2 + 1
        bar_width = column - 34 - gap
        percent = percent + 1
        count = int(percent * 100 / len(lst))
        percentSign = percentSign + 1
        countColumn = int(percentSign * (bar_width) / len(lst))
        finalSign = "█" * countColumn
        print(f"{count}%|{finalSign}", end="")
        print(
            f"\033[{(5 + bar_width + 1)}G| {percentSign}/{len(lst)}", end="\r")
        yield t
