import multiprocessing
import time
import random

def soma(id, valores):
    total: int = 0
    for v in valores:
        total = total + v
        time.sleep(0.2)
    print('Linha', id, '- soma:', total)

def main():
    id: int = 0
    v1: int = 0
    v2: int = 0
    v3: int = 0
    v4: int = 0
    v5: int = 0
    num_threads: int = 3
    params = []

    for i in range(num_threads):
        id = i + 1
        v1 = random.randint(1, 100)
        v2 = random.randint(1, 100)
        v3 = random.randint(1, 100)
        v4 = random.randint(1, 100)
        v5 = random.randint(1, 100)
        params.append((id, [v1, v2, v3, v4, v5]))

    with multiprocessing.Pool(processes=num_threads) as pool:
        pool.starmap(soma, params)

if __name__ == '__main__':
    main()