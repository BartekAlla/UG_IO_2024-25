import numpy as np


def sig(x):
    return 1 / (1 + np.exp(-x))


def forwardPass(wiek, waga, wzrost):
    hidden1 = (wiek * -0.46122) + (waga * 0.97314) + (wzrost * -0.39203) + 0.80109
    hidden1_po_aktywacji = sig(hidden1)
    hidden2 = (wiek * 0.78548) + (waga * 2.10584) + (wzrost * -0.57847) + 0.43529
    hidden2_po_aktywacji = sig(hidden2)
    output = (hidden1_po_aktywacji * -0.81546) + (hidden2_po_aktywacji * 1.03775) - 0.2368
    return output


print(forwardPass(23, 75, 176))
print(forwardPass(48, 97, 178))
