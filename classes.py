from kivy.app import App


class Gui(App):

    def build(self):

        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.config import Config

        bl = BoxLayout()
        self.lbl = Label(text='SELECT LOGIN OPTION', font_size=40)
        bl.add_widget(self.lbl)
        bl.add_widget(Button(text='LOG IN'))
        bl.add_widget(Button(text='SIGN UP'))
        return bl


class Identification:

    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXIST users(
                            userid INT PRIMARY KEY,
                            login TEXT,
                            password TEXT,
                            );""")

    def entry(self):
        pass

    def login(self):
        pass

    def registration(self):
        pass
