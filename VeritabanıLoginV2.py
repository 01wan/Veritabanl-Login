from tkinter import *
import sqlite3
import webbrowser

login = Tk()
login.title("Login Panel")
login.geometry("500x500")

dnameText = Label(login, text="Kullanıcı adı: ", font=('Arial', 15))
dnameText.pack()
dname = Entry(login)
dname.pack()

dpassText = Label(login, text="Şifre: ", font=('Arial', 15))
dpassText.pack()
dpass = Entry(login)
dpass.pack()

database_connect = sqlite3.connect("login.db")

with sqlite3.connect("login.db") as database_connect:
    imlec = database_connect.cursor()
    imlec.execute(
        """CREATE TABLE IF NOT EXISTS accounts(username TEXT, password TEXT) """)


#   for i in veriler:


    def kayit():
        uname = dname.get()
        upass = dpass.get()

        imlec.execute("""INSERT INTO accounts VALUES(?, ?)""", (uname, upass))

        imlec.execute("""SELECT *FROM accounts""")

    def giris():
        uname = dname.get()
        upass = dpass.get()
        global linkEntry

        imlec.execute(
            """SELECT *FROM accounts WHERE username = ? and password = ?""", (uname, upass))
        data = imlec.fetchone()

        def gonder(x):
            x = linkEntry.get()
            webbrowser.open(x)
            linkOppening = Label(
                look, text="Link açılıyor..", font=('Arial', 15))
            linkOppening.pack()

        if data:
            look = Tk()
            look.title("GÖNDER")
            look.geometry("500x500")

            linkText = Label(look, text="Link: ", font=('Arial', 15))
            linkText.pack()
            linkEntry = Entry(look)
            linkEntry.pack()

            gonderButton = Button(look, text="Gönder", font=(
                'Arial', 15), command=lambda: gonder(linkEntry))
            gonderButton.pack()

            welcome = Label(
                login, text=f"Hoş geldin {data[0]}", font=('Arial', 15))
            welcome.pack()
            look.mainloop()
        else:
            welcome = Label(login, text="Hatalı giriş!", font=('Arial', 15))
            welcome.pack()
            print("Hatalı giriş!")


#    account = imlec.fetchall()
#    for hesaplar in account:
#        print(hesaplar)

    kayitButton = Button(login, text="Kayıt ol", font=(
        'Arial', 15), command=lambda: kayit())
    kayitButton.pack()

    loginButton = Button(login, text="Giriş yap", font=(
        'Arial', 15), command=lambda: giris())
    loginButton.pack()

    database_connect.commit()

    login.mainloop()
