// my_moveit_cpp_interface.cpp
#include <ros/ros.h>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_interface/move_group_interface.h>


int main(int argc, char** argv) {
    ros::init(argc, argv, "my_moveit_cpp_interface");
    ros::NodeHandle node_handle;
    //取得有關手臂的資訊
    ros::AsyncSpinner spinner(1);
    spinner.start();
    // Set up MoveIt
    static const std::string PLANNING_GROUP = "small_arm";

    // Your MoveIt C++ code here
    moveit::planning_interface::MoveGroupInterface move_group_interface(PLANNING_GROUP);
    moveit::planning_interface::PlanningSceneInterface planning_scene_interface; //可新增移除物件

    const moveit::core::JointModelGroup* joint_model_group =
    move_group_interface.getCurrentState()->getJointModelGroup(PLANNING_GROUP);

    // namespace rvt = rviz_visual_tools;
    // moveit_visual_tools::MoveItVisualTools visual_tools("panda_link0");
    // visual_tools.deleteAllMarkers();

    return 0;
}

