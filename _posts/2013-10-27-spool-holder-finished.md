---
layout: post
title: "Spool holder finished"
tags: [prusa-i2]
---

I've had an interesting few days with the Reprap :)  It started at lunchtime on Friday when I popped out to the workshop to print a part on my new filament holder.  I was trying Cura in place of Slic3r to generate the gcode for the printer as the latter was having trouble with a particular part.  Cura coped better with the part in question and the print started, but then Cura crashed and forced my printer to completely retract the filament.  In my last post, I mentioned that the filament hasn't been feeding cleanly and the workaround (until I figure out the cause) is to over-tighten the extruder idler to clamp the filament more firmly against the hobbed bolt.  Well, this is fine as long as everything is left alone as much as possible - it doesn't like being loosened and tightened to replace the filament, apparently.  Due to the layered nature of the printed parts, the extruder idler split around the pivot bolt when I tightened it again.  Previous experience has shown that superglue does a good job of welding damaged parts if left for 24 hours so I disassembled the extruder, repaired the idler and clamped it in a vice overnight.  The next day, everything looked good.  I reassembled the extruder and started the next print but the hot-end wouldn't come up to temperature.  I began investigating ...

The short version of a long and frustrating tale is that there were three separate faults: the PTFE cover on the heating resistor had worn through and was causing it to short on the heater block, one of the heater wires into the plug at the board had broken and one of the thermistor leads had snapped.  Anyway, all of those faults are now fixed and the parts are more securely fixed so it shouldn't happen again.  I learned a lot about diagnosing heater issues in the process too.

A side-benefit of this trouble with the hot-end was that I was able to trace the cause of the poor filament feed - the PTFE liner has narrowed near the hot-end, likely due to being deformed by leaking PLA.  The solution to this is to order a supply of PTFE tubing which is now on its way from Hong Kong.  In the meantime, keeping everything tight should see me through and I took the opportunity to print a replacement idler just in case my original repair fails or it breaks again somewhere else.  Another piece of good news is that the PTFE tape I applied to help reduce hot-end leaking seems to be working well.

With all of that out of the way, I had a lot less time over the weekend to do actual calibration and printing but, in addition to printing the spare extruder idler, I did manage to finish the spool holder and filament guide meaning filament changing should be a much less frequent event.  The quality of the prints is getting fairly good - certainly equal to the Reprap parts I bought on ebay last year.  Layer height is currently 0.3mm although I'm looking to reduce that some more over the coming week.  I also plan to look into stabilisers for the print bed and z-axis as wobbles in those are showing up in some of my prints.  Solving those should also enable me to increase the printing speed.

I'll leave you with some photos of the spool holder:

![](/images/prusa-i2/IMG_0014.tn.jpg)

![](/images/prusa-i2/IMG_0016.tn.jpg)
