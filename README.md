# Excel-Password-Recover

`Excel-Password-Recover` is an open-source tool that could help you recover lost passwords for your excel spreadsheets. This works for macOS, but support for Windows is iffy.

> Disclaimer: This tool is limited to security research only, and the user assumes all legal and related responsibilities arising from its use! The author assumes no legal responsibility!

> Note: This project is unmaintained as it is far more efficient to crack the hash itself via a rainbow table rather than brute force. I realized this after I made this and quickly switched methods.

## Usage

### Run as Bash
> bash run.sh

### Run as Python Module

> python main.py --file FILENAME --wordlist WORDLIST -v

```
ARGUMENTS:
   --file, -f               excel file to crack (.xlsx) (required)

GLOBAL OPTIONS:

   --verbose, -v            verbose (optional, default: false)
   --wordlist, -w           wordlist (.txt) (optional)
   --help, -h               show help (default: false)```
