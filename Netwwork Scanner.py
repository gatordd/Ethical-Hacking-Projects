#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_target():
    # creates an object that can handle user input / options after the .py command
    parser = argparse.ArgumentParser()

    # Adds options to the object
    parser.add_argument("-t", "--target", dest="target", help="Target IP address range. Ex: 10.0.2.1/24")

    # allows the object to understand what the user has entered, and handle it
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target, use -h or --help for more info.")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff:")
    arp_req_broad = broadcast/arp_request
    answered_list = scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]


    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_target()

scan_result = scan(options.target)
print_result(scan_result)
