import sys
sys.path.append('../laplacian-leader-follower-dynamics')
import numpy as np
import randomMatrix

def generateRandomElementTest():
    # check that values on or below diagonal are zero
    for i in range(3, 9):
        for j in range(i, 0, -1):
            testValue = randomMatrix.generateRandomElement(i, j)
            if testValue != 0:
                raise Exception('generateRandomElementTest did not pass - nonzero element on or below diagonal')
    # check that values above diagonal are 0 or 1
    for i in range(3, 9):
        for j in range(i + 1, 9):
            testValue = randomMatrix.generateRandomElement(i, j)
            if not (testValue == 1 or testValue == 0):
                raise Exception('generateRandomElementTest did not pass - element above diagonal that is not 0 nor 1')
    print('')
    print('generateRandomElement passed')

def generateAdjacencyMatrixTest():
    dim = 9
    for i in range(99):
        mat = randomMatrix.generateAdjacencyMatrix(dim)
        matTranspose = np.transpose(mat)
        # check that the sum of the ith column and row are equal
        for j in range(dim):
            rowSum = np.sum(mat[j])
            columnSum = np.sum(matTranspose[j])
            if rowSum != columnSum:
                raise Exception('generateAdjacencyMatrix did not pass')
    print('')
    print('generateAdjacencyMatrix passed')


generateRandomElementTest()
generateAdjacencyMatrixTest()

print('')
print('all tests passed')
print('')