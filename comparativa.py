#comparar el tiempo en paralelo y secuencial

import time
from multiprocessing import Pool
from time import sleep
import random
def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration
def paral():
    urls = ["a.com", "b.com", "c.com", "d.com"]
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)


def secuencial():
    urls = ["a.com", "b.com", "c.com", "d.com"]
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)
    print('\n')
    for i in output:
        print(i)

def main():
    start = time.time()
    paral()
    end = time.time()
    print("Tiempo en paralelo", end - start)
    start = time.time()
    secuencial()
    end = time.time()
    print("Tiempo en secuencial", end - start)        
    