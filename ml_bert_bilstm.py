# -*- coding: utf-8 -*-
"""ML BERT BiLSTM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-C9eEZs5py-pdcgzj92XyJ4NCXug6Ty_

# Preprocessing
"""

import numpy as np
import pandas as pd

df = pd.read_csv("Final_Bhaav_dataset.csv")
df

# code to change list into string
#for i in range(len(df)):
#  name = df['header'][i]
#  df['header'][i] = name[2:len(name)-3]

df['Annotation'].value_counts()

df.head()

df = df.sample(frac=1).reset_index(drop=True)
df

# save dataframe to csv
#df.to_csv('Bhaav.csv', index=False)

df.groupby('Annotation').count()

"""# Dataset Visualization"""

import matplotlib.pyplot as plt
import seaborn as sns

col = 'Annotation'
fig, (ax1, ax2)  = plt.subplots(nrows=1, ncols=2, figsize=(12,8))
explode = list((np.array(list(df[col].dropna().value_counts()))/sum(list(df[col].dropna().value_counts())))[::-1])[:10]
labels = list(df[col].dropna().unique())[:10]
sizes = df[col].value_counts()[:10]
#ax.pie(sizes, explode=explode, colors=bo, startangle=60, labels=labels,autopct='%1.0f%%', pctdistance=0.9)
ax2.pie(sizes,  explode=explode, startangle=60, labels=labels,autopct='%1.0f%%', pctdistance=0.9)
ax2.add_artist(plt.Circle((0,0),0.6,fc='white'))
sns.countplot(y =col, data = df, ax=ax1)
ax1.set_title("Count of each emotion")
ax2.set_title("Percentage of each emotion")
plt.show()

"""# Tokenization"""

import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Tokenize the text into words
def tokenize_sentence(sentence):
  tokens = word_tokenize(str(sentence))
  return tokens
df['Sentences']= df['Sentences'].apply(tokenize_sentence)

df['Sentences'][16]

df.index

