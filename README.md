# Todo list touch display - Raspberry Pi

## Project Need

To do lists can pile up quickly and can often hinder rather than help performance give the nature of human psychology: studies have shown that having too many options available reduces the likelihood that a selection will be made.  In particular, one study presented supermarket customers with a variable number of jams: customers were more likely to try and buy a jam when fewer options were provided.

Additionally, applications that exist for mobile devices are likely under utilized given the above phenomenon.  Because most mobile users have man apps, the likelihood that they will visit their todo list frequently is likely diminished.

With this in mind, I aim to create a todo list that will only display 4 todo items at a time with no option to rearrange priority (because this would lead to task avoidance).  The wall mounted computer for the todo list application will turn on when a user passes, increasing the likelihood that the list will be visited.  Additionally, since only one application will be used by the computer, users will retain focus on the todo list when interacting with the computer.  

Note: First versions are being tested in Python2.  May not work in Python3 at this time.

## Project Roadmap

For new users trying to understand the source code, I have the following structure:

1. A naming convention is used to separate utility scripts, client scripts, and server scripts.  Client here refers to the program which adds list items to our wall-mounted application.  Server refers to the wall-mounted application.  Utility scripts contain generic functions which are utilized by the client and server scripts, and can be reused outside the scope of this project.

2. No special libraries are utilized in this project.  All libraries utilized are innate to Python.

3. The todolist display does NOT update immediately when a new item is added to the list by the client; instead, new items will only appear on the display in the event that an item is deleted (further preventing task avoidance)


## Work Required as of 4/19/2017

As of 4/19/2017, communication between server and client is functional (python2).  Server is fully functional as regards the todo list.  

[ ] Server scripts do not shut down gracefully on ctrl + c, correct
[ ] As of right now, ONLY todolist will be displayed. Need to alter tkinter script to allow for other lists
[ ] Finish integrating the motion sensor.  Script written but not tested.
[ ] Create script that will add items to the todo list at a given date and time.  For instance, garbage day falls on a Wednesday for me; every Wednesday I want to see a garbage todo at the top of the list, and in the event I don't delete the task, I want it automatically deleted on thursday.
