import datetime
import subprocess
from typing import List

def run_command(command: List[str]) -> bool:
    """
    执行外部命令并返回执行是否成功。

    Args:
        command: 命令及其参数列表，如 ["ls", "-l"]

    Returns:
        成功返回 True，否则返回 False。
    """
    print(f"Running command: {' '.join(command)}")
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        # 若需要查看正常输出，可在此记录 result.stdout
        print(f"Command succeeded.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        if e.stdout:
            print(f"STDOUT:\n{e.stdout}")
        if e.stderr:
            print(f"STDERR:\n{e.stderr}")
        return False
    except (FileNotFoundError, PermissionError) as e:
        print(f"System error while running command: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def main():
    local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"local_time: {local_time}")
    
    run_command(["git", "add", "."]) and run_command(["git", "commit", "-m", f"update: {local_time}"]) and run_command(["git", "push"])

if __name__ == "__main__":
    main()
