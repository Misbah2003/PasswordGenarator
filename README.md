# PasswordGenerator

Hello guys! This is a password-generator that I programmed with Python.
The usage is very simple: when you execute the file you only have to specify how long the password should be. If you don't enter anything, the default length will be 9 characters long.
Then a password with numbers, upper- and lower-case letters and symbols will be generated. I hope you like it!

At the beginning of the code I import "random" so that the program can generate random numbers, letters and symbols.
Then I import "colorama", which helps to highlight some output. However, in order to reset the font color automatically (important for the following outputs), I set the "autoreset" to True.
First of all, the program needs to know the length of the password to be generated, so the user has to enter the length of the password.
If the user does not enter anything, the default length is 9 characters (simply because passwords usually have to be at least 8 characters long).
I also made sure that the program does not crash if the user accidentally makes an invalid entry, hence "try" and "except".
If the conversion from string to integer is successful, the program generates a password from upper and lower case letters, numbers from 0 to 9 and symbols. 
Finally, the user is asked if he/she wants another/new password, if he/she enters "y" for "yes", a new one is generated, otherwise not.
