from datetime import datetime
import os
import json
from tkinter import messagebox


class File_Engine(object):

    def __init__(self):
        pass

    def error_found(error):
        try:

            
            messagebox.showerror(f'FileEngineError', f'Error:{error}')
            with open(f"FILE_SAVES/ERROR_REPORTS/" + f"errorrecent.err", 'w') as f:
                f.writelines(f"error = {error}")
                f.close()

            print(error + "CheckErrorReport")
            error = ""
        except BaseException as error:

            with open(f"FILE_SAVES/ERROR_REPORTS/error.fatal", 'w') as f:
                f.writelines(f"{error}")

    def init(*args):

        try:
            r = "FILE_SAVES/SAVE_REPORTS"
            d = "FILE_SAVES"
            q = "FILE_SAVES/ERROR_REPORTS/"
            os.mkdir(d, mode=0o777, dir_fd=None)
            os.mkdir(r, mode=0o777, dir_fd=None)
            os.mkdir(q, mode=0o777, dir_fd=None)



        except FileExistsError as error:

            File_Engine.error_found(error)


    def save_file(file_name, var_name, var_to_save):
        try:
            timenow = datetime.now()
            d = "FILE_SAVES/"
            var_to_save = str(var_to_save)
            tmp = []
            tmp.append(file_name)
            with open(d + file_name + ".py", 'w') as f:
                f.writelines(var_name + '=' + var_to_save)
                f.close()
                messagebox.showinfo(f"FileEngine", f"File: {file_name} Has Been Saved Succefully")
            for files in os.walk("FILE_SAVES"):
                with open(f'FILE_SAVES/SAVE_REPORTS/save_history{tmp}.log', 'w') as f:
                    f.writelines(f"Var_name:{var_name} Var_value: {var_to_save} \nTime Of Update: {timenow}\n")
                    f.close()

        except BaseException as error:
            print("SaveFile_Engine.init() to make engine directory")
            File_Engine.error_found(error)


    def dumpfile(Dict, filename):
        json_object = json.dumps(Dict)
        with open(f"{filename}.json", "w") as f:
            f.write(json_object)