# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:50:35 2024

@author:
Metehan Özdeniz

Documentation:
https://metehanozdeniz.com/projects/2024-04-30-text-classification-and-sentiment-analysis-using-cnn/
"""

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle
import matplotlib.pyplot as plt
import numpy as np

class Prediction():
    def __init__(self, model_path, token_path):
        self.model_path = model_path
        self.token_path = token_path

    # Load model and tokenizer
    def load_model(self):
        # Modelin yüklenmesi
        self.model = load_model(self.model_path)
        
        # Tokenizer'ın yüklenmesi 
        with open(self.token_path, 'rb') as f:
            self.tokenizer = pickle.load(f)
    
    # Prediction Function
    def predict(self, text):
        # Metinlerin sayısal değerlere dönüştürülmesi 
        sequences = self.tokenizer.texts_to_sequences([text])

        # Metinlerin aynı boyuta getirilmesi 
        x_new = pad_sequences(sequences, maxlen=50) 

        # Tahmin 
        predictions = self.model.predict([x_new, x_new])
        
        # Duyguların tanımlanması
        emotions = {0: 'korku', 1: 'mutlu', 2: 'öfke', 3:'üzgün'}

        # # Tahmin sonuçlarının görselleştirilmesi
        # label = list(emotions.values())
        # probs = list(predictions[0])
        # labels = label
        # plt.subplot(1, 1, 1)
        # bars = plt.barh(labels, probs)
        # plt.xlabel('Tahmin', fontsize=15)
        # plt.ylabel('Duygular', fontsize=15)
        # ax = plt.gca()
        # ax.bar_label(bars, fmt = '%.2f')
        # plt.show()

        # Tahmin sonuçlarının döndürülmesi 
        return emotions[np.argmax(predictions)], predictions