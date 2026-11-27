import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Découpe un tableau 2D entre les indices start et end.

    Affiche la forme du tableau d'origine, puis celle du tableau découpé.

    Args:
        family: liste de listes de même longueur.
        start: indice de la première ligne gardée (entier, peut être négatif).
        end: indice de fin, exclu (entier, peut être négatif).

    Returns:
        La partie découpée sous forme de liste, ou None en cas d'erreur.
    """
    try:
        assert isinstance(family, list), "ce n'est pas une liste"
        assert len(family) > 0, "la liste est vide"
        assert isinstance(start, int) and isinstance(end, int), "not a int"
        assert all(isinstance(x, list)
                   for x in family), "one element is not a list"
        assert all(len(family[0]) == len(
            n) for n in family), "The list have element with not the same size"
        assert isinstance(
            start, bool) and isinstance(
            end, bool), "You use boolean not int"
        array = np.array(family)
        newList = array[start: end]
        print(f"My shape is :", np.shape(array))
        print(f"My new shape is :", np.shape(newList))

    except AssertionError as err:
        print(f"AssertionError: {err}")
        return None

    return newList.tolist()


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("--- cas du sujet ---")
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("--- family n'est pas une liste ---")
    print(slice_me("abc", 0, 2))

    print("--- une ligne n'est pas une liste ---")
    print(slice_me([[1, 2], 3], 0, 1))

    print("--- start n'est pas un entier ---")
    print(slice_me(family, "a", 2))

    print("--- slicing vide ---")
    print(slice_me(family, 3, 1))

    print("--- liste vide ---")
    print(slice_me([], 0, 1))

    print("--- lignes de tailles différentes ---")
    print(slice_me([[1, 2], [3]], 0, 1))

    print(slice_me(family, 1.5, 2))
    print(slice_me(family, True, 2))


if __name__ == "__main__":
    main()
