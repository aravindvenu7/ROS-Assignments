#!user/bin/env python
import roslib
from geometry_msgs.msg import Twist
import rospy
from sensor_msgs.msg import PointCloud2
import point_cloud2
from math import copysign

def slavebot():
   
       while not rospy.is_shutdown():
        
        # Dimensions of box in which LiDAR will search for the master turtlebot
        minx = rospy.get_param("~minx", -1)
        maxx = rospy.get_param("~maxx", 1)
        miny = rospy.get_param("~miny", -0.3)
        maxy = rospy.get_param("~maxy", 0.3)
        maxz = rospy.get_param("~maxz", 0.4)
        
        # distance of 1m as specified in the project statement
        goal_dist = rospy.get_param("~goal_dist", 1)
        
        # How far away from the goal distance (in meters) before the robot reacts
        z_limit = rospy.get_param("~z_limit", 0.05)
        
        # max error should be 0.05 m
        x_limit = rospy.get_param("~x_limit", 0.05)
        z_weight = rospy.get_param("~z_weight", 1.0)
		x_weight = rospy.get_param("~x_weight", 2.5)
        max_angularspeed = rospy.get_param("~max_angularspeed", 2.0)
        min_angularspeed = rospy.get_param("~min_angularspeed", 0.0)
        max_linearspeed = rospy.get_param("~max_linearspeed", 0.3)
        min_linearspeed = rospy.get_param("~min_linearspeed", 0.1)
        cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist)

        rospy.Subscriber('point_cloud', PointCloud2, movement)
        rospy.wait_for_message('point_cloud', PointCloud2)
        
def movement(self, msg):
       
        n=0
		x=0
		y=0
		z=0
		
        
        # Reading LiDAR points
        for point in point_cloud2.read_points(msg, skip_nans=True):
            pt_x = point[0]
            pt_y = point[1]
            pt_z = point[2]
            if -pt_y > min_y and -pt_y < max_y and  pt_x < max_x and pt_x > min_x and pt_z < max_z:
                x += pt_x
                y += pt_y
                z += pt_z
                n += 1
        move_cmd = Twist()
        if n:    
            x /= n 
            y /= n 
            z /= n
            if (abs(z - goal_z) > z_threshold) or (abs(x) > x_threshold):     
                linear_speed = (z - goal_z) * z_scale
                angular_speed = -x * x_scale
                 linear_speed = copysign(max(min_linear_speed, 
                                            min(max_linear_speed, abs(linear_speed))), linear_speed)
                angular_speed = copysign(max(self.min_angular_speed, 
                                             min(self.max_angular_speed, abs(angular_speed))), angular_speed)
    
                move_cmd.linear.x = linear_speed
                move_cmd.angular.z = angular_speed
        self.cmd_vel_pub.publish(move_cmd)

        
      
		
                   
if __name__ == '__main__':
    try:
	    rospy.init_node("slavebot")
        slavebot()
        
    except rospy.ROSInterruptException: pass 
        

