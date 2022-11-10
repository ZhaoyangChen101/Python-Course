try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter

import os

mainWindows = tkinter.Tk()

mainWindows.title("Grid Demo")
mainWindows.geometry("640x480-8-200")
mainWindows['padx'] = 8

label = tkinter.Label(mainWindows, text="TKinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# 当同一处有几个板块stack的时候，可以将该行weight调低，这样伸缩的时候比例改变较小。
# 当同一处几个板块并列的时候，可以将该列weight调低，这样伸缩的时候比例改变较小。
mainWindows.columnconfigure(0, weight=100)
mainWindows.columnconfigure(1, weight=1)   # 因为扩张的越快，收缩也会越快，所以给了一个小的weight给scroll bar
mainWindows.columnconfigure(2, weight=1000)
mainWindows.columnconfigure(3, weight=600)
mainWindows.columnconfigure(4, weight=1000)
mainWindows.rowconfigure(0, weight=1)
mainWindows.rowconfigure(1, weight=10)  # 因为在延伸窗口会对listbox有好处，所以此行的weight就比较高。
mainWindows.rowconfigure(2, weight=1)
mainWindows.rowconfigure(3, weight=3)
mainWindows.rowconfigure(4, weight=3)

# add a listbox
fileList = tkinter.Listbox(mainWindows)
fileList.grid(row=1, column=0, sticky="nsew", rowspan=2)
fileList.config(border=2, relief='sunken')  # flat, grooved, raised, ridged, solid
# add elements to the listbox
for zone in os.listdir('/usr/bin'):  # '/Windows/System32'
    fileList.insert(tkinter.END, zone)  # tkinter.END表示新元素插入的位置在最后。如果此位置是0，就是表示插入在最开始。
# add a scroll bar
listScroll = tkinter.Scrollbar(mainWindows, orient=tkinter.VERTICAL, command=fileList.yview)   # command后面只应该写方法的名称，即不写括号那种。
# orient=tkinter.VERTICAL -> scrollbar要竖着放。
# yview -> Query and change the vertical position of the view.
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
# one further step to link scroll box to the list box
fileList['yscrollcommand'] = listScroll.set

# frame for the  radio buttons
optionFrame = tkinter.LabelFrame(mainWindows, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()  # 表示只能选一个，选另一个的时候，先选的那一个自动取消。
rbValue.set(1)  # default option: 3rd option
# radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# result & text field -> widget to display the result
resultLable = tkinter.Label(mainWindows, text="Result")  # Label -> 标题
resultLable.grid(row=2, column=2, sticky='nw')           # Entry -> text field
result = tkinter.Entry(mainWindows)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindows, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))  #from_ to 和这里的values等价
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)  # from_后面的下划线是和python自带的from关键字做一个区分
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
# 先定义好对象即其放在什么板块中，然后设置在该板块中的位置。
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
# 对板块内部的元素进行排版，增加padding
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainWindows)
dateFrame.grid(row=4, column=0, sticky='new')
# Date labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# Date spinner
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                                                        "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# buttons
okButton = tkinter.Button(mainWindows, text="OK")
# cancelButton = tkinter.Button(mainWindows, text="Cancel", command=mainWindows.quit())
# command后面的方法如果写了括号，就不能成功执行了，因为这样就表示将方法的值返回给command，此处就成了command=None。
# cancelButton = tkinter.Button(mainWindows, text="Cancel", command=mainWindows.quit)  # 这个就可以了。
cancelButton = tkinter.Button(mainWindows, text="Cancel", command=mainWindows.destroy)  # 这个就可以了。
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')



mainWindows.mainloop()

print(rbValue.get())  #radio button选择的哪一个此处就返回哪一个的value。
