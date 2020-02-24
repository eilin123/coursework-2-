#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy  
#Jointstates package contains the states of our robot's joints etc vel,pos,effect
from sensor_msgs.msg import JointState 
# Header- to publish a message 
from std_msgs.msg import Header


def talker():
# initialise class publisher - instance to publish in the topic; the message between the publisher and subscriber
    
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)

    rospy.init_node('lin_joint_state_publisher')
    rate = rospy.Rate(10) # 10hz

####### Joint 1:
    joint_1 = JointState()# creating an instance
    joint_1.header = Header() # creating a header
    joint_1.header.stamp = rospy.Time.now() # a header file contains the time.stamp which tells you when the message was published to ensure the subscriber takes the most recent message from 						      publisher(talker)

    while not rospy.is_shutdown(): # user input
	####### Joint 1:
	joint_1.name = ['base_link_link_1', 'my_first_link1_link_2','link2_link_3']
	print "User input for joint 1:"
	coordinates = raw_input()
	new_coord = float(coordinates)

	####### Joint 2:
	print "User input for joint 2:"
	coordinates1 = raw_input()
	new_coord1 = float(coordinates1)

	while new_coord1 < -1 or new_coord1 > 1:
		print"Error, beyond joint limit, must be between 1 and -1. Please enter again:" 
		coordinates1 = raw_input()
		new_coord1 = float(coordinates1)

	
	####### Joint 3
	print "User input for joint 3:"
	coordinates2 = raw_input()
	new_coord2 = float(coordinates2)

	while new_coord2 < 0 or new_coord2 > 1:
		print"Error, beyond joint limit, must be between 1 and -1. Please enter again:" 
		coordinates2 = raw_input()
		new_coord2 = float(coordinates2)

	joint_1.position = [new_coord, new_coord1, new_coord2]
	joint_1.header.stamp =rospy.Time.now()
	pub.publish(joint_1)

	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
