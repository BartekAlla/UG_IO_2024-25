from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

# Original
df_original = df[['sepal length (cm)', 'sepal width (cm)', 'species']]
stats_original = df[['sepal length (cm)', 'sepal width (cm)']].agg(['min', 'max', 'mean', 'std'])
# Min-max
scaler_minmax = MinMaxScaler()
df_minmax = pd.DataFrame(scaler_minmax.fit_transform(df[['sepal length (cm)', 'sepal width (cm)']]), columns=['sepal length (cm)', 'sepal width (cm)'])
df_minmax['species'] = df['species']
stats_minmax = df_minmax[['sepal length (cm)', 'sepal width (cm)']].agg(['min', 'max', 'mean', 'std'])

# Z-score
scaler_zscore = StandardScaler()
df_zscore = pd.DataFrame(scaler_zscore.fit_transform(df[['sepal length (cm)', 'sepal width (cm)']]), columns=['sepal length (cm)', 'sepal width (cm)'])
df_zscore['species'] = df['species']
stats_zscore = df_zscore[['sepal length (cm)', 'sepal width (cm)']].agg(['min', 'max', 'mean', 'std'])


colors = ['blue', 'orange', 'green']
labels = iris.target_names

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

for species in df_original['species'].unique():
    axs[0].scatter(df_original[df_original['species'] == species]['sepal length (cm)'],
                   df_original[df_original['species'] == species]['sepal width (cm)'],
                   color=colors[species], label=labels[species])
axs[0].set_title('Original Dataset')
axs[0].set_xlabel('Sepal length (cm)')
axs[0].set_ylabel('Sepal width (cm)')
axs[0].legend()

for species in df_minmax['species'].unique():
    axs[1].scatter(df_minmax[df_minmax['species'] == species]['sepal length (cm)'],
                   df_minmax[df_minmax['species'] == species]['sepal width (cm)'],
                   color=colors[species], label=labels[species])
axs[1].set_title('Min-Max Normalised Dataset')
axs[1].set_xlabel('Sepal length (cm)')
axs[1].set_ylabel('Sepal width (cm)')
axs[1].legend()

for species in df_zscore['species'].unique():
    axs[2].scatter(df_zscore[df_zscore['species'] == species]['sepal length (cm)'],
                   df_zscore[df_zscore['species'] == species]['sepal width (cm)'],
                   color=colors[species], label=labels[species])
axs[2].set_title('Z-Score Scaled Dataset')
axs[2].set_xlabel('Sepal length (cm)')
axs[2].set_ylabel('Sepal width (cm)')
axs[2].legend()

plt.tight_layout()
plt.show()
print("Original data:\n", stats_original)
print("\nMin-Max normalization:\n", stats_minmax)
print("\nZ-Score scaling:\n", stats_zscore)
# Oryginalne dane daja rzeczywiste wartości, co pokazuje pełny obraz rozkładu.
# Min-Max podaje dane dla wszystkich gatunków w tej samej skali co ułatwia interpretacje.
# Z-Score ułatwia porównanie cech w modelach opartych na statystyce.
# Na podstawie oryginalnych danych nie jesteśmy w stanie wyciągnąc bez głębszej analizy wniosków.
# Z sredniej dla min-max można wywnioskować, że dla przedziału [0, 1] wszystkie kwiaty maja wartość średnia - typową dla gatunku.
# Odchylenie standardowe dla min-max jest mniejsze, niż dla oryginalnych danych przez co różnice pomiędzy osobnikami są mniej wyraźne.
# w z-score wartości minimum ujemne wskazują, że niektóre osobniki są znacznie poniżej średniej. To samo dla max, ale powyżej średniej.
