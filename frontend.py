from tkinter import *

# creating a window for our content
window = Tk()

# creating a label
labelTitle = Label(window, text="Title")
# positioning a label
labelTitle.grid(row=0, column=0)

labelYear = Label(window, text="Year")
labelYear.grid(row=0, column=2)

labelAuthor = Label(window, text="Author")
labelAuthor.grid(row=1, column=0)

labelISBN = Label(window, text="ISBN")
labelISBN.grid(row=1, column=2)

text_title = StringVar()
# StringVar() creates a spatial variable
titleEntry = Entry(window, textvariable=text_title)
# textvariable expects a spatial variable
titleEntry.grid(row=0, column=1)

text_year = StringVar()
yearEntry = Entry(window, textvariable=text_year)
yearEntry.grid(row=0, column=3)

text_Author = StringVar()
AuthorEntry = Entry(window, textvariable=text_Author)
AuthorEntry.grid(row=1, column=1)

text_ISBN = StringVar()
ISBNEntry = Entry(window, textvariable=text_ISBN)
ISBNEntry.grid(row=1, column=3)

# adding a ListBox
bookList = Listbox(window, height=6, width=35)
# positioning the scollbar
bookList.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)  # positioning the scollbar


# Attaching Vertical Scrollbar and Book listbox together

# The vertical scrollbar along the y-axis will be set to "scrollbar"
bookList.configure(yscrollcommand=scrollbar.set)

# When you scroll the scrollbar "yview" i.e vertical view of bookList will change
scrollbar.configure(command=bookList.yview)

# Creating Buttons

viewAllBtn = Button(window, text="View All", width=12)
viewAllBtn.grid(row=2, column=3)

searchEntryBtn = Button(window, text="View Entry", width=12)
searchEntryBtn.grid(row=3, column=3)

addEntryBtn = Button(window, text="Add Entry", width=12)
addEntryBtn.grid(row=4, column=3)

updateBtn = Button(window, text="Update", width=12)
updateBtn.grid(row=5, column=3)

deleteBtn = Button(window, text="Delete", width=12)
deleteBtn.grid(row=6, column=3)

closeBtn = Button(window, text="Close", width=12)
closeBtn.grid(row=7, column=3)


window.mainloop()
