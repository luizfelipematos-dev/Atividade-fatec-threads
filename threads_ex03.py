import multiprocessing
import time
import random

pulo_max: int = 5
distancia_max: int = 30

def sapo(num):
    percorrido: int = 0
    salto: int = 0
    while percorrido < distancia_max:
        salto = random.randint(1, pulo_max)
        percorrido = percorrido + salto
        print('Sapo', num, 'pulou', salto, 'cm e ja percorreu', percorrido, 'cm')
        time.sleep(0.3)
    print('Sapo', num, 'CHEGOU!')

def main():
    num_sapos: int = 5
    sapos = [0] * num_sapos
    for i in range(num_sapos):
        sapos[i] = i + 1
    with multiprocessing.Pool(processes=num_sapos) as pool:
        pool.map(sapo, sapos)

if __name__ == '__main__':
    main()