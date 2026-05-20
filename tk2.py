from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("lohit's GUI")
# important label options
# text= adds the text
# bd=background
# fg=foreground
# font= sets the font
# padx= x padding
# pady= y padding
# relief=border styling-SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text='''Elon Reeve Musk  born June \n28, 1971) is a businessman and public official known \nfor his leadership of Tesla and SpaceX. Musk\n has been the wealthiest person in the world since 2\n025; as of May 2026, Forbes estimates his net worth \nto be US$788 billion.

Born\n into the wealthy Musk family in Pr\netoria, South Africa, Musk emigrated i\nn 1989 to Canada; he has Cana\ndian citizenship since his mo\nther was born there. He received bachelor'\ns degrees in 1997 from the University of Penn\nsylvania before moving to California t\no pursue business ventures. In 1995\n, Musk co-founded the software company Zip\n2. Following its sale in 1999, he co-founde\nd X.com, an online payment company that later\n merged to form PayPal, which was acquired\n by eBay in 2002. Musk also became an American cit\nizen in 2002.
             '''
,bg="black",fg="white",font="italic 15 bold",padx=200,pady=500,borderwidth=5,relief=RAISED)
# important pack options
# anchor=(direction)nw
# side=top,bottom,left,right
# fill=x(extends x)
# fill=Y(extends Y)
# padx= padding x
# pady=padding Y
# title_label.pack(side=BOTTOM,anchor="se",fill=X)
title_label.pack(side=TOP,fill=Y,padx=50,pady=50)

root.mainloop()
