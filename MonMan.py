import subprocess
def ps(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode != 0:
        print(f"Command failed: {cmd}")
        print(f"Error: {completed.stderr.decode('utf-8') if completed.stderr else 'No error output'}")
        exit(1)
    if not completed.stdout:
        return completed.returncode
    return completed.stdout.decode('utf-8')


disInfo = ps("Get-DisplayInfo")
print(disInfo)


monDisable = input("Enter ID of monitor to toggle: ")
selectedMon = ps(f"Get-DisplayInfo | Where-Object -Property DisplayId -EQ {monDisable}")
selectedMonActive = ps(f"(Get-DisplayInfo | Where-Object -Property DisplayId -EQ {monDisable}).Active").strip() == 'True'
if selectedMonActive:
    print(f"Disabling monitor {monDisable}")
    ps(f"Disable-Display -DisplayId {monDisable}")
else:
    print(f"Enabling monitor {monDisable}")
    ps(f"Enable-Display -DisplayId {monDisable}")