#!/usr/bin/env python3
import os

os.system('clear')

def get_certificate(server_name):
    print(f"Retrieving certificate information for {server_name}...\n")
    command = f"openssl s_client -showcerts -servername {server_name} -connect {server_name}:443 2> /dev/null | openssl x509 -inform pem -noout -text"
    certificate_info = os.system(command)
    if certificate_info:
        print("openssl commands executed successfully.")
        return certificate_info
    else:
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a server name as an argument.")
        sys.exit(1)
    server_name = sys.argv[1]
    output = get_certificate(server_name)
    if output:
        print(output)
    else:
        print("No certificate information retrieved.")
