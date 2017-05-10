---
layout: post
title: "Prototype Update"
tags: [badscore]
---

A short update to the prototype: I've swapped the binary score LEDs with the BCD to 7 segment drivers and corresponding displays which I ordered last week.

![](/images/badscore/IMG_0259.tn.jpg)

As a prototype, it works well and proves the concept.  However, I'm not happy about the leading zeros on scores below 10.  The driver chips do support a blank output but it requires using all of the input lines and I was hoping to keep the number of pins down.  The green displays are also very dim, unlike the red ones, so I'm going to look into that.  One alternative to investigate may be to drive the displays directly from the Arduino using multiplexing, or to multiplex the driver chips, especially if it allows me to switch to a regular ATMEGA328-based Arduino rather than the larger 2560-based Arduino Mega.
