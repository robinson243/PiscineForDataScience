# def compte():
#     print("début")
#     yield 1
#     print("après le 1")
#     yield 10
#     print("fin")

# g = compte()

from time import sleep
from tqdm import tqdm
# from Loading import ft_tqdm
# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
# print()
for elem in tqdm(range(333)):
    sleep(0.005)
    
print()
