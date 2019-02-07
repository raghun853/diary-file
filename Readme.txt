This is a diary program:

Takes the file name and message as the input, appends the provided file with below:

date : time : message 


If the file is not provided then it creates a file "test.txt" in the location where the package is installed.

Installation instruction:

Download the wheel file and then use : 
pip install diaryFile


Usage instruction:
from diaryFile import diaryMaster

diaryobj = diaryMaster(dirpath='/home/Downloads',file_name="test.txt")
diaryobj.diaryWrite("This is a test")

test.txt:
17-09-2018 13:40:40 : This is a test

Inputs: 
Both the inputs are optional
dirpath ==> If not provided then it defaults to the directory where the package is installed.
file_name ==> This is the file that will be created if not already existing, if it exists then the code will append the file provided. It defaults to "test.txt".

