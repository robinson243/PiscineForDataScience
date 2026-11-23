def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    tab = []
    if len(height) != len(weight):
        err = "AssertionError: len of weight and height are not equal"
        print(AssertionError(err))
        return tab

    for i in range(len(height)):
        val = weight[i] / (height[i] * height[i])
        tab.append(val)
    return tab


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    tab = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            tab.append(True)
        else:
            tab.append(False)
    return tab


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
