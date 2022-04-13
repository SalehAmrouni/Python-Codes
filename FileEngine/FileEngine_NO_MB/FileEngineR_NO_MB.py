from datetime import datetime
import os



class File_Engine(object):

    def __init__(self):
        pass

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

            for files in os.walk("FILE_SAVES"):
                with open(f'FILE_SAVES/SAVE_REPORTS/save_history{tmp}.log', 'w') as f:
                    f.writelines(f"Var_name:{var_name} Var_value: {var_to_save} \nTime Of Update: {timenow}\n")
                    f.close()
