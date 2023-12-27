#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
# init moveit command
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
# init robot command
robot = moveit_commander.RobotCommander()
# init planningSenceInterface
scene = moveit_commander.PlanningSceneInterface()

group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)

# Create DisplayTrajectory
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)
#
#planning_frame = move_group.get_planning_frame()
#print "============ Planning frame: %s" % planning_frame
#
#eef_link = move_group.get_end_effector_link()
#print "============ End effector link: %s" % eef_link
#
#group_names = robot.get_group_names()
#print "============ Available Planning Groups:", robot.get_group_names()
#
#print "============ Printing robot state"
#print robot.get_current_state()
#print ""
# we can get values from the group and adject some of the values
#joint_goal = move_group.get_current_joint_values()
#joint_goal[0] = 0
#joint_goal[1] = -pi/4
#joint_goal[2] = 0
#joint_goal[3] = -pi/2
#joint_goal[4] = 0
#joint_goal[5] = pi/3

#move_group.go(joint_goal, wait=True)
#move_group.stop()
x = -0.137242990199
y = 0.266800247714
z = 0.0803476590822

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.w = 1.0
pose_goal.position.x = x
pose_goal.position.y = y
pose_goal.position.z = z

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)
# Calling `stop()` ensures that there is no residual movement
move_group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
move_group.clear_pose_targets()



#box_pose = geometry_msgs.msg.PoseStamped()
#box_pose.header.frame_id = "base_link"
#box_pose.pose.orientation.w = 1.0
#box_pose.pose.position.z = 0.07 # slightly above the end effector
#box_name = "box"
#scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))
