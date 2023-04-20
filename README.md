# Python Pomodoro Timer

![License](https://img.shields.io/github/license/bbland1/pomodoro-timer-python?style=plastic)
![Top Language](https://img.shields.io/github/languages/top/bbland1/pomodoro-timer-python?style=plastic)
![Contributors](https://img.shields.io/github/contributors-anon/bbland1/pomodoro-timer-python?style=plastic)

A GUI of the "Tomato Timer". This will allow the user to set work, short break and long break times that use the work break cycle with the pomodoro timer method. Once the user inputs the minutes they want each part to take they can hit start and the timer on the tomato will start counting down. It uses checkmarks that come up after each completion of a work cycle that will show how many work rounds have been completed. It can be used to boost productivity.


Screen recording with work, mini break and long break set at 1 min to show functionality:








https://user-images.githubusercontent.com/104288486/192043379-f87f1a7e-6404-42f5-8ba7-4036549869d7.mov





## Requirements

Installing from the [requirements.txt](./requirements.txt) handles everything needed for this project.

## Built With

* [Python](https://www.python.org) make sure that depending on your python install method that tkinter is properly installed by your version


### How to Use:
* With the program open you can press start right away and it set the intervals to the default time of 25 min work, 5 min short break, 20 min long break.
* If you would like to change the times on any of the intervals changing the numbers in the inputs before hitting start will do that.
* When the timer is started the start button will change to a pause button, the words on the page will change to state which interval the timer is in(work, short break, or long break), and the program can be closed by hitting the I'm finished button.

#### Some special details
* At the last 10 seconds of the interval a bell sound is trigger to get the attention of the user to the transition in interval type.
* At the interval switch When the actual switch happens a pop up displaying the interval that it is on.
  - The top level pop up has the same button functionality to pause, reset, close the program with the additional ability to just continue
  - If the user does not click any button in the pop up within 10 seconds it will close itself as the timer keeps going.
  - The pop up is a top level so it will show on top of the program or any programs and if the user has a full screen the screen will probably switch to make the timer and the time pop up the focus of that moment. 

### Local Development
1. Download or clone this repository.
2. (Optional) [Setup a virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate it to install requirements into the virtual environment to run instead of your computers global environment.
3. Install the project requirements.
```shell 
pip install -r requirements.txt
```
4. Run the program
```shell
python main.py
```

### Launching
Creating an executable program from this python project is possible. While it was not done with this code here it is possible. Some methods for making the executable are listed in this article [here](https://towardsdatascience.com/how-to-easily-convert-a-python-script-to-an-executable-file-exe-4966e253c7e9).

### License
See the [LICENSE](./LICENSE) file for license rights and limitations (MIT).


