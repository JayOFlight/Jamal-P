#!/usr/bin/env python
import rospy
from serial import Serial
from std_msgs.msg import UInt16
from sensor_msgs.msg import Joy

class roboteq(object):
    def __init__(self):
        self.dev = Serial('/dev/ttyACM0',
                           115200)
        self.rate = rospy.Rate(10)
        self.sub = rospy.Subscriber('joy', Joy, self.cb)
    def cb(self,msg):
        left = (int)(msg.axes[0] * 1000)
        right = (int)(msg.axes[1] * 1000)
        self.dev.write(('!G 1 {}\r\n').format(left))
        self.dev.write(('!G 2 {}\r\n').format(right))
    def close(self):
        self.dev.close()
    def run(self):
        try:
            while not rospy.is_shutdown():
                self.rate.sleep()
                rospy.spin()
        except Exception as e:
            rospy.logerr("Something broke: %s", str(e))
        finally:
            self.close()
if __name__ == '__main__':
    rospy.init_node('roboteq_joy')
    roboteq().run()
