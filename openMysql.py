import os
import psutil 
import time

def open_path(path):
    
    if os.path.exists(path):
        os.startfile(path)  
    else:
        print(f"Please {path} check path")

def close_path(process_name):
    process_name = "MySQLWorkbench.exe"  
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            try:
                proc.terminate()  
                print(f"{process_name} is closed (PID: {proc.info['pid']})")
            except psutil.NoSuchProcess:
                print("can't find the process")
            except Exception as e:
                print(f"can not clsse the process: {e}")


"""
if __name__ == "__main__":
    open_mysql_workbench()
    time.sleep(10)
    close_mysql_workbench()
"""