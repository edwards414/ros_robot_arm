
# ROS1開發筆記

### 模擬機手臂
建置虛擬模型

控制器Gazebo

模型 URDF 將3D模型插入UADF中，建立敘述套件

## 計算圖層(computation graph)

- Massage:各節點的通訊，透過定義的資料結構
- Topic:中心點，節點將資料上傳，個節點透過訂閱的方式取得訊息
- Service:透過reply and request的方式
- client端發送request後，須等伺服器reply才結束
- Bag:透過rosba感測，將傳感器的值打包，即可放置另主機觀測

## 日期進度

Ubuntu安裝ros

### 2023/9/8 
- 安裝ubuntu 20.04 juammy
- 發現沒有 release ros1 
- 換ubuntu focal

- 安裝ros1 

- 成功啟動小烏龜

- Ros-turtlesim

- Roscore建立topic

- Rosrun turtlesim tirtlesim_node建立tirtlesim_node節點

- Rosrun turtlesim draw_square 讓小烏龜執行畫正方形的任務



## turtlesim 啟動畫面
![ros_turtlesim](img/a2.png)

### 2023/9/11

完成使用usb_cam + image_view
graph

![ros_turtlesim](img/a5.png)

     rosrun image_view image_view image:=/usb_cam/image_raw
### 2023/9/17
#### face_tracker_pkg臉部追蹤
遇到找不到kobuki_gazebo_plugins套件
導致catkin_make無法正常運行

在ros-wiki中kobuki_gazebo_plugins只有
這個版本
我使用的ubentu是20.04

ros版本是notic

notic為ros1的最後一個版本,很多package沒有更新過來
### 2023/10/15
建立ros_aiml

使用PyAIML

AIML檔說明
模板對話

使用者輸入 my name is fxrbindi

系統回應 nice to see you
```AIML
<category>
    <pattern>
       my name is * 
    </pattern>
    <template>
        nice to see you 
    </template>
</category>

```
#### pyaiml
```python
import aiml
bot.aiml.Kernel()
bot.setBotPredicate("name",JIBO)
bot.learn('sample.aiml')
print bot.respond("MY NAME FXRBINDI")
```

### 安裝ROS sound play

```bash
sudo apt-get update
```
安裝 libgstreamer


## 完成docker env、ros workspace

### - ubuntu16.04
### - python2.7
### - ros kinetic

### 目前位置docker contrainer d0

    docker run -it -v /dev:/dev -e DISPLAY:$DISPLAY ...
    

![](img/a6.png)
![](img/a7.png)

## roslaunch 所有檔案 
docker 容器無法連接host的揚聲器

```bash
[WARN] [1697383034.902519]: Sound command issued, but no node is subscribed to the topic. Perhaps you forgot to run soundplay_node.py?
```

![](img/a8.png)

修改所有launch權限

```bash
sudo chmod +x *.launch
roslaunch ros_aiml start_chat.launch 
roslaunch ros_aiml start_tts_chat.launch 
roslaunch ros_aiml start_speech_chat.launch 
```

![](img/a9.png)

## 10/21

### 使用rosserial 連接stm32

### 10/28

### ubuntu更改系統預設路徑（中文-->英文）

    gedit ~/.config/user-dirs.dirs

新增或修改

    XDG_DESKTOP_DIR="$HOME/Desktop"  
    XDG_DOWNLOAD_DIR="$HOME/Download"  
    XDG_TEMPLATES_DIR="$HOME/Templates"  
    XDG_PUBLICSHARE_DIR="$HOME/Public"  
    XDG_DOCUMENTS_DIR="$HOME/Documents"  
    XDG_MUSIC_DIR="$HOME/Music"  
    XDG_PICTURES_DIR="$HOME/Pictures"  
    XDG_VIDEOS_DIR="$HOME/Videos"

####   ***須將所有的中文名稱改成英文才會同步

## stm32cubeide無法build,需要配置*.elf的檔案才能build

#### - 1.IDE內部生成project檔案有內含Debug檔案
#### - 2.STM32CubeMX裡面沒有

### 解決使用IDE內的檔案生成

## STM32CubeIDE 燒入 arm-none-eabi-gdb 

#### 找不到libncurses.so.5(需要額外安裝)

Could not determine GDB version using command 


![](img/a11.png)

    sudo apt-get install libncurses5 libncurses5:i386
    
    
## 2023/10/31

stm32 uart 拒絕連線



## 使用新的workspace_1.13.5

使用stm32cubeide內生成l4r5 init file



建立inc製作.h檔案

    roslaunch rosserial_stm32 make_library.py 


將chatter內的Inc cp -avr 到workspace/rosserial/Inc/




建立
https://hackmd.io/@JINGCCC/rosserial_1?fbclid=IwAR3HZk-Y4dT-3glBGB2fagztaaS9PIjeFyiFROs-Ebdbmk028D78qVus07Y

環境建制完成

分析msg資料 
https://blog.csdn.net/qq_38288618/article/details/102931684

