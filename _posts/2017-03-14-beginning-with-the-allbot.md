---
layout: post
title: "Beginning with the AllBot"
tags: [allbot]
---

I stumbled across [Velleman's Allbot](http://allbot.eu/) a short while ago and thought it looked like a fun project so, as they publish [printable versions of the plastic parts](http://www.thingiverse.com/thing:1434665) and I had most of the required hardware, I decided to build one to play with.  I'm starting with the 4-leg/2-joint version.  Here's a photo of the initial build:

![](/images/allbot/IMG_0203.tn.jpg)

Printing was straightforward although I did need to use Meshmixer to deepen the captive nut holes on the servo mounts.  Assembly, once I'd fixed the servo mounts, was also simple and the software was trivial to install and get running.  Initially, I'm just using a cheap sensor shield to connect the servos and I haven't yet decided on a power source.  Overall, I'd say it's a really well-maintained project and it's great that they've chosen to open source their code and plastic parts as well as selling complete kits.

For now, I'm just going to have some fun hacking about with this, making improvements and maybe using it to learn about stuff like inverse kinematics which might benefit from having a small quadruped robot to experiment with.  Longer-term, I may try writing some ROS driver code for it.  It's also given me some ideas for improving the strength of my larger Hexapod's legs so there's a possibilty that these two project will converge at some point in the future.
