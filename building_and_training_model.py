# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:50:35 2024

@author:
Metehan Özdeniz

Documentation:
https://metehanozdeniz.com/projects/2024-04-30-text-classification-and-sentiment-analysis-using-cnn/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.metrics import Precision, Recall
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras import layers
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import ZeroPadding1D
import pickle

# Veriyi okuma ve işleme
train_df = pd.read_csv("dataset/train.txt", delimiter=';', header=None, names=['sentence','label'])
val_df = pd.read_csv("dataset/val.txt", delimiter=';', header=None, names=['sentence','label'])
test_df = pd.read_csv("dataset/test.txt", delimiter=';', header=None, names=['sentence','label'])

train_df.head(10)

train_df['label'].value_counts() # etiketlerin sayısı

train_df['label'].unique() # etiketlerin isimleri benzeyenler var mı diye kontrol

# Eğitim Veri Seti Etiket Dağılımı
label_counts = train_df['label'].value_counts()
light_colors = sns.husl_palette(n_colors=len(label_counts)) # renk paleti olşuturulması
sns.set(style="whitegrid") # arka plan rengi
plt.figure(figsize=(6,6))
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140, colors=light_colors) # pasta grafiği oluşturulması
plt.title('Eğitim Veri Seti Etiket Dağılımı')
plt.show()

# Test Veri Seti Etiket Dağılımı
label_counts = test_df['label'].value_counts()
light_colors = sns.husl_palette(n_colors=len(label_counts)) # renk paleti olşuturulması
sns.set(style="whitegrid") # arka plan rengi
plt.figure(figsize=(6,6))
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140, colors=light_colors) # pasta grafiği oluşturulması
plt.title('Test Veri Seti Etiket Dağılımı')
plt.show()

# Doğrulama Veri Seti Etiket Dağılımı
label_counts = val_df['label'].value_counts()
light_colors = sns.husl_palette(n_colors=len(label_counts)) # renk paleti olşuturulması
sns.set(style="whitegrid") # arka plan rengi
plt.figure(figsize=(6,6))
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140, colors=light_colors) # pasta grafiği oluşturulması
plt.title('Doğrulama Veri Seti Etiket Dağılımı')
plt.show()

# Eğitim veri setindeki veriler dengesiz olduğu için ve veri setini daha dengeli hale getirmeliyim.
# Bunun için veri setindeki en az olan etiket sayısına sahip olan 2 etiket olan `sevgi` ve `şaşkın` etiketlerini çıkartacağım

train_df = train_df[~train_df['label'].str.contains('sevgi')] # sevgi etiketini çıkartılması
train_df = train_df[~train_df['label'].str.contains('şaşkın')] # şaşkın etiketini çıkartılması

# Şimdi geriye kalan `mutlu`, `üzgün`, `öfke` ve `korku` etiketleri hala dengesiz bir şekilde dağılmış durumda.
# Bu etikerlerin dağılımını olabildiğince birbirine yaklaştırıyorum.

mutlu = train_df[train_df['label'] == 'mutlu'].sample(n=2200, random_state=20) # mutlu etiketine sahip rastgele 2200 veri
uzgun = train_df[train_df['label'] == 'üzgün'].sample(n=2200, random_state=20) # üzgün etiketine sahip rastgele 2200 veri
korku = train_df[train_df['label'] == 'korku'].sample(n=1937, random_state=20)
ofke = train_df[train_df['label'] == 'öfke'].sample(n=2160, random_state=20)

new_train_df = pd.concat([mutlu, uzgun, korku, ofke]) # rastgele seçilen bu verilerin birleştirilmesi

train_df = new_train_df.sample(frac=1, random_state=20).reset_index(drop=True) # birleştirilen verileri karıştırarak train_df yi yeniden oluşturuyorum

train_df.label.value_counts() # etiketlerin sayısı

label_counts = train_df['label'].value_counts()
light_colors = sns.husl_palette(n_colors=len(label_counts))
sns.set(style="whitegrid")
plt.figure(figsize=(6, 6))
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140, colors=light_colors)
plt.title('Eğitim Veri Seti Etiket Dağılımı')
plt.show()

# Artık eğitim veri seti daha dengeli hale geldi.
# Bu işlemlerin aynısını `test_df` ve `val_df` dataframeleri içinde yapacağım.

val_df.label.value_counts()

# sevgi ve şaşkın etiketlerinin çıkartılması
val_df = val_df[~val_df['label'].str.contains('sevgi')]
val_df = val_df[~val_df['label'].str.contains('şaşkın')]

