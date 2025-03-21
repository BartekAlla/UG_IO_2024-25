import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import textwrap

# Załaduj treść artykułu z pliku txt
# https://www.nature.com/articles/d41586-024-04216-1
with open("../article.txt", "r", encoding="utf-8") as file:
    text = file.read()

# a) Wyświetlanie oryginalnego tekstu
print("Fragment oryginalnego tekstu:\n", text[:500], "\n...")

# b) Tokenizacja
nltk.download('punkt')
nltk.download('punkt_tab')
tokens = word_tokenize(text)
print("Liczba słów po tokenizacji:", len(tokens))

# c) Usunięcie stop-words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Liczba słów po usunięciu klasycznych angielskich stop-words:", len(filtered_tokens))

# d) Dodanie dodatkowych słów do stop-words (jeśli potrzeba)
additional_stopwords = ['said', 'would', 'also', ',', '.', '"', '“', ':', "'", '?', '‘', '‛', '’', '‘', '’', '_', '-', '´', '`', '„', '”']
stop_words.update(additional_stopwords)
filtered_tokens = [word for word in filtered_tokens if word.lower() not in stop_words]
print("Liczba słów po dodaniu dodatkowych stop-words, w tym znaków:", len(filtered_tokens))

# e) Lematyzacja - uzyto WordNet
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("Liczba słów po lemantyzacji:", len(lemmatized_tokens))

# f) Wektor zliczający słowa i wykres słupkowy
word_counts = Counter(lemmatized_tokens)
most_common_words = word_counts.most_common(10)
print("Most common words:", most_common_words)

# Wykres słupkowy
words, counts = zip(*most_common_words)
wrapped_words = ['\n'.join(textwrap.wrap(word, width=10)) for word in words]
plt.bar(wrapped_words, counts)
plt.xlabel("Słowa")
plt.ylabel("Częstotliwość")
plt.title("Top 10 słów")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# g) Chmura tagów
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_counts)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud")
plt.show()


# Liczba słów po tokenizacji: 1828
# Liczba słów po usunięciu klasycznych angielskich stop-words: 1144
# Liczba słów po dodaniu dodatkowych stop-words, w tym znaków: 927
# [nltk_data]   Package wordnet is already up-to-date!
# Liczba słów po lemantyzacji: 927
