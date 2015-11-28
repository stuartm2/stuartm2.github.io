---
layout: post
title: "Start of ROS 2-Wheeled Robot"
tags: [rosbot]
---

One of my long-term goals is to build a small quadcopter for underground mine exploration which can go boldly where braver men fear to tread - or wisely choose to prolong their life by avoiding in many cases!  I've built a larger quadcopter with manual control and various safety features like 'return to base' for above-ground flying but with the physically enclosed and radio-hostile environment of an underground mine, the same features just won't work.

Following a bit of investigation, it seems that I want some kind of autonomous robot platform with SLAM (simultaneous localization and mapping) functionality.  Of the options available, ROS (Robotic Operating System) looks like the best fit for me: it's free, modular, open source, runs on Linux, supports Python and has a lot of libraries available off-the-shelf including some quadcopter and SLAM-related ones.

This all feels like a logical next step for me, combining my electronics and programming skills.  Robotics was also what I planned to study at university before my life got sidetracked by the fledgling Internet all those years ago.  No regrets of course, the web was definitely the right career choice, but I've spent too long ignoring an interest in robotics and, from reading more about ROS, it seems the technology has now arrived where it's possible to do more than line-following and maze solving on a hobby budget (although those things are lots of fun, I'm sure).

So, in an effort to learn about ROS, and robotics more generally, without starting on the high-risk task of making a quadcopter explore autonomously without shredding the furniture, I've decided to build a wheeled robot based on the Raspberry Pi 2 board (which I already have).  This is a catch-up covering a few weeks of progress so far.

2-wheeled chassis are readily and cheaply available on eBay - here's the one I've purchased:

![](/images/rosbot/IMG_0008.tn.jpg)

It comes with motors and basic rotation encoders but will need a motor driver and rotation sensors.  Rather than the usual L293-based driver, I found a small module based on the TB6612FNG and made by Sparkfun.  The sensors were a bit more tricky because of the spacing needed to accomodate the wide encoders but some were found and ordered.  They didn't readily fit in the cutouts provided on the board so I designed and printed an under-chassis support ([thing 1160661](http://www.thingiverse.com/thing:1160661/)):

![](/images/rosbot/IMG_0009.tn.jpg)

![](/images/rosbot/IMG_0010.tn.jpg)

The chassis has plenty of pre-drilled holes but none suitable for the Pi board so I designed and printed a suitable support for that which places it in the centre of the chassis and offsets it to allow access to the various ports and the card slot without obstructing the wheels ([thing 1160666](http://www.thingiverse.com/thing:1160666)):

![](/images/rosbot/IMG_0011.tn.jpg)

Finally, I had to settle on a power supply.  Longer-term, I might go with a LiPo battery but right now, I have sufficient AA NiMH batteries and holders to allow me to proceed without any more purchases.  I designed and printed a simple frame which puts a 3xAA holder on each side and sits over the passive wheel providing a good counter-balance to anything I choose to put on the other end of the chassis ([thing 1160677](http://www.thingiverse.com/thing:1160677)):

![](/images/rosbot/IMG_0013.tn.jpg)

From my early reading and following the introductory tutorials, ROS appears to have a steep learning curve.  The next step will be to get it installed on the Pi and get it talking to the motors.  Stay tuned!
