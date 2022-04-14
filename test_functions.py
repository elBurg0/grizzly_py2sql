import grizzly

def udf1(a: int) -> int:
    return a + 3

def udf2(a: int) -> str:
    i:float = a + 2.31
    return "g_" + i

def udf3(a: int) -> int:
    i: int = 22
    m: int = a + i
    for i in range(1, a):
        if i + a > 20:
            return 20 * a
        else:
            return 0 
    return m

def udf4(a: int) -> str:
    c = "g_"
    n = 2.1
    f = 0
    g_df1 = grizzly.read_table("speedtest")
    #g_df1.generateQuery()
    for row in g_df1:
        f = f + a + row.test_id
    t: float = f + n
    return c + t

def udf5(a: int) -> str:
    f = 0
    # Kommentar
    g_df1 = grizzly.read_table("speedtest")
    g_df1 = g_df1[g_df1.test_id == a] 


    for row in g_df1:
        if row.test_id >= a -2:
            if row.test_id <= a +2:
                if row.test_number > 40:
                    f = f + row.test_number
    return f

def udf6(a: int) -> str:
    f = 0
    g_df1 = grizzly.read_table("speedtest")
    g_df1 = g_df1[g_df1.test_float > 10] 

    for tuple in g_df1:
        if tuple.test_float > tuple.test_number:
            continue
        elif tuple.test_id > a:
            break
        if tuple.test_number > 20:
            f = f + tuple.test_number
    return f
