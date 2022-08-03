import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

results = pd.read_csv("formula1_2022season_raceResults.csv")

results.columns = [x.split()[0] + "_" + x.split()[1] if len(x.split())>1 else x for x in results.columns]

yarislar = np.arange(1,14)
puanlar = np.arange(0,27)


"""" MERCEDES """

ham = results.Driver == "Lewis Hamilton"
rus = results.Driver == "George Russell"

hamilton = results[ham]
russell = results[rus]




""" FERRARI """

lec = results.Driver == "Charles Leclerc"
sai = results.Driver == "Carlos Sainz"

leclerc = results[lec]
sainz = results[sai]




plt.subplot(2,1,1)

plt.grid(True)
plt.xlabel("Yarışlar")
plt.ylabel("Puan ve Sıralama Turları Sonucu")
plt.title("Charles Leclerc vs Carlos Sainz 2022 Sezonu")
plt.xticks(yarislar)
plt.yticks(puanlar)


plt.plot(yarislar,leclerc.Points,'-o', color = "red" ,label = "LEC Race",linewidth=2)
plt.plot(yarislar,sainz.Points,'-o', color = "blue" ,label = "SAİ Race",linewidth=2)

plt.plot(yarislar,leclerc.Starting_Grid,'b:', color = "red" ,label = "LEC Quali", linewidth=2)
plt.plot(yarislar,sainz.Starting_Grid,'b:', color = "blue" ,label = "SAİ Quali", linewidth=2)
plt.legend()
plt.show()
plt.subplot(2,1,2)

plt.grid(True)
plt.title("Lewis Hamilton vs George Russell 2022 Sezonu")
plt.xticks(yarislar)
plt.yticks(puanlar)
plt.xlabel("Yarışlar")
plt.ylabel("Puan ve Sıralama Turları Sonucu")



plt.xlabel("Yarışlar")
plt.ylabel("Puan ve Sıralama Turları Sonucu")

plt.plot(yarislar,hamilton.Points,'-o', color = "blue" ,label = "HAM Race",linewidth=2)
plt.plot(yarislar,russell.Points,'-o', color = "red" ,label = "RUS Race",linewidth=2)

plt.plot(yarislar,hamilton.Starting_Grid,'b:', color = "blue" ,label = "HAM Quali", linewidth=2)
plt.plot(yarislar,russell.Starting_Grid,'b:', color = "red" ,label = "RUS Quali", linewidth=2)
plt.legend()
plt.show()













