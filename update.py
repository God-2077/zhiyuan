import datetime
import os
from sqlite3 import Blob
import sys
import subprocess

def run_command(command:list)->bool:
    print(f"running [{command}]", end="")
    try:
        subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}", end="\n")
        return False
    print(f"success running [{command}]", end="\n")
    return True

def main():
    local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"local_time: {local_time}")
    
    run_command(["git", "add", "."]) and run_command(["git", "commit", "-m", f"update: {local_time}"]) and run_command(["git", "push"])

if __name__ == "__main__":
    main()
