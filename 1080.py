import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'kategori': ['A', 'B', 'C', 'D', 'E'],
        'nilai': [20, 35, 30, 25, 40],
        'ststus': ['pelajar', 'mahasiswa', 'bekerja', 'wirausaha', 'beban negera']}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 6)) #atur ukuran gambar
'''sns.barplot(x='kategori', y='nilai', data=data)
plt.title('Grafik Batang')
plt.xlabel('Kategori')
plt.ylabel('Nilai')'''
plt.pie(df['nilai'], labels=df['kategori'],autopct='%1.1f%%')
plt.show()
