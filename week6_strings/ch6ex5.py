str = 'X-DSPAM-Confidence:0.8475'
start = str.find(':')
out = str[start+1:]
out = float(out)
kind = type(out)
print(out)
