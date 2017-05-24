import gym
from random import randint
from statistics import mean
from collections import Counter

testGames = 10000
trainThreshold = 50
env = gym.make('CartPole-v0')
print env.reset()


def createTrainingData():
    trainingData = []
    scores = []
    for _ in range(testGames):
        observation = env.reset()
        score = 0
        gameData = []
        for t in range(200):
            action = randint(0, 1)
            prevObs = observation
            observation, reward, done, info = env.step(action)
            gameData.append({'action': action, 'prevObs': prevObs})
            score += reward
            if done:
                break
        if score > trainThreshold:
            one = [0, 1]  # one-hot format
            zero = [1, 0]
            for data in gameData:
                if data['action'] == 1:
                    trainingData.append([data['prevObs'], one])
                elif data['action'] == 0:
                    trainingData.append([data['prevObs'], zero])

            scores.append(score)
    print "Mean: {}".format(mean(scores))
    print (Counter(scores))
    return trainingData


createTrainingData()
