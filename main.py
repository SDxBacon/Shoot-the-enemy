from tkinter import *
import time

class canvas(Canvas) :
    def __init__ (self) :
        self.root=Tk()
        self.root.title('射擊遊戲')
        super(canvas,self).__init__(self.root,width=640,height=480,bg='#ffffff')
        self.pack()
        rd=[[1,0,0,0]
        ,[2,0,0,0]
        ,[2,1,0,0]
        ,[3,3,1,0]
        ,[5,4,1,1]
        ,[5,5,3,2]
        ,[5,6,3,3]
        ,[5,5,5,5]]
        self.step()
        for dk in rd:
            self.mob1.ru(int(dk[0]))
            self.mob2.ru(int(dk[1]))
            self.mob3.ru(int(dk[2]))
            self.mob4.ru(int(dk[3]))
            while len(self.mob1.items+self.mob2.items+self.mob3.items+self.mob4.items)>0:
                self.loop()
        self.sp.dkkd+=100
        self.sp.dk+=100
        self.mob1.ru(15)
        self.mob2.ru(15)
        self.mob3.ru(10)
        self.mob4.ru(10)
        while len(self.mob1.items+self.mob2.items+self.mob3.items+self.mob4.items)>0:
                self.loop()
        self.create_text(320,240,text='you win')
        self.root.mainloop()

    def step(self):
        self.mob1=mob1(self)
        self.mob2=mob2(self)
        self.mob3=mob3(self)
        self.mob4=mob4(self)

        self.sp=sprinnn(self)
    
    def loop(self):
        self.sp.loop(self.mob1.xys,self.mob3.xys)
        self.mob1.loop(self.sp.sixy,self.sp.xy)
        self.mob2.loop(self.sp.sixy,self.sp.xy)
        self.mob3.loop(self.sp.sixy,self.sp.xy)
        self.mob4.loop(self.sp.sixy,self.sp.xy)

        self.sp.dkkd-=self.mob1.ud+self.mob2.ud+self.mob3.ud+self.mob4.ud

        if self.sp.dkkd<1:
            import sys;sys.exit()

        self.root.update()
        time.sleep(0.01)

class sprinnn:
    def __init__(self,canvas):
        self.canvas=canvas
        self.x = 0
        self.sif=si(canvas)
        self.item = self.canvas.create_rectangle(200,430,250,480,fill='Black')
        self.canvas.bind('<Motion>',self.mot)
        self.canvas.bind('<B1-Motion>',self.b1mot_si)
        self.canvas.bind('<Button-1>',self.sit)
        self.moveby(self.x)
        self.dk=50
        self.time=0
        self.dkkd=50
        self.timee=0
        self.text= self.canvas.create_text(50,10,width=80,text='剩餘子彈數'+str(self.dk))
        self.text2= self.canvas.create_text(50,10,width=80,text='剩餘血量'+str(self.dkkd))

    def loop(self,siixys,ssixys):
        self.moveby(self.x)

        self.sif.loop_move()
        self.time+=1
        self.timee+=1

        if self.time>49:
            self.dk+=1
            self.time=0
        if self.timee>249:
            self.dkkd+=2
            self.timee=0

        self.sixy=self.sif.xys
        self.xy=self.canvas.coords(self.item)

        self.canvas.delete(self.text)
        self.text= self.canvas.create_text(40,10,width=100,text='剩餘子彈數'+str(self.dk))
        self.canvas.delete(self.text2)
        self.text2= self.canvas.create_text(40,20,width=100,text='剩餘血量'+str(self.dkkd))

    def moveby(self,x):
        self.xy = self.canvas.coords(self.item)
        self.xu = self.x-(self.xy[0]+self.xy[2])//2
        self.canvas.move(self.item,self.xu,0)

    def mot(self,event):
        self.x = event.x

    def b1mot_si(self,event):
        self.x=event.x

        if self.dk>0 and self.time%4==0:
            self.dk-=1
            self.xy=self.canvas.coords(self.item)
            self.xt=(self.xy[0]+self.xy[2])//2
            self.sif.sie(self.xt)

    def sit(self,event):
        if self.dk>0:
            self.dk-=1
            self.xy=self.canvas.coords(self.item)
            self.xt=(self.xy[0]+self.xy[2])//2
            self.sif.sie(self.xt)

class si:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
        self.xy=[0,0,0,0]

    def sie(self,x):
        self.items.append(self.canvas.create_rectangle(x-5,430,x+5,400))

    def loop_move(self):
        self.xys=[]
        for item in range(len(self.items)):
            if item<len(self.items):
                self.canvas.move(self.items[item],0,-10)

                self.xy=self.canvas.coords(self.items[item])

                if self.xy[1]<39:

                    try:
                        self.canvas.delete(self.items[item])
                        del self.items[item]
                    except:
                        pass
                else:
                    self.xys.append(self.xy)

