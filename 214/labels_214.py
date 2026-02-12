#################################################################################
#   a214_TR_button6.py
#   Example Solution: Adds a button.
################################################################################
import tkinter as tk

def test_my_button():
    # TODO: Use get method of ent_password when the button is pressed,
    # and store the result
    user_pass = ent_password.get()
    username = ent_username.get()
    # TODO: Configure the label in frame_auth to display the password
    display = "Here, " + username + ", here's your password: " + user_pass 
    lbl_display.config(text=display)
    frame_auth.tkraise()
    root.title("Inside the Vault")


# main window
root = tk.Tk()
root.wm_geometry("400x200")
root.title("Authentication")


# create empty frame
frame_login = tk.Frame(root, background="Black")
frame_login.grid(row=0, column=0, sticky='news')

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_login,text='Username:',font="Times")
lbl_username.pack(pady=5)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login,text='Password:', font='Arial')
lbl_password.pack(padx=5)

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack(padx=175, pady=20)

lbl_display = tk.Label(frame_auth,text='Password:', font='Arial')
lbl_display.pack(padx=5)

frame_login.tkraise()
root.mainloop()