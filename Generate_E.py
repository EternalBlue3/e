from decimal import Decimal, getcontext
getcontext().prec = int(input("Precision: "))+10
e = Decimal(0)
f = Decimal(1)
n = Decimal(1)
while True:
    olde = e
    e += Decimal(1) / f
    if e == olde:
        break
    f *= n
    n += Decimal(1)

e = str(e)
e = e[:len(e)-10]

File_Write = str(e)
fh = open("E_100k.txt","w")
fh.write(File_Write)
fh.close()
