# trs80m100-list
Python program to convert tokenised TRS 80 Model 100/102/200 BASIC program file to text.

The TRS-80 Model 100/102/200 and the compatible Kyocera Kyotronic-85 and Olivetti M10
all use the same tokenized BASIC file format. This program reads a tokenized BASIC file
and displays the readable text version of the program.

The converted program can be read and edited and loaded back into the computer as a text file
(.DO extension) or used to port to other versions of BASIC.

As the file format is very simple with no header or magic numbers there is no error checking.

Note: the NEC PC-8xxx portable computers do not use the same tokenized BASIC file format.

# Usage
```
Usage: trs80m100_list.py [-h] [-cr] infile

Convert tokenised TRS 80 Model 100/102/200 BASIC program file to text

positional arguments:
  infile

optional arguments:
  -h, --help  show this help message and exit
  -cr         Add CR at end of line (*nix/MacOS)
```
# References
File format details from: http://fileformats.archiveteam.org/wiki/Tandy_200_BASIC_tokenized_file
