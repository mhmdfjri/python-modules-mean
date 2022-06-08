import math
def mean(data):
    print('Mean dari data:',round(sum(data)/len(data),2))
def var(data):
    avg = sum(data)/len(data)
    var = sum((x-avg)**2 for x in data)/len(data)
    print(f'Variansi dari data: {var:,.2f}')
def std(data):
    avg = sum(data)/len(data)
    std = math.sqrt(sum((x-avg)**2 for x in data)/len(data))
    print(f'Standar Deviasi dari data: {std:,.2f}')
def median(data):
    n = len(data)
    data.sort()
    if len(data) % 2 == 0:
        m1 = data[n//2]
        m2 = data[n//2 - 1]
        med = (m1 + m2)/2
    else:
        med = data[n//2]
    print(f'Median dari data: {med:,.2f}')