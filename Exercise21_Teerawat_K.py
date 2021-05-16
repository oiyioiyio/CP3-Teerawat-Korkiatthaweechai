from tkinter import *
import math

def leftclickButton(event):
    labelResult.configure(text=BMIResult(textBoxHeight.get(), textBoxlWeight.get()))

def BMIResult(Height, Weight):
    try:
        Result = float(Weight) / math.pow(float(Height) / 100, 2)
    except:
        return "ค่าที่ท่านกรอกไม่ถูกต้อง"

    if Result > 30.0:
        return "อ้วนมาก"
    elif Result > 25.0:
        return "อ้วน"
    elif Result > 23.0:
        return "น้ำหนักเกิน"
    elif Result > 18.6:
        return "น้ำหนักปกติ เหมาะสม"
    elif Result < 18.5:
        return "ผอมเกินไป"

main = Tk()
labelHeight = Label(main, text='ส่วนสูง (cm)')
labelHeight.grid(row=0,column=0)
textBoxHeight  = Entry(main)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(main, text='น้ำหนัก (Kg)')
labelWeight.grid(row=1,column=0)
textBoxlWeight = Entry(main)
textBoxlWeight.grid(row=1,column=1)
calculateButton = Button(main,text='คำนวณ')
calculateButton.bind('<Button-1>', leftclickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(main, text='ผลลัพธ์')
labelResult.grid(row=2,column=1)
main.mainloop()
