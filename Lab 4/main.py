import time
from itertools import permutations

import numpy as np
import pandas as pd
from tabulate import tabulate


def runM1():
    mat = pd.read_csv("6citytsp.csv", header=None).values
    table_data = {}

    for row in range(mat.shape[0]):
        startCity = row
        mat = pd.read_csv("6citytsp.csv", header=None).values
        cityNames = list(range(mat.shape[0]))
        cityNames.remove(startCity)
        per = list(permutations(cityNames))
        st = time.process_time()
        bestTourLength = np.inf
        bestTour = []
        for tour in per:
            tourLength = 0
            for i in range(len(tour) - 1):
                tourLength += mat[tour[i], tour[i + 1]]
                tourLength += mat[tour[i + 1], startCity]
                tourLength += mat[startCity, tour[0]]
            if tourLength < bestTourLength:
                bestTourLength = tourLength
                bestTour = list(tour)
        et = time.process_time()
        time_taken_ms = (et - st) * 1000
        table_data[row] = [bestTourLength, bestTour, time_taken_ms]

    print(tabulate(pd.DataFrame(table_data).T, tablefmt="pretty", headers=["Path Length", "Tour", "Elapsed Time"]))


if __name__ == '__main__':
    runM1()
