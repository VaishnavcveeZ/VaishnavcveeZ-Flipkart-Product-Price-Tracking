from tkinter import *
import tkinter.font as font
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL=''
PRICE=0
BUDG=1
MAIL=''
PSW=''
RMAIL=''

SCAN=True

while True:
    print('STARTED')
    window=Tk()
    window.configure(bg='#99a9e8')
    window.title('FLIPKART TRACK')
    window.geometry('800x300')

    headers={"User-Agents":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}

    def checkPrice():
        print('CHECK PRICE.....')
        url=urlEntry.get()
        globals()['URL']=url
        budget=ePrice.get()
        try:
            bud=0
            globals()['BUDG']=float(budget)
            bud=float(budget)
        except:
            pass

        
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser").text
        

        price=re.findall('₹.\S+',soup)
        for p in range(2):
            p=price[p]
        
            l=0
            for i in range(len(p)):

                if p[i]==',':
                    l=1
                    pPrice=p
                    break
            if l==1:
                break
            else:
                pPrice=price[0]

        price=''
        for i in range(len(pPrice)):
            x=pPrice[i]
            try:
                y=float(x)
                price += x
            except:
                if x==',':
                    continue
                if len(price)>0:

                    break
                continue
        price=float(price)
        print('PRICE IS : ',price)
        globals()['PRICE']=price
        cPrice.delete(0,END)
        cPrice.insert(0,price)
        globals()['price']=price
        try:
            if len(url)>0 and len(budget)>0 and bud != 0:
                next=Button(window,bg="#3b7cff",fg="white",text='next' ,command=lambda:pageC(2)).grid(row=10,column=5,pady=20)
        except:
            pass
        


    def sendMail(recv,mail,psw):
        recv= recv
        mail= mail
        psw= psw

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(mail,psw)
        subject = 'Price fell down !'
        body = globals()['URL']
        message = f"Subject : {subject}\n\n{body}"
        server.sendmail(
            mail,
            recv,
            message
        )
        print('Email Has Been Sent !')
        server.quit()
        quit()



    #tkinter UI Config.

    try:
        if i==1:
            pass
    except:
        run=0
        st=1
        page=1
        i=1
    if st==0:
        break

    def pageC(a):
       
        if a==2:
            page=2
        else:
            page=1
        globals()['page']=page
        window.destroy()
        
    def exit():
        globals()['st']=0
        quit()

    def preSend():
        mail=mailEntry.get()
        globals()['MAIL']=mail
        psw=pswdEntry.get()
        globals()['PSW']=psw
        recv=recvEntry.get()
        globals()['RMAIL']=recv
        if len(mail)>0 and len(psw)>0 and len(recv)>0:
             SCAN=True
             while SCAN:
                 if globals()['PRICE'] < globals()['BUDG']:
                     sendMail(recv,mail,psw)
                     
                     SCAN=False



     #tkinter ui            

    stop=Button(window,bg="#9e331b",fg="white",text='stop' ,command=exit).grid(row=0,column=10,pady=20)

    if page==1:
        
        urllab=Label(window,bg='#99a9e8',text='Enter URL :').grid(row=1)

        urlEntry=Entry(window,bg='white',fg='black',width=45)
        urlEntry.grid(row=1,column=1,columnspan=5,padx=45,pady=5,ipady=5)

        cPricelab=Label(window,bg='#99a9e8',text='Current price :').grid(row=3)

        cPrice=Entry(window,bg='white',fg='black',width=25,)
        cPrice.grid(row=3,column=1,columnspan=2,padx=45,pady=5,ipady=5)

        ePricelab=Label(window,bg='#99a9e8',text='Expected low price :').grid(row=3, column=4 )

        ePrice=Entry(window,bg='white',fg='black',width=25)
        ePrice.grid(row=3,column=6,columnspan=1,padx=30,pady=5,ipady=2)

        checkPrice=Button(window,bg="#3b7cff",fg="white",text='check rate' ,command=checkPrice).grid(row=10,column=2,pady=20)

        


    if page==2:
        

        maillab=Label(window,bg='#99a9e8',text='Enter sender mail Id :').grid(row=1)

        mailEntry=Entry(window,bg='white',fg='black',width=45)
        mailEntry.grid(row=1,column=1,columnspan=5,padx=45,pady=5,ipady=5)

        pswdlab=Label(window,bg='#99a9e8',text='Enter Two Step Veryfication code :').grid(row=2)

        pswdEntry=Entry(window,bg='white',fg='black',width=45)
        pswdEntry.grid(row=2,column=1,columnspan=5,padx=45,pady=5,ipady=5)

        recvlab=Label(window,bg='#99a9e8',text='Enter reciever mail :').grid(row=3)

        recvEntry=Entry(window,bg='white',fg='black',width=45)
        recvEntry.grid(row=3,column=1,columnspan=5,padx=45,pady=5,ipady=5)

        start=Button(window,bg="#3b7cff",fg="white",text='START' ,command=preSend).grid(row=4,column=4,pady=20)

        back=Button(window,bg="#3b7cff",fg="white",text='back' ,command=lambda:pageC(1)).grid(row=4,column=2,pady=20)
   
    try:
        budget=ePrice.get()
        
    except:
        pass



    window.mainloop()