# MAC Changer

## Description
`MAC Changer` is a Python script designed to change the MAC address of a network interface on a Linux system. It allows users to either specify a new MAC address or reset the MAC address to its original (default) state.

## Features
- Change the MAC address of a specified network interface.
- Save the default MAC address for future resets.
- Reset the MAC address to the saved default.

## Requirements
- Python 3.x
- Linux operating system (for `ifconfig` command)
- `argparse` module (standard with Python 3.x)
- `subprocess` module (standard with Python 3.x)
- `json` module (standard with Python 3.x)
- `re` module (standard with Python 3.x)

## Installation
No installation required. Simply download the script and run it using Python.

## Usage

### Change MAC Address
To change the MAC address of a specific interface:
```bash
python mac_changer.py -i <interface> -m <new_mac_address>
```
Example:
```bash
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

### Reset MAC Address
To reset the MAC address to the original (default) MAC address:
```bash
python mac_changer.py -i <interface> --reset
```
Example:
```bash
python mac_changer.py -i eth0 --reset
```

## Options
- `-i, --interface` : The network interface to change the MAC address (e.g., `eth0`, `wlan0`).
- `-m, --mac` : The new MAC address to set for the interface.
- `--reset` : Reset the MAC address to the original (default) MAC address.

## How It Works
1. **Change MAC**:
    - The script takes the interface and the new MAC address as input.
    - It brings the interface down, changes the MAC address, and then brings the interface up.
2. **Save Default MAC**:
    - The script saves the current MAC address to a JSON file (`default_mac.json`) the first time it is run.
3. **Reset MAC**:
    - If the `--reset` option is used, the script retrieves the saved MAC address from `default_mac.json` and sets it back.

## Example
```bash
# Change the MAC address of eth0 to 00:11:22:33:44:55
python mac_changer.py -i eth0 -m 00:11:22:33:44:55

# Reset the MAC address of eth0 to the default
python mac_changer.py -i eth0 --reset
```

## Troubleshooting
- Ensure you have administrative privileges (run the script with `sudo` if necessary).
- Make sure `ifconfig` is available on your system.
- Check for typos in the interface name or MAC address.

## License
This project is licensed under the MIT License.

## Disclaimer
This script is intended for educational purposes only. Use it responsibly and ensure you have permission to change MAC addresses on the network you are using.

