from tkinter import*
import random
main = Tk()
main.geometry("1200x600")
main.title("Coke Stadium")
main.resizable(0,0)
icon = PhotoImage(file = "all\\OP7.png")
main.call("wm","iconphoto",main._w,icon)
ans=" "
#used for exiting the program
def exit_all():
    main.destroy()


#all background images
background_image = PhotoImage(file= "all\OP1.png")
background_image2 = PhotoImage(file= "all\OP2.png")
background_image3 = PhotoImage(file= "all\OP3.png")
background_image4 = PhotoImage(file= "all\OP4.png")
background_image5 = PhotoImage(file= "all\OP5.png")
background_image6 = PhotoImage(file= "all\OP6.png")
background_image7 = PhotoImage(file= "all\OP9.png")
background_image8 = PhotoImage(file= "all\OP11.png")
background_image9 = PhotoImage(file= "all\OP12.png")
background_image13 = PhotoImage(file= "all\OP13.png")

#all frames

frame2=Frame(main,width=1200,height=600)
background_label2 = Label(frame2,image= background_image )
background_label2.place(x=0, y=0, relwidth=1, relheight=1)


num_of_seats=""#for total number of seats
checkval=0 #for calculating total payment
net_price = 0 #total payment
seat_number = random.randint(10000,100000)#for booking number
cardno = 0#credit card number
NUM1 = 0#for number of seats
count = 1#for number of seats
xax,yax,no=60,190,1#for positioning of seats

