from sklearn.cluster import AffinityPropagation
from sklearn.manifold import TSNE
from sklearn.metrics import pairwise
from nba_py import player

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# preprocess data
player_list = player.PlayerList(season='2016-17').info()
id_name = player_list[[0,2]]
id_name = id_name.rename(columns={'PERSON_ID': 'PLAYER_ID'})

df = pd.read_pickle('16-17allplayers_totals')
df = df[df['MIN']>15]
df = df[df['GP']>30]
id_list = df[[0]]
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 7]], axis=1)
print(df)

# use affinity propagation to cluster data
data = df.as_matrix()
similarity = pairwise.cosine_similarity(data)
X = AffinityPropagation().fit(similarity)
labels = X.labels_
#print(len(labels))

# output result to csv file
id_list['label'] = pd.Series(labels, index=id_list.index)
name_labels = pd.merge(id_list, id_name, on='PLAYER_ID')
sort = name_labels.sort_values('label', ascending=False)
sort.to_csv('cluter_result.csv')

# embed cluter result into 2D with t-SNE and plot result
embedding = TSNE(perplexity=17, learning_rate=300).fit_transform(data)
core_samples_mask = np.zeros_like(labels, dtype=bool)
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for k, col in zip(unique_labels, colors):
    class_member_mask = (labels == k)
    xy = embedding[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', ls='-', label=k, markerfacecolor=col,
             markeredgecolor='k', markersize=6)

plt.legend()
plt.title('Visualization of player clustering result.')
plt.show()