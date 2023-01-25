close all
clear
clc

bag = rosbag('Prueba3.bag');
disp(bag.AvailableTopics(:,["NumMessages", "MessageType"]));
lidarBagSel = select(bag,"Topic","/slamware_ros_sdk_server_node/map");