import random
class mob1:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
        self.sii=sii(canvas)
        self.xys=[]

    def ru(self,gj):
        for f in range(gj):
            self.x=random.randint(0,590)
            self.items.append([self.canvas.create_rectangle(self.x,0,self.x+50,50,fill='blue'),5,self.canvas.create_text(self.x+25,25,text='5')])
    
    def loop(self,sixy,spxy):
        self.ud=self.sii.loop(spxy)
        for itme in range(len(self.items)):
            if itme<len(self.items):

                self.random=random.randint(1,50)#移動
                if self.random==1:
                    self.random=random.randint(1,2)
                    self.xy=self.canvas.coords(self.items[itme][0])
                    if self.random==1:
                        if self.xy[2]<640:
                            self.random=random.randint(1,15)
                            self.canvas.move(self.items[itme][0],self.random,0)
                    else:
                        if self.xy[0]>0:
                            self.random=random.randint(1,15)*-1
                            self.canvas.move(self.items[itme][0],self.random,0)

                self.random=random.randint(1,100)#射擊
                if self.random==1:
                    self.xy=self.canvas.coords(self.items[itme][0])
                    self.x=(self.xy[2]+self.xy[0])//2
                    self.sii.si(self.x)

            if itme<len(self.items):
                self.xy=self.canvas.coords(self.items[itme][0])#碰撞
                for six in sixy:
                    if self.xy[3]>six[1] and self.xy[0]<six[2] and self.xy[2]>six[0]:
                        self.items[itme][1]-=1
                        try:
                            if self.items[itme][1]<1:
                                self.canvas.delete(self.items[itme][0])
                                self.canvas.delete(self.items[itme][2])
                                del self.items[itme]
                        except:
                            self.canvas.delete(self.items[itme][0])
                            self.canvas.delete(self.items[itme][2])
                            del self.items[itme]

            if itme<len(self.items):
                self.canvas.delete(self.items[itme][2])
                self.xy=self.canvas.coords(self.items[itme][0])
                self.x=(self.xy[0]+self.xy[2])//2
                self.items[itme][2]=self.canvas.create_text(self.x,25,text=str(self.items[itme][1]))
        self.xys=self.sii.xys

class mob2:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
        self.sii=sii(canvas)
        self.xys=[]

    def ru(self,gj):
        for f in range(gj):
            self.x=random.randint(0,590)
            self.items.append([self.canvas.create_rectangle(self.x,0,self.x+50,50,fill='Red'),5,self.canvas.create_text(self.x+25,25,text='5')])
    
    def loop(self,sixy,spxy):
        self.ud=self.sii.loop(spxy)
        for itme in range(len(self.items)):
            if itme<len(self.items):

                self.random=random.randint(1,10)#移動
                if self.random==1:
                    self.random=random.randint(1,2)
                    self.xy=self.canvas.coords(self.items[itme][0])
                    if self.random==1:
                        if self.xy[2]<640:
                            self.random=random.randint(1,15)
                            self.canvas.move(self.items[itme][0],self.random,0)
                    else:
                        if self.xy[0]>0:
                            self.random=random.randint(1,15)*-1
                            self.canvas.move(self.items[itme][0],self.random,0)

                self.random=random.randint(1,40)#射擊
                if self.random==1:
                    self.xy=self.canvas.coords(self.items[itme][0])
                    self.sii.si(self.xy[0])
                    self.sii.si(self.xy[2])

            if itme<len(self.items):
                self.xy=self.canvas.coords(self.items[itme][0])#碰撞
                for six in sixy:
                    if self.xy[3]>six[1] and self.xy[0]<six[2] and self.xy[2]>six[0]:
                        self.items[itme][1]-=1
                        try:
                            if self.items[itme][1]<1:
                                self.canvas.delete(self.items[itme][0])
                                self.canvas.delete(self.items[itme][2])
                                del self.items[itme]
                        except:
                            self.canvas.delete(self.items[itme][0])
                            self.canvas.delete(self.items[itme][2])
                            del self.items[itme]

            if itme<len(self.items):
                self.canvas.delete(self.items[itme][2])
                self.xy=self.canvas.coords(self.items[itme][0])
                self.x=(self.xy[0]+self.xy[2])//2
                self.items[itme][2]=self.canvas.create_text(self.x,25,text=str(self.items[itme][1]))

class sii:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
    
    def si(self,x):
        self.items.append(self.canvas.create_rectangle(x+5,50,x-5,70,fill='Orange'))
    
    def loop(self,spxy):
        self.xys=[]
        self.ud=0
        for itme in range(len(self.items)):
            if itme<len(self.items):
                self.xy=self.canvas.coords(self.items[itme])
                self.xys.append(self.xy)
                if self.xy[3]>434:
                    try:
                        if spxy[0]<self.xy[2] and self.xy[0]<spxy[2]:
                            self.ud+=1
                        self.canvas.delete(self.items[itme])
                        del self.items[itme]
                    except:
                        pass
                try:
                    self.canvas.move(self.items[itme],0,8)
                except:
                    pass
        return  self.ud

