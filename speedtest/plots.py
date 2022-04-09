import matplotlib.pyplot as plt

def plot(func_name, times):
    mdict_x = {}
    mdict_y = {}

    for i, e in enumerate(times):
        try:
            mdict_x[times[i][1]] += [times[i][0]/ 1000] 
            mdict_y[times[i][1]] += [times[i][2]/ 1000]
        except KeyError:
            mdict_x[times[i][1]] = [times[i][0]/ 1000]
            mdict_y[times[i][1]] = [times[i][2]/ 1000]

    for key in mdict_x:
        plt.plot(mdict_x[key], mdict_y[key], label=key)

    plt.title('Performancevergleich SQL: ' + func_name)
    plt.xlabel('Anzahl an Iterationen in T')
    plt.ylabel('Zeit in s')
    plt.legend()
    plt.show()