stopwords_hi = ['तुम','मेरी','मुझे','क्योंकि','हम','प्रति','अबकी','आगे','माननीय','शहर','बताएं','कौनसी','क्लिक','किसकी','बड़े','मैं','and','रही','आज','लें','आपके','मिलकर','सब','मेरे','जी','श्री','वैसा','आपका','अंदर', 'अत', 'अपना', 'अपनी', 'अपने', 'अभी', 'आदि', 'आप', 'इत्यादि', 'इन', 'इनका', 'इन्हीं', 'इन्हें', 'इन्हों', 'इस', 'इसका', 'इसकी', 'इसके', 'इसमें', 'इसी', 'इसे', 'उन', 'उनका', 'उनकी', 'उनके', 'उनको', 'उन्हीं', 'उन्हें', 'उन्हों', 'उस', 'उसके', 'उसी', 'उसे', 'एक', 'एवं', 'एस', 'ऐसे', 'और', 'कई', 'कर','करता', 'करते', 'करना', 'करने', 'करें', 'कहते', 'कहा', 'का', 'काफ़ी', 'कि', 'कितना', 'किन्हें', 'किन्हों', 'किया', 'किर', 'किस', 'किसी', 'किसे', 'की', 'कुछ', 'कुल', 'के', 'को', 'कोई', 'कौन', 'कौनसा', 'गया', 'घर', 'जब', 'जहाँ', 'जा', 'जितना', 'जिन', 'जिन्हें', 'जिन्हों', 'जिस', 'जिसे', 'जीधर', 'जैसा', 'जैसे', 'जो', 'तक', 'तब', 'तरह', 'तिन', 'तिन्हें', 'तिन्हों', 'तिस', 'तिसे', 'तो', 'था', 'थी', 'थे', 'दबारा', 'दिया', 'दुसरा', 'दूसरे', 'दो', 'द्वारा', 'न', 'नहीं', 'ना', 'निहायत', 'नीचे', 'ने', 'पर', 'पर', 'पहले', 'पूरा', 'पे', 'फिर', 'बनी', 'बही', 'बहुत', 'बाद', 'बाला', 'बिलकुल', 'भी', 'भीतर', 'मगर', 'मानो', 'मे', 'में', 'यदि', 'यह', 'यहाँ', 'यही', 'या', 'यिह', 'ये', 'रखें', 'रहा', 'रहे', 'ऱ्वासा', 'लिए', 'लिये', 'लेकिन', 'व', 'वर्ग', 'वह', 'वह', 'वहाँ', 'वहीं', 'वाले', 'वुह', 'वे', 'वग़ैरह', 'संग', 'सकता', 'सकते', 'सबसे', 'सभी', 'साथ', 'साबुत', 'साभ', 'सारा', 'से', 'सो', 'ही', 'हुआ', 'हुई', 'हुए', 'है', 'हैं', 'हो', 'होता', 'होती', 'होते', 'होना', 'होने', 'अपनि', 'जेसे', 'होति', 'सभि', 'तिंहों', 'इंहों', 'दवारा', 'इसि', 'किंहें', 'थि', 'उंहों', 'ओर', 'जिंहें', 'वहिं', 'अभि', 'बनि', 'हि', 'उंहिं', 'उंहें', 'हें', 'वगेरह', 'एसे', 'रवासा', 'कोन', 'निचे', 'काफि', 'उसि', 'पुरा', 'भितर', 'हे', 'बहि', 'वहां', 'कोइ', 'यहां', 'जिंहों', 'तिंहें', 'किसि', 'कइ', 'यहि', 'इंहिं', 'जिधर', 'इंहें', 'अदि', 'इतयादि', 'हुइ', 'कोनसा', 'इसकि', 'दुसरे', 'जहां', 'अप', 'किंहों', 'उनकि', 'भि', 'वरग', 'हुअ', 'जेसा', 'नहिं']
punctuations = ['nn','9','8','7','6','5','4','3','2','1','n', '।','/', '`', '+', '"', '?', '▁(', '$', '@', '[', '_', '!', ',', ':', '^', '|', ']', '%', '&', '.', ')', '(', '#', '*', '', ';', '-', '}','|','"',"'"]
to_be_removed = stopwords_hi + punctuations
for i in range(len(df)):
  if i in df.index:
    df['Sentences'][i]=[ele for ele in df['Sentences'][i] if ele not in (to_be_removed)]

df.head()

max = 0

for i in df['Sentences']:

  if len(i) > max:
    max = len(i)

print(max)

# list of words to string
def word_to_sentence(list1):
  sent = ' '.join(list1)
  return sent
df['Sentences']= df['Sentences'].apply(word_to_sentence)
df

"""# Encoding

## TF-IDF Encoding
"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer1 = TfidfVectorizer()
docs1 = np.array([df['Sentences']])
# tokenize and build vocab
vectorizer1.fit(docs1.ravel())
# summarize
print(vectorizer1.vocabulary_)
print(vectorizer1.idf_)
# encode document
vector = vectorizer1.transform(docs1.ravel())
# summarize encoded vector
print(vector.shape)
print(vector.toarray())

X1= vector.toarray()
X1
y= np.array(df["Annotation"])
print(y[0:10])

"""## Count Vectorizer encoding

"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

vectorizer0 = CountVectorizer()
# Create sample set of documents
docs0 = np.array([df['Sentences']])
# Fit the bag-of-words model
bag = vectorizer0.fit_transform(docs0.ravel())
# Get unique words / tokens found in all the documents. The unique words / tokens represents
print(vectorizer0.get_feature_names_out())
print(vectorizer0.vocabulary_)
print(bag.toarray())

X = bag.toarray()
print(X[0:5])
y= np.array(df["Annotation"])
print(y[0:5])

"""## Hash Encoding"""

from sklearn.feature_extraction.text import HashingVectorizer

