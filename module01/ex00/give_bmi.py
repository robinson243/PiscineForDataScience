def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    tab = []
    try:
        assert isinstance(weight, list) and isinstance(
            height, list), "One of element is not a list"
        assert len(height) == len(
            weight), "len of weight and height are not equal"

        for i in range(len(height)):
            val = weight[i] / (height[i] * height[i])
            tab.append(val)
    except AssertionError as err:
        print(err)
    return tab


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    tab = []
    try:
        assert isinstance(bmi, list
                          ), "One of element is not a list"
        for i in range(len(bmi)):
            if bmi[i] > limit:
                tab.append(True)
            else:
                tab.append(False)
    except AssertionError as e:
        print(e)
    return tab


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
