str = 'X-DSPAM-Confidence:0.8475'  #string example
start = str.find(':') #searching for semicolon
out = str[start+1:] #Moving forward one position from semicolon
out = float(out)
kind = type(out)
print(out)
