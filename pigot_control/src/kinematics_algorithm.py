#coding=utf-8
import numpy as np
import math
import tarj_data as td

l1 = 0.15  #最初0.15
l2 = 0.35
l3 = 0.35
radio = 40
rate = 2


def forward_gait():
    gait_data = np.zeros((radio, 12))
    x_line, y_line, z_line = gait_line()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = z_line[t]    #这里是和后退有差别的地方
            zb = z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = z_line[t]
            zb = z_line[t - 20]
        
        #仔细看,每一行的前3个数据和后3个数据相同, 次前3个和后次3个数据相同, 这意味这是对角步态!
        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(xf, yf, zf)
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(xb, yb, zb) 
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
        
    return rate, gait_data

def forward_gait2():
    gait_data = np.zeros((radio, 12))
    x_line, y_line, z_line = gait_line2()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = z_line[t]    #这里是和后退有差别的地方
            zb = z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = z_line[t]
            zb = z_line[t - 20]
        
        #仔细看,每一行的前3个数据和后3个数据相同, 次前3个和后次3个数据相同, 这意味这是对角步态!
        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(xf, yf, zf)
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(xb, yb, zb) 
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
        
    return rate, gait_data



def backward_gait():
    gait_data = np.zeros((radio, 12))
    x_line, y_line, z_line = gait_line()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = -z_line[t]
            zb = -z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = -z_line[t]
            zb = -z_line[t - 20]

        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(xf, yf, zf)
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
    return rate, gait_data

def turnleft_gait():
    gait_data = np.zeros((radio, 12))
    data = turn_line(1)
    for t in range(gait_data.shape[0]):
        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(data[0, t], data[4, t], data[8, t])
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(data[1, t], data[5, t], data[9, t])
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(data[2, t], data[6, t], data[10, t])
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[3, t], data[7, t], data[11, t])
    return rate, gait_data

def turnright_gait():
    gait_data = np.zeros((radio, 12))
    data = turn_line(-1)
    for t in range(gait_data.shape[0]):
        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(data[0, t], data[4, t], data[8, t])
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(data[1, t], data[5, t], data[9, t])
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(data[2, t], data[6, t], data[10, t])
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[3, t], data[7, t], data[11, t])
    return rate, gait_data

def slantleft_gait():
    gait_data = np.zeros((radio, 12))
    data = td.slantleft_gait(1)
    for t in range(gait_data.shape[0]):
        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(data[0, t], data[2, t], data[4, t])
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(data[1, t], data[3, t], data[5, t])
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(data[1, t], data[3, t], data[5, t])
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[0, t], data[2, t], data[4, t])
    return rate, gait_data

def slantright_gait():
    gait_data = np.zeros((radio, 12))
    data = td.slantleft_gait(-1)
    for t in range(gait_data.shape[0]):
        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(data[0, t], data[2, t], data[4, t])
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(data[1, t], data[3, t], data[5, t])
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(data[1, t], data[3, t], data[5, t])
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[0, t], data[2, t], data[4, t])
    return rate, gait_data


def jump_gait():

    return 

def keep_gait():
    gait_data = np.zeros((radio, 12))
    rate = 2
    x_line, y_line, z_line = keep_line()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            #f x,y,z是一组脚 b x,y,z是一组角
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = z_line[t]
            zb = z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = z_line[t]
            zb = z_line[t - 20]

        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(xf, yf, zf)
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
    return rate, gait_data

def clam_gait():
    gait_data = np.zeros((radio, 12))
    rate = 2
    x_line, y_line, z_line = keep_line()
    for t in range(gait_data.shape[0]):
        if (t < 20):
            xf = 0.4
            xb = 0
            yf = 0.15
            yb = 0.15
            zf = 0.1
            zb = 0.1
        else:
            xf = 0.4
            xb = 0
            yf = 0.15
            yb = 0.15
            zf = 0.1
            zb = 0.1

        gait_data[t, 0], gait_data[t, 1 ], gait_data[t, 2 ] = leg_ikine(xf, yf, zf)
        gait_data[t, 3], gait_data[t, 4 ], gait_data[t, 5 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 6], gait_data[t, 7 ], gait_data[t, 8 ] = leg_ikine(xb, yb, zb)
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
    return rate, gait_data #gait_data是个40行12列的数组
    

#这个函数很关键
def leg_ikine(x, y, z):  #我估计这是解逆运动学方程 通过目标位置或者叫姿势 解出关节角 通俗讲就是关节要转的角度
    theta1 = math.atan2(y, x) + math.atan2(l1, -(x**2 + y**2 - l1**2)**0.5)
    c1 = math.cos(theta1)    
    s1 = math.sin(theta1) 
    c3 = (x**2 + y**2 + z**2 - l1**2 - l2**2 - l3**2) / (2 * l2 * l3)
    s3 = (1 - c3**2)**0.5
    theta3 = math.atan2(s3, c3)
    s2p = (l3 * s3) / ((y * s1 + x * c1)**2 + z**2)**0.5
    c2p = (1 - s2p**2)**0.5
    theta2p = -math.atan2(s2p, c2p)
    thetap = -math.atan2(z, -(y * s1 + x * c1))
    theta2 = theta2p - thetap
    return theta1 - math.pi, theta2, theta3


def gait_line():
    data = td.forward_gait()
    x_line = data[0, :]
    y_line = data[1, :]
    z_line = data[2, :]
    return x_line, y_line, z_line

def gait_line2():
    data = td.forward_gait2()
    x_line = data[0, :]
    y_line = data[1, :]
    z_line = data[2, :]
    return x_line, y_line, z_line

def keep_line():
    data = td.keep_gait()
    x_line = data[0, :] #切边 第一行所有元素
    y_line = data[1, :]
    z_line = data[2, :]
    return x_line, y_line, z_line

def turn_line(direction):
    data = td.turn_gait(direction)
    return data

def jump_line():
    xf_line = np.zeros((20))

    return


