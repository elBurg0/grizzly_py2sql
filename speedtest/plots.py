from main import compare_sql
import matplotlib.pyplot as plt
import grizzly

def myfunc3(a: int) -> str:
    c = "g_"
    n = 2.1
    f = 0

    g_df1 = grizzly.read_table("speedtest")
    g_df1.generateQuery()
    for row in g_df1:
        f = f + a + row.test_id
    
    t: float = f + n
    return c + t

def myfunc2(a: int) -> str:
    n: float = 22.3
    i: int = 2
    f: str = "hello"
    return a + i

def plot(func, times):
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

    plt.title('Performancevergleich SQL: ' + func.__name__)
    plt.xlabel('Anzahl an Iterationen in T')
    plt.ylabel('Zeit in s')
    plt.legend()
    plt.show()

if __name__ == "__main__": 
    func = myfunc2
    times = []
    test_iterations2 = [10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]
    test_iterations = []

    for f in range(1, 200):
        if f % 20 == 0:
            test_iterations.append(f)

    print(test_iterations)

    try:
        for i,_ in enumerate(test_iterations):
            times += compare_sql(i, test_iterations, func)
            print("\n")
    except KeyboardInterrupt as e:
        print(e)
    
    plot(func, times)