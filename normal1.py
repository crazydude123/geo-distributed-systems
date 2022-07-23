
from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap

filename = "results_Utah_Wis_clem_Algo_2.txt"
results = []
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        k = float(a[0])
        results += [k]
print(len(results))


import numpy as np
a = np.percentile(results, 60)
b = np.percentile(results, 80)
c = np.percentile(results, 95)


print("95th percentile: ", c)
print("80th percentile: ", b)
print("60th percentile: ", a)


results60 = []
results80 = []
results95 = []

for i in results:
    if i < a:
        results60 += [i]
    if i < b:
        results80 += [i]
    if i < c:
        results95 += [i]

meanu =  np.mean(results)
print("mean: ", meanu)
results1 = pd.Series(results)
results60 = pd.Series(results60)
results80 = pd.Series(results80)
results95 = pd.Series(results95)

from pylab import *
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Read CSV file using pandas
# KDE plotting using seaborn


titled = ("\n".join(wrap("KDE Plot for 60th, 80th and 95th percentile latencies of GETs with Child_1 in Wisconsin, Child_2 in Utah and parent at Clemson University; algorithm 1 implemented \n", 60)))
plt.title(titled)
#plt.title("Histogram for GETs addressed directly to other children nodes by Child_1")
plt.xlabel("Latency (ms)")
plt.ylabel("Probability Density") 
#sn.kdeplot(data=results1, shade=True, color="black", label="80th percentile")
sn.kdeplot(data=results60, shade=True, color="red", label="60th percentile = 77.550 ms")
sn.kdeplot(data=results80,  shade=True, color="green", label="80th percentile = 77.570 ms")
sn.kdeplot(data=results95,  shade=True, color="blue", label="95th percentile = 77.605 ms")
#plt.legend()
#sn.histplot(data=results1, color="lime", kde=False, alpha=0.4, bins=25, legend=True, label="Mean = 0.322 ms")
#sn.histplot(data=results80, color="green", kde=False, alpha = 0.2, label="80th percentile", bins=100)
#sn.histplot(data=results90, color="blue", kde=False, alpha = 0.2, label="90th percentile", bins=100)

#legend1 = plt.legend(["Child_1 = Utah", "Child_2 = Utah", "Parent = Clemson"], loc="upper left")

#plt.gca().add_artist(legend1)
plt.legend(loc = "upper left")
plt.show()