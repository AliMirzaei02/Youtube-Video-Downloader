import pytube
from pytube import YouTube
from tkinter import *
from tkinter import filedialog, messagebox


def Download():
    try:
        selected = listbox.curselection()
        video = video_qualities[selected[0]]
        filename = name.get()
        location = path.get()

        if filename == '' and location != '':
            video.download(location)
        elif filename != '' and location == '':
            location = 'Downloads'
            video.download(location, str(filename)+'.mp4')
        elif filename == '' and location == '':
            location = 'Downloads'
            video.download(location)
        else:
            video.download(location, str(filename)+'.mp4')

        messagebox.showinfo('DownloadSuccessfully','Downloaded and saved in\n'+ location)
    
    except NameError:
        messagebox.showerror('NameError', 'Set the link and try again.')
    except IndexError:
        messagebox.showerror('IndexError', 'Choose a resolution and try again.')
    except:
        messagebox.showerror('Error', 'Connection failed.\nChoose another resolution and try again.')


def Reset():
    name.set('')
    path.set('')
    link.set('')
    listbox.delete(0,END)


def Browse():
	download_Directory = filedialog.askdirectory(title='Save Video')
	path.set(download_Directory)


def SetLink():
    try:
        URL = YouTube(link.get())

        global video_qualities
        video_qualities = URL.streams.filter(mime_type='video/mp4')

        count = 1
        for v in video_qualities:
            splited = str(v).split(' ')
            resolution = splited[2]+"   "+splited[3]+"   "+splited[4]
            listbox.insert(END, str(count)+'-   '+str(resolution)+'\n\n')
            count += 1
    
    except pytube.exceptions.RegexMatchError:
        messagebox.showerror('RegexMatchError', 'The Regex pattern did not return any matches for the video')
    except pytube.exceptions.ExtractError:
        messagebox.showerror ('ExtractError', 'An extraction error occurred for the video')
    except pytube.exceptions.VideoUnavailable:
        messagebox.showerror('VideoUnavailable', 'The following video is unavailable')
    except:
        messagebox.showerror('Error', 'Connection failed.')



root = Tk()
root.geometry('400x500')
root.iconbitmap(r'icon.ico')
root.configure(background='red')
root.resizable(False, False)
root.title("YouTube Video Downloader")


name = StringVar()
path = StringVar()
link = StringVar()


Label(root, text='Link: ', fg='white' ,bg='red', font='arial 12 bold').place(x=10, y=10)
Entry(root, width=41, textvariable=link, fg='red').place(x=30, y=40)
Button(root, text='Set link', font='arial 7 bold', command=SetLink, width=12, fg='red' ,bg='white', relief=GROOVE).place(x=282, y=40)

listbox = Listbox(root, font='arial 8 bold', width = 55, height = 13, bd=3, borderwidth=1, fg='red' ,bg='white', relief=GROOVE)
listbox.place(x=30, y=80)

Label(root, text='Name: ', fg='white' ,bg='red', font='arial 12 bold').place(x=10, y=290)
Entry(root, width=55, textvariable=name, fg='red').place(x=30, y=320)

Label(root, text='Path: ', fg='white' ,bg='red', font='arial 12 bold').place(x=10, y=360)
Entry(root, width=41, textvariable=path, fg='red').place(x=30, y=390)
Button(root, text='Browse', font='arial 7 bold', command=Browse, width=12, fg='red' ,bg='white', relief=GROOVE).place(x=282, y=390)

Button(root, text='Download', font='arial 15 bold', fg='red' ,bg='white', command = Download).place(x=253, y=440)

Button(root, text='Reset', font='arial 15 bold', fg='red' ,bg='white', command = Reset).place(x=30, y=440)


root.mainloop()