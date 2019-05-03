#!/usr/bin/env python
<<<<<<< HEAD
#coding=utf-8
=======
# -*- coding: utf-8 -*
>>>>>>> 3bb435b0de6d0dba72d20d871a34d0bc29441e5c
 
import  os
import  sys
import  tty, termios
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float64

 
# 全局变量
pub_action = rospy.Publisher('action_command', String, queue_size=10)
 
def keyboardLoop():
    #初始化
    rospy.init_node('smartcar_teleop')
    rate = rospy.Rate(1)
  
    #显示提示信息
    print("Reading from keyboard")
    print("Use WASD keys to control the robot")
<<<<<<< HEAD
    #print("Press Caps to move faster")
    print("Press p to quit")
=======
>>>>>>> 3bb435b0de6d0dba72d20d871a34d0bc29441e5c
 
    #读取按键循环
    while not rospy.is_shutdown():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
		#不产生回显效果
        old_settings[3] = old_settings[3] & ~termios.ICANON & ~termios.ECHO
        try :
            tty.setraw( fd )
            ch = sys.stdin.read( 1 )
        finally :
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
 
        if (ch == 'p'):
            exit()
        else:
            rospy.set_param('pigot/action_state_param', ch)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        keyboardLoop()
    except rospy.ROSInterruptException:
        pass