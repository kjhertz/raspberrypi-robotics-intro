# raspberrypi-robotics-intro

This is a project for getting started with robotics using the Raspberry Pi and the Pi2Go-lite robot kit. The project is a work in progress but intends to emulate some of the points in Nick Mccrea's great tutorial (link below).

1. Getting started
==================

1.1 Raspberry Pi
----------------

Setting up your Raspberry Pi: https://www.raspberrypi.org/

1.2 Pi2Go robot kit
-------------------
Pi2Go robot kit: http://4tronix.co.uk/

Assebly instructions: http://4tronix.co.uk/blog/?p=452

Short Pi2Go tutorials:  www.theraspberrypiguy.com/raspberry-pi-robots/


1.3 Robot Programming Tutorial
------------------------------

Great introduction to robot control: http://www.toptal.com/robotics/programming-a-robot-an-introductory-tutorial

1.3 IDE
------
I will be using Visual Studio for various reasons, hence solution *.sln files will be included.

2. Robot Program Structure
==========================
The robot programming structure consists of three main parts: Supervisor, Interface and Robot. The supervisor acts as the robots brain which reads and send messages from the actual or simulated robot through the interface.

2.1 
