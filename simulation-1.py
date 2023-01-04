from tkinter import *
from time import sleep

root = Tk()
canvas = Canvas(root, width=1000, height=1000)
root.title("Simulation")


canvas.grid(column=0,row=3)
tank1=canvas.create_line(100,100,100,300,300,300,300,100,fill='black',width=2)
tank2=canvas.create_line(600,600,600,800,800,800,800,600,fill='black',width=2)
rect1=canvas.create_rectangle(102,120,298,298, fill="skyblue",width=0)
rect2=canvas.create_rectangle(602,800,798,800, fill="skyblue",width=0)
#pipe=canvas.create_polygon(298,270,450,270,450,770,604,770,604,750,470,750,470,250,298,250,fill="skyblue")
pipe=canvas.create_line(300,270,450,270,450,770,600,770 ,fill='black',width=2)
pipe=canvas.create_line(300,250,470,250,470,750,600,750 ,fill='black',width=2)





x=120
y=800

 
  
def start():
    
  
  global x,rect1,after_id,rect2,y,xx,yy,rect
  xx=300
  yy=320
  if x<298: 
    x=x+1
    canvas.delete(rect1)
   
   
    for i in range(20):
        q='sqr'+str(i)
        canvas.delete(q)
    rect1=canvas.create_rectangle(102,x,298,298,fill="skyblue",width=0)
    canvas.delete(rect2)
    y=y-1
    rect2=canvas.create_rectangle(602,y,798,800, fill="skyblue",width=0)
    if x%2==0:
    
        for i in range(4):
            q='sqr'+str(i)
            rect=canvas.create_rectangle(xx,270,yy,250 ,fill="skyblue",width=0,tags=q)
            xx=xx+40
            yy=yy+40
    else:
        xx=320
        yy=340
        for i in range(4):
            q='sqr'+str(i)
                  
        
            rect=canvas.create_rectangle(xx,270,yy,250 ,fill="skyblue",width=0,tags=q)
            xx=xx+40
            yy=yy+40
    
    if x%2==0:
        xc=270
        yc=290
    
        for i in range(12):
            q='sqr'+str(i)
            rect=canvas.create_rectangle(450,xc,470,yc,fill="skyblue",width=0,tags=q)
            xc=xc+40
            yc=yc+40
    else:
        xc=290
        yc=310
        for i in range(12):
            q='sqr'+str(i)
                  
        
            rect=canvas.create_rectangle(450,xc,470,yc,fill="skyblue",width=0,tags=q)
            xc=xc+40
            yc=yc+40
    if x%2==0:
        xv=450
        yv=470
        for i in range(4):
            q='sqr'+str(i)
            rect=canvas.create_rectangle(xv,770,yv,750 ,fill="skyblue",width=0,tags=q)
            xv=xv+40
            yv=yv+40
    else:
        xv=470
        yv=490
        for i in range(4):
            q='sqr'+str(i)
                  
        
            rect=canvas.create_rectangle(xv,770,yv,750 ,fill="skyblue",width=0,tags=q)
            xv=xv+40
            yv=yv+40
    after_id=canvas.after(100,start)
    if x==298:
        canvas.after_cancel( after_id)
   

def stop1():
    
    canvas.after_cancel( after_id)
        

btn=Button(text='Start',width=10,height=3,command=start)
btn.configure(relief=RIDGE)
btn.grid(column=1,row=0)

btn=Button(text='Stop',width=10,height=3,command=stop1)
btn.configure(relief=RIDGE)
btn.grid(column=1,row=1)



root.mainloop()