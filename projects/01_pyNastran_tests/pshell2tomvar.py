import pandas as pd

path = 'models/source.bdf'

# Using Pandas with a column specification
col_specification = [(0, 8), (9, 16), (17, 24), (25, 32), (33, 40), (34, 48), (49, 56), (57,64), (58,72), (73, 80)]
data = pd.read_fwf(path, colspecs=col_specification, header=None)
#data.columns=['keyword','idx','f3','f4','f5','f6','f7','f8','f9']
pshells_df = data[(data[0]=="PSHELL")]

for i, p in pshells_df.iterrows():
    thickness = float(p[3])
    pid = int(p[1])
    xlb = thickness
    xub = 15.0
    #1 2 3 4 5 6 7 8 9 10
    #TOMVAR ID TYPE PID PNAME/FID XINIT XLB XUB DELXV
    #“DLINK” TID C0 C1
    #“DDVAL” DSVID
    #“STRESS” STLIM
    if (thickness < xub):
        print("{keyword:8s}{id:>8s}{type:>8s}{pid:>8s}{pname:>8s}{xinit:>8s}{xlb:>8s}{xub:>8s}{delxv:>8s}".format(
            keyword="TOMVAR", id=str(pid), type="PSHELL",pid=str(pid), pname="T",xinit=str(thickness),xlb=str(xlb), xub=str(xub), delxv="" ))