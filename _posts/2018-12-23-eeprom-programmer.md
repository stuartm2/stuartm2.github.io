---
layout: post
title: "EEPROM Programmer"
tags: [8bit-comp]
---

![](/images/8bit-comp/IMG_0581.tn.jpg)

In his series, Ben makes an EEPROM programmer with an Arduino and includes the data which he wants to program in with the Arduino code.  This is fine but it does require reprogramming the Arduino every time you want to upload different data to the EEPROM.  To avoid this, I decided to write an Arduino sketch which programs the EEPROM from data it receives via the serial connection.  By doing this, it's possible to program the EEPROM without altering the Arduino code and also to send the EEPROM data in a variety of ways (eg: serial terminal, Python script, text file, etc).  The code for actually reading from and writing to the EEPROM remains the same as Ben's code.

## Protocol

I want to be able to read and write individual address locations as well as dump the contents of the entire EEPROM.  I tried sending and receiving raw binary data over serial but found that it limited my options for interacting with the programmer (eg: no Arduino serial terminal) so I decided to use normal ASCII.  Here's the basic protocol I came up with:

    AAAA    - Read data from address AAAA
    AAAA:DD - Write data DD to address AAAA
    FFFF    - Dump the entire EEPROM contents

I chose FFFF as the 'dump' command because it's outside the available address range of the EEPROMs used in this project, allows me to use the same string-to-hex conversion code as the other commands and is easy to remember.  Here's what an example serial terminal session might look like:

    000F\n    # Returns 000F:00
    000F:55\n # Writes 0x55 to location 0x000F
    FFFF\n    # Returns 0000: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 55
              #         0010: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
              #         ...

## Arduino Code

The first step is to get the serial data into a normalised form, terminated with a newline character (either \r or \n):

    char cmdbuf[10]; // Command buffer
    int atInd = 0;   // Current location in the buffer

    [... Ben's EEPROM functions here ...]

    void clearBuffer() {
        for (int i = 0; i < 10; i += 1) {
            cmdbuf[i] = 0;
        }

        atInd = 0;
    }

    void loop() {
        while (Serial.available()) {
            char c = Serial.read();

            if (c == '\r' || c == '\n') {
                String cmd = String(cmdbuf);
                cmd.trim();
                cmd.toUpperCase();
                processCmd(cmd);

The processCmd function looks like this:

    void processCmd(String cmd) {
        if (cmd.length() != 4 && cmd.length() != 7) {
            return; // Invalid command
        }

        int addr = hexstrToInt(cmd.substring(0, 4));

        // Dump EEPROM contents
        if (addr == 0xFFFF) {
            printContents();
        }

        // Write data
        else if (cmd.length() == 7 && cmd[4] == ':') {
            writeEEPROM(addr, hexstrToInt(cmd.substring(5)));
        }

        // Read data
        else if (cmd.length() == 4) {
            char buf[20];
            sprintf(buf, "%04x:%02x", addr, readEEPROM(addr));
            Serial.println(buf);
        }
    }

To convert the string representation of the hexadecimal value to an integer, we loop through each character in the string:

    int hexstrToInt(String hexstr) {
        int data = 0;

        for (int i = 0; i < hexstr.length(); i += 1) {
            char c = hexstr.charAt(i);

ASCII characters '0' to '9' have values from 48 to 57 consecutively so, if the character is within that range, we subtract 48 to get its integer representation.  Similarly, characters 'A' to 'F' (hex 10-15) have values from 65 to 70 consecutively so, if the character is in that range, we subtract 55 to get its integer representation.  Any other character is treated as 0.  Here's how that looks in code:

            int val = 0;

            if (c >= 48 && c <= 57) {
                val = c - 48;
            } else if (c >= 65 && c <= 70) {
                val = c - 55;
            }

Then, we shift the current value of data by 4-bits and OR the new character's value onto it:

            data = (data << 4) | val;
        }

        return data;
    }

For a 2 byte hex string, say 042A (1066), the shifting process looks like this:

                   0000 (data << 4) | 0x0 = 0
              0000 0100 (data << 4) | 0x4 = 4
         0000 0100 0010 (data << 4) | 0x2 = 66
    0000 0100 0010 1010 (data << 4) | 0xA = 1066

Finally, we return to the loop function and clear the buffer ready for the next command:

                clearBuffer();
            } else if (atInd == 9) { // End of buffer. Discard
                clearBuffer();

Or, if the character wasn't a newline and we still have space in the buffer, we append it:

            } else {
                cmdbuf[atInd] = c;
                atInd += 1;
            }
        }
    }

## Sending Data

We can now send data to the EEPROM over the serial port.  I'm using Python and the [PySerial](https://pyserial.readthedocs.io/) library here.  First, we create a simple Programmer class(eeprom.py):

    import serial
    from time import sleep

    class Programmer():
        def __init__(self, port, speed=57600):
            self.port = port
            self.speed = speed
            self.ser = None

        def __enter__(self):
            self.connect()
            return self

        def __exit__(self, type, value, traceback):
            self.close()

        def write_data(self, addr, data):
            s = b'%04x:%02x\n' % (addr, data)
            self.ser.write(s)
            sleep(0.01)

        def connect(self):
            self.ser = serial.Serial(self.port, self.speed)
            print("Connected to port: " + self.port)

        def close(self):
            self.ser.close()

We can use this script to clear the EEPROM by writing 0s to every address):

    from eeprom import Programmer

    with Programmer('/dev/my_device') as prog:
        for i in range(2048):
            prog.write_data(i, 0)

To program the display EEPROM with both decimal and 2s-compliment data, I used this script:

    from eeprom import Programmer

    # Hex values to display digits 0-9 on a 7-segment display
    DIGITS = [0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x70, 0x7F, 0x7B]

    with Programmer('/dev/my_device') as prog:
        for val in range(256):
            # Regular numbers
            prog.write_data(val,        DIGITS[val % 10])         # 1s
            prog.write_data(val + 256,  DIGITS[(val / 10) % 10])  # 10s
            prog.write_data(val + 512,  DIGITS[(val / 100) % 10]) # 100s
            prog.write_data(val + 768,  0)

            # 2s complement
            if val > 127:
                val2c = abs(val - 256)
                sign = 0x01
            else:
                val2c = val
                sign = 0

            prog.write_data(val + 1024, DIGITS[val2c % 10])         # 1s
            prog.write_data(val + 1280, DIGITS[(val2c / 10) % 10])  # 10s
            prog.write_data(val + 1536, DIGITS[(val2c / 100) % 10]) # 100s
            prog.write_data(val + 1792, sign)

___

## Resources

 * GitHub: [Programmer code and scripts](https://github.com/stuartm2/EEPROM_programmer)
