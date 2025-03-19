# This is the template code for the CNE335 Final Project
# Mustafa Alghuraibawi
# CNE 335 Winter

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Mustafa")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    EC2server = Server('34.211.5.59')
    # TODO - Call Ping method and print the results
    print(EC2server.ping())
