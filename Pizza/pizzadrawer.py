from tkinter import *
import random

#colors = ["red", "orange", "green", "blue", "violet"]
colors = ["blue"]
    
#scale = 1
maxwidth = maxheight = 1000
    
rmin = cmin = float('+inf')
rmax = cmax = float('-inf')
    
slices = []
    
fin = open("medium_out.txt","r")
   
for slicenumber in range(int(fin.readline())):
    # r1, c1, r2, c2 = row(int)
    riga = fin.readline()
    r1, c1, r2, c2 = riga.split()
    r1 = int(r1)
    c1 = int(c1)
    r2 = int(r2)
    c2 = int(c2)
        
    r2 += 1; c2 += 1
    rmin = min(r1, rmin)
    cmin = min(c1, cmin)
    rmax = max(r2, rmax)
    cmax = max(c2, cmax)
    slices.append((r1, c1, r2, c2))
    
scale = min(maxwidth // cmax, maxheight // rmax)
    
master = Tk()
w = Canvas(master, width=cmax*scale, height=rmax*scale)
w.pack()
    
for slice in slices:
    print(slice)
    r1, c1, r2, c2 = [dim * scale for dim in slice]
    w.create_rectangle(c1, r1, c2, r2, fill=random.choice(colors))
  
mainloop()

