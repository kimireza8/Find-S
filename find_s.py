import pandas as pd
import numpy as np

dataset = pd.read_csv('sport.csv')
print("Data Set : ", dataset)

datatraining = np.array(dataset)[:, 1:-1]
print("Data Training : ", datatraining)

target = np.array(dataset)[:, -1]
print("Target : ", target)

def find_s_algorithm(datatraining, target):
    hypothesis = None
    for i, val in enumerate(target):
        if val == 'Yes':
            if hypothesis is None:
                hypothesis = datatraining[i].copy()
            else:
                for j in range(len(hypothesis)):
                    if hypothesis[j] != datatraining[i][j]:
                        hypothesis[j] = '?'
    return hypothesis

hypothesis = find_s_algorithm(datatraining, target)
print("Hipotesa: ", hypothesis)

datatest1 = ['Sunny', 'Warm', 'Normal', 'Strong', 'Cool', 'Same']
datatest2 = ['Rainy', 'Warm', 'Normal', 'Strong', 'Cool', 'Change']

# Fungsi untuk memprediksi apakah datatest akan "Enjoy Sport" atau "Don't Sport"
def predict(hypothesis, datatest):
    for i in range(len(hypothesis)):
        if hypothesis[i] != '?' and hypothesis[i] != datatest[i]:
            return "Don't Sport"
    return "Enjoy Sport"

prediction1 = predict(hypothesis, datatest1)
print("Prediction for datatest1:", prediction1)

prediction2 = predict(hypothesis, datatest2)
print("Prediction for datatest2:", prediction2)