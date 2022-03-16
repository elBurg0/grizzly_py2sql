import time

def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print(f'--- TIME: {f.__name__} function took {(time2-time1)*1000.0:.0f} ms')
        return ret
    return wrap