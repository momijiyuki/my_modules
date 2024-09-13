from functools import wraps
import time
# https://qiita.com/nshinya/items/b6746a0c07e9e20389e8

def paramdecorator(func):
    def param(*args, **kwargs):
        def wrapper(f):
            return func(f, *args, **kwargs)
        return wrapper
    return param

@paramdecorator
def timecounter(func, dump=False):
    """time count wrapper

    Parameters
    ----------
    func : _type_
        _description_
    dump : bool, optional
        return , by default False
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("--start--")
        starttime = time.time()
        ans = func(*args, **kwargs)
        print("---end---")
        endtime = time.time()

        print(f"経過時間：{endtime-starttime}")
        if dump:
            return ans, endtime-starttime
        return ans
    return wrapper

@timecounter(dump=True)
def __anyfc(num):
    """_summary_
    本体
    Parameters
    ----------
    num : _type_
        _description_

    Returns
    -------
    int
        _description_
    """
    # num = 0
    for i in range(2000):
        for j in range(2000):
            num += i*j
    return num


if __name__=="__main__":
    ans, times = __anyfc(1)
    # print(anyfc.__doc__)
    print(ans, times)
