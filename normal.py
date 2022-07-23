# read numbers from results.txt and store it in results
filename = "results.txt"
results = []
with open(filename) as file:
    for line in file:
        a = line.strip("\n").split(" ")
        k = float(a[0])*1000
        results += [k]
print(len(results))


import numpy as np
a = np.percentile(results, 60)
b = np.percentile(results, 80)
c = np.percentile(results, 90)
d = np.percentile(results, 95)

results60 = []
results80 = []
results90 = []
results95 = []

for i in results:
    if i < a:
        results60 += [i]
    elif i < b:
        results80 += [i]
    elif i < c:
        results90 += [i]
    elif i < d:
        results95 += [i]

print(results60)
import matplotlib.pyplot as plt
import numpy as np
'''
np.random.seed(42)


plt.hist(results, density=True, bins=1000)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data')
plt.show()
'''
import seaborn as sns
import pandas as pd
x1 = results
x2 = results
x3 = results
# change results to a pandas series
results1 = pd.Series(results)
results60 = pd.Series(results60)
results80 = pd.Series(results80)
results90 = pd.Series(results90)
results95 = pd.Series(results95)
#kwargs = dict(alpha=0.5, bins=100, density=True, histtype='step', stacked=True)
kwargs = dict(alpha=0.7, bins=100, density =True)
plt.hist(results1, **kwargs, label='All', color='y')

plt.hist(results60, **kwargs, color='g', label='60th percentile')

plt.hist(results90, **kwargs, color='r', label='90th percentile')

plt.hist(results95, **kwargs, color='b', label='95th percentile')

plt.gca().set(title='Frequency Histogram of Diamond Depths', ylabel='Probability')
plt.xlim(0, 1)
plt.legend()
plt.show()