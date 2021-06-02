import numpy as np
#npa = numpy array

def sigmoid_act(npa):
    return 1/(1+np.power(np.e, npa))

def reluTop(npa):
    return min(1, npa)