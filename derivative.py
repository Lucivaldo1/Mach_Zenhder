import numpy as np
def derivative(data):
    derive = np.zeros(len(data[:, 1]))
    derive[1:-1] = (data[2:, 1] - data[:-2, 1]) / (data[2:, 0] - data[:-2, 0])  # central
    derive[0] = (data[1, 1] - data[0, 1]) / (data[1, 0] - data[0, 0])  # foward for the first value
    derive[-1] = (data[-1, 1] - data[-2, 1]) / (data[-1, 0] - data[-2, 0])  # backward for the last value

    return np.transpose([data[:, 0], derive])