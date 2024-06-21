import subprocess

if __name__ == "__main__":
    # List the commands in order
    cmd = ['python3', 'testcmd.py']
    # Run the subprocess.run() command to execute the commands then capture the output
    result = subprocess.run(cmd, capture_output=True, check=False, text=True)
    
    # Checks if it's an error that's returned or no errors
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)
    
    # Exit program with the exit code of the computed command
    exit(result.returncode)
