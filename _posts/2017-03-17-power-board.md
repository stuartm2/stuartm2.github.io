---
layout: post
title: "Power Board"
tags: [allbot]
---

To allow the Allbot to operate untethered, I need to find a suitable on-board power supply.  The off-the-shelf product includes a shield with 4xAA batteries but that wouldn't work for me as the sensor shield I'm using doesn't have a right-angled servo header to allow another shield to be mounted above it.  I do have some spare 16340 Li-ion rechargeable cells and holders, however, and there's a perfect space for them on the underside of the robot's body.  So I etched a simple PCB with the battery holders, a small 5V BEC, a power switch and a 3-pin connector for 5V, ground and scaled unregulated voltage for low-voltage detection.  Here's the resulting board:

![](/images/allbot/IMG_0207.tn.jpg)

![](/images/allbot/IMG_0208.tn.jpg)

And here it is fitted:

![](/images/allbot/IMG_0209.tn.jpg)

![](/images/allbot/IMG_0210.tn.jpg)
