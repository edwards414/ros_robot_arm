FROM osrf/ros:melodic-desktop-full
# nvidia-container-runtime
RUN apt update \
&& apt install nano\
&& apt install rviz\
&& useradd -m -s /bin/bash -u 1000 fxrbindi\
&& 


RUN source 
ENV NVIDIA_VISIBLE_DEVICES \
${NVIDIA_VISIBLE_DEVICES:-all}

ENV NVIDIA_DRIVER_CAPABILITIES \
${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics
