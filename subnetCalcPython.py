import ipaddress

def subnet_calculator():
    print("Subnet Calculator")
    print("-----------------")
    
    while True:
        # Get user input
        ip_input = input("Enter IP address (e.g., 192.168.1.1 or 192.168.1.1/24): ")
        
        try:
            # Parse the network
            if '/' in ip_input:
                network = ipaddress.IPv4Network(ip_input, strict=False)
            else:
                subnet_mask = input("Enter subnet mask (e.g., 255.255.255.0): ")
                network = ipaddress.IPv4Network(f"{ip_input}/{subnet_mask}", strict=False)
            
            # Display network information
            print("\nNetwork Information:")
            print(f"IP Address: {network.network_address + 1}")  # First usable host
            print(f"Network Address: {network.network_address}")
            print(f"Broadcast Address: {network.broadcast_address}")
            print(f"Subnet Mask: {network.netmask}")
            print(f"Wildcard Mask: {network.hostmask}")
            print(f"CIDR Notation: /{network.prefixlen}")
            print(f"Total Hosts: {network.num_addresses}")
            print(f"Usable Hosts: {network.num_addresses - 2}")
            
            # Calculate and display IP range
            if network.num_addresses > 2:
                print(f"Host Range: {network.network_address + 1} - {network.broadcast_address - 1}")
            else:
                print("Host Range: N/A (network doesn't support usable hosts)")
            
            # Calculate network class
            first_octet = int(str(network.network_address).split('.')[0])
            if first_octet < 128:
                network_class = 'A'
            elif first_octet < 192:
                network_class = 'B'
            elif first_octet < 224:
                network_class = 'C'
            elif first_octet < 240:
                network_class = 'D (Multicast)'
            else:
                network_class = 'E (Reserved)'
            print(f"Network Class: {network_class}")
            
            # Check if IP is private
            print(f"Private Network: {'Yes' if network.is_private else 'No'}")
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter valid IP address and subnet mask.")
        
        # Ask to continue
        choice = input("\nCalculate another subnet? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    subnet_calculator()