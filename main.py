import argparse
from cracker import Cracker

parser = argparse.ArgumentParser(description='Excel password cracker')

parser.add_argument("-w", "--wordlist", help="Add wordlist to crack password", default="default")
parser.add_argument("-f", "--file", help="Add excel filename to crack.", required=True)
parser.add_argument("-v", "--verbose", help="Prints out each password.", action="store_true")

args = parser.parse_args()
print(args)


if args.file:
    print("Running Josh's excel cracker...")
    newCracker = Cracker(str(args.file), bool(args.verbose), str(args.wordlist))
