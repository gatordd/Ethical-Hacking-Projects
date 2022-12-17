#!/usr/bin/env python
# Above is the shebang (not sure how to figure this out; look up later)

import subprocess
import optparse

def get_arguments():
    # creates an object that can handle user input / options after the .py command
    parser = optparse.OptionParser()

    # Adds options to the object
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", "--MAC", dest="new_mac", help="New MAC Address")

    # allows the object to understand what the user has entered, and handle it
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use -h or --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC, use -h or --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # Formated in list form so that it hardens the user input and user cannot input another linux command
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
