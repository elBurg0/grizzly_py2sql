c = "g_"
n = 2.1
f = 0
g_df1 = grizzly.read_table("speedtest")
g_df1[g_df1["test_number"] > 20]
for row in g_df1:
    if row.test_id >= a -2:
        if row.test_id <= a +2:
            if row.test_number > 40:
                f = f + row.test_number

return f