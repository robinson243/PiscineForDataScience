from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
for elem in ft_tqdm(range(8)):
    sleep(0.005)
print()
for elem in tqdm(range(8)):
    sleep(0.005)
print()

# mon_compteur = ft_tqdm(range(10))  # Rien ne s'exécute ici ! (Lazy
# evaluation)

# # L'exécution du corps de la fonction démarre seulement au premier appel de next()

# while True:
#     print(next(mon_compteur))  # Affiche : Début du compteur... puis 1
# # print(next(mon_compteur))  # Affiche : 2
# # print(next(mon_compteur))
