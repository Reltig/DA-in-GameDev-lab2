import gspread
import numpy as np

gc = gspread.service_account(filename='unity-370611-f6118ba12b9e.json')
sh = gc.open("UnitySheets")
x = [3, 21, 22, 34, 54, 34, 55, 67, 89, 99]
x = np.array(x)
y = [2, 22, 24, 65, 79, 82, 55, 130, 150, 199]
y = np.array(y)
i = 0
while i < len(x):
    i+=1
    a,b = map(str, [x[i-1],y[i-1]])
    a = a.replace('.', ',')
    b = b.replace('.', ',')
    sh.sheet1.update(('A' + str(i)), a)
    sh.sheet1.update(('B' + str(i)), b)