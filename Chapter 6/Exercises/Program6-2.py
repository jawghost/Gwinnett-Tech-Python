# This program reads and displays the contents
# of the philosophers.txt file.
def main():
    # Open a file named philosophers.txt
    infile = open('philosphers.txt', 'r')

    #Read the file's contents.
    file_contents = infile.read()
    
