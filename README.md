# Todo list touch display - Raspberry Pi

## Project Scope

A Raspberry Pi will host the guts of the application.  Server pi will be connected directly to touch display and wall-mounted.  A motion sensor will be mounted to turn the display on when there is motion, and the screen will shut off after 2.5 mins until it senses motion again.

The touch display itself will show a todo list, with optional christmas lists, learning lists, and other displays.

Client device will use cli to send information to the server pi.  The client device may request the current lists from the server, delete items from lists, add items to lists, etc.  

Note: First versions are being tested in Python2.  May not work in Python3 at this time.
