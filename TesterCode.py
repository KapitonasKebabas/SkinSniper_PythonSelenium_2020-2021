flaoutas = "Float: 0.005648656884"
floutINT = 0
strFlaot = ""
for simbolis in flaoutas:
    if ord(simbolis) >= 48 and ord(simbolis) <= 57:
        strFlaot += simbolis
    if ord(simbolis) == 44:
        strFlaot += "."
    if ord(simbolis) == 46:
        strFlaot += "."
floutINT = float(strFlaot)
print(floutINT)