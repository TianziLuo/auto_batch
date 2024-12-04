import subprocess
        
def run_batch_as_admin(batch_file_path):
        
        # build command
        command = f'powershell -Command "Start-Process cmd.exe -ArgumentList \'/c "{batch_file_path}"\' -Verb runAs"'
        
        # run command
        subprocess.run(command, shell=True, check=True)
        #  f-string
        print(f"{batch_file_path} is run")
