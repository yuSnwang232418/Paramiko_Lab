# Yuxi's Paramiko Lab

## Introduction

Network Automation Lab based on GNS3 platform, Python, Paramiko library (Win environment for this lab). 

## Function

1) Connect to all the devices within the network with SSH (SSH connect related configuration on Router/Switch required).
2) Read the configuration files.
3) Shell to send command and retrieve the result of command execution.
4) Output the result of command execution to files (file name in device_RID, YY, MM, DD, TIME format).
5) Above function can easily tranform to Configuration Backup function.

## Topology
![image](https://github.com/user-attachments/assets/92e8558f-0a12-4b8f-9e70-b2d2c3807384)

## Pre-requirements
1) GNS, GNS VM, VMware Workstation.
2) IOU images
3) Use Router, switch (optional), end device (Cloud) in GNS3.
4) Connect Router/L3 Switch, switch to VMnet interface of GNS Cloud. GNS automatically have two Ethernet adapter VMware Network Adapters named VMnet-id.
5) Configure the IP address on connected interface of Router/L3 Switch. Ensure they are in the same subnet as VMware Network Adapters'.

Can sucessfully ping from windows to network in GNS VM.
![image](https://github.com/user-attachments/assets/03278498-4c88-47b5-a8c4-68c848bf5d2d)
