#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    while not rospy.is_shutdown():
    	name=input()
    	rospy.loginfo(name)
    	pub.publish(name)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