mutlu = val_df[val_df['label'] == 'mutlu'].sample(n=250, random_state=20)
uzgun = val_df[val_df['label'] == 'üzgün'].sample(n=250, random_state=20)
korku = val_df[val_df['label'] == 'korku'].sample(n=212, random_state=20)
ofke = val_df[val_df['label'] == 'öfke'].sample(n=275, random_state=20)

df_sampled = pd.concat([mutlu, uzgun, korku, ofke])

val_df = df_sampled.sample(frac=1, random_state=20).reset_index(drop=True)

label_counts = val_df['label'].value_counts()
light_colors = sns.husl_palette(n_colors=len(label_counts))
sns.set(style="whitegrid")
plt.figure(figsize=(6, 6))
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140, colors=light_colors)
plt.title('Doğrulama Veri Seti Etiket Dağılımı')
plt.show()

test_df.label.value_counts()

# sevgi ve şaşkın etiketlerinin çıkartılması
test_df = test_df[~test_df['label'].str.contains('sevgi')]
test_df = test_df[~test_df['label'].str.contains('şaşkın')]

mutlu = test_df[test_df['label'] == 'mutlu'].sample(n=250, random_state=20)
uzgun = test_df[test_df['label'] == 'üzgün'].sample(n=250, random_state=20)
korku = test_df[test_df['label'] == 'korku'].sample(n=224, random_state=20)
ofke = test_df[test_df['label'] == 'öfke'].sample(n=274, random_state=20)

new_test_df = pd.concat([mutlu, uzgun, korku, ofke])

test_df = new_test_df.sample(frac=1, random_state=20).reset_index(drop=True)

label_counts = test_df['label'].value_counts()
light_colors = sns.husl_palette(n_colors=len(label_counts))
sns.set(style="whitegrid")
plt.figure(figsize=(6, 6))
plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140, colors=light_colors)
plt.title('Test Veri Seti Etiket Dağılımı')
plt.show()

# Verileri Ayırma
train_text = train_df['sentence']
train_label = train_df['label']

val_text = val_df['sentence']
val_label = val_df['label']

test_text = test_df['sentence']
test_label = test_df['label']

#Encoding
encoder = LabelEncoder() # etiketlerin sayısal değerlere dönüştürülmesi
tr_label = encoder.fit_transform(train_label)
val_label = encoder.transform(val_label)
ts_label = encoder.transform(test_label)

# Şimdi cümleleri sayısal değerlere dönüştürerek model tarafından kullanılabilir hale getiriyorum.
tokenizer = Tokenizer(num_words=10000) # metinlerin sayısal değerlere dönüştürülmesi
tokenizer.fit_on_texts(train_text)

sequences = tokenizer.texts_to_sequences(train_text)
tr_x = pad_sequences(sequences, maxlen=50) # metinlerin boyutlarının eşitlenmesi
tr_y = to_categorical(tr_label, num_classes=4) # etiketlerin kategorik hale getirilmesi

sequences = tokenizer.texts_to_sequences(val_text)
val_x = pad_sequences(sequences, maxlen=50)
val_y = to_categorical(val_label, num_classes=4)

sequences = tokenizer.texts_to_sequences(test_text)
ts_x = pad_sequences(sequences, maxlen=50)
ts_y = to_categorical(ts_label, num_classes=4)

# Modelin Oluşturulması
max_words = 10000
max_len = 50
embedding_dim = 32

# Branch 1
inputs1 = layers.Input(shape=(max_len,))  # inputs1 için giriş katmanı tanımlanması

branch1 = layers.Embedding(max_words, embedding_dim)(inputs1) # Embedding katmanı
branch1 = layers.Conv1D(64, 3, padding='same', activation='relu')(branch1) # Conv1D katmanı (64 filtre, 3 kernel boyutu)
branch1 = layers.BatchNormalization()(branch1) # BatchNormalization katmanı. Katman çıktılarını normalize eder.
branch1 = layers.ReLU()(branch1) # ReLU katmanı
branch1 = layers.Dropout(0.5)(branch1) # Dropout katmanı. Aşırı uyum (overfitting) önlemek için
branch1 = layers.GlobalMaxPooling1D()(branch1) # GlobalMaxPooling1D katmanı (en büyük değeri alır)

# Branch 2
inputs2 = layers.Input(shape=(max_len,))  # inputs2 için giriş katmanı tanımlanması

