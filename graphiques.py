import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data = pd.read_csv("out/conc.csv")  # Remplace "data.csv" par le nom de ton fichier
#data = pd.read_csv("out/post.csv")
data = pd.read_csv("out/fanout.csv")


stats = data.groupby('PARAM')['AVG_TIME'].agg(['mean', 'std']).reset_index()

plt.figure(figsize=(8,5))
plt.bar(stats['PARAM'].astype(str), stats['mean'], yerr=stats['std'], capsize=5, color='cornflowerblue')
plt.xlabel("Nombre d'utilisateurs concurrents")
#plt.xlabel("Nombre de post par user")
#plt.xlabel("Nombre de followee")
#plt.ylabel("Temps moyen par requête (s)")
#plt.title("Temps moyen par requête selon le nombre de posts")
plt.title("Temps moyen par requête selon le nombre de followee")
#plt.title("Temps moyen par requête timeline")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()