#return ticket module
def anber():
    frame2=Frame(main,width=1200,height=600)
    background_label2 = Label(frame2,image= background_image13 )
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)

    seat_numberr = random.randint(1000,10000)
    no = 1
    ticket = 1
    class return1 :

        def match3(self,day,match):
            s_m1=Frame(main,width=1200,height=600)
            s_m1.place(x=0,y=0)
                                

            background_labelm = Label(s_m1,image= background_image8 )
            background_labelm.place(x=0, y=0, relwidth=1, relheight=1)

            new_day = day+"C"
            seat_label = Label(s_m1,text="Enter your seat number(1-40):",font=("times",14,"bold"),bg="#3c3c3c",fg="white").place (x = 400,y=300)           
            seat_num = Entry(s_m1)
            seat_num.place(x=670,y=300)
            tic_label = Label(s_m1,text="Enter your ticket number:",font=("times",14,"bold"),bg="#3c3c3c",fg="white").place (x = 400,y=350)  
            tic_num = Entry(s_m1)
            tic_num.place(x= 670, y = 350)
            def func():
                
                global no
                no = int(seat_num.get())
                global ticket
                ticket = int(tic_num.get())
                global ans 
                for i in range(1,no+1):

                    with open(new_day+"\\"+match+"\\s"+str(i)+".txt","r") as p:
                        Bgg=p.readlines()
                        Bg = str(Bgg[1])
                        if Bg == str(ticket) :
                           
                            with open(new_day+"\\"+match+"\\s"+str(i)+".txt","w") as t:
                                t.write("GREEN"+"\n"+str(seat_numberr))
                            break   
                else:
                    ans= "No such ticket found"

                if ans != "No such ticket found":
                    ans = "Booking Cancelled"
                if ans=="Booking Cancelled":
                    Label(s_m1,image=background_image9).place(x=0,y=0,relheight=1,relwidth=1)
                    Button(s_m1,text="EXIT",font=("algerian",20,"bold"),bg = "#3c3c3c",fg="white",command=exit_all).place(x=550,y=500)
                    

                    
                elif ans== "No such ticket found":
                    Label(s_m1,text=ans,font=("arial",15,"bold"),bg="#3c3c3c",fg="white").place(x=518,y=450)
                
                                
            ok = Button(s_m1,text="    Done    ",fg="white",font=("arial",12,"bold"),bg="#3c3c3c",command=func).place(x=564,y=530)     
             


    class everythingr :
        
        def rmonday(self,day):


            wsun=Frame(main,width=1200,height=600,bg="WHITE")
            wsun.place(x=0,y=0)
            background_labels = Label(wsun,image= background_image3 )
            background_labels.place(x=0, y=0, relwidth=1, relheight=1)
                        
                        
                       
            with open(day+"\\m1t1.txt","r") as m1:
                ts1=m1.read()
            with open(day+"\\m1t2.txt","r") as m2:
                ts2=m2.read()
            with open(day+"\\m2t1.txt","r") as m3:
                ts3=m3.read()
            with open(day+"\\m2t2.txt","r") as m4:
                ts4=m4.read()
            with open(day+"\\m3t1.txt","r") as m5:
                ts5=m5.read()
            with open(day+"\\m3t2.txt","r") as m6:
                ts6=m6.read()
            time_1="(10:00AM-12:00PM)"
            time_2="(01:00PM-03:00PM)"
            time_3="(04:00PM-06:00PM)"

                       
            VsMatches=Label(wsun,text="There are following matches on "+day+".\n\n1- {} vs {} {}\n\n2- {} vs {} {}\n\n3- {} vs {} {}".format(ts1,ts2,time_1,ts3,ts4,time_2,ts5,ts6,time_3),bg="#3c3c3c",fg="white")
         
            VsMatches.config(font=("Gabriola",15,"bold"))
            VsMatches.place(x=460,y=228)
                        
                        
            def formatch1():
                pi=return1()
                pi.match3(day,"m1")
                     
                        
            def formatch2():
                pi=return1()
                pi.match3(day,"m2")
                                     
                                
                        
            def formatch3():
                pi=return1()
                pi.match3(day,"m3")
                                                         
           
            b_m1=Button(wsun,text="   Match 1   ",font = ('Gabriola',15),bg = "#3c3c3c",fg="white",command=formatch1)
            b_m2=Button(wsun,text="   Match 2   ",font = ('Gabriola',15),bg = "#3c3c3c",fg="white",command = formatch2)
            b_m3=Button(wsun,text="   Match 3   ",font = ('Gabriola',15),bg = "#3c3c3c",fg="white",command = formatch3)

            b_m1.place(x=450,y=500)
            b_m2.place(x=575,y=500)
            b_m3.place(x=693,y=500)


    v1 = 2
    days = ""

    def get1():
        global v1
        global days
        v1 = v.get()
        
        if v1 == 0 :
            days = "MONDAY"
        elif v1 == 1 :
            days = "TUESDAY"

        elif v1 == 2 :
            days = "WEDNESDAY"

        elif v1== 3 :
            days = "THURSDAY"

        elif v1 == 4 :
            days = "FRIDAY"

        elif v1== 5 :
            days = "SATURDAY"

        elif v1 == 6 :
            days = "SUNDAY"


        pi=everythingr()
        pi.rmonday(days)


    v = IntVar()
    v.set(1)
    #inital radio buttons
    monday = Radiobutton(frame2,variable = v,value=0,bg = "#3c3c3c").place(x=549,y=322)
    tuesday = Radiobutton(frame2,variable = v,value=1,bg = "#3c3c3c").place(x=549,y=348)
    wednesday = Radiobutton(frame2,variable = v,value=2,bg = "#3c3c3c").place(x=549,y=376)
    thursday = Radiobutton(frame2,variable = v,value=3,bg = "#3c3c3c").place(x=549,y=403)
    friday = Radiobutton(frame2,variable = v,value=4,bg = "#3c3c3c").place(x=549,y=431)
    saturday = Radiobutton(frame2,variable = v,value=5,bg = "#3c3c3c").place(x=549,y=458)
    Sunday = Radiobutton(frame2,variable = v,value=6,bg = "#3c3c3c").place(x=549,y=484)
    done = Button(frame2,text="     Done     ",font= 50,bg = "#3c3c3c",fg="white",command = get1).place(x = 560, y = 529)

    frame2.place(x=0,y=0)


