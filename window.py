from tkinter import *
from tkinter import messagebox
#ekranın tam ortasında başlatmak için
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
def btn_clicked():
    result = messagebox.showerror("Hata", "Form kapatılacak. Emin misiniz?")
    if result:
        window.destroy()

def btn_x():
     window.destroy()
     
window = Tk()

window.geometry("200x200")
window.configure(bg = "#000000")
window_width = 200
window_height = 200
center_window(window, window_width, window_height)
window.overrideredirect(True)   #pencere bölmesini gizler kücült kapat buttonlarının olduğu windows formunu

canvas = Canvas(
    window,
    bg = "#000000",
    height = 200,
    width = 200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    212.5, 67.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 59, y = 154,
    width = 81,
    height = 36)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    98.0, 130.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0, show="*")

entry0.place(
    x = 13, y = 118,
    width = 170,
    height = 22)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    99.5, 80.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 15, y = 68,
    width = 169,
    height = 22)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_x,
    relief = "flat",
    background="black")

b1.place(
    x = 169, y = -2,
    width = 32,
    height = 32)

window.resizable(False, False)
window.mainloop()
