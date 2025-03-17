# This is the code for the CNE335 Final Project
# Mason Jones
# CNE 335 Winter

from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Mason Jones")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server = Server('35.88.147.193')
    print(server.ping())
