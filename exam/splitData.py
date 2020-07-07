from numpy.random.mtrand import randint

def rafinare(vector):
    trainOutputRafinat = []
    for i in vector:
        trainOutputRafinat.append(i[0])
        
    return trainOutputRafinat
'''
Imparte vectorul in indexi de antrenament si indexi de test
'''
def getTrainingAndTest(vect):
    testIndexes = [] 
    for i in range(int(len(vect)/5)):
        rand = randint(0,len(vect)-1)
        while rand in testIndexes:
            for i in range(10):
                rand = randint(0,len(vect)-1)
        testIndexes.append(rand)
    
    testIndexes.sort()
    
    trainIndexes = [] 
    for i in range(len(vect)):
        if i not in testIndexes:
            trainIndexes.append(i)
            
    #print(testIndexes)
    #print(trainIndexes)
    
    return trainIndexes, testIndexes

'''
Construieste matrice de input care contine pe o linie x1, x2, ... xn (toate feature-urile)
'''
def getInputData(trainIndexes, testIndexes, vectX, vectY):
    X = []
    testX = []
    for i in trainIndexes:
        linie = [vectX[i], vectY[i]]
        X.append(linie)
        
    for i in testIndexes:
        linie = [vectX[i], vectY[i]]
        testX.append(linie)
        
    return X, testX
'''
Contruiteste matrice de input in cazul in care avem un singur feature
'''
def getInputDataUni(trainIndexes, testIndexes, vectX):
    X = []
    testX = []
    for i in trainIndexes:
        linie = [vectX[i]]
        X.append(linie)
        
    for i in testIndexes:
        linie = [vectX[i]]
        testX.append(linie)
        
    return X, testX
'''
Transforma outputul intr-o matrice care contine pe fiecare linie un output (linia k -> yk)
'''
def getOutputData(trainIndexes, testIndexes, output):
    Y = []
    testY = []
    for i in trainIndexes:
        Y.append(output[i])
    
    for i in testIndexes:
        testY.append(output[i])
        
    return Y, testY