branch2 = layers.Embedding(max_words, embedding_dim)(inputs2)
branch2 = layers.Conv1D(64, 3, padding='same', activation='relu')(branch2)
branch2 = layers.BatchNormalization()(branch2)
branch2 = layers.ReLU()(branch2)
branch2 = layers.Dropout(0.5)(branch2)
branch2 = layers.GlobalMaxPooling1D()(branch2)

concatenated = layers.Concatenate()([branch1, branch2]) # Branch1 ve Branch2'nin birleştirilmesi

#Birleştirilen katmanların dense katmanı tarafından gizli katmana bağlanması
hid_layer = layers.Dense(128, activation='relu')(concatenated) # Gizli katman
dropout = layers.Dropout(0.3)(hid_layer) # Dropout katmanı. Overfitting önlemek için
output_layer = layers.Dense(4, activation='softmax')(dropout) # Çıkış katmanı

# Define the model with separate inputs
model = Model(inputs=[inputs1, inputs2], outputs=output_layer)

# Modelin Derlenmesi
model.compile(optimizer='adamax', loss='categorical_crossentropy', metrics=['accuracy', Precision(), Recall()])

model.summary()

# Modelin Eğitilmesi
batch_size = 50
epochs = 10
history = model.fit([tr_x, tr_x], tr_y, epochs=epochs, batch_size=batch_size, validation_data=([val_x, val_x], val_y))

# Sonuçları Değerlendirme ve Görselleştirme
(loss, accuracy, percision, recall) = model.evaluate([tr_x, tr_x], tr_y)
print(f'Loss: {round(loss, 2)}, Accuracy: {round(accuracy, 2)}, Precision: {round(percision, 2)}, Recall: {round(recall, 2)}')

(loss, accuracy, percision, recall) = model.evaluate([ts_x, ts_x], ts_y)
print(f'Loss: {round(loss, 2)}, Accuracy: {round(accuracy, 2)}, Precision: {round(percision, 2)}, Recall: {round(recall, 2)}')

history.history.keys()


# Görseleştirme
tr_acc = history.history['accuracy']
tr_loss = history.history['loss']
val_acc = history.history['val_accuracy']
val_loss = history.history['val_loss']

index_loss = np.argmin(val_loss)
val_lowest = val_loss[index_loss]
index_acc = np.argmax(val_acc)
acc_highest = val_acc[index_acc]


Epochs = [i + 1 for i in range(len(tr_acc))]
loss_label = f'Best epoch = {str(index_loss + 1)}'
acc_label = f'Best epoch = {str(index_acc + 1)}'


plt.figure(figsize=(20, 12))
plt.style.use('fivethirtyeight')


plt.subplot(2, 2, 1)
plt.plot(Epochs, tr_loss, 'r', label='Training loss')
plt.plot(Epochs, val_loss, 'g', label='Validation loss')
plt.scatter(index_loss + 1, val_lowest, s=150, c='blue', label=loss_label)
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(Epochs, tr_acc, 'r', label='Training Accuracy')
plt.plot(Epochs, val_acc, 'g', label='Validation Accuracy')
plt.scatter(index_acc + 1, acc_highest, s=150, c='blue', label=acc_label)
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)


plt.suptitle('Model Training Metrics Over Epochs', fontsize=16)
plt.show()

y_true=[] # gerçek etiketlerin tutulacağı liste
for i in range(len(ts_y)): # gerçek etiketlerin alınması
    x = np.argmax(ts_y[i]) 
    y_true.append(x)


preds = model.predict([ts_x, ts_x]) # tahminlerin alınması
y_pred = np.argmax(preds, axis=1) # tahminlerin en yüksek değerli indexlerinin alınması
y_true = np.argmax(ts_y, axis=1) # gerçek etiketlerin en yüksek değerli indexlerinin alınması
y_pred

plt.figure(figsize=(8,6))
emotions = {0: 'öfke', 1: 'korku', 2: 'mutlu', 3:'üzgün'}
emotions = list(emotions.values())
cm = confusion_matrix(y_true, y_pred.ravel())
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=emotions, yticklabels=emotions)

# Sınıflandırma Raporu
clr = classification_report(y_true, y_pred)
print(clr)

# Modelin Kaydedilmesi
with open('tokenizer.pkl', 'wb') as tokenizer_file: # tokenizer nesnesinin kaydedilmesi
    pickle.dump(tokenizer, tokenizer_file)

model.save('emotions_detect_model.h5')