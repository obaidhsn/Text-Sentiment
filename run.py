import subprocess

# path to virtual environment's Python interpreter
venv_python_path = "env/Scripts/python.exe"  

# path to Python script
script_path = "main.py"

# Command to run the script using the virtual environment's Python interpreter
command = [venv_python_path, script_path]

try:
    # Run the script
    subprocess.check_call(command)
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}")
