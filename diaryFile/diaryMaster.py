import sys
import datetime
import os

class diaryMaster:
    def __init__(self,dirpath='',file_name="test.txt"):
        try:
            #if dirpath=='' or not dirpath:
            #    dir_path = os.path.dirname(os.path.realpath(__file__))

            if os.path.isfile(dirpath):
                dir_path=os.path.dirname(os.path.realpath(dirpath))
                file_path = dir_path

            else:
                if os.path.isdir(dirpath):
                    dir_path=os.path.realpath(dirpath)
                    file_path = os.path.join(dir_path, file_name)
                else:
                    dir_path = os.path.dirname(os.path.realpath(dirpath))
                    file_path = dir_path

        except:
            dir_path=os.path.dirname(os.path.realpath(dirpath))
            file_path = os.path.join(dir_path, file_name)

        
        self.file_obj = open(file_path, 'ab+')

    def writeFile(self, file_obj, message):
        timestamp_format = '%d-%m-%Y %H:%M:%S'
        message_str = datetime.datetime.now().strftime(timestamp_format)
        message_str += ' : '
        message_str += message
        message_str += "\r\n\r"
        file_obj.write(message_str.encode())

    def closeFile(self):
        self.file_obj.close()

    def diaryWrite(self,message):
        self.writeFile(self.file_obj, message)
        self.closeFile()

if __name__=='__main__':
    diaryobj = diaryMaster()
    diaryobj.diaryWrite("This is a test")
