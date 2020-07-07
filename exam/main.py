filePath = 'tshirts.csv'
from reader import loadData, loadDataS
from splitData import getTrainingAndTest, getInputDataUni, getOutputData
from sklearn import neural_network
from sklearn import metrics
from sklearn.linear_model import SGDRegressor

temp, fShirts = loadData(filePath, 'temperature', 'femaleTshirts')
mShirts, ignored = loadData(filePath, 'maleTshirts', 'temperature')

t = [26,26,25,25,27,27,27,27,24,25,23,27,27,22,24,27,24,23,25,27,26,22,24,24,24,25,24,25,23,25]
'''
Numarare tricouri barbati/femei
'''
totalF = 0
totalM = 0
for i in range(len(fShirts)):
    totalF += fShirts[i]
    totalM += mShirts[i]
    
if totalF > totalM:
    print("Tricourile pentru femei se vand mai bine!")
elif totalF < totalM:
    print("Tricourile pentru barbati se vand mai bine!")
else:
    print("Se vand la fel de bine!");
    
'''
Model tricouri barbati
'''
trainI, testI = getTrainingAndTest(temp)
inputTrain, inputTest = getInputDataUni(trainI, testI, temp)
outputTrain, outputTest = getOutputData(trainI, testI, mShirts)

classifier = neural_network.MLPClassifier(max_iter=5000) #CHANGE TO 50000
classifier.fit(inputTrain, outputTrain)

regressor = SGDRegressor()
nrEpoci = 5000
for i in range(nrEpoci):
    regressor.partial_fit(inputTrain,outputTrain)
        


predict = classifier.predict(inputTest)

error = metrics.mean_squared_error(outputTest, predict)
print("Eroare pentru model: ", error)


'''
Prezicere pe baza temperaturii din luna viitoare
'''
predictedTemp = []
for i in t:
    predictedTemp.append([i])
predictSold = classifier.predict(predictedTemp)
predictSoldGD = regressor.predict(predictedTemp)
sold = 0
soldGD = 0
for i in predictSold:
    sold+= i
for i in predictSoldGD:
    soldGD+= i    
print(sold)
print(soldGD)

'''
Subiectul c
'''
filePath = "tshirtsNew.csv"
temp, fShirts = loadData(filePath, 'temperature', 'femaleTshirts')
mShirts, ignored = loadData(filePath, 'maleTshirts', 'temperature')
place, competition = loadDataS(filePath,'location','competitions')

'''
numberPlace = []
for i in place:
    if i == 'high-school':
        numberPlace.append(1)
    elif i == 'park':
        numberPlace.append(2)
    elif i == 'stadium':
        numberPlace.append(3)
    else:
        numberPlace.append(4)

numberComp = []      
for i in competition:
    if i == 'many':
        numberPlace.append(1)
    elif i == 'veryFew':
        numberPlace.append(2)
    elif i == 'few':
        numberPlace.append(3)
    elif i == 'medium':
        numberPlace.append(4)
    else:
        numberPlace.append(5)
'''
newOutputData = []
newInput = []
for i in range(len(place)):
    if place[i] == 'high-school' and competition[i] == 'many':
        newOutputData.append(mShirts[i])
        newInput.append(temp[i])
        
'''
Train new model
'''
predictedTemp2 = []
for i in newInput:
    predictedTemp2.append([i])
regressor2 = SGDRegressor()
nrEpoci = 5000

for i in range(nrEpoci):
    regressor2.partial_fit(predictedTemp2,newOutputData)

predictTemp3 = [[25]]  
a = regressor2.predict(predictTemp3)
b = regressor.predict(predictTemp3)
print(regressor2.predict(predictTemp3))
print(regressor.predict(predictTemp3))

print("Diferenta este:", a - b)
    