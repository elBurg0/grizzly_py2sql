import matplotlib.pyplot as plt

def plot(func_name, times):
    # add a dictonary for the x (number of iterations) and y (duration of iteration) values of each testcase
    # Fomrat: {'PL/PY - Local Postgres DB': [0.02, 0.04], 'PL/SQL - Local Pluggable Oracle DB': [0.02, 0.04]}
    mdict_x = {}
    mdict_y = {}

    # A time_set contains [number of iterations, name of testcase, duration in ms]
    for time_set in times:
        try:
            mdict_x[time_set[1]] += [time_set[0]/ 1000] 
            mdict_y[time_set[1]] += [time_set[2]/ 1000]
        except KeyError:
            mdict_x[time_set[1]] = [time_set[0]/ 1000]
            mdict_y[time_set[1]] = [time_set[2]/ 1000]

    for key in mdict_x:
        plt.plot(mdict_x[key], mdict_y[key], label=key)

    plt.title('Performancevergleich SQL: ' + func_name)
    plt.xlabel('Anzahl an Iterationen in T')
    plt.ylabel('Zeit in s')
    plt.legend()
    plt.show()