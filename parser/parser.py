import re


f = open("cryptoassets.txt", "r", encoding="utf-8")
# split into lines
cal = f.read().split("\n")

# cc start
cc_start = None

# token start
token_start = None

# get line for cryptocurrencies
for line in range(len(cal)):
    if "## Crypto currencies" in cal[line]:
        cc_start = line

    if "## Tokens" in cal[line]:
        token_start = line

# parse the cryptocurrencies into csv
cc_cal = cal.copy()
cc_number = None

# match cc number
match = re.search(r'\((\d+)\)', cc_cal[cc_start])
if match:
    cc_number = match.group(1)
    
cc_title = "name,ticker,supported on Ledger Live?,ledger id"

cc_str = cc_title
cc_str += "\n"
for line in range(cc_start+2, token_start-1):
    if "|--|--|--|--|" in cc_cal[line]:
        del cc_cal[line]

    
    cc_line = cc_cal[line][1:-1].split(" | ")
    line_str = ""
    for x in cc_line:
        line_str += x+","
    cc_str += line_str[:-1]
    cc_str += "\n"

# TEST PRINT
# print(cc_number)
# print(cc_str)

# ---------------------------------------------------

token_title = "parent currency,ticker,contract,name,status,ledger id"
token_cal = cal.copy()
token_str = token_title
token_str += "\n"

# match token number
match = re.search(r'\((\d+)\)', token_cal[token_start])
if match:
    token_number = match.group(1)

for line in range(token_start+2, len(token_cal)-2):
    if "|--|--|--|--|--|--|" in token_cal[line]:
        del token_cal[line]

    
    token_line = token_cal[line][1:-1].split(" | ")
    line_str = ""

    if len(token_line) > 6:
        merged = token_line[3]+" // "+token_line[4]
        token_line[3] = merged
        token_line.pop(4)
        
    for x in token_line:

        if "," in x:
            x = x.replace(",", ";")
            
        line_str += x+","
        
    token_str += line_str[:-1]
    token_str += "\n"

# print(token_number)
# print(token_str)

# Assign to csv

with open('cc.csv', 'w', encoding="utf-8") as out:
    out.write(cc_str)
with open('token.csv', 'w', encoding="utf-8") as out:
    out.write(token_str)
