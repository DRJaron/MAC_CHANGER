# MADE BY YARON SHAGALOV

import subprocess
import argparse
import re
import json
import os

DEFAULT_MAC_FILE = "default_mac.json"

def get_arguments():
    parser = argparse.ArgumentParser(description="MAC address changer")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_argument("--reset", action="store_true", help="Reset MAC address to the original MAC address")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
   
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address!")

def save_default_mac(interface, mac_address):
    data = {interface: mac_address}
    with open(DEFAULT_MAC_FILE, 'w') as file:
        json.dump(data, file)
    print(f"[+] Saved default MAC address for {interface}: {mac_address}")

def load_default_mac(interface):
    if os.path.exists(DEFAULT_MAC_FILE):
        with open(DEFAULT_MAC_FILE, 'r') as file:
            data = json.load(file)
            return data.get(interface)
    return None    

options = get_arguments()

if options.reset:
    default_mac = load_default_mac(options.interface)
    if default_mac:
        print(f"[+] Resetting MAC address for {options.interface} to default: {default_mac}")
        change_mac(options.interface, default_mac)
    else:
        print(f"[!] No default MAC address found for {options.interface}")
else:
    current_mac = get_current_mac(options.interface)
    print(f"Current MAC = {current_mac}")

    if not os.path.exists(DEFAULT_MAC_FILE):
        save_default_mac(options.interface, current_mac)

    if options.new_mac:
        change_mac(options.interface, options.new_mac)
        current_mac = get_current_mac(options.interface)
        if current_mac == options.new_mac:
            print(f"MAC address was successfully changed to {current_mac}")
        else:
            print("[!] MAC address did not change!")

# defult mac = 00:0c:29:7b:85:3c   