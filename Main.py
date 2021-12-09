import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from pytube import YouTube
import time
import textwrap

# UI of the program
color = 'grey'
rf = tk.RAISED #  this tells whatever widget that has it to be raised
win = tk.Tk()
win.title("GUI FOR PYTUBE")# sets the title for the gui program
win.geometry("1000x1000")
win.configure(bg = color)# sets the color of the root/main widget
win.columnconfigure(1,weight = 1)

frame1 = tk.Frame(win,
    relief = tk.GROOVE, 
    bg = color
)
frame1.grid(row=2, 
    column=0,  
    pady=50,
    padx = 50,
    sticky = tk.N
#  this frame encapsulates the url input 
    
)
h1 = ttk.Label(
    win,
    text = 'Gui for pytube',
    relief=rf,
    background = color
    )
h1.grid(row=0,column=0)
#  i call this h1 because am also a front dev and just comparing h1 html tag here makes my code  more readable. The same thing applies to the image, i named the variable img just to increase code readabilty.


img1 = ImageTk.PhotoImage(Image.open('assets/Pytube.png'))
img_container = ttk.Label(
    win,
    background = color,
    image = img1,
    relief= tk.GROOVE,
    borderwidth = 5
)
img_container.grid(row = 1, column=0,sticky = tk.N)

# this allows users to enter data specifically the videos's url from youtube should be pasted
get_Url = ttk.Label(frame1, 
    text="Enter YouTube Video Link : ",
    background='#ffbfbf',
    relief = rf
)
get_Url.grid(row=0, column=0,sticky= tk.W)
# this binds videoUrl variable to whatever the user enters
videoUrl = tk.StringVar()
# this allows users to enter data specifically the videos's url from youtube should be pasted
yt_link = ttk.Entry(frame1, width=60, textvariable = videoUrl)
yt_link.grid(row=1,
    columnspan=3, 
    padx=0, 
    pady=3
)

#  this just displays a for users to see what is happening under the hood
# so if anything goes wrong you will see a message
show_status = ttk.Label(frame1, 
    text="status bar",
    background='#ffbfbf',
    relief = rf
)
show_status.grid(row=3, column=0, sticky= tk.W)


show_status_widget = ttk.Label(frame1,background="white", foreground = "black",width=60)
show_status_widget.grid(row=4, 
    columnspan=3, 
    padx=0, 
    pady=3
)
# this button must  be pressed inorder download the video
downloadBtn = tk.Button(frame1, text="Download Video",
    width=15,
    relief = rf,
    command=lambda:startDownload()
)
downloadBtn.grid(row=7, 
    columnspan=3, 
    padx=13, 
    pady=7
)

# this is the last frame which is the parent for our list and progress bar 
frame2 = tk.Frame(win,
    relief=rf, 
    background= color
)
frame2.grid(row=3, 
    column=0, 
    padx=70, 
    pady=10,
    sticky = tk.N
)

# this is where the user can go and choose a quality 
lislab = ttk.Label(frame2,
    text = 'Choose the quality'
)
lislab.grid(row = 1,column=0)
lisbox = tk.Listbox(
    frame2,
    relief=rf,
    width = 40,
    height = 8,
    selectmode = tk.SINGLE #the user can only choose one item at a time
)
lisbox.grid(row = 2,column=0)

# this will go under the hood and get the qualities from the youtube
show_videoQuality = tk.Button(frame2,text= "Get video quality", command = lambda: video_quality())
show_videoQuality.grid(row=3,column=0)
# still in development
progressbar = ttk.Progressbar(frame2)
progressbar.grid(row=4,column=0, pady= 30)

#  Pytube logic

def video_quality():
    ''' Gets the quality of a video and binds it to the list and inserts it into the list'''
    url = videoUrl.get()
    try: 
      yt = YouTube(url)
    except: 
       messagebox.showwarning('warning',textwrap.fill('Please check internet connection and try again also check that you have pasted the url correctly.',width =40))
    else:
      video_qualities = yt.streams.filter(progressive= True)
      for v in video_qualities:
    	  m = str(v).split(' ')
    	  y = m[1]
    	  sizev = v.filesize * (9.5367431640625*10**-7)
    	  vs = round(sizev,2)
    	  lisbox.insert(tk.END,f'{y} ==> size: {(vs)}mb')


def startDownload():
    ''' starts the download process when the downlpad button is clicked'''
    url = videoUrl.get()
    try:
      yt = YouTube(url)
    except:
      messagebox.showwarning('warning',textwrap.fill('Please check internet connection and try again also check that you have pasted the url correctly.',width =40))
    else:
      if lisbox.curselection() ==  ():
        justDownload = yt.streams.get_highest_resolution()
        show_status_widget.configure(text = f"video saved at {justDownload.download()}")
      else:
        choice = lisbox.get(lisbox.curselection(),last = None)
        
        decoded_choice = choice[6:8]
        
        intialization = yt.streams.get_by_itag(int(decoded_choice))
        show_status_widget.configure(text = f"video saved at {intialization.download()}")
      

win.mainloop()
#https://youtu.be/tPEE9ZwTmy0q