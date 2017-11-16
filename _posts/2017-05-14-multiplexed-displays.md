---
layout: post
title: "Multiplexed Displays"
tags: [badscore]
cover_img: /images/badscore/cover.prototype-update.jpg
---

Following some experimentation, it seems that driving the 7-segment LEDs directly from the Arduino with multiplexing is the best way to get a bright and consistent display.  This uses a total of 11 pins and allows me to resolve the leading zeros issue but it leaves me with a decision to make over the base Arduino plaform:

 * stick with the Mega2560 which has enough pins but will take up a lot of space in the final product or
 * use multiple Atmega328-based devices communicating via i2c or serial which will keep the space down but be a bit more complex.

I've decided to test the second option and see how reliable it is as it'll make for a more compact final product.  If I was developing this as a commercial product, I'd probably go with the Mega2560, an Arm-based chip or something else with lots of I/O as I'd be able to embed it directly on a board and have it assembled in a factory but, for this home-built one-off, that's not really a viable option at this stage.

The current state of the project is that communications over an i2c bus are working and the 7 segment LED display and main input buttons are working.  Next up is the bi-colour set counter LEDs and then I'll need to work on the remote controllers.