#booking a ticket module start
#2 to execute
class todo :

    def match3(self,day,match):
        s_m1=Frame(main,width=1200,height=600)
        s_m1.place(x=0,y=0)
                        

        background_labelm = Label(s_m1,image= background_image4 )
        background_labelm.place(x=0, y=0, relwidth=1, relheight=1)
                    
        
        num = IntVar()
        num.set(1)
        
        one = Radiobutton(s_m1,variable = num,value=1,text="One",font=13,bg="#3c3c3c").place(x=400,y=270)
        two = Radiobutton(s_m1,variable = num,value=2,text="Two",font=13,bg="#3c3c3c").place(x=500,y=270)
        three = Radiobutton(s_m1,variable = num,value=3,text="Three",font=13,bg="#3c3c3c").place(x=600,y=270)
        four = Radiobutton(s_m1,variable = num,value=4,text="Four",font=13,bg="#3c3c3c").place(x=700,y=270)
        five = Radiobutton(s_m1,variable = num,value=5,text="Five",font=13,bg="#3c3c3c").place(x=800,y=270)
        
        vipCheck=IntVar()
        vip=Checkbutton(s_m1,text="Click here if you want to buy \"VIP\" ticket.",font = ('Gabriola',15),variable=vipCheck,bg="#3c3c3c")
        vip.place(x=400,y=300)
        refCheck=IntVar()
        refresh=Checkbutton(s_m1,text="Click here if you want refreshments with your ticket.",font = ('Gabriola',15),variable=refCheck,bg="#3c3c3c")
        refresh.place(x=400,y=350)

        ll=Label(s_m1,text="Enter Points(1 Rs for 10 Points):",font = ('Gabriola',15),bg="#3c3c3c")
        ll.place(x=405,y=395)
        points=Entry(s_m1)
        points.place(x=645,y=410)
        cc = Label(s_m1,text="Enter your credit card number:",font = ('Gabriola',15),bg="#3c3c3c")
        cc.place(x=405,y=480)
        ccp = Entry(s_m1)
        ccp.place(x=645,y=495)
        
        def reciept():
            price=1000
            refreshments=500
            vipvalue=vipCheck.get()
            global checkval
            checkval=refCheck.get()
            localnum = num.get()
            pointval=int(points.get())
            price-=round(pointval/10)
            global cardno
            cardno = ccp.get()
            
            if checkval==1:
                price=price+refreshments
            if vipvalue==1:
                price+=1000
            price=price*localnum
            if price < 0:
                price = 0
            l_p=Label(s_m1,text="TOTAL PRICE = {} .Rs".format(price*localnum),font = ('Gabriola',13),bg="#3c3c3c",fg="white")
            l_p.place(x=550,y=440)


        b_p=Button(s_m1,text="Check price",font = ('Gabriola',12),bg="white",command = reciept)
        b_p.place(x=800,y=400)               
        
        def new ():
            global NUM1
            NUM1 = num.get()

            global cardno
            cardno = str(ccp.get())
            
            
            pi = qwerty()
            pi.allo(day+"C",match)


        seats=Button(s_m1,text="Go to Book seat",font = ('Gabriola',12),command=new,bg="white")
        seats.place(x=800,y=500)


