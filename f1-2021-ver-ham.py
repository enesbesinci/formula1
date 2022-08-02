import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veri = pd.read_csv("formula1_2021season_raceResults.csv")


yarislar = np.arange(1,23)
puanlar = np.arange(0,27)

tracks = veri.Track.unique()

veri.columns = [x.split()[0] + "_" + x.split()[1] if len(x.split())>1 else x for x in veri.columns]

a = veri.Driver == "Max Verstappen"
b = veri.Starting_Grid == 1
c = veri["Position"]

verquali = veri[a]
verrace = veri[a & c]

d = veri.Driver == "Lewis Hamilton"
e = veri["Position"]


hamquali = veri[d]
hamrace = veri[d & e]


plt.plot(yarislar,verquali.Points, '-o', color = "orange" ,label = "Verstappen Puan",linewidth=2)
plt.plot(yarislar,verrace.Starting_Grid, 'r--',  color = "orange", label = "Verstappen Sıralama",linewidth=2)

plt.plot(yarislar,hamquali.Points, '-o', color = "blue", label = "Hamilton Puan",linewidth=2)
plt.plot(yarislar,hamrace.Starting_Grid, 'r--', color = "blue", label = "Hamilton Sıralama",linewidth=2)

plt.text(x=14,y=0, s="Monza")
plt.text(x=6,y=0, s="Azerbaycan")


plt.legend(loc = 'upper left')
plt.xticks(yarislar)
plt.yticks(puanlar)
plt.xlabel("Yarışlar")
plt.ylabel("Puan ve Sıralama Turları Sonucu")
plt.title("2021 Max Verstappen vs Lewis Hamilton")
plt.grid(True)
plt.show()

# plt.subplot(2,1,1)
# plt.plot(yarislar,verquali.Points, '-o', color = "orange" ,label = "Verstappen Puan",linewidth=2)
# plt.subplot(2,1,2)
# plt.plot(yarislar,hamquali.Points, '-o', color = "blue", label = "Hamilton Puan",linewidth=2)
# plt.show()






    








 
 