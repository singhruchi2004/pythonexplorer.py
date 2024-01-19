from tkinter import * 
import os 
import shutil
from tkinter import messagebox as mb 
from tkinter import filedialog as fd  


def openAFile():
    
    files = fd.askopenfilename(
        title="Select a file of any type",filetypes=[("All files", "*.*")]
    )
    os.startfile(os.path.abspath(files))


def copyAFile():
    copythefile = fd.askopenfilename(
        title="Select a file to copy",filetypes=[("All files", "*.*")]
    )
    
    dirToPaste = fd.askdirectory(title="Select the folder to paste the file")
    try:
        shutil.copy(copythefile, dirToPaste)
        mb.showinfo(title="File copied!",message="The file has been copied to the destination."
        )
    except:
        mb.showerror(title="Error!",message="File is unable to copy . Please try again!"
        )

def deleteAFile():
    
    files = fd.askopenfilename(
        title="Choose a file to delete",filetypes=[("All files", "*.*")]
    )
    
    os.remove(os.path.abspath(files))
    mb.showinfo(title="File deleted!", message="The selected file has been deleted.")



def renameAFile():
    rename_win = Toplevel(win_root)
    rename_win.title("Rename File")
    rename_win.geometry("300x100+300+250")
    rename_win.resizable(0, 0)
    rename_win.configure(bg="#F6EAD7")

    
    rename_label = Label(
        rename_win,text="Enter the file name:",font=("Calibri", "8"),bg="white",fg="blue"
    )
    
    rename_label.pack(pady=4)
    rename_field = Entry(rename_win,width=26,textvariable=fileNameEntered,relief=GROOVE,
        font=("Calibri", "10"),bg="white",fg="blue"
    )
    
    rename_field.pack(pady=4, padx=4)

    
    submitButton = Button(
        rename_win,text="Submit",command=NameSubmit,width=14,relief=GROOVE,font=("Calibri", "9"),
        bg="white",fg="blue",activebackground="#709218",activeforeground="#FFFFFF"
    )
    submitButton.pack(pady=2)



def showFilePath():
    files = fd.askopenfilename(title="Select the file to rename", filetypes=[("All files", "*.*")])
    return files



def NameSubmit():
    renameName = fileNameEntered.get()
    
    fileNameEntered.set("")
    fileName = showFilePath()
    
    newFileName = os.path.join(os.path.dirname(fileName), renameName + os.path.splitext(fileName)[1])
    os.rename(fileName, newFileName)
    mb.showinfo(title="File Renamed!", message="The selected file has been renamed.")

def openAFolder():
    
    folder1 = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder1)


def deleteAFolder():
    folderToDelete = fd.askdirectory(title='Select Folder to delete')
    os.rmdir(folderToDelete)
    mb.showinfo("Folder Deleted!", "The selected folder has been deleted!")



def moveAFolder():
    folderToMove = fd.askdirectory(title='Select the folder you want to move')
    mb.showinfo(message='Folder has been selected to move. Now, select the desired destination.')
    des = fd.askdirectory(title='Destination')
    try:
        
        shutil.move(folderToMove, des)
        mb.showinfo("Folder moved!", 'The selected folder has been moved to the desired Location')
    except:
        mb.showerror('Error!', 'The Folder cannot be moved. Make sure that the destination exists')



def listFilesInFolder():
    i = 0
    
    folder1= fd.askdirectory(title="Select the Folder")
    files = os.listdir(os.path.abspath(folder1))
    listFilesWindow = Toplevel(win_root)
    
    listFilesWindow.title(f'Files in {folder1}')
    listFilesWindow.geometry("300x500+300+200")
    listFilesWindow.resizable(0, 0)
    listFilesWindow.configure(bg="white")


    the_listbox = Listbox(
        listFilesWindow,selectbackground="#F24FBF",font=("Calibri", "10"),background="white"
    )
    the_listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    the_scrollbar = Scrollbar(
        the_listbox,orient=VERTICAL,command=the_listbox.yview
    )
    the_scrollbar.pack(side=RIGHT, fill=Y)
    
    the_listbox.config(yscrollcommand=the_scrollbar.set)

    
    while i < len((files)):
        the_listbox.insert(END, "[" + str(i + 1) + "] " + files[i])
        i += 1
    the_listbox.insert(END, "")
    the_listbox.insert(END, "Total Files: " + str(len(files)))


if __name__ == "__main__":

    win_root = Tk()
    win_root.title("File Explorer")
    win_root.geometry("400x600+650+250")
    win_root.resizable(0, 0)
    win_root.configure(bg="white")

    
    header_frame = Frame(win_root, bg="#D8E9E6")
    buttons_frame = Frame(win_root, bg="skyblue")


    header_frame.pack(fill="both")
    buttons_frame.pack(expand=TRUE, fill="both")

    header_label = Label(
        header_frame,text="File Explorer",font=("Calibri", "16"),bg="white",fg="blue"
    )

    
    header_label.pack(expand=TRUE, fill="both", pady=12)

    
    open_button = Button(
        buttons_frame,text="Open a File",font=("Calibri", "15"),width=20,bg="white",fg="blue",relief=GROOVE,
        activebackground="blue",command=openAFile
    )
    
    rename_button = Button(
        buttons_frame,
        text="Rename a File",font=("Calibri", "15"),width=20,bg="white",fg="blue",relief=GROOVE,
        activebackground="white",command=renameAFile
    )
    
    copy_button = Button(
        buttons_frame,text="Copy the File",font=("Calibri", "15"),width=20,bg="white",fg="blue",
        relief=GROOVE,activebackground="blue",command=copyAFile
    )

    
    delete_button = Button(
        buttons_frame,text="Delete a File",font=("Calibri", "15"),width=20,bg="white",fg="blue",
        relief=GROOVE,activebackground="white",command=deleteAFile
    )
    
    open_folder_button = Button(
        buttons_frame,text="Open a Folder",font=("Calibri", "15"),width=20,bg="white",fg="Blue",
        relief=GROOVE,activebackground="blue",command=openAFolder
    )

    
    delete_folder_button = Button(
        buttons_frame,text="Delete Folder",font=("Calibri", "15"),width=20,bg="white",fg="blue",relief=GROOVE,
        activebackground="blue",command=deleteAFolder
    )


    move_folder_button = Button(
        buttons_frame,text="Move the Folder",font=("Calibri", "15"),width=20,bg="white",fg="Blue",relief=GROOVE,
        activebackground="Blue",command=moveAFolder
    )
    
    list_button = Button(
        buttons_frame,text="List files in Folder",font=("Calibri", "15"),width=20,bg="white",fg="Blue",relief=GROOVE,
        activebackground="Blue",command=listFilesInFolder
    )
    
    fileNameEntered = StringVar()

    
    open_button.pack(pady=9)
    rename_button.pack(pady=9)
    copy_button.pack(pady=9)
    delete_button.pack(pady=9)
    move_folder_button.pack(pady=9)
    open_folder_button.pack(pady=9)
    delete_folder_button.pack(pady=9)
    list_button.pack(pady=10)
    win_root.mainloop()