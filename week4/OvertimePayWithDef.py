hours = input('How many hours did you work? ')
rate = input('What is you hourly rate? ')
H = float(hours)
R = float(rate)

def Computepay(H, R):
    if H <= 40:
        normalpay = H * R
        return normalpay
    elif H > 40:
        P = R * 40
        OTH = H - float(40) #OTH = Over Time Hours
        OTR = 1.5 * R #OTR = Over Time Rate
        OTP = OTR * OTH #OTP = Over Time Pay
        TP = OTP + P #TP = total pay
        return TP
    
pay = Computepay(H, R)

print ('your total pay will be ', pay)
