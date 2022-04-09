    c = "g_"
    n = 2.1
    f = 0
    g_df1 = grizzly.read_table("speedtest")
    g_df1.generateQuery()
    for row in g_df1:
        if row.test_id >= a -2:
            if row.test_id <= a +2:
                f = f + row.test_id
                

        
    t: float = f + n
    return f