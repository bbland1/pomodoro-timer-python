# Pomodoro-Timer

A GUI of the "Tomato Timer". This will allow the user to set work, short break and long break times that use the work break cycle with the pomodoro timer method. Once the user inputs the minutes they want each part to take they can hit start and the timer on the tomato will start counting down. It uses checkmarks that com up after each completion of a work cycle that will show how many work rounds have been completed.

Once the user hits start the button changes to a pause button which when clicked will change to a resume button. The timer can be reset with the reset button and the whole program can be closed by hitting th finished button. While the timer is running once the round gets to 10 seconds or less it triggers the bell of the system so that at user can hear the change from work to break coming and vice versa. When the actual switch happens a pop up shows up saying it's time for a break or work and has the button functionality to pause, reset, close the program or just continue. If the user does not click any button in the pop up within 10 seconds it will close itself as the timer keeps going.

The pop up is a top level so it will show on top of the program or any programs and if the user has a full screen the screen will probably switch to make the timer and the time pop up the focus of that moment. 

To use the program the repo can be forked and then ran with `python main.py`

What was used: Python with tkinter

Screen recording with work, mini break and long break set at 1 min to show functionality:






https://user-images.githubusercontent.com/104288486/192043379-f87f1a7e-6404-42f5-8ba7-4036549869d7.mov





**Personal Highlights:**
I built something that I can actually use, but also this started as a really simple just straight up timer and I just wanted to add the more functionality to it and allow it to be used in a way I'll actually acknowledge the switch betweens the rounds I think I got it to do that and look nice. Plus it felt good to work through the logic of how it functions.

**Struggles in the process:**
Most of the struggles with this were tkinter specific. It isn't the best documented thing out there so I would have to do a decent amount of searching to find close to what I was trying to do. Then when I found a few sources that were very good it was a lot easier but finding something that documents the nuances in a way that made sense was hard.

**What I learned:**
Mostly how much the research experience I have from chemistry really is useful when looking for ways to do things in programming. It really is about find the correct way to search your question and being able to parse through the information.
