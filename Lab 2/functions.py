def mean(array):
    return sum(array) / len(array)
def median(array):
    length = len(array)
    if length % 2 == 0:
        return array[length / 2] + array[(length / 2) + 1]
    else:
        return array[length / 2]
def variance(array, meanValue, whichType):
    sumValue = 0
    for i in range(len(array)):
        diff = (array[i] - meanValue)
        sumValue += diff * diff
    if whichType == "sample":
        return sumValue / len(array)
    elif whichType == "population":
        return sumValue / (len(array) - 1)
    else:
        return "Mention the Valid Type"
dataset = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
meanV = mean(dataset)
print("Sample Type Variance: ", variance(dataset, meanV, "sample"))
print("Population Type Variance: ", variance(dataset, meanV, "population"))
