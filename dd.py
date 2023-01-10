from tkinter import*
import speedtest
root=Tk()

root.title("Internetspeed Test")
root.geometry("360*600")
root.resizable(False,False)
root.configuration(bg="#1a212d")
def check():
    
    test=speedtest.speedtest()
    
    uploading=round(test.upload()/(1024*1024),2)
    upload.config(text=uploading)
    
    downloading=round(test.downloading()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text=downloading)
    
    servernames=[]
    
    test.get_servers(servernames)
    ping.config(text=results.ping)
    
#icon
    
image_icon=photoimage(file="logo.png")
root.iconphoto(False,image_icon)

#Images

Top=photoImage(file="top.png")label(root,image=Top,bg="#1a212d").pack()
main=PhotoImage(file="main.png")
lable(root,image=main,bg="#1a212d").pack(pady=(40,0))
button=photoImage(file="button.png")
Button=Button(root,image=button,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2"pady=10)

#label1

Lable(root,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)
Lable(root,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)
Lable(root,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=260,y=0)
Lable(root,text="MS",font="arial 7 bold",bg="#384056",fg="White").place(x=60,y=80)
Lable(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="White").place(x=165,y=80)
Lable(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="White").place(x=275,y=80)
Lable(root,text="DOWNLOAD",font="arial 15 bold",bg="#384056",fg="White").place(x=140,y=280)
Lable(root,text="MBPS",font="arial 15 bold",bg="#384056",fg="White").place(x=155,y=380)

ping=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="White")
ping.place(x=70,y=60,anchor="center")

download=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="White")
download.place(x=180,y=60,anchor="center")

upload=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="White")
upload.place(x=290,y=60,anchor="center")

Download=Label(root,text="00",font="arial 40 bold",bg="#384056",fg="White")
Download.place(x=185,y=350,anchor="center")

