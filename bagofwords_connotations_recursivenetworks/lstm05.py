# Load LSTM network and generate text
import sys
import numpy as np
from nltk.tokenize import wordpunct_tokenize
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import to_categorical
# load ascii text and covert to lowercase
filename = "wonderland.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()
# create mapping of unique chars to integers
tokenized_text = wordpunct_tokenize(raw_text)
tokens = sorted(list(dict.fromkeys(tokenized_text)))

#print("Tokens: ")
#print(tokens)
tok_to_int = dict((c, i) for i, c in enumerate(tokens))
int_to_tok = dict((i, c) for i, c in enumerate(tokens))
#print("TokensToNumbers: ")
#print(tok_to_int)

# summarize the loaded data
n_tokens = len(tokenized_text)
n_token_vocab = len(tokens)
print("Total Tokens: ", n_tokens)
print("Unique Tokens (Token Vocab): ", n_token_vocab)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_tokens - seq_length, 1):
	seq_in = tokenized_text[i:i + seq_length]
	seq_out = tokenized_text[i + seq_length]
	dataX.append([tok_to_int[tok] for tok in seq_in])
	dataY.append(tok_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)
# reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_token_vocab)
# one hot encode the output variable
y = to_categorical(dataY)
# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
# load the network weights
filename = "../models/bagofwords/big-token-model-10-4.2784.keras"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
# pick a random seed
start = np.random.randint(0, len(dataX)-1)
pattern = dataX[start]
print("Seed:")
print("\"", ' '.join([int_to_tok[value] for value in pattern]), "\"")
# generate tokens
print("Generated text:")
for i in range(100):
	x = np.reshape(pattern, (1, len(pattern), 1))
	x = x / float(n_token_vocab)
	prediction = model.predict(x, verbose=0)
	index = np.argmax(prediction)
	result = int_to_tok[index]
	seq_in = [int_to_tok[value] for value in pattern]
	sys.stdout.write(result+" ")
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
print("\nDone.")
# Seed:
#" “ the queen of hearts , she made some tarts , all on a summer day : the knave of hearts , he stole those tarts , and took them quite away !” “ consider your verdict ,” the king said to the jury . “ not yet , not yet !” the rabbit hastily interrupted . “ there ’ s a great deal to come before that !” “ call the first witness ,” said the king ; and the white rabbit blew three blasts on the trumpet , and called out , “ first witness !” the first "
# Generated text:
# , “ i ’ s , “ the , “ ’ t , said the ,” said the , “ the ’ s , “ the , said ’ t , “ the , said ’ t , “ the , said ’ t , “ the , said ’ t , “ the , said ’ t , “ the , said ’ t , “ the , said ’ t , “ the , said ’ t , “ the , said ’ t , “ the , said the t , “ the , “ ’ t

# Po douczeniu:
# Seed:
# " - bye , feet !” ( for when she looked down at her feet , they seemed to be almost out of sight , they were getting so far off ). “ oh , my poor little feet , i wonder who will put on your shoes and stockings for you now , dears ? i ’ m sure _i_ shan ’ t be able ! i shall be a great deal too far off to trouble myself about you : you must manage the best way you can ;— but i must be kind to them ,” thought alice "
# Generated text:
# , “ i ’ s sure important ’ t , “ the , said ’ s , “ i , “ alice said ’ t t ,” said the hatter , “ i ’ s ,” said the hatter , “ i ’ s ,” said the hatter , “ i ’ s ,” said the hatter , “ i ’ s ,” said the hatter , “ i ’ s ,” said the hatter , “ i ’ s ,” said the hatter , “ i ’ s ,” said the hatter , “ i ’ s ,” said
