inputs = input()
hr = 0

if inputs[8] == 'A':
    if inputs[0] == '1' and inputs[1] == '2':
        hr = 0
    else:
        hr = int(inputs[0])*10 + int(inputs[1])
else:
    if inputs[0] == '1' and inputs[1] == '2':
        hr = 12
    else:
        hr = int(inputs[0])*10 + int(inputs[1]) + 12

if len(str(hr)) == 1:
    temp = str(hr)
    hr = '0' + temp

print(hr, inputs[2:8], sep="")
