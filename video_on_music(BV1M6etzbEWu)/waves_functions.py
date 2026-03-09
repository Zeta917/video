from manim import *

def swave(x,t,n:int = 1,resistance:bool = True,basic_A:float = 2,basic_f:float = 25):
    if n%2 == 0:
        if resistance:
            if t == 0:
                return 0
            if t > 0:
                return basic_A*(np.exp(-1*t)-np.exp(-3))*np.sin(basic_f*n*t)*np.sin(9*n*PI*x/128)
        else:
            if t == 0:
                return 0
            if t > 0:
                return basic_A*np.sin(basic_f*n*t)*np.sin(9*n*PI*x/128)
    if n%2 != 0:
        if resistance:
            if t == 0:
                return 0
            if t > 0:
                return basic_A*(np.exp(-1*t)-np.exp(-3))*np.sin(basic_f*n*t)*np.cos(9*n*PI*x/128)
        else:
            if t == 0:
                return 0
            if t > 0:
                return basic_A*np.sin(basic_f*n*t)*np.cos(9*n*PI*x/128)
        
def mixed_swave(x,t,n:int = 6,resistance:bool = True,basic_A:float = 2,basic_f:float = 25):
    w = 0
    for i in range(1,n+1):
        w += swave(x,t,i,resistance,basic_A/n,basic_f)
    return w

def wave(x,t,dir:int = 0,A:float = 2,f:float = 1,phi:float = 0,u:float = 1):
    if dir == 0:
        s = -64/9
        if x-s > t*u:
            return 0 
        if x-s <= t*u:
            return A*np.sin(2*PI*f*(t - (x-s)/u)+phi)
    if dir == 1:
        s = 64/9
        if s-x > t*u:
            return 0 
        if s-x <= t*u:
            return A*np.sin(2*PI*f*(t - (s-x)/u)+phi)

def wave_packet(x,t,dir:int = 0,A:float = 2,f:float = 1,phi:float = 0,u:float = 2):
    if dir == 0:
        if t < 0:
            return 0
        else:
            s = -64/9
            if x-s > t*u or x-s < t*u-u/(2*f):
                return 0 
            if t*u-u/(2*f) <= x-s <= t*u:
                return A*np.sin(2*PI*f*(t - (x-s)/u)+phi)
    if dir == 1:
        if t < 0:
            return 0
        else:
            s = 64/9
            if s-x > t*u or s-x < t*u-u/(2*f):
                return 0 
            if t*u-u/(2*f) <= s-x <= t*u:
                return A*np.sin(2*PI*f*(t - (s-x)/u)+phi)

def wave_graph(n: float,A: float = 0.3,color: ManimColor = WHITE):
    return FunctionGraph(lambda x:A*np.sin(PI*n*x/3),x_range = [0,3],stroke_color = color)