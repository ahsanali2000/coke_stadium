#imoprting tkinter module for GUI
from tkinter import *
main=Tk()
main.geometry("1200x600")#setting geometry
main.title("Coke Stadium")#main title
main.resizable(0,0)#making window a 
icon = PhotoImage(file= "all\\OP7.png")
main.call("wm","iconphoto",main._w,icon)

#making a global variable to use inside function
match_s=0
#all backgrounds
background_image = PhotoImage(file= "all\\OP1P.png")
background_image2 = PhotoImage(file= "all\\OP2.png")
background_image3 = PhotoImage(file= "all\\OP3.png")
background_image4 = PhotoImage(file= "all\\OP4.png")
background_image5 = PhotoImage(file= "all\\OP5.png")
background_image6 = PhotoImage(file= "all\\OP6.png")
background_image7 = PhotoImage(file= "all\\OP3P.png")
background_image8 = PhotoImage(file= "all\\OP8.png")
background_image9 = PhotoImage(file= "all\\OP9.png")
background_image10 = PhotoImage(file= "all\\OP10.png")
#all frames
frame1=Frame(main,width=1200,height=600)
frame1.pack()
background_label2 = Label(frame1,image= background_image9 )
background_label2.place(x=0, y=0, relwidth=1, relheight=1)
#to exit
def exit_win():
    main.destroy()
#class to use functions with multiple parameter in order to use same code multiple times
class mainfunctions():
    
#A function to change the name of teams
    def modify(self,day):
        frame3=Frame(main,width=1200,height=600)
        frame3.place(x=0,y=0)
        bg=Label(frame3,image=background_image7)
        bg.place(x=0,y=0,relheight=1,relwidth=1)
        #lables for entries
        Label(frame3,text="First team of first match",font=("times",14,"bold"),bg="#3c3c3c").place(x=400,y=220)
        Label(frame3,text="Second team of first match",font=("times",14,"bold"),bg="#3c3c3c").place(x=400,y=250)
        Label(frame3,text="First team of Second match",font=("times",14,"bold"),bg="#3c3c3c").place(x=400,y=330)
        Label(frame3,text="Second team of Second match",font=("times",14,"bold"),bg="#3c3c3c").place(x=400,y=360)
        Label(frame3,text="First team of third match",font=("times",14,"bold"),bg="#3c3c3c").place(x=400,y=460)
        Label(frame3,text="Second team of third match",font=("times",14,"bold"),bg="#3c3c3c").place(x=400,y=490)
        
        #entries for names of teams
        m1t1E=Entry(frame3)
        m1t1E.place(x=700,y=220)
        m1t2E=Entry(frame3)
        m1t2E.place(x=700,y=250)
        m2t1E=Entry(frame3)
        m2t1E.place(x=700,y=330)
        m2t2E=Entry(frame3)
        m2t2E.place(x=700,y=360)
        m3t1E=Entry(frame3)
        m3t1E.place(x=700,y=460)
        m3t2E=Entry(frame3)
        m3t2E.place(x=700,y=490)
        def changing():
            #getting values of entries to write in the txt files
            m1t1=m1t1E.get()
            m1t2=m1t2E.get()
            m2t1=m2t1E.get()
            m2t2=m2t2E.get()
            m3t1=m3t1E.get()
            m3t2=m3t2E.get()
            #writing the input of entries into files behind
            with open(day+"\\m1t1.txt","w") as m1:
                ts1=m1.write(str(m1t1))
            with open(day+"\\m1t2.txt","w") as m2:
                ts2=m2.write(str(m1t2))
            with open(day+"\\m2t1.txt","w") as m3:
                ts3=m3.write(str(m2t1))
            with open(day+"\\m2t2.txt","w") as m4:
                ts4=m4.write(str(m2t2))
            with open(day+"\\m3t1.txt","w") as m5:
                ts5=m5.write(str(m3t1))
            with open(day+"\\m3t2.txt","w") as m6:
                ts6=m6.write(str(m3t2))
            Label(frame3,image= background_image8).place(x=0,y=0,relwidth=1,relheight=1)
            
            Button(frame3,text="EXIT",font= ("algerian",20,"bold"),bg = "#3c3c3c",command=exit_win).place(x=580,y=500)

        Button(frame3,text="     Done     ",font= 50,bg = "#3c3c3c",fg="white",command = changing).place(x=575,y=530)
#a function to clear all the booked seats
    def clear(self,day,match):
        #a loop to reduce the code and work everytime with different txt files
        for i in range(1,41):
            with open(day+"C\\"+"m"+str(match)+"\\"+"s"+str(i)+".txt","w") as x:
                c=x.write("GREEN")
            frame4=Frame(main,height=600,width=1200).place(x=0,y=0)
            Label(frame4,image=background_image10).place(x=0,y=0,relheight=1,relwidth=1)
            Button(frame4,text="EXIT",font= ("algerian",20,"bold"),bg = "#3c3c3c",command=exit_win).place(x=580,y=500)

                
#this function ask to select the day for which you want to clear the booked seats
def clear_it():
    frame2=Frame(main,width=1200,height=600)
    frame2.place(x=0,y=0)
    background_label2 = Label(frame2,image= background_image )
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)
    days = ""
