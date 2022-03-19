from example import compare_sql
import config
import matplotlib.pyplot as plt
import psycopg2
import cx_Oracle

times = []
test_iterations2 = [10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]
test_iterations = [5, 10, 100, 1000, 10000, 50000, 100000]

if __name__ == "__main__": 
    for f in range(1, 10000000):
        if f % 250000 == 0:
            test_iterations.append(f)

    print(test_iterations)

    for i,_ in enumerate(test_iterations):
        times += compare_sql(i, test_iterations)
        print("\n")

mdict_x = {}
mdict_y = {}

for i, e in enumerate(times):
    try:
        mdict_x[times[i][1]] += [times[i][0]/ 1000000] 
        mdict_y[times[i][1]] += [times[i][2]/ 1000]
    except KeyError:
        mdict_x[times[i][1]] = [times[i][0]/ 1000000]
        mdict_y[times[i][1]] = [times[i][2]/ 1000]

for key in mdict_x:
    plt.plot(mdict_x[key], mdict_y[key], label=key)

plt.title('Performancevergleich SQL')
plt.xlabel('Anzahl an Iterationen in M')
plt.ylabel('Zeit in s')
plt.legend()
plt.show()