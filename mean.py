import csv
import statistics as stats
f=open("c-104 data.csv")
csvo = csv.reader(f)
data = list(csvo)
data.pop(0)
sumofcases= 0
cases = []
for i in range(len(data)):
    collumn = float(data[i][1])
    sumofcases+=collumn
    cases.append(collumn)
mean = sumofcases/len(cases)
print(mean)
median = stats.median(cases)
print(median)
mode = stats.mode(cases)
print(mode)

