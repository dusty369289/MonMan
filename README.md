# MonMan

**MonMan** (Monitor Manager) is a Windows utility for managing multiple monitors through PowerShell commands. It allows you to easily enable and disable displays without navigating through Windows display settings.

## Features

- 🖥️ Interactive monitor selection
- ⚡ Quick toggle monitors on/off
- 📋 Display detailed monitor information (ID, name, status)
- 🐍 Python-based with PowerShell integration
- 💻 Multiple launch options (Python, PowerShell, Batch)

## Requirements

- **Operating System**: Windows (with PowerShell support)
- **Python**: Python 3.x (for `MonMan.py`)
- **PowerShell Module**: [DisplayConfig](https://www.powershellgallery.com/packages/DisplayConfig) module

### Installing DisplayConfig Module

The scripts rely on PowerShell's `DisplayConfig` module for monitor management. Install it with:

```powershell
Install-Module -Name DisplayConfig -Scope CurrentUser
```

Or as Administrator:

```powershell
Install-Module -Name DisplayConfig
```

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/dusty369289/MonMan.git
   cd MonMan
   ```

2. Ensure Python 3.x is installed (for Python script):
   ```bash
   python --version
   ```

3. Install the DisplayConfig PowerShell module (see Requirements above)

## Usage

MonMan provides three different scripts for different use cases:

### 1. Interactive Monitor Manager (`MonMan.py`)

The Python script provides an interactive interface to toggle any monitor:

```bash
python MonMan.py
```

**How it works:**
1. Displays a list of all connected monitors with their IDs and status
2. Prompts you to enter the monitor ID you want to toggle
3. Enables the monitor if it's disabled, or disables it if it's enabled

**Example output:**
```
DisplayId : 1
DisplayName : SAMSUNG
Active : True
...

Enter ID of monitor to toggle: 1
Disabling monitor 1
```

### 2. Preset Monitor Toggle (`MonMan.ps1`)

The PowerShell script is configured to toggle a specific monitor by name:

```powershell
.\MonMan.ps1
```

**Configuration:**
- Edit the script to change the target monitor name:
  ```powershell
  $tvmonOB = Get-DisplayInfo | Where-Object -Property DisplayName -EQ 'SAMSUNG'
  ```
- Replace `'SAMSUNG'` with your monitor's display name

### 3. Batch File Launcher (`MonMan.bat`)

The batch file is a simple wrapper that launches the PowerShell script:

```cmd
MonMan.bat
```

**Note:** Update the path in `MonMan.bat` to point to your `MonMan.ps1` location:
```batch
set PS_COMMAND="C:\Path\To\Your\MonMan.ps1"
```

## Common Use Cases

### Toggle a specific monitor quickly
Use `MonMan.ps1` configured for your preferred monitor. Great for:
- Switching to/from a TV display
- Disabling a secondary monitor for gaming
- Quick monitor configuration changes

### Choose which monitor to toggle
Use `MonMan.py` for an interactive experience where you can:
- See all available monitors
- Select which one to toggle each time
- View monitor status before making changes

## Troubleshooting

### "Get-DisplayInfo: The term 'Get-DisplayInfo' is not recognized"
- Install the DisplayConfig module: `Install-Module -Name DisplayConfig`

### "Command failed" errors
- Ensure you're running PowerShell with appropriate permissions
- Some display operations may require administrator privileges

### Script doesn't find your monitor
- Run `Get-DisplayInfo` in PowerShell to see available monitors
- Update the DisplayName filter in `MonMan.ps1` to match your monitor's exact name

## DisplayConfig Commands

This project uses the following PowerShell DisplayConfig commands:

- `Get-DisplayInfo` - Retrieves information about all displays
- `Enable-Display -DisplayId <id>` - Enables a display by ID
- `Disable-Display -DisplayId <id>` - Disables a display by ID

For more information, visit: https://www.powershellgallery.com/packages/DisplayConfig

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests for improvements!

## Author

Created by dusty369289
