import time

import numpy as np
import pandas as pd
from tabulate import tabulate


def runM2():
    df = pd.read_csv('6citytsp.csv', header=None).values.astype(float)
    table_data = {}

    for row in range(df.shape[0]):
        df = pd.read_csv('6citytsp.csv', header=None).values.astype(float)
        stCity = row
        nextBestCity = 0
        tourLength = 0
        tour = [stCity]
        df[df == 0] = np.inf
        df1 = df.copy()
        st = time.process_time()
        for i in range(df.shape[0] - 1):
            if i == 0:
                tourLength += min(df[stCity, :])
                nextBestCity = np.argmin(df[stCity, :])
                tour.append(nextBestCity)
                df[:, stCity] = np.inf
                df[:, nextBestCity] = np.inf
            else:
                tourLength += min(df[nextBestCity, :])
                nextBestCity = np.argmin(df[nextBestCity, :])
                tour.append(nextBestCity)
                # df[:, nextBestCity] = np.inf
        tourLength += df1[nextBestCity, stCity]
        et = time.process_time()
        table_data[row] = [tourLength, tour, et - st]

    print(tabulate(pd.DataFrame(table_data).T, tablefmt="pretty", headers=["Path Length", "Tour", "Elapsed Time"]))


if __name__ == '__main__':
    runM2()
