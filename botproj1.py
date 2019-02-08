#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
PI = 3.1415926535897
from time import sleep




	


def rad(deg):
	return deg*2*PI/360


def moveturtle():

	total_distance = 0

	
	print("Let's move your robot")

	

	angs = input("Input speed (degrees/sec):")
	angs = angs*2*PI/360
	radius = 0.5
	
	linearspeed = angs*radius

    
	while not rospy.is_shutdown():
        
        
        
		vel_msg.linear.x = linearspeed
		vel_msg.angular.z = angs

		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		angle = rad(360)

#  circle
		velocity_publisher.publish(vel_msg)
		

		while True:
			t1 = rospy.Time.now().to_sec()
			current_angle = angs*(t1-t0)
			if abs(current_angle)>angle:
				total_distance+=linearspeed*(t1-t0)
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				vel_msg.linear.x = 0

				velocity_publisher.publish(vel_msg)
				
				break

		
		  
		vel_msg.angular.z=angs
		velocity_publisher.publish(vel_msg)

		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		angle = rad(90)

		while True:
			t1 = rospy.Time.now().to_sec()
			current_angle = angs*(t1-t0)
			if abs(current_angle)>angle:
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				vel_msg.linear.x = 0

				velocity_publisher.publish(vel_msg)
				

				break

		sleep(1)

		vel_msg.linear.x=linearspeed
		velocity_publisher.publish(vel_msg)

		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		distance = 2*radius

		while True:
			t1 = rospy.Time.now().to_sec()
			current_distance = linearspeed*(t1-t0)
			if current_distance>distance:
				total_distance+=linearspeed*(t1-t0)
				
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				vel_msg.linear.x = 0

				velocity_publisher.publish(vel_msg)
				break
		  

		#  opposite circle


		vel_msg.angular.z=-angs
		velocity_publisher.publish(vel_msg)

		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		angle = rad(90)
		  
		while True:
			t1 = rospy.Time.now().to_sec()
			current_angle = angs*(t1-t0)
			if abs(current_angle)>angle:
				
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				vel_msg.linear.x = 0

				velocity_publisher.publish(vel_msg)
				break


		vel_msg.linear.x = linearspeed
		vel_msg.angular.z = -angs

		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		angle = rad(360)

		velocity_publisher.publish(vel_msg)
		rospy.loginfo('MSG published')

		while True:
			t1 = rospy.Time.now().to_sec()
			current_angle = angs*(t1-t0)
			if abs(current_angle)>angle:
				total_distance+=linearspeed*(t1-t0)
				
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				vel_msg.linear.x = 0

				velocity_publisher.publish(vel_msg)
				break


		#  back to origin

		vel_msg.angular.z=-angs
		velocity_publisher.publish(vel_msg)

		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		angle = rad(90)

		while True:
			t1 = rospy.Time.now().to_sec()
			current_angle = abs(angs)*(t1-t0)
			if abs(current_angle)>angle:
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				vel_msg.linear.x = 0

				velocity_publisher.publish(vel_msg)
				break

		sleep(1)

		vel_msg.linear.x=linearspeed
		velocity_publisher.publish(vel_msg)

		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		distance = 2*radius

		while True:
			t1 = rospy.Time.now().to_sec()
			current_distance = linearspeed*(t1-t0)
			if current_distance>distance:
				total_distance+=linearspeed*(t1-t0)
			    vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				vel_msg.linear.x = 0

				velocity_publisher.publish(vel_msg)
				break

		  rospy.loginfo('actual distance : '+str(total_distance))
		  calc_distance = 2*(2*PI*radius)+2*(2*radius)
		  rospy.loginfo('calculated Distance : '+str(calc_distance))
		  rospy.loginfo('error : '+str(total_distance-calc_distance))
		  break




if __name__ == '__main__':
    try:
    	# node

		rospy.init_node('robot1', anonymous=True)
		velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
		
		vel_msg = Twist()
        
		moveturtle()

    except rospy.ROSInterruptException: pass