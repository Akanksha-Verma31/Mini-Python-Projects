# kivy library is used to make apps
# it is having many things inside this library like grids, label, etc which we call its sub parts
# now we would be importing then here

import kivy
from kivy.app import App    # to make app
from kivy.uix.gridlayout import GridLayout     # to make grids
from kivy.uix.label import Label     # inside grids we need to label them
from kivy.uix.textinput import TextInput    # to take input from user
from kivy.uix.button import Button     # it will create a button, clicking on which it will show all the data stored

class LibraryGrid(GridLayout):
    def __init__(self, **kwargs):
        super(LibraryGrid, self).__init__()
        self.cols = 4

        self.add_widget(Label(text="Student Name : "))
        self.a_name = TextInput()
        self.add_widget(self.a_name)

        self.add_widget(Label(text="Name of Book : "))
        self.a_book = TextInput()
        self.add_widget(self.a_book)

        self.add_widget(Label(text="Issue Date : "))
        self.a_issue = TextInput()
        self.add_widget(self.a_issue)

        self.add_widget(Label(text="Return Date : "))
        self.a_return = TextInput()
        self.add_widget(Label(text="Fine : "))

        self.add_widget(Label(text="Fine : "))
        self.a_fine = TextInput()
        self.add_widget(self.a_fine)

        self.press = Button(text="Click here to print information")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name of the Student : " +self.a_name.text)
        print("Name of the Book : "+self.a_book.text)
        print("Issue Date : "+self.a_issue.text)
        print("Return Date : "+self.a_return.text)
        print("Any Fine : "+self.a_fine.text)

class LibraryApp(App):
    def build(self):
        return LibraryGrid()

if __name__ == '__main__':
    LibraryApp().run()
