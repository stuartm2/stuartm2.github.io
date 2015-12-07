---
layout: post
title: "ROS Software - Robot Moves"
tags: [rosbot]
---

This post sums up the past week's reading and tinkering to get the basic software in place and the wheels moving under control of ROS.

![](/images/rosbot/IMG_0021.tn.jpg)

The first choice was which OS to install on the Raspberry Pi to host ROS.  The two obvious options are [Raspbian](http://www.raspbian.org/) and [Ubuntu](http://www.ubuntu.org/).  Ubuntu offers the ARM version of their regular OS and the new [Snappy version](https://developer.ubuntu.com/en/snappy/) which is being billed as a prime candidate for ROS applications.  I'd already had a bit of a play with Snappy a few months ago and, while it looks very promising, running ROS on it right now looks like it would be an exercise in frustration because it's so new and I don't have much experience with either system so I've decided not to pursue it for now.

That leaves me with Raspbian or regular Ubuntu.  I'm planning on using a USB dongle but the one I have (Edimax) only works out-of-the-box with Raspbian.  This would seem to make the choice obvious but it's never that easy, sadly.  Raspbian, which is an easier OS install, fell apart on the more complex ROS install whereas Ubuntu was relatively trivial.  I'm sure both of these issues can be resolved, given time, but in an effort to avoid getting bogged down early in this project, I decided to go with Ubuntu and use an old mini router (which functions as an ethernet-to-wifi bridge) temporarily so I can focus on the ROS side of the equation.  With Ubuntu installed, SSH and Screen set up, and ROS installed and running, it's time to move on to the ROS libraries to get my robot moving ...

As with the the operating system, there seem to be two ROS library options: [ROS-Serial](http://wiki.ros.org/rosserial_arduino) and [ROS-Arduino-Bridge](http://wiki.ros.org/ros_arduino_bridge).  ROS-Serial would seem to be the more 'official' option but it looks like it'll need a fair amount of custom code to actually drive the motors and rotation sensors as it's a general-purpose ROS message implementation.  I installed it to have a bit of a test and it worked immediately but there was a fair amount of latency with message processing so I decided to look closer at the other option.

At first glance, ROS-Arduino-Bridge looked like it was going to be a lot of work as the code is designed for specific driver boards but I discovered that my motor driver behaves exactly the same as the Pololu VNH5019 (after tweaking the pin assignments).  I wasn't so fortunate with the rotation sensors as the code assumes a directional sensor whereas mine is just a simple non-directional one, however, with a little hacking I got it working.  Because the ROS message parsing is done on the Pi rather than the Arduino, latency is noticably lower too.

The net result, after all this, is the robot actually moved.  There's still some tuning to be done because it doesn't behave quite as expected (or maybe it's my expectations which need adjusting).  I also need to sort out the big mess of wiring so I've ordered a prototyping PCB for the Pi and will transfer all of the Arduino electronics over to that when it arrives.