## - 或者在run configuration設定
##　- 生成方式ide(build compile)


cp -avr命令将以递归方式复制文件和目录

    https://www.youtube.com/watch?v=cq0HmKrIOt8&ab_channel=LearnembeddedsystemswithGeorge


### stm32cubeide無法build'project Explorer失蹤

- 設定workspace import .ioc

- 打開project explorer

- window -> show view

- 設定ln 硬連結(hard link)到workspace

![](img/a10.png)

hard link not allowed for directory

## rosserial


``` c
    /*
     * rosserial Publisher Example
     * Prints "hello world!"
     */
    
    // Use the following line if you have a Leonardo or MKR1000
    //#define USE_USBCON
    
    #include <ros.h>
    #include <std_msgs/String.h>
    
    ros::NodeHandle nh;
    
    std_msgs::String str_msg;
    ros::Publisher chatter("chatter", &str_msg); //把自己設定成公開者
    
    char hello[13] = "hello world!"; 
    
    void setup()
    {
        nh.initNode();
        nh.advertise(chatter);
        // 是用來告訴ROS節點要廣播（advertise）一個特定主題，讓其他節點可以訂閱它。這個操作通常在ROS節點初始化的過程中完成。
    }
    
    void loop()
    {
        str_msg.data = hello;
        chatter.publish( &str_msg );
        nh.spinOnce();
        delay(1000);
    }

```

## 2023/10/31
完成uart-stm32連接

需要驗證的東西：

- 如何在stm32上收到host端傳送的資訊
- 從stm32上publish發布資料,用本機rostopic echo 
- 確認個節點的關西

## 2023/11/13
docker ros melodic建立

    docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --name=ros-melodic -v /home/fxrbindi/Desktop/ros_robot_arm-main/virtual_robot_arm/parol6_ws/:/parol6_ws ros:melodic

docker nvidia toolkit配置




https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

![](img/a13.png)

## 2023/11/25
### 主要完成parol6虛擬rviz檢視手臂

### tf：transform，ROS中管理3D座標系變換的工具。只要告訴tf兩個相關聯座標系的座標變換訊息，tf會幫你一直記錄這個兩個座標系的座標變換，即使兩個座標系處於運動中。
https://blog.csdn.net/tiancailx/article/details/78910317


#### static_transform_publisher 發佈一個從父座標係到靜態子系的一個座標變換
#### 發布yaw pitch roll
![](img/a12.png)

#### static_transform_publisher x y z yaw pitch roll frame_id child_frame_id period_in_ms

    Publish a static coordinate transform to tf using an x​​/y/z offset in meters and yaw/pitch/roll in radians. (yaw is rotation about Z, pitch is rotation about Y, and roll is rotation about X). The period, in milliseconds, specifies how often to send a transform. 100ms (10hz) is a good value.

#### static_transform_publisher x y z qx qy qz qw  frame_id child_frame_id period_in_ms

    Publish a static coordinate transform to tf using an x​​/y/z offset in meters and quaternion. The period, in milliseconds, specifies how often to send a transform. 100ms (10hz) is a good value.

### 實際使用
#### 發布頻率（50ms = 5HZ）
#### 在ROS中，map座標系經常被用作固定的全局參考座標系，通常代表地圖或世界座標系。框架base_link通常與機器人的底座或根部相關聯。

    rosrun tf static_transform_publisher 0 0 0 0 0 0 map base_link 50

#### launch node 可以寫
    <node pkg="tf" type="static_transform_publisher" name="base_link"
    args="0 0 0 0 0 0 map base_link 50" />

![](img/a12.jpeg)

## 2023/11/30
### moveit 
- getting start
- c++ interface
- python interface
- commander scripting
## 2023/12/9
### URDF 說明
#### 1.藉由原點連接各個link,link之間使用joint做連結

#### - Link : 手臂的臂
#### - Joint : 關節
<img src = "img/joint_link.png" width = "500">

#### 2.URDF有父子架構,透過上一層的改變下一層也會跟著改變
#### 機械手臂上的應用,link部件我們我有分base_link.link0~5,原點（origin）的部份就是base_link,最大的就是base_link,最小是link5,link0旋轉,他的子連結都會旋轉

<img src = "img/parent_child.png" width = "500">




### 完成fusion360 to urdf

### 主裝完成

![](img/link_all.png)

### 設定節點設定運動旋轉

![](img/set_joint.png)

### 原點設定
![](img/red_view.png)

### [範例連結](https://youtu.be/Pokyu91hb_o?si=6cvBPNjJHlcICVq2)
### 支援輸出URDF[github:fusion2urdf](https://github.com/syuntoku14/fusion2urdf)
### 組合建轉body(myscript)[back2body](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-convert-multiple-assembly-components-back-to-solid-bodies-in-Fusion-360.html)
### 模型倒掉[fusion_z軸直立](https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/How-to-change-the-orientation-of-the-origin-planes-in-Fusion-360.html)

### rviz查看

<img src = "img/urdf_rviz_demo.png">

