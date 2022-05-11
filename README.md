# Tinder_Data_Display
A simple program to view one's Tinder data. Modified to be novice-friendly, not stylistically impressive.


# Notes
 - To request your data from Tinder simply follow this link to the Tinder help page https://www.help.tinder.com/hc/en-us/articles/115005626726-How-do-I-request-a-copy-of-my-personal-data-

 - This guide is made for MacOS, but the general principals are all the same for Windows (if you're using Linux, you're on your own).


# Get Started
1. Make sure all needed dependecies are installed
  - Python 3.8+ can be downlaoded via the offical Python website https://www.python.org/downloads/
  - The graphics module is made by John Zelle and can be downloaded by typing the following command into your Terminal: pip3 install graphics.py
  - Numpy, a math module, can be retrieved via another console command: pip3 install numpy
  - MatPlotLib, the module used to draw the graphs, is also a console command: pip3 install matplotlib

2. Downlaod the data_parse.py file to a folder (I'd recommend making a folder on your Desktop named Tinder_Stuff as this is what I will use as an example)
  - NOTE: You MUST have data.json in the same folder as data_parse.py, if you don't this will cause file not found errors (see troubleshooting below)


# Running the Program via Terminal
We have to be in the folder with the python file to run it, so here I am going to go step by step of how to navigate to a folder on my Desktop named Tinder_Stuff
1. Open your Terminal, and navigate to your Desktop directory with the command: cd Desktop
2. Once in the Desktop directory, navigate to the desired folder with the command: cd Tinder_Stuff
3. Now inside the folder you are ready to run the program with the command: python3 data_parse.py
4. Once you are done, use the 'Exit' button and not x-out, or Python will yell at you in the console (but don't worry nothing is actually wrong)


# Troubleshooting
- If you are given the error "FileNotFoundError: [Errno 2] No such file or directory: 'data.json'" and you are on a Mac
  1. Ensure your data.json file is in the same folder as data_parse.py
  2. If it is, the next best option is to modify the python code itself with the absolute path of the data file
  3. Open Finder and navigate to your data.json file
  4. Right click (two finger click on track pad) and select the "Get Info" option
  5. Under the 'General' dropdown, go to the 'Where:' field, highlight starting after the first colon and ending after the folder name (ex. Tinder_Stuff), and then copy
  6. Open the data_parse.py file with TextEdit (or a white-space sensitive text editor) DO NOT USE WORD FOR THIS, be very careful as Python is a space sensitive language, so if at any point you think you messed up, you can just x-out of the editor without saving and start fresh
  7. Go to the line below '# PUT THE FULL PATH TO YOUR data.json FILE HERE', and paste the path we copied inside of the single quotes so it looks something like this (with your username substituted for the NAME slot): fullPath = '/Users/NAME/Desktop/Tinder_Stuff/'
  8. Now add data.json to the end of that string, so that the inside of the single quotes looks aproximately like: '/Users/NAME/Desktop/Tinder_Stuff/data.json'
  9. SAVE your changes (go to 'File' in the top bar, then click 'Save')
  10. Now x-out of the TextEdit window, and you should be all good to run the program

- If you are given the error "FileNotFoundError: [Errno 2] No such file or directory: 'data.json'" and you are on Windows
  1. Follow all the steps for Mac but beware there may be some pathing issues as Windows uses backslashes (Mac uses forward slashes) and this script isn't made to deal with the random escape characters that generates. My best advice for that would be adding an 'r' before the absolute path of your json file so it would look like: fullPath = r'C:\Users\NAME\Desktop\Tinder_Stuff\data.json'
  2. Also for the absolute path on Windows the option on right click is called 'Properties' not 'Get Info'



