from datetime import datetime
import os
import json
from tkinter import messagebox


class File_Engine(object):

    def __init__(self):
        pass

    def error_found(error):


        error.__str__()
        messagebox.showerror(f'FileEngineError', f'Error:{error}')

    def save_file(file_name, var_name, var_to_save):
        try:
            timenow = datetime.now()

            var_to_save = str(var_to_save)
            tmp = []
            tmp.append(file_name)
            with open(f"{file_name}.py", 'w') as f:
                f.writelines(var_name + '=' + var_to_save)
                f.close()
                messagebox.showinfo(f"FileEngine", f"File: {file_name} Has Been Saved Succefully")


        except BaseException as error:
            print("SaveFile_Engine.init() to make engine directory")
            File_Engine.error_found(error)