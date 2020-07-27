#!/bin/python

import csv
import random
import math
import operator

def caculate(train, test):
    dis = 0
    for i in range(len(train) - 1):
        dis += pow((train[i] - test[i]), 2)
    return math.sqrt(dis)
    
def getResult(neigthbor):
    vote = {}
    for i in range(len(neigthbor)):
        label = neigthbor[i][-1] 
        if label in vote:
            vote[label] += 1
        else:
            vote[label] = 1

    sortedVotes = sorted(vote.iteritems(), key=operator.itemgetter(1),reverse=True) 
    return sortedVotes[0][0]

def neigthbor(trains, test, k): 
    distances = []
   
    for i in range(len(trains)):
        dist = caculate(trains[i], test)
        distances.append((trains[i], dist))

    distances.sort(key=operator.itemgetter(1))

    neigthbor = []
    for i in range(k):
        neigthbor.append(distances[i][0])
    return neigthbor
         

def loadData(fileName, split, trains, tests):
    with open(fileName, 'rw') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

        for x in range(len(dataset)):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trains.append(dataset[x])
            else:
                tests.append(dataset[x])

def accuracy(labels, predicts):
    total = len(labels)
    right = 0
    for i in range(total):
        if (labels[i] == predicts[i]):
            right += 1
    return (right / float(total)) * 100.00

if __name__ == '__main__':
    trains = []
    tests = []
    loadData('data.txt', 0.67, trains, tests)

    predicts = []
    labels = []

    for i in range(len(tests)):
        knn = neigthbor(trains, tests[i], 3)
        result = getResult(knn)
        predicts.append(result)
        labels.append(tests[i][-1])
 
    score = accuracy(labels, predicts) 
    print("accuracy: " + str(score))
