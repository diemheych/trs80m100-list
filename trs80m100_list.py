#
# trs80m100_list.py - Convert tokenised TRS 80 Model 100/102/200 BASIC program file to text
#
# Usage: trs80m100_list.py [-h]        Help
#                          [-cr]       Add CR at end of line (*nix/MacOS)
#                          infile      Tokenised TRS 80 Model 100/102/200 BASIC program file
#
#
# The TRS-80 Model 100/102/200 and the compatible Kyocera Kyotronic-85 and Olivetti M10
# all use the same tokenized BASIC file format. This program reads a tokenized BASIC file
# and displays the readable text version of the program.
#
# The converted program can be read and edited and loaded back into the computer as a text file
# (.DO extension).
#
# As the file format is very simple with no header or magic numbers there is no error checking.
#
# Note: the NEC PC-8xxx portable computers do not use the same tokenized BASIC file format.
#
# Copyright (c) 2024 Darren Hosking @calculatorclique https://github.com/diemheych
# 
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
#
import argparse

Tokens = {
128: "END",
129: "FOR",
130: "NEXT",
131: "DATA",
132: "INPUT",
133: "DIM",
134: "READ",
135: "LET",
136: "GOTO",
137: "RUN",
138: "IF",
139: "RESTORE",
140: "GOSUB",
141: "RETURN",
142: "REM",
143: "STOP",
144: "WIDTH",
145: "ELSE",
146: "LINE",
147: "EDIT",
148: "ERROR",
149: "RESUME",
150: "OUT",
151: "ON",
152: "DSKO$",
153: "OPEN",
154: "CLOSE",
155: "LOAD",
156: "MERGE",
157: "FILES",
158: "SAVE",
159: "LFILES",
160: "LPRINT",
161: "DEF",
162: "POKE",
163: "PRINT",
164: "CONT",
165: "LIST",
166: "LLIST",
167: "CLEAR",
168: "CLOAD",
169: "CSAVE",
170: "TIME$",
171: "DATE$",
172: "DAY$",
173: "COM",
174: "MDM",
175: "KEY",
176: "CLS",
177: "BEEP",
178: "SOUND",
179: "LCOPY",
180: "PSET",
181: "PRESET",
182: "MOTOR",
183: "MAX",
184: "POWER",
185: "CALL",
186: "MENU",
187: "IPL",
188: "NAME",
189: "KILL",
190: "SCREEN",
191: "NEW",
192: "TAB(",
193: "TO",
194: "USING",
195: "VARPTR",
196: "ERL",
197: "ERR",
198: "STRING$",
199: "INSTR",
200: "DSKI$",
201: "INKEY$",
202: "CSRLIN",
203: "OFF",
204: "HIMEM",
205: "THEN",
206: "NOT",
207: "STEP",
208: "+",
209: "-",
210: "*",
211: "/",
212: "^",
213: "AND",
214: "OR",
215: "XOR",
216: "EQV",
217: "IMP",
218: "MOD",
219: "\\",
220: ">",
221: "=",
222: "<",
223: "SGN",
224: "INT",
225: "ABS",
226: "FRE",
227: "INP",
228: "LPOS",
229: "POS",
230: "SQR",
231: "RND",
232: "LOG",
233: "EXP",
234: "COS",
235: "SIN",
236: "TAN",
237: "ATN",
238: "PEEK",
239: "EOF",
240: "LOC",
241: "LOF",
242: "CINT",
243: "CSNG",
244: "CDBL",
245: "FIX",
246: "LEN",
247: "STR$",
248: "VAL",
249: "ASC",
250: "CHR$",
251: "SPACE$",
252: "LEFT$",
253: "RIGHT$",
254: "MID$",
255: "'"
}

parser = argparse.ArgumentParser(description='Convert tokenised TRS 80 Model 100/102/200 BASIC program file to text')
parser.add_argument('infile')
parser.add_argument("-cr", action="store_true",help="Add CR at end of line (*nix/MacOS)")

args = vars(parser.parse_args())
arg_count = len(args)

f = open(args['infile'],"rb")
pgm = bytearray(f.read())
f.close()
#print(pgm)
length = len(pgm)

current_token = 2

while current_token < length:
    line = pgm[current_token] + pgm[current_token + 1] * 256
    print(line, end=' ')
    current_token = current_token + 2
    while pgm[current_token] != 0:
        if pgm[current_token] > 127:
            print(Tokens[pgm[current_token]],end='')
            current_token = current_token + 1
        else:
            if pgm[current_token:current_token+3] == b':\x8e\xff':
                print("'",end='')
                current_token = current_token + 3
            else:
                print(chr(pgm[current_token]), end='')
                current_token = current_token + 1
    if args['cr']: print('\r', end='')
    print()
    current_token = current_token + 3
     