#3 to execute
class qwerty :

    def allo(self,day,match):

        
        wsun1=Frame(main,width=1200,height=600,bg="white")
        wsun1.place(x=0,y=0)    
        background_labelm = Label(wsun1,image= background_image2 )
        background_labelm.place(x=0, y=0, relwidth=1, relheight=1)
        head = Label(wsun1,text="All AVALIABLE SEATS",font = ('Gabriola',20),bg="white").place(x=500,y=10)
        
        
        xax,yax,no=60,190,1
        def func(xax,yax,no,day,match):
            
            def red():
                if Backk == "GREEN":
                    
                    global count

                    def back():
                        end = Frame(main,width=1200,height=600,bg="white")
                        end.place(x=0,y=0)
                        background_label1234 = Label(end,image= background_image5 )
                        background_label1234.place(x=0, y=0, relwidth=1, relheight=1)

                        title1 = Label (end,text="Booking  Confirmed for "+str(NUM1)+" person/people.",bg="#3c3c3c",fg='white',font=20)
                        
                        title1.place(x=460,y= 150)
                        x = day.capitalize()
                        y= len(x)-1
                        final = ""
                        for i in range (0,y):
                            final= final + x[i]
                        details = Label(end,text="Looking forward to see you on "+final+"!",font=20,bg="#3c3c3c",fg='white').place(x=460,y=450)
                        number = Label(end,text="Credit Card Number : "+cardno,font=20,bg="#3c3c3c",fg='white').place(x = 460 , y = 200)
                        ticket_no= Label(end,text="Your booking number is :"+str(seat_number)+" (Same for all seats)",font=20,bg="#3c3c3c",fg='white').place(x=460,y=250)
                        seat_number_for_end = Label(end,text="Your seat number is/are : "+num_of_seats,font=20,bg="#3c3c3c",fg='white').place(x=460,y=300)
                        help1= Label(end,text="(Booking & Seat Number required for future verification)",font=20,bg="#3c3c3c",fg='white').place(x=460,y=350)
                        total_price = Label(end,text="Total Payment : "+str(net_price)+" Rs",font=20,bg="#3c3c3c",fg='white').place(x=460,y=400)
                        def view():
                            end1 = Frame(main,width=1200,height=600,bg="white")
                            end1.place(x=0,y=0)
                            background_label1234 = Label(end1,image= background_image6 )
                            background_label1234.place(x=0, y=0, relwidth=1, relheight=1)
                            extit_all =Button(end1,text="Exit",font=("arial",17,"bold"),bg = "#3c3c3c",fg="white",relief="flat",command=exit_all).place(x=1109,y=540)

                        view_map= Button(end,text="  View Full Map  ",font = ('Gabriola',15),bg = "#3c3c3c",fg="white",command = view)
                        view_map.place(x=560,y=490)
                    


                    if count <= (NUM1):
                    
                        seatr = Button(main,text="SEAT-"+str(no),bg="red").place(x=xax,y=yax)
                        with open(day+"\\"+match+"\\s"+str(no)+".txt","w") as p:
                                newBg=p.write("RED"+"\n"+str(seat_number))

                        #price checks
                        if no == 26 or no == 27 or no == 28 or no == 29 or no == 30 or no == 31 or no == 32 or no == 33 or no == 34 or no == 35 :
                            if checkval == 1:
                                net_price = 2000 + 500
                            else:
                                net_price = 2000

                        else:
                            if checkval == 1:
                                net_price = 1000 + 500
                            else:
                                net_price = 1000
                        global num_of_seats
                        
                        num_of_seats+=str(no)+"  "
                                
                        if count == (NUM1) :
                            confirm= Button(main,text="CONFIRM TICKET/S",font=17,bg = "#3c3c3c",fg="white",command = back).place(x=1020,y=15)
                        count += 1
                        
                    else:
                        error = Tk()
                        error.geometry("200x70")
                        error.title("Error")
                        message = Label(error,text="Can not select more seats",font=16).place(x=10,y=30)
                    
                else:
                    pass
                
            with open(day+"\\"+match+"\\s"+str(no)+".txt","r") as c:
                Bgg=c.read()
            Bg = Bgg.split()
            Backk = Bg[0]
            seat = Button(main,text="SEAT-"+str(no), bg=Backk,command = red).place(x=xax,y=yax)


        
        for i in range(1,11):
                    
           
            func(xax,yax,no,day,match)
            no = no +1
            yax = yax + 50
            if yax%440 == 0:
                xax,yax = 140,190

        xax,yax=1000,190

        for i in range(11,21):
                            
            func(xax,yax,no,day,match)
            no = no +1
            yax = yax + 50
            if yax%440 == 0:
                xax,yax = 1090,190

        #b1
        func(240,120,21,day,match)
        func(240,70,22,day,match)
        func(320,120,23,day,match)
        func(320,70,24,day,match)
        func(400,90,25,day,match)
        #vip1
        func(240,460,26,day,match)
        func(240,510,27,day,match)
        func(320,460,28,day,match)
        func(320,510,29,day,match)
        func(400,490,30,day,match)
        #vip2
        func(800,460,31,day,match)
        func(800,510,32,day,match)
        func(880,460,33,day,match)
        func(880,510,34,day,match)
        func(720,490,35,day,match)
        #a1
        func(800,70,36,day,match)
        func(800,120,37,day,match)
        func(880,70,38,day,match)
        func(880,120,39,day,match)
        func(720,90,40,day,match)


