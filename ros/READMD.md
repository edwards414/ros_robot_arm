
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

### 9/8 
- 安裝ubuntu 20.04 juammy
- - 發現沒有 release ros1 
- 換ubuntu focal

- 安裝ros1 

- 成功啟動小烏龜

- Ros-turtlesim

- Roscore建立topic

- Rosrun turtlesim tirtlesim_node建立tirtlesim_node節點

- Rosrun turtlesim draw_square 讓小烏龜執行畫正方形的任務



## turtlesim 啟動畫面
![ros_turtlesim](img/a2.png)

### 9/11

完成使用usb_cam + image_view
graph

![ros_turtlesim](img/a5.png)

     rosrun image_view image_view image:=/usb_cam/image_raw
### 9/17
#### face_tracker_pkg臉部追蹤
遇到找不到kobuki_gazebo_plugins套件
導致catkin_make無法正常運行

在ros-wiki中kobuki_gazebo_plugins只有
這個版本
我使用的ubentu是20.04

ros版本是notic

notic為ros1的最後一個版本,很多package沒有更新過來
### 10/15
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

# 建立ros workspace

建立資料夾

```bash
mkdir –p ~/catkin_ws/src
```

```bash
cd ~/catkin_ws/src
```
1

完成使用usb_cam + image_view
graph

 rosrun image_view image_view image:=/usb_cam/image_raw

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



