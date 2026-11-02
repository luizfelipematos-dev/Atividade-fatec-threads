import multiprocessing
import time

def imprime(id):
    time.sleep(0.5)
    print('Thread #' + str(id))

def main():
    num_threads: int = 5
    ids = [0] * num_threads
    for i in range(num_threads):
        ids[i] = i
    with multiprocessing.Pool(processes=num_threads) as pool:
        pool.map(imprime, ids)

if __name__ == '__main__':
    main()