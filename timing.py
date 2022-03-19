import time

def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        time_clean = int(f"{(time2-time1)*1000.0:.0f}")
        print(f'--- TIME: {f.__name__} function took {time_clean} ms')
        return ret, time_clean
    return wrap