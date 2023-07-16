from statistics import geometric_mean,mode,harmonic_mean
import numpy as np
array = np.array([2, 3, 4, 7, 7, 8, 1])
array_stat = [2, 3, 4, 7, 7, 8, 1]
rangeStats = max(array) - min(array)
mean = np.mean(array)
median = np.median(array)
mode = mode(array_stat)
standardDeviation = np.std(array)
var = standardDeviation * standardDeviation
gm = geometric_mean(array_stat)
hm = harmonic_mean(array_stat)
print(
    f"Range: {rangeStats}\nMean: {mean}\nMedian: {median}\nMode (Stat): {mode}\nVariance: {var}\n"
    f"Standard Deviation: {standardDeviation}\nGeometric Mean: {gm}\nHarmonic Mean: {hm}")
