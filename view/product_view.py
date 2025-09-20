from tkinter import *
import tkinter as tk
import tkinter.messagebox as msg
from tools.validation import *
from data_base.db_module import *

# عملکرد دکمه save
def save_order():
    try:
        product_name_validator(product_name.get())
        save_order(product_name.get(), order_datetime.get(),status.get(), deliver_datetime.get())
        msg.showinfo("Save", "order saved")
    except Exception as e:
        msg.showerror("Error", f"{e}")

# عملکرد دکمه show
def show_sent_product():
    try:
        msg.showinfo("sent products", find_sent_orders )
    except Exception as e:
        msg.showerror("Error", f"{e}")


# نشان دادن کالاهای ریجکت شده
msg.showwarning("Rejected products", find_rejected_orders )

window = Tk()
window.geometry("600x450")
window.title("orders")
window.configure(bg="light pink")
Label(text="order information", bg="yellow", font=30).place(x=235, y=5)

# product
product_name = StringVar()
Label(text="product:", bg="light pink", font=30).place(x=15, y=40)
Entry(window, textvariable=product_name, width=45).place(x=80, y=44)

#order datetime
order_datetime = StringVar()
Label(text="oder date:", bg="light pink", font=30).place(x=15, y=80)
Label(text="order time:", bg="light pink", font=30).place(x=280, y=80)


# status
status = StringVar(value="None")
Label(text="status:", bg="light pink", font=30).place(x=15, y=157)
Radiobutton(window, text="None", variable=status, value="None",font=30, bg="light pink").place(x=15, y=194)
Radiobutton(window, text="send", variable=status, value="send",font=30, bg="light pink").place(x=95, y=194)
Radiobutton(window, text="delivered", variable=status, value="delivered",font=30, bg="light pink").place(x=175, y=194)
Radiobutton(window, text="rejected", variable=status, value="rejected",font=30, bg="light pink").place(x=280, y=194)

#deliver datetime
deliver_datetime = StringVar()
# deliver_date = StringVar()
# deliver_time = StringVar()
Label(text="deliver date: ", bg="light pink", font=30).place(x=15, y=237)
Label(text="deliver time: ", bg="light pink", font=30).place(x=280, y=237)




#ذخیره سفارش
Button(window, text="Save order", width=15, command=save_order, font=50).place(x=230, y=340)

#کالا های سند شده
Button(window, text="Show all sent orders", width=30, command=show_sent_product, font=50).place(x=165, y=380)


window.mainloop()
