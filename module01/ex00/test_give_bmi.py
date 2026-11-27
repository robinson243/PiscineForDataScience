"""Batterie de tests pour give_bmi et apply_limit (ex00, module Array).

Usage : place ce fichier dans ex00/ a cote de give_bmi.py,
puis lance `python3 test_give_bmi.py`.

Pour chaque cas d'erreur, ta fonction doit gerer l'erreur elle-meme
(message clair, pas de traceback). Si une exception remonte jusqu'ici,
le test affiche [CRASH] : c'est ce qui invaliderait l'exo en evaluation.
"""
from give_bmi import give_bmi, apply_limit


def run(label, func, *args):
    """Appelle func(*args), affiche le resultat ou [CRASH] si ca plante."""
    print(f"--- {label}")
    try:
        result = func(*args)
        print(f"    retour : {result!r}  ({type(result).__name__})")
        return result
    except Exception as e:
        print(f"    [CRASH] {type(e).__name__}: {e}")
        return None


def close(a, b):
    """Compare deux listes de floats a 1e-9 pres."""
    return (isinstance(a, list) and len(a) == len(b)
            and all(abs(x - y) < 1e-9 for x, y in zip(a, b)))


def main():
    """Lance tous les tests."""
    print("========== CAS NORMAUX (resultat verifie) ==========")
    ok = 0
    total = 0

    expected_bmi = [165.3 / 2.71 ** 2, 38.4 / 1.15 ** 2]
    r = run("exemple du sujet", give_bmi, [2.71, 1.15], [165.3, 38.4])
    total += 1
    if close(r, expected_bmi):
        ok += 1
        print("    [OK]")
    else:
        print(f"    [FAIL] attendu une list ~ {expected_bmi}")

    r = run("entiers", give_bmi, [2, 1], [80, 50])
    total += 1
    if close(r, [20.0, 50.0]):
        ok += 1
        print("    [OK]")
    else:
        print("    [FAIL] attendu [20.0, 50.0] (list)")

    r = run("apply_limit du sujet", apply_limit, expected_bmi, 26)
    total += 1
    if r == [False, True]:
        ok += 1
        print("    [OK]")
    else:
        print("    [FAIL] attendu [False, True] (list)")

    r = run("apply_limit : egal a la limite", apply_limit, [26, 26.0], 26)
    total += 1
    if r == [False, False]:
        ok += 1
        print("    [OK]")
    else:
        print("    [FAIL] attendu [False, False] ('above' = strictement)")

    print(f"\n{ok}/{total} cas normaux OK")

    print("\n========== CAS D'ERREUR (ne doivent PAS crasher) ==========")
    print("Regarde si le message est clair et si le retour te parait logique.\n")
    run("tailles differentes", give_bmi, [1.8], [70, 80])
    run("une string dans height", give_bmi, [1.8, "a"], [70, 80])
    run("une string dans weight", give_bmi, [1.8, 1.7], [70, "b"])
    run("None dans une liste", give_bmi, [1.8, None], [70, 80])
    run("booleen dans une liste", give_bmi, [1.8, True], [70, 80])
    run("taille a zero", give_bmi, [0], [70])
    run("taille negative", give_bmi, [-1.8], [70])
    run("listes vides", give_bmi, [], [])
    run("height n'est pas une liste", give_bmi, "abc", [70])
    run("height = None", give_bmi, None, [70])
    run("apply_limit : bmi pas une liste", apply_limit, "abc", 26)
    run("apply_limit : string dans bmi", apply_limit, [22.5, "x"], 26)
    run("apply_limit : limit n'est pas un int", apply_limit, [22.5], "26")
    run("apply_limit : liste vide", apply_limit, [], 26)


if __name__ == "__main__":
    main()
