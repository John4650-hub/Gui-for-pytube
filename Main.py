import sys
from tkinter import *
from tkinter import ttk,filedialog
from tkinter import messagebox as m_box
from PIL import ImageTk, Image
from pytube import YouTube

#bind to lable to show video's title
videoTitle = None
#bind to entry to show the storage adress
vStgAdrs = None

def video_quality(urlVariable, lis):
    url = urlVariable.get()
    yt = YouTube(url)
    video_qualities = yt.streams.filter(progressive= True)
    i = 1
    for v in video_qualities:
        m = str(v).split(' ')
        y = m[1]
        sizev = v.filesize * (9.5367431640625*10**-7)
        vs = round(sizev,2)
        lis.insert(i,f'  {y} ==> size: {(vs)}mb')
        i+=1


def startDownload(urlVariable, lisBoxObject):
    url = urlVariable.get()
    listB = lisBoxObject
    yt = YouTube(url)
    if listB.curselection() == ():
        justDownload = yt.streams.get_by_itag('18')
        justDownload.download()
    else: 
        quality = str(listB.get(listB.curselection(),last=None))
        letsDownload = yt.streams.get_by_itag(quality)
        letsDownload.download()

#ui of the app
color = 'grey'
rf = RAISED # this tells whatever widget that has it to be raised
win = Tk()
win.title("GUI FOR PYTUBE")
win.configure(bg = color)

frame1 = Frame(win,
    relief = GROOVE, 
    bg = color
)
frame1.grid(row=2, 
    column=0, 
    padx=70, 
    pady=50
)
h1 = ttk.Label(
    win,
    text = 'Gui for pytube',
    relief=rf,
    background = color
    )
    
h1.grid(row=0,column=0)

img1 = ImageTk.PhotoImage(Image.open('assets/Pytube.png'))
img_container = ttk.Label(
    win,
    background = color,
    image = img1,
    relief= GROOVE,
    borderwidth = 5
)
img_container.grid(row = 1, column=0)
get_info = ttk.Label(frame1, 
    text="Enter YouTube Video Link : ",
    background='#ffbfbf',
    relief = rf
)
get_info.grid(row=0, column=0,sticky= W)

videoUrl = StringVar()
yt_link = ttk.Entry(frame1, width=60, textvariable = videoUrl)
yt_link.grid(row=1,
    columnspan=3, 
    padx=0, 
    pady=3
)

yt_link.focus()
get_info = ttk.Label(frame1, 
    text="Choose download path ",
    background='#ffbfbf',
    relief = rf
)
get_info.grid(row=3, column=0, sticky= W)

download_path = ttk.Entry(frame1, width=60)
download_path.grid(row=4, 
    columnspan=3, 
    padx=0, 
    pady=3
)

btn1 = Button(frame1, text="Download Video",
    width=15,
    relief = rf,
    command=lambda:print(startDownload(videoUrl,lisbox))
)
btn1.grid(row=7, 
    columnspan=3, 
    padx=13, 
    pady=7
)

frame2 = Frame(win,
    relief=rf, 
    background= color
)

frame2.grid(row=3, 
    column=0, 
    padx=70, 
    pady=10
)

lislab = ttk.Label(frame2,
    text = 'Choose the quality'
)
lislab.grid(row = 1,column=0)

lisbox = Listbox(
    frame2,
    relief=rf,
    width = 40,
    height = 8,
    selectmode = SINGLE
)
lisbox.grid(row = 2,column=0)
videoQuality_get = Button(frame2,text= "Get video quality", command = lambda: video_quality(videoUrl, lisbox))
videoQuality_get.grid(row=3,column=0)
progressbar = ttk.Progressbar(frame2)
progressbar.grid(row=4,column=0, pady= 30)

# Pytube logic

# video_quality(yt,lisbox)

win.mainloop()