vectorizer = HashingVectorizer(n_features=100)
docs2 = np.array([df['Sentences']])
vector = vectorizer.transform(docs2.ravel())
# summarize encoded vector
print(vector.shape)
print(vector.toarray())

X2 =vector.toarray()
print(X2[0:5])
y= np.array(df["Annotation"])
print(y[0:5])

"""# Data Splitting"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X1,df['Annotation'], test_size = 0.2, random_state = 50,stratify=df['Annotation'])

X_train.shape
y_train.shape

X_train

y_train.value_counts()

y_test.value_counts()

max = 0

for i in X_train:

  if len(i) > max:
    max = len(i)

print(max)

"""# ML model using tfidf

### Naive Bayes
"""

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV

param_grid_nb = {
    'var_smoothing': np.logspace(0,-9, num=100)
}

# Build a Gaussian Classifier
nb_model = GridSearchCV(estimator=GaussianNB(), param_grid=param_grid_nb, verbose=1, cv=10, n_jobs=-1)

# Model training
nb_model.fit(X_train, y_train)

# Predict Output
nb_predicted = nb_model.predict(X_test)

from sklearn.metrics import classification_report
print('Gaussian NB Classification Report')
print(classification_report(y_test, nb_predicted))

import sklearn.metrics as metrics
score1 = metrics.accuracy_score(y_test, nb_predicted)
print('Accuracy: %0.3f' %score1)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
lr_cm = confusion_matrix(y_test, nb_predicted)
#Plot the confusion matrix.
sns.heatmap(lr_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('Naive Bayes Confusion Matrix',fontsize=10)
plt.show()

"""### Logistic regression"""

# Logistic Regression
from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression(random_state=42)

lr_model.fit(X_train, y_train)

# Predict Output

lr_predicted = lr_model.predict(X_test)

from sklearn.metrics import classification_report
print('LR Classification Report')
print(classification_report(y_test, lr_predicted))

