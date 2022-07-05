import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-option', required=True)
parser.add_argument('-text file', required=True)
try:
    option = sys.argv[1]
    file = sys.argv[2]
    option_lst = ['-l', '-c', '-w', '-n', '-a', '-h']
    if option not in option_lst:
        print("Only Allowed options are {}".format(option_lst))

    def read_file(file, option):
        with open(file) as myfile:
            if option == '-l':
                result = sum(1 for line in myfile)

            if option == '-c':
                text = myfile.read().strip().split()
                result = sum(len(word) for word in text)
            
            if option == '-w':
                words = myfile.read().strip().split()
                result = len(words)

            if option == '-n':
                words = myfile.read()
                result = re.findall(r"[-+]?\d*\.\d+|\d+", words)
            
            if option == '-a':
                words = myfile.read()
                result = re.sub('[^a-zA-Z]+', '', words)
            return result
    response = read_file(file, option)
    print("{} {}".format(response, file))
except Exception:
    parser.print_usage()