#this function gets the value of selected day from radiobuttons at the bottom and assign it to the days variable
    def get2():
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
        frame3=Frame(main,height=600,width=1200).place(x=0,y=0)
        Label(frame3,image=background_image3).place(x=0,y=0,relheight=1,relwidth=1)
        #specified time at which three matches of a day can be played
        time_1="(10:00AM-12:00PM)"
        time_2="(01:00PM-03:00PM)"
        time_3="(04:00PM-06:00PM)"
        #this function get the input of match selection from the user using the radiobuttons at the bottom
        def value_get():
            global match_s
            m1=m.get()
            if m1==1:
                match_s=1
            elif m1==2:
                match_s=2
            elif m1==3:
                match_s=3
            calling=mainfunctions()
            calling.clear(days,match_s)
    
        #labels for matches
        Label(frame3,text="Match 1  {}".format(time_1),font=("algerian",14,"bold")).place(x=510,y=275)
        Label(frame3,text="Match 2  {}".format(time_2),font=("algerian",14,"bold")).place(x=510,y=350)
        Label(frame3,text="Match 3  {}".format(time_3),font=("algerian",14,"bold")).place(x=510,y=425)
        #radiobuttons for selection of match added on same frame because only one of them can be selected from those which are on same frame  
        m=IntVar()
        m.set(0)
        match1 = Radiobutton(frame3,variable = m,value=1,bg = "#3c3c3c").place(x=450,y=275)
        match2 = Radiobutton(frame3,variable = m,value=2,bg = "#3c3c3c").place(x=450,y=350)
        match3 = Radiobutton(frame3,variable = m,value=3,bg = "#3c3c3c").place(x=450,y=425)
        Button(frame3,text="CLEAR THE BOOKED TICKETS",font=("algerian",16,"bold"),bg = "#3c3c3c",fg="white",command = value_get).place(x = 456, y = 508)
    #radiobutton for the selection of day added on same frame because only one of them can be selected from those which are in same frame
    v = IntVar()
    v.set(0)

    monday = Radiobutton(frame2,variable = v,value=0,bg = "#3c3c3c").place(x=549,y=322)
    tuesday = Radiobutton(frame2,variable = v,value=1,bg = "#3c3c3c").place(x=549,y=348)
    wednesday = Radiobutton(frame2,variable = v,value=2,bg = "#3c3c3c").place(x=549,y=376)
    thursday = Radiobutton(frame2,variable = v,value=3,bg = "#3c3c3c").place(x=549,y=403)
    friday = Radiobutton(frame2,variable = v,value=4,bg = "#3c3c3c").place(x=549,y=431)
    saturday = Radiobutton(frame2,variable = v,value=5,bg = "#3c3c3c").place(x=549,y=458)
    Sunday = Radiobutton(frame2,variable = v,value=6,bg = "#3c3c3c").place(x=549,y=484)
    done = Button(frame2,text="     Done     ",font= 50,bg = "#3c3c3c",fg="white",command = get2).place(x = 560, y = 529)




#this function ask to select the day for which you want to change names of teams for upcomming matches
def week():
    frame2=Frame(main,width=1200,height=600)
    frame2.place(x=0,y=0)
    background_label2 = Label(frame2,image= background_image )
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)
    days = ""
    #this function gets the value of selected day from radiobuttons at the bottom and assign it to the days variable
    def get1():
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
        calling=mainfunctions()
        calling.modify(days)
    #radiobutton for the selection of day added on same frame because only one of them can be selected from those which are in same frame
    v = IntVar()
    v.set(0)

    monday = Radiobutton(frame2,variable = v,value=0,bg = "#3c3c3c").place(x=549,y=322)
    tuesday = Radiobutton(frame2,variable = v,value=1,bg = "#3c3c3c").place(x=549,y=348)
    wednesday = Radiobutton(frame2,variable = v,value=2,bg = "#3c3c3c").place(x=549,y=376)
    thursday = Radiobutton(frame2,variable = v,value=3,bg = "#3c3c3c").place(x=549,y=403)
    friday = Radiobutton(frame2,variable = v,value=4,bg = "#3c3c3c").place(x=549,y=431)
    saturday = Radiobutton(frame2,variable = v,value=5,bg = "#3c3c3c").place(x=549,y=458)
    Sunday = Radiobutton(frame2,variable = v,value=6,bg = "#3c3c3c").place(x=549,y=484)
    done = Button(frame2,text="     Done     ",font= 50,bg = "#3c3c3c",fg="white",command = get1).place(x = 560, y = 529)


#Buttons which are shown on maininterface to ask for choice if he\she wants to clear the booked tickers or change the names of teams for upcomming matches

clear_button=Button(frame1,text="Clear Booked Tickets",font= ("algerian",20,"bold"),bg = "#3c3c3c",fg="white",command=clear_it).place(x=440,y=300)
edit_button=Button(frame1,text="Change name of teams",font=("algerian",20,"bold"),bg = "#3c3c3c",fg="white",command=week).place(x=440,y=400)
end=Button(frame1,text="EXIT",font=("algerian",20,"bold"),bg = "#3c3c3c",fg="white",command=exit_win).place(x=560,y=507)

main.mainloop()