## 2023/12/10
### 加入moveit外掛模組
### mo
<img src = "img/move_group.png" >


<img src = "img/moveit_group_ch.jpg" >



### 設定moveit assistant

### [相關連結](https://docs.ros.org/en/kinetic/api/moveit_tutorials/html/doc/setup_assistant/setup_assistant_tutorial.html)

    roslaunch moveit_setup_assistant setup_assistant.launch

### 使用urdf生成的srm_arm.urdf.xacro檔案
<img src = "img/moveit_assistant_input.png" >

### 設定self-collisions碰撞點個數（官方推薦設成10,000）
<img src = "img/self-collision.png" >

### planing group
<img src = "img/planing_group.png" >

### ROS Control
<img src = "img/ros_control_msg.png" >

### export
### 如果是使用su ursr,需要使用root

    sudo chmod a+w 資料夾位置

<img src = "img/moveit_export.png" >

### python 指令控制

<img src = "img/python_command.png" >

#### 將結果紀錄到c   
    rec c
#### 換名稱
    goal = c
#### 更改第一軸 
    goal[0] = 0.1
#### 規劃＆執行
    plan
    execute
# ----------------
### 2023/12/11
### 主要學習建立package
#### package基本架構

    catkin_create_pkg <package name> rospy std_msgs roscpp
#### 程式補充
##### - rospy.info()將訊息打印出來
##### - 第一行需要宣告 #! /user/bin/env python
##### - 使用sys.argv[1]可以抓取command的參數
##### - pub.publish(vel)將資料發布出去

    /tu_ws/src/turtle_one/scripts/turtlemove.py

<img src = "img/turtle_pkg_python.png" >

### rosrun
    rosrun turtle_one turtlemove.py
### 補充package裡的CMakeList.txt
#### 可以直接使用化名(python不能用)

    add_executable(turtle_move_node src/turtlemove.cpp)

#### run 

    rosrun turtle_one turtle_move_node


### 錯誤訊息

the selection cannot be launch, and there are no recent
    
https://www.youtube.com/watch?v=oa95SuiNPcY&t=192s&ab_channel=easycoding


## 2023/12/17
### small_arm gazebo_rviz_graph
![Alt text](img/ros_gazebo_rviz_graph.png)

### small_arm rviz_graph
![Alt text](img/arm_config_rviz_graph.png)

![Alt text](img/panda_arm_demo_gazebo_graph.png)

















# 建立ros workspace

建立資料夾

```bash
mkdir –p ~/catkin_ws/src
0


在ros工作空間新增額外資料夾，存放套件

```bash
cd  ~/catkin_ws/ && catkin_make
```

把工作空間環境加入.bashrc檔中

```bash
echo “source ~/catkin_ws/devel/setup.bash” >> ~/.
bashrc
```

重新加載

```bash
source ~/.bashrc

echo $ROS_PACKAGE_PATH
```
### 節點可視圖(topic,node)

```ros1
rostopic rpt-graph rpt-graph
```

- rostopic bw    
        display bandwidth used by topic
    
- rostopic delay    
    display delay of topic from timestamp in header
- 可以印出massage資料
    - rostopic echo    
    print messages to screen

    - rostopic find    
    find topics by type
    
    - rostopic hz    
    display publishing rate of topic    

### 印出publishers和subscribers指令


    rostopic info

![info](img/a4.png)

print information about active topic

    rostopic list    
list active topics

### 指令透過publisher直接發送data 
    rostopic pub    
publish data to topic

### 傳送的資料格式    

    rostopic type    
print topic or field type

## Error
### 問題1

    ERROR: cannot launch node of type [usb_cam/usb_cam_node]: Cannot locate node of type [usb_cam_node] in package [usb_cam]. Make sure file exists in package path and permission is set to executable (chmod +x)
無法連接到node

解決 => 在catkin_make時有package沒有安裝到導致roslaunch時導入錯誤

### 問題2
    image_view無法透過usb_cam-test.launch開啟

解決=>在lauch後,使用rosrun 單獨建立node還需要解決
 ＝
安裝sound_play套件


波浪 fn+shift+esc




## 已完成：

 - ### ros workspace 工作環境建立
 - ### ros aiml 專案launch
 - ### 安裝雙系統
 - ### stm32cubeide安裝(lib5.so)
 - ### rosserial launch
 - ### docker ros + nvidia
 - ### x11畫面分享（docker -> ubuntu)
 - ### ros虛擬教學板小車成功啟動
 - ### docker rviz 可以啟動
 - ### dockerfile
 - ### c 語言語法入門
 - ### 建立機械手臂urdf
 - ### 發起pola6手臂urdf
 - ### moveit assistant

## 未完成：
 - ### 創pkg去控制arm
 - ### 將作者ardiuno code轉成Hal庫

## 錯誤：
 - ### docker /dev特權問題
su fxrbindi 
source ros_entrypoint.sh 
cd virtual_robot_arm/
cd parol6_ws/
source devel/setup.bash 