class ssi:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
    
    def si(self,x):
        self.items.append(self.canvas.create_rectangle(x+5,50,x-5,70,fill='skyblue'))
    
    def loop(self,spxy):
        self.xys=[]
        self.ud=0
        for itme in range(len(self.items)):
            if itme<len(self.items):
                self.xy=self.canvas.coords(self.items[itme])
                self.xys.append(self.xy)
                if self.xy[3]>434:
                    try:
                        if spxy[0]<self.xy[2] and self.xy[0]<spxy[2]:
                            self.ud+=1
                        self.canvas.delete(self.items[itme])
                        del self.items[itme]
                    except:
                        pass
                try:
                    self.canvas.move(self.items[itme],0,8)
                except:
                    pass
        return  self.ud

class mob3:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
        self.sii=ssi(canvas)
        self.xys=[]

    def ru(self,gj):
        for f in range(gj):
            self.x=random.randint(0,590)
            self.items.append([self.canvas.create_rectangle(self.x,0,self.x+50,50,fill='Green'),5,self.canvas.create_text(self.x+25,25,text='5')])
    
    def loop(self,sixy,spxy):
        self.ud=self.sii.loop(spxy)
        for itme in range(len(self.items)):
            if itme<len(self.items):

                self.random=random.randint(1,50)#移動
                if self.random==1:
                    self.random=random.randint(1,2)
                    self.xy=self.canvas.coords(self.items[itme][0])
                    if self.random==1:
                        if self.xy[2]<640:
                            self.random=random.randint(1,15)
                            self.canvas.move(self.items[itme][0],self.random,0)
                    else:
                        if self.xy[0]>0:
                            self.random=random.randint(1,15)*-1
                            self.canvas.move(self.items[itme][0],self.random,0)

                self.random=random.randint(1,100)#射擊
                if self.random==1:
                    self.xy=self.canvas.coords(self.items[itme][0])
                    self.x=(self.xy[2]+self.xy[0])//2
                    self.sii.si(self.x)

            if itme<len(self.items):
                self.xy=self.canvas.coords(self.items[itme][0])#碰撞
                for six in sixy:
                    if self.xy[3]>six[1] and self.xy[0]<six[2] and self.xy[2]>six[0]:
                        self.items[itme][1]-=1
                        try:
                            if self.items[itme][1]<1:
                                self.canvas.delete(self.items[itme][0])
                                self.canvas.delete(self.items[itme][2])
                                del self.items[itme]
                        except:
                            self.canvas.delete(self.items[itme][0])
                            self.canvas.delete(self.items[itme][2])
                            del self.items[itme]

            if itme<len(self.items):
                self.canvas.delete(self.items[itme][2])
                self.xy=self.canvas.coords(self.items[itme][0])
                self.x=(self.xy[0]+self.xy[2])//2
                self.items[itme][2]=self.canvas.create_text(self.x,25,text=str(self.items[itme][1]))
        self.xys=self.sii.xys

class mob4:
    def __init__(self,canvas):
        self.canvas=canvas
        self.items=[]
        self.sii=ssi(canvas)
        self.xys=[]

    def ru(self,gj):
        for f in range(gj):
            self.x=random.randint(0,590)
            self.items.append([self.canvas.create_rectangle(self.x,0,self.x+50,50,fill='Purple'),5,self.canvas.create_text(self.x+25,25,text='5')])
    
    def loop(self,sixy,spxy):
        self.ud=self.sii.loop(spxy)
        for itme in range(len(self.items)):
            if itme<len(self.items):

                self.random=random.randint(1,10)#移動
                if self.random==1:
                    self.random=random.randint(1,2)
                    self.xy=self.canvas.coords(self.items[itme][0])
                    if self.random==1:
                        if self.xy[2]<640:
                            self.random=random.randint(1,15)
                            self.canvas.move(self.items[itme][0],self.random,0)
                    else:
                        if self.xy[0]>0:
                            self.random=random.randint(1,15)*-1
                            self.canvas.move(self.items[itme][0],self.random,0)

                self.random=random.randint(1,40)#射擊
                if self.random==1:
                    self.xy=self.canvas.coords(self.items[itme][0])
                    self.sii.si(self.xy[0])
                    self.sii.si(self.xy[2])

            if itme<len(self.items):
                self.xy=self.canvas.coords(self.items[itme][0])#碰撞
                for six in sixy:
                    if self.xy[3]>six[1] and self.xy[0]<six[2] and self.xy[2]>six[0]:
                        self.items[itme][1]-=1
                        try:
                            if self.items[itme][1]<1:
                                self.canvas.delete(self.items[itme][0])
                                self.canvas.delete(self.items[itme][2])
                                del self.items[itme]
                        except:
                            self.canvas.delete(self.items[itme][0])
                            self.canvas.delete(self.items[itme][2])
                            del self.items[itme]

            if itme<len(self.items):
                self.canvas.delete(self.items[itme][2])
                self.xy=self.canvas.coords(self.items[itme][0])
                self.x=(self.xy[0]+self.xy[2])//2
                self.items[itme][2]=self.canvas.create_text(self.x,25,text=str(self.items[itme][1]))

if __name__=='__main__':
    canvas()