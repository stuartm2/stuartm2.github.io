---
layout: post
title: "Voltage Sensor"
tags: [quadx450]
---

While doing the [initial flight tests]({% post_url 2016-09-06-first-test-flights %}), I noticed that the low battery alert I'd set up on the handset wasn't working.  To be honest, it's been so long since I set it up that I forget if it ever worked.  I suspect it didn't as I've had a FrSky voltage sensor lying around for a while which I seem to recall ordering after I found that the voltage alarm didn't work last time and then put it aside when I discovered that it wouldn't connect to my D4R-II receiver's data port.

Anyway, this led me to have a bit of a rethink about the telemetry arrangements.  Of the two telemetry ports on the Pixhawk, the first definitely has to be used for the radio telemetry.  The second is currently connected to the D4R-II where it sends all sorts of data to the handset.  However, to do this I had to sacrifice the data overlay on my video feed and I'm now thinking that may have been the wrong choice.  The only really useful piece of data on the handset is the quadcopter's battery voltage because, while I'm likely to be far more focused on the quadcopter or its video feed while flying, the audible low battery alarm is pretty essential and having it on the handset means it'll work regardless of whether I'm using the radio telemetry data or not.

So I started looking at the voltage sensor again with the aim of reclaiming the second telemetry port for video OSD.  A little reading on the D4R-II's data port combined with some basic testing on the sensor revealed that I *can* send the voltage sensor's data to the handset directly via the data port's A2 pin - I just needed to change the connector.  I added a balance lead plug while I was at it.  Here's the rewired voltage sensor:

![](/images/quadx450/IMG_0167.tn.jpg)

And here it is, covered and stuck in place on the front of the receiver:

![](/images/quadx450/IMG_0168.tn.jpg)
