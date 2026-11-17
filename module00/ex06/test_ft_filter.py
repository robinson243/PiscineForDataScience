"""Batterie de tests pour ft_filter : compare ton ft_filter au vrai filter.

Usage : place ce fichier dans ex06/ puis lance `python test_ft_filter.py`.
"""
from ft_filter import ft_filter


def run(name, func, iterable_factory):
    """Compare ft_filter et filter sur un cas, sans planter."""
    try:
        expected = list(filter(func, iterable_factory()))
    except Exception as e:
        expected = f"{type(e).__name__}"
    try:
        got = list(ft_filter(func, iterable_factory()))
    except Exception as e:
        got = f"{type(e).__name__}"
    status = "OK  " if got == expected else "FAIL"
    print(f"[{status}] {name}")
    if status == "FAIL":
        print(f"        attendu : {expected}")
        print(f"        obtenu  : {got}")
    return status == "OK  "


def main():
    """Lance tous les tests."""
    def is_even(x):
        """Renvoie True si x est pair."""
        return x % 2 == 0

    def gen():
        """Petit générateur de test."""
        yield from [0, 1, 2, 3, 4]

    cases = [
        # --- cas de base ---
        ("liste + fonction", is_even, lambda: [1, 2, 3, 4, 5, 6]),
        ("liste + lambda", lambda x: x > 2, lambda: [1, 2, 3, 4]),
        ("aucun élément ne passe", lambda x: False, lambda: [1, 2, 3]),
        ("tous les éléments passent", lambda x: True, lambda: [1, 2, 3]),
        # --- itérable vide ---
        ("liste vide", is_even, lambda: []),
        ("chaîne vide", str.isupper, lambda: ""),
        # --- autres itérables que list ---
        ("tuple", is_even, lambda: (1, 2, 3, 4)),
        ("chaîne de caractères", str.isupper, lambda: "HeLLo WoRLD"),
        ("range", is_even, lambda: range(10)),
        ("dict (itère sur quoi ?)", lambda k: k > 1, lambda: {1: "a", 2: "b", 3: "c"}),
        ("générateur", is_even, gen),
        # --- le cas spécial de la doc ---
        ("function = None", None, lambda: [0, 1, "", "a", None, [], [0], False, True]),
        ("None + valeurs falsy only", None, lambda: [0, "", None, [], {}, 0.0, False]),
        ("None + liste vide", None, lambda: []),
        # --- fonctions renvoyant autre chose qu'un bool ---
        ("fonction renvoyant int/str", lambda x: x % 3, lambda: range(7)),
        ("fonction identité", lambda x: x, lambda: [0, 1, "", "x"]),
        # --- cas d'erreur : doit lever comme filter ---
        ("itérable = int (non itérable)", is_even, lambda: 42),
        ("function non appelable", 42, lambda: [1, 2]),
    ]

    ok = sum(run(*c) for c in cases)

    print()
    # --- __doc__ ---
    same_doc = ft_filter.__doc__ == filter.__doc__
    print(f"[{'OK  ' if same_doc else 'FAIL'}] __doc__ identique à filter.__doc__")
    ok += same_doc

    # --- type de retour : à méditer, pas forcément bloquant ---
    r = ft_filter(None, [1])
    print(f"[INFO] type renvoyé par ft_filter : {type(r).__name__} "
          f"(filter renvoie : {type(filter(None, [1])).__name__})")

    total = len(cases) + 1
    print(f"\n{ok}/{total} tests OK")


if __name__ == "__main__":
    main()