#1 to execute
class everything :
    
    def rmonday(self,day):


                    wsun=Frame(main,width=1200,height=600,bg="WHITE")
                    wsun.place(x=0,y=0)
                    background_labels = Label(wsun,image= background_image3 )
                    background_labels.place(x=0, y=0, relwidth=1, relheight=1)
                    
                    
                   
                    with open(day+"\\m1t1.txt","r") as m1:
                        ts1=m1.read()
                    with open(day+"\\m1t2.txt","r") as m2:
                        ts2=m2.read()
                    with open(day+"\\m2t1.txt","r") as m3:
                        ts3=m3.read()
                    with open(day+"\\m2t2.txt","r") as m4:
                        ts4=m4.read()
                    with open(day+"\\m3t1.txt","r") as m5:
                        ts5=m5.read()
                    with open(day+"\\m3t2.txt","r") as m6:
                        ts6=m6.read()
                    time_1="(10:00AM-12:00PM)"
                    time_2="(01:00PM-03:00PM)"
                    time_3="(04:00PM-06:00PM)"

                   
                    VsMatches=Label(wsun,text="There are following matches on "+day+".\n\n1- {} vs {} {}\n\n2- {} vs {} {}\n\n3- {} vs {} {}".format(ts1,ts2,time_1,ts3,ts4,time_2,ts5,ts6,time_3),bg="#3c3c3c",fg="white")
     
                    VsMatches.config(font=("arial",14,"bold"))
                    VsMatches.place(x=380,y=258)
                    
                    
                    def formatch1():
                        pi=todo()
                        pi.match3(day,"m1")
                         
                    
                    def formatch2():
                        pi=todo()
                        pi.match3(day,"m2")
                                 
                            
                    
                    def formatch3():
                        pi=todo()
                        pi.match3(day,"m3")
                                                     
       
                    b_m1=Button(wsun,text="   Match 1   ",font = ('arial',13,"bold"),bg = "#2E2E2E",fg="white",relief='flat',command=formatch1)
                    b_m2=Button(wsun,text="   Match 2   ",font = ('arial',13,"bold"),bg = "#2E2E2E",fg="white",relief='flat',command = formatch2)
                    b_m3=Button(wsun,text="   Match 3   ",font = ('arial',13,"bold"),bg = "#2E2E2E",fg="white",relief='flat',command = formatch3)

                    b_m1.place(x=443,y=513)
                    b_m2.place(x=566,y=513)
                    b_m3.place(x=686,y=513)
                           


def book_ticket():
    


        frame2=Frame(main,width=1200,height=600)
        background_label2 = Label(frame2,image= background_image )
        background_label2.place(x=0, y=0, relwidth=1, relheight=1)
                       


        v1 = 2
        days = ""

        def get1():
            global v1
            global days
            v1 = v.get()
            
            if v1 == 0 :
                days = "MONDAY"
            elif v1 == 1 :
                days = "TUESDAY"

            elif v1 == 2 :
                days = "WEDNESDAY"

            elif v1== 3 :
                days = "THURSDAY"

            elif v1 == 4 :
                days = "FRIDAY"

            elif v1== 5 :
                days = "SATURDAY"

            elif v1 == 6 :
                days = "SUNDAY"

            pi=everything()
            pi.rmonday(days)




        v = IntVar()
        v.set(0)

        monday = Radiobutton(frame2,variable = v,value=0,bg = "#3c3c3c").place(x=549,y=322)
        tuesday = Radiobutton(frame2,variable = v,value=1,bg = "#3c3c3c").place(x=549,y=348)
        wednesday = Radiobutton(frame2,variable = v,value=2,bg = "#3c3c3c").place(x=549,y=376)
        thursday = Radiobutton(frame2,variable = v,value=3,bg = "#3c3c3c").place(x=549,y=403)
        friday = Radiobutton(frame2,variable = v,value=4,bg = "#3c3c3c").place(x=549,y=431)
        saturday = Radiobutton(frame2,variable = v,value=5,bg = "#3c3c3c").place(x=549,y=458)
        Sunday = Radiobutton(frame2,variable = v,value=6,bg = "#3c3c3c").place(x=549,y=484)
        done = Button(frame2,text="     Done     ",font= ("calibri",14,"bold"),bg = "#2E2E2E",fg="black",relief='flat',command = get1).place(x = 557, y = 525)

        frame2.place(x=0,y=0)
frame1=Frame(main,width=1200,height=600).pack()
Label(frame1,image=background_image7).place(x=0,y=0,relheight=1,relwidth=1)

book_button=Button(frame1,text="      Book Ticket     ",font= ("calibri",20,"bold"),bg = "#2E2E2E",fg="white",relief='flat',command=book_ticket).place(x=500,y=300)
return_button=Button(frame1,text="    Return Ticket    ",font=("calibri",20,"bold"),bg = "#2E2E2E",fg="white",relief='flat',command=anber).place(x=500,y=400)
end=Button(frame1,text="EXIT",font=("calibri",20,"bold"),bg = "#3c3c3c",fg="white",relief='flat',command=exit_all).place(x=575,y=505)
main.mainloop()
#end
