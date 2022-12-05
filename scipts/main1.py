import gspread
import numpy as np

gc = gspread.service_account(filename='unity-370611-f6118ba12b9e.json')
sh = gc.open("UnitySheets")
price = np.random.randint(2000, 10000, 11)
mon = list(range(1,11))
i = 0
while i<= len(mon):
    i+=1
    if i==0:
        continue
    else:
        tempInf = ((price[i-1] - price[i-2])/price[i-2])*100
        tempInf = str(tempInf)
        tempInf = tempInf.replace('.', ',')
        sh.sheet1.update(('A' + str(i)), str(i))
        sh.sheet1.update(('B' + str(i)), str(price[i-1]))
        sh.sheet1.update(('C' + str(i)), tempInf)
        print(tempInf)