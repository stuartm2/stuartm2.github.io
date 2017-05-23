---
layout: post
title: "Prototype Finished"
tags: [badscore]
---

I've had a busy weekend working on this prototype and it's now completely working.  Here's a short video showing it in operation:

<div align="center">
<iframe width="560" height="315" src="//www.youtube.com/embed/zP7rkjwITfw" frameborder="0" allowfullscreen></iframe>
</div>

The main unit counts scores with increment and decrement buttons on the unit for each team.  A sharp tone sounds for each increment and a flat tone for each decrement.  If one team reaches the required number of points to win the game (following normal badminton rules) then either a game or set win is announced with a short tune and the set counter LEDs flash.  When a new game begins, the soft reset button is pressed which clears the scores and set counter LEDs appropriately.

Due to not having enough pins to have a separate input for each increment and decrement button, I've used a potential divider to put each team's increment and decrement buttons on a single analog pin.  By default, the output is at +V/2; pressing the decrement button takes output close to ground and pressing the increment button takes it close to +V.  Here's what that part of the circuit looks like:

![](/images/badscore/sch-sw.png)

and here's the code (in this case, for the green team):

    int grnBtnVal = analogRead(GRN_INCDEC_PIN);

    if (grnBtnVal >= 750 && !grnIncDecBtnState) {
      grnIncDecBtnState = true;
      grnScore += 1;
      startTune(1);
    } else if (grnBtnVal <= 250 && !grnIncDecBtnState && grnScore > 0) {
      grnIncDecBtnState = true;
      grnScore -= 1;
      startTune(2);
    } else if (grnBtnVal > 250 && grnBtnVal < 750) {
      grnIncDecBtnState = false;
    }

Each team has a small wireless controller which allows them to increment their score when they win a point.  I've used RFM69 modules to provide the wireless communications.

The next step of this project is to work out how to power the various parts and test them to ensure the power sources will last for at least 2 hours (our usual playing time).  I'll probably start the main unit on AA batteries and see how they cope.  The wireless controllers will probably start with some kind of rechargeable li-ion cell and I expect I'll need to look into some kind of low power sleep functionality to ensure good battery life.  I've also got to spend some time learning how to design and produce a circuit with KiCad so there may be a bit of a delay before this prototype becomes a usable product.
