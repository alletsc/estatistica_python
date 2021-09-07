import random
import numpy as np
import pandas as pd


data = {'codigo': np.arange(1,11).tolist()}
dataset = pd.DataFrame(data)

def amostragem_reservatorio(dataset, amostras):
    stream = []
    for i in (len(dataset)):
        stream.append()
    i = 0
    tamanho = len(data)
    reservatorio = [0] * amostras
    for i in range(amostras):
        reservatorio[i] = stream[i]
    while i < tamanho:
        j = random.randrange(i + 1)
        if j < amostras:
            reservatorio[j] = stream[i]
        i += 1
    return data.iloc[reservatorio]

df_amostra_reservatorio = amostragem_reservatorio(dataset, 3)
df_amostra_reservatorio.shape