from datetime import datetime
import time


# Part 1
def clock(n):
    """
    parameter
    ---------
    n : int
        any integer
     
    returns
    -------
    time in the form of (HH:MM:SS) which run for n seconds
    """
    # Your code here
    Time_ = n
    while Time_ >= 0:
        currenttime = datetime.now().strftime('%H:%M:%S')
        time.sleep(1)
        print(currenttime,end='\r')
        Time_ = Time_ - 1
    

# Part 2
def lcm(a, b):
    """
    parameter
    ---------
    a : int
        any integer
    b : int
        any integer

    returns
    -------
    lcm of a and b
    """
    a_original = a
    b_original = b
    # Your code here
    while a != b:
        if a < b:
            a += a_original
        elif b < a:
            b += b_original   
    if a == b:
        return a

# Part 3
def gcf(a, b):
    # Your code here
    """
    Parameter
    ---------
    a : int
        any integer
    b : int
        any integer

    returns
    -------
    gcf of a and b
    """
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

