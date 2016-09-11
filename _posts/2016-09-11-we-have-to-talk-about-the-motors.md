---
layout: post
title: "We Have to Talk About the Motors"
tags: [quadx450]
---

Alright, I'm going to be honest here - the results of my first test flights earlier in the week have left me rather disappointed.  In terms of sensible battery usage, I'm getting around 5-6 minutes at hover which is about as bad as it was before.  So I decided to learn a bit more about this stuff and see how I can get the kind of flight times I'm looking for.

After some research, I ended up signing up for a month's subscription of [ecalc](http://www.ecalc.ch/xcoptercalc.php) and plugging a whole load of numbers into it.  Sure enough, based on current equipment and weight, the ecalc tool estimates a hover flight time of 6 minutes:

![](/images/quadx450/ecalc1.png)

In simple terms, to get more flight time I need motors which are able to lift more weight per-amp.  Of course, this gets a whole lot more complex when I want to retain my frame and 20A ESCs.  After much hunting, I chose 4 DYS 650KV pancake motors as they were available in the UK at a reasonable price.  They work with both 3S and 4S batteries as well as props from 10" to 12".  The optimal combo is 4S with 12x3.8 props but 12" props won't fit on my frame without major modifications and it'll need new ESCs so I'm not going to do that.  Running at 3S with my existing 10x4.7 props isn't going to work because the motors will barely produce enough thrust to get off the ground (ecalc won't even give figures based on that conbination) so I've ordered a set of 11x4.7 props to test the motors out although I won't expect much of an improvement:

![](/images/quadx450/ecalc2.png)

Things start to get more intesting when I put a lightweight, low-C 4S/8AH battery in the mix.  Running my existing 10x4.7 props to keep everything safely within the limits of my ESCs, we scoot well past my original goal of 12 mins:

![](/images/quadx450/ecalc3.png)

Suffice to say, the new battery is in the post ...

Upgrading the cheapo plastic 10x4.7 props to decent carbon items produces estimates of another 4 minutes:

![](/images/quadx450/ecalc4.png)

If I put the new 11x4.7 plastic props on with the 4S battery we go up again and should still be within the ESCs capabilities:

![](/images/quadx450/ecalc5.png)

And finally, if I find the ESCs can cope with the 11x4.7 props *and* I upgrade them to carbon items, ecalc estimates a over 21 minutes with all the measures in the green:

![](/images/quadx450/ecalc6.png)

All of these new parts are going to arrive over the next two weeks which gives me plenty of time to design the final part (the gimbal for the pilot's video camera) and finish tweaking the flight controller.  And if I can achieve anywhere close to these numbers once everything's fitted, I'll be one happy bunny!
