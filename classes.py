from kivy.app import App


class GuiApp(App):




    def build(self):

        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.config import Config
        from kivy.uix.textinput import TextInput
        import sqlite3

        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                                        userid INT PRIMARY KEY,
                                        login TEXT,
                                        password TEXT
                                            );""")

        Config.set('graphics', 'resizable', 0)
        Config.set('graphics', 'width', 500)
        Config.set('graphics', 'height', 500)
        Config.write()
        bl = BoxLayout(orientation='vertical')
        self.lbl = Label(text='SELECT LOGIN OPTION', font_size=40)
        bl.add_widget(self.lbl)

        bl2 = BoxLayout(orientation='vertical')

        self.txt_1 = TextInput(text='', font_size=40)
        self.txt_2 = TextInput(text='', font_size=40)
        bl2.add_widget(self.txt_1)
        bl2.add_widget(self.txt_2)
        bl.add_widget(bl2)

        bl3 = BoxLayout(orientation='horizontal')
        bl3.add_widget(Button(text='LOG IN', font_size=40, on_press=self.login))
        bl3.add_widget(Button(text='SIGN UP', font_size=40, on_press=self.registration))
        bl.add_widget(bl3)
        return bl

    def entry(self):
        pass

    def login(self, instance):

        login = self.txt_1.text
        password = self.txt_2.text
        self.cur.execute("""SELECT * FROM users""")
        all_of_that = self.cur.fetchall()

        for i in range(1, 9999):
            if i in all_of_that:
                self.cur.execute(f"SELECT * FROM users WHERE login={login}")
                user_all = self.cur.fetchall()
                print(user_all)

                break

    def registration(self, instance):
        login = self.txt_1.text
        password = self.txt_2.text
        self.cur.execute("""SELECT * FROM users""")
        all_of_that = self.cur.fetchall()
        userid = ()

        for i in range(1, 9999):
            if i not in all_of_that:
                userid = i
                break

        all_of_that = (userid, login, password)
        self.cur.execute("""INSERT INTO users VALUES(?, ?, ?);""", all_of_that)
        self.conn.commit()




