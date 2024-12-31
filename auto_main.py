
import time
import os
from run_firewall import run_batch_as_admin
from openMysql import open_path,close_path
from window_position import set_window_position

batch_file_path_firewall = r"C:\uServePro\FireWall.bat"
batch_file_path_language = r"C:\uServePro\install_services_auto.bat"
mysql_workbench_path = r"C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe"
destop_path = os.path.join(os.path.expanduser("~"), "Desktop")
mysql_process_name = "MySQLWorkbench.exe"
desktop_process_name = "explorer.exe"

#step 1 run batches
run_batch_as_admin(batch_file_path_firewall)
time.sleep(6)
run_batch_as_admin(batch_file_path_language)
#step 2: open Mysql
open_path(mysql_workbench_path)
set_window_position("MySQL Workbench", 900, 100, 800, 600) 
time.sleep(25)
#step 3
open_path(destop_path)
set_window_position("explorer", 100, 100, 800, 600)