import sklearn.metrics as metrics
score2 = metrics.accuracy_score(y_test, lr_predicted)
print('Accuracy: %0.3f' %score2)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
lr_cm = confusion_matrix(y_test, lr_predicted)
#Plot the confusion matrix.
sns.heatmap(lr_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('Logistic regression Confusion Matrix',fontsize=10)
plt.show()

"""### SVC"""

# "Support Vector Classifier"
from sklearn.svm import SVC
svm_model = SVC(C=1.0, kernel='linear', degree=3, gamma='auto')

# fitting x samples and y classes
svm_model.fit(X_train, y_train)

# Predict Output
svm_predicted = svm_model.predict(X_test)

from sklearn.metrics import classification_report
print('SVC Classification Report')
print(classification_report(y_test, svm_predicted))

import sklearn.metrics as metrics
score3 = metrics.accuracy_score(y_test, svm_predicted)
print('Accuracy: %0.3f' %score3)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
svc_cm = confusion_matrix(y_test, svm_predicted)
#Plot the confusion matrix.
sns.heatmap(svc_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('SVC Confusion Matrix',fontsize=10)
plt.show()

"""### Decision Tree Classifier"""

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier(criterion='gini', random_state=1)
dt_model.fit(X_train, y_train)

# Predict Output
dt_predicted = dt_model.predict(X_test)

from sklearn.metrics import classification_report
print('DT Classification Report')
print(classification_report(y_test, dt_predicted))

import sklearn.metrics as metrics
score4 = metrics.accuracy_score(y_test, dt_predicted)
print('Accuracy: %0.3f' %score4)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
dt_cm = confusion_matrix(y_test, dt_predicted)
#Plot the confusion matrix.
sns.heatmap(dt_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('DT Confusion Matrix',fontsize=10)
plt.show()

"""### XGBoost"""

# xgboost Classifier
import xgboost as xgb
# Create the XGBoost classifier
xg_model = xgb.XGBClassifier()

# Train the model on the training data
xg_model.fit(X_train, y_train)

# Predict Output
xg_predicted = xg_model.predict(X_test)

from sklearn.metrics import classification_report
print('XGBoost Classification Report')
print(classification_report(y_test, xg_predicted))

import sklearn.metrics as metrics
score5 = metrics.accuracy_score(y_test, xg_predicted)
print('Accuracy: %0.3f' %score5)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
xgbc_cm = confusion_matrix(y_test, xg_predicted)
#Plot the confusion matrix.
sns.heatmap(xgbc_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('XGBoost Confusion Matrix',fontsize=10)
plt.show()

"""### KNN"""

# KNN Classifier
from sklearn.neighbors import KNeighborsClassifier
# Create the KNN classifier with k=3 (you can choose a different value for k)
knn_model = KNeighborsClassifier(n_neighbors=5)

# Train the model on the training data
knn_model.fit(X_train, y_train)

# Predict Output
knn_predicted = knn_model.predict(X_test)

from sklearn.metrics import classification_report
print('KNN Classification Report')
print(classification_report(y_test, knn_predicted))

import sklearn.metrics as metrics
score6 = metrics.accuracy_score(y_test, knn_predicted)
print('Accuracy: %0.3f' %score6)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
knn_cm = confusion_matrix(y_test, knn_predicted)
#Plot the confusion matrix.
sns.heatmap(knn_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('KNN Confusion Matrix',fontsize=10)
plt.show()

"""## One Vs All Classifier"""

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
ovr_model = OneVsRestClassifier(SVC())
history=ovr_model.fit(X_train, y_train)

# Predict Output
ovr_predicted = ovr_model.predict(X_test)

from sklearn.metrics import classification_report
print('OVR Classification Report')
print(classification_report(y_test, ovr_predicted))

import sklearn.metrics as metrics
score7 = metrics.accuracy_score(y_test, ovr_predicted)
print('Accuracy: %0.3f' %score7)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
ovr_cm = confusion_matrix(y_test, ovr_predicted)
#Plot the confusion matrix.
sns.heatmap(ovr_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('OVR Confusion Matrix',fontsize=10)
plt.show()

"""## Light GBM"""

# LGBMClassifier
from lightgbm import LGBMClassifier
#lightGBM_model = LGBMClassifier(n_estimators = 100, objective='multiclass', boosting_type='gbdt', n_jobs=5, random_state=5)
lightGBM_model = LGBMClassifier(n_jobs=5, random_state=5) # same results as above
lightGBM_history = lightGBM_model.fit(X_train, y_train)

l_pred = lightGBM_model.predict(X_test)

from sklearn.metrics import classification_report
print('LightGBM Classification Report')
print(classification_report(y_test, l_pred))

import sklearn.metrics as metrics
score8 = metrics.accuracy_score(np.array(y_test), l_pred)
print('Accuracy: %0.3f' %score8)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
lightGBM_cm = confusion_matrix(y_test, l_pred)
#Plot the confusion matrix.
sns.heatmap(lightGBM_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('LightGBM Confusion Matrix',fontsize=10)
plt.show()

"""## RF"""

from sklearn.ensemble import RandomForestClassifier
# creating a RF classifier
clf = RandomForestClassifier(n_estimators = 100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
from sklearn import metrics
print("ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
print('Random Forest Classification Report')
print(classification_report(y_test, y_pred))

import sklearn.metrics as metrics
score9 = metrics.accuracy_score(np.array(y_test), y_pred)
print('Accuracy: %0.3f' %score9)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
#compute the confusion matrix.
rf_cm = confusion_matrix(y_test, y_pred)
#Plot the confusion matrix.
sns.heatmap(rf_cm, annot=True, fmt='g')

plt.ylabel('Prediction',fontsize=10)
plt.xlabel('Actual',fontsize=10)
plt.title('Random Forest Confusion Matrix',fontsize=10)
plt.show()

"""# Bert Model"""

#! pip install simpletransformers

from transformers import AutoTokenizer,TFBertModel
tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased')
bert = TFBertModel.from_pretrained('bert-base-multilingual-cased')

# here tokenizer using from bert-base-cased

x_train = tokenizer(
    text= X_train.tolist(),
    add_special_tokens=True,
    max_length=128,
    truncation=True,
    padding=True,
    return_tensors='tf',
    return_token_type_ids = False,
    return_attention_mask = True,
    verbose = True)

x_test = tokenizer(
    text=X_test.tolist(),
    add_special_tokens=True,
    max_length=128,
    truncation=True,
    padding=True,
    return_tensors='tf',
    return_token_type_ids = False,
    return_attention_mask = True,
    verbose = True)

x_test['input_ids']

x_test

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.initializers import TruncatedNormal
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers.legacy import Adam

import tensorflow as tf
tf.config.experimental.list_physical_devices('GPU')

max_len = 128
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense


input_ids = Input(shape=(max_len,), dtype=tf.int32, name="input_ids")
input_mask = Input(shape=(max_len,), dtype=tf.int32, name="attention_mask")


embeddings = bert(input_ids,attention_mask = input_mask)[0] #(0 is the last hidden states,1 means pooler_output)
out = tf.keras.layers.GlobalMaxPool1D()(embeddings)
out = Dense(128, activation='relu')(out)
out = tf.keras.layers.Dropout(0.2)(out)
out = Dense(32,activation = 'relu')(out)

y = Dense(5,activation = 'softmax')(out)

model = tf.keras.Model(inputs=[input_ids, input_mask], outputs=y)
model.layers[2].trainable = True
# for training bert our lr must be so small

optimizer = Adam(
    learning_rate=5e-05, # this learning rate is for bert model , taken from huggingface website
    epsilon=1e-08,
    decay=0.01,
    clipnorm=1.0)

# Set loss and metrics
loss =CategoricalCrossentropy(from_logits = True)
metric = CategoricalAccuracy('accuracy'),
# Compile the model
model.compile(
    optimizer = optimizer,
    loss = loss,
    metrics = metric)

model.summary()



train_history = model.fit(
    x ={'input_ids':x_train['input_ids'],'attention_mask':x_train['attention_mask']} ,
    y = to_categorical(y_train),
    validation_data = (
    {'input_ids':x_test['input_ids'],'attention_mask':x_test['attention_mask']}, to_categorical(y_test)
    ),
  epochs=50,
    batch_size=64
)

import matplotlib.pyplot as plt
# Extract training and validation accuracy values from train_history
train_accuracy = train_history.history['accuracy']
val_accuracy = train_history.history['val_accuracy']

# Plot Training and Validation Accuracy
epochs = range(1, len(train_accuracy) + 1)
plt.plot(epochs, train_accuracy, 'b', label='Training Accuracy')
plt.plot(epochs, val_accuracy, 'r', label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()
plt.show()

# Extract training and validation accuracy values from train_history
train_accuracy = train_history.history['loss']
val_accuracy = train_history.history['val_loss']

# Plot Training and Validation Accuracy
epochs = range(1, len(train_accuracy) + 1)
plt.plot(epochs, train_accuracy, 'b', label='Training Loss')
plt.plot(epochs, val_accuracy, 'r', label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()

from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(y_test, y_pred)

# Plot Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=[0,1,2,3,4], yticklabels=[0,1,2,3,4])
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""# BiLSTM"""

import tensorflow
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Bidirectional, Embedding, LSTM, Dense, Dropout,GlobalMaxPooling1D,TimeDistributed
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

#Using keras to tokenize and pad inputs
tokenize = Tokenizer(oov_token="<OOV>")
tokenize.fit_on_texts(df['Sentences'])
word_index = tokenize.word_index
train = tokenize.texts_to_sequences(df['Sentences'])
data = pad_sequences(train, padding="post")

#Getting length of the padded input
maxlen = data.shape[1]
print(maxlen)

#Example of padded inputs
print(data[0])
print(len(word_index))

len(word_index)

import numpy as np
from tensorflow.keras.utils import to_categorical
encoded_labels = to_categorical(df['Annotation'], num_classes=5)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data,encoded_labels, test_size = 0.2, random_state = 50)

vocab_size = len(word_index) + 1

model = Sequential()
model.add(Embedding(vocab_size, 32))
model.add(Bidirectional(LSTM(128, return_sequences=True)))
model.add(Bidirectional(LSTM(64)))
#model.add(GlobalMaxPooling1D())
model.add(Dense(5, activation="softmax"))

#callbacks: checkpoint, csv_logger
from keras.callbacks import ModelCheckpoint, CSVLogger
checkpoint = ModelCheckpoint("bi-lstm-model.hdf5", monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
csv_log=CSVLogger('bi-lstm_log.csv',separator=',',append=False)
callbacks_list=[checkpoint,csv_log]

model.compile(loss = "categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test), callbacks=callbacks_list)

"""# Results of BiLSTM"""

from keras.models import load_model
model = load_model('bi-lstm-model.hdf5')

model.summary()

# code to load model
import numpy as np
import tensorflow as tf

# Load the training history from bilstm.npy
history = np.load('bilstm.npy', allow_pickle=True).item()

# Load the trained model from bi-lstm-model.hdf5
model = tf.keras.models.load_model('bi-lstm-model.hdf5')

np.save('bilstm.npy',history.history)

# add history. history if you are printing after training the model
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
epochs = range(1, len(history.history['accuracy']) + 1)
plt.plot(epochs, history.history['accuracy'], 'b', label='Training Accuracy')
plt.plot(epochs, history.history['val_accuracy'], 'r', label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(epochs, history.history['loss'], 'b-', label='Training Loss')
plt.plot(epochs, history.history['val_loss'], 'r-', label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

y_test_arg = np.argmax(y_test, axis=1)
Y_pred = np.argmax(model.predict(X_test), axis=1)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test_arg, Y_pred)

Y_pred[:7]

y_test[:7]

y_test_arr = []
index = 0
for i in y_test:
  for j in range(len(i)):
    if i[j] == 1.0:
      y_test_arr.append(j)
      index += 1

y_test_arr[:7]

from sklearn.metrics import classification_report
print('Bi-LSTM Classification Report')
print(classification_report(y_test_arr, Y_pred))

import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', xticklabels=[0,1,2,3,4], yticklabels=[0,1,2,3,4])
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()

model.evaluate(X_test,y_test)

test_text = "उसकी बेहद निर्मम टिपटियां सबको उसके खिलाफ गुस्सा दिलाने में कामयाब हो गईं"
test_sequence = tokenize.texts_to_sequences([test_text])
test_data = pad_sequences(test_sequence, padding="post", maxlen=maxlen)
predictions = model.predict(test_data)
predicted_class = np.argmax(predictions[0])
predicted_class

predictions

prediction_result = np.array(predictions)
prediction_result

# Assuming you have the class names in a list
class_names = ['Anger', 'Surprise', 'Joy', 'Sad', 'Neutral']
print('Input text: ',test_text)
# Normalize prediction probabilities
normalized_probabilities = prediction_result / np.sum(prediction_result)

# Convert to percentage format
percentage_probabilities = normalized_probabilities * 100

# Get the predicted class index
predicted_class = np.argmax(prediction_result)

# Print the class with its corresponding percentage probability
for i, percentage in enumerate(percentage_probabilities[0]):
    class_label = class_names[i]
    print(f"{class_label}: {percentage:.5f}%")

# Print the predicted class
predicted_class_label = class_names[predicted_class]
print(f"Predicted Class: {predicted_class_label} ({percentage_probabilities[0][predicted_class]:.5f}%)")

