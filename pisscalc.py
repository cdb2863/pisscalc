#!/usr/bin/python
# Python Internet Subnet(S) Calculator
# Well written subnet calculator for those who flunked out of networking school, or those whom'st have since lost the subnetting juice
# © 2022 Christopher D. Beliveau
import argparse
import ipaddress as ip

def main():
    # Initialize argument parser, add arguments, and parse arguments.
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('subnet', type=str, help='the subnet you want more information about')
    args = arg_parser.parse_args()

    # Process the input
    the_subnet = ip.ip_network(args.subnet)
    usable_hosts = []
    for host in the_subnet.hosts():
        usable_hosts.append(host)
    first_usable = usable_hosts[0]
    last_usable = usable_hosts[-1]
    n_usable = len(usable_hosts)

    # Print information about the subnet
    print(f'[Network Address]: {the_subnet.network_address}')
    print(f'[Subnet Mask]: {the_subnet.netmask}')
    print(f'[Wildcard Mask]: {the_subnet.hostmask}')
    print(f'[Prefix Length]: /{the_subnet.prefixlen}')
    print(f'[Usable Range]: {first_usable} - {last_usable}')
    print(f'[Broadcast Address]: {the_subnet.broadcast_address}')
    print()
    return

if __name__ == '__main__':
    main()