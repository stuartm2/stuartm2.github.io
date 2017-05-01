---
layout: post
title: "The Initial Plan and Prototype"
tags: [badscore]
---

We play badminton with a couple of friends every week.  It's great fun but we're all getting older and keeping track of the score is becoming more difficult :D  More realistically, we just get stuck into the game and, with some rallys taking a while to win and requiring considerable physical effort, it's not unusual for some or all of us to have forgotten what the scores were by the time we need them.  Then there are those occasions where everyone thinks they remember what the score is, but we all come up with different numbers.  Anyway, this seems like the kind of problem which could be solved with an Arduino ...

Here are my initial thoughts on features which the counter should have:

* Automatically count scores and announce winners
* Small wireless button worn on finger/wrist/bat/waist - one for each team, colour-coded
* Double-sided score display clips to net post
* Large 7 segment LED display - 2 colours (red & green?) corresponding to wireless button colour
* Increment/decrement button for each team on display in case of accidental scoring or button failure
* Set counter with 3x bi-colour LEDS
* Buzzer when score changes or team wins (victorious tune?)
* Reset button on display (long/very long press for resetting current game/set? or intelligent decision based on current game/set state?)

Based on this, I assembled an initial prototype of the main unit to test the basic concept and see how the code might look:

![](/images/badscore/IMG_0255.tn.jpg)

It looks like the green team is on for a big win here.  You can see that the current score for each team is being displayed in binary for now.  Rather than driving 7 segment LED displays directly from the Arduino, I'm going to save a considerable number of pins by using intermediary BCD to 7 segment driver chips (CD4056BE) - reducing the pin count per team from 13 to 6.  I might need to push that up to 7 if I decide to disable the 10s counter rather than having a leading zero for scores lower than 10.

The code is in a public Github repository: [https://github.com/stuartm2/Badminton_Score_Counter](https://github.com/stuartm2/Badminton_Score_Counter)

I have the driver chips and 7 segment LEDs on order so the next step will be to add those to the prototype and see how they work.
