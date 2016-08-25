---
layout: post
title: "Improvement Notes"
tags: [quadx450]
---

Following up from my [first post on this project]({% post_url 2016-08-14-x450-quadcopter-status %}), I stumbled across my notes from last October outlining the various issues we'd experienced during the first few flights:

### Video signal issues

We could only get good video up to a range of about 100-200 metres.  I couldn't tell if this was a problem with the antenna alignment or interference from the quadcopter itself.  The first thing to try is cloverleaf antennas so I've bought a pair of those as well as making a pair - it'll be interesting to see how differently they perform.  I may also try placing the TX antenna below the main frame to see if that makes any difference.

### Poor video quality

The video got completely desaturated when pointed at the ground.  This is a major issue because the ground is what we're most interested in.  Admittedly the conditions weren't ideal with the low sun of a late afternoon in October but I'm hoping for some improvements.  For starters, we've upgraded to a GoPro clone which will hopefully do a better job of managing saturation levels.  I may also experiment with a small sun hood to see if that improves things.

### Lack of video recording

Upgrading to the GoPro clone will solve this.  This has, of course, necessitated the acquisition of an under-slung brushless gimbal which has been the major reason for this redesign of the quadcopter body.  I also had to design a new carrier for the camera as the generic one which came with the gimbal was a bit rubbish.  If I can find the files, I'll post up some details.  I'll still be keeping the FPV camera as the primary video source for piloting.

### Short flight time

The initial flight time with a 2200mAH 3S LiPo was about 7-8 minutes.  I've since purchased a 4000mAH 3S LiPo which will hopefully provide a decent increase.  We'll also be looking at pre-flight planning and experimenting with GPS mission planning software to make better use of the time we have available to us.

### Poor battery life confidence

Related to the short flight time, my Pixhawk clone wasn't able to send telemetry data to my FrSky Taranis handset via the D4R-II receiver so we had to return to base in plenty of time.  I've since constructed a simple level-switching bridge which enables telemetry and I've set up some alerts so we should be able to push the limits a bit further in future.

### No bystander video

We didn't have a ground station setup for our initial flights so bystanders were watching the grainy, monochromatic video over my shoulder.  For future flights, I'm hoping to set up a proper ground station with video and telemetry screens separate from my handset.  I may also put the GoPro clone on a separate video transmitter.

Once the quadcopter's back up in the air, I'll use these notes to assess how effective the improvements have been.
