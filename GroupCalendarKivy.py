# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.textinput import TextInput

import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView

Window.clearcolor = (100/255, 150/255, 200/255, 0.3)

class RemovableButton(Button):
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.parent.remove_widget(self)
            return True
        # return super(RemovableButton, self).on_touch_down(touch)
        pass

    def on_touch_up(self, touch):
        if touch.button == 'left':
            if self.collide_point(touch.x, touch.y):
                self.opacity = 1
                return True
    
# class AddGroupCalendarButton(Button):
#     def on_touch_down(self, touch):
#             if self.collide_point(touch.x, touch.y):
#                 print("add calendar")
#                 return True
            

class MyLayout(FloatLayout):
    my_calendar = ObjectProperty(None)
    group_calendar_box = ObjectProperty(None)
    add_group_calendar_button = ObjectProperty(None)



    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        
        self.count = 0
        
        # when clicked, the new group cal but adds a new group cal to grid

        # print(self.group_calendar_box.button)


        # self.add_widget(Button(text="My Calendar"))
 
        # self.inside = GridLayout()
        # number_of_group_calendars = 2
        # self.inside.rows = 1 + number_of_group_calendars

        # self.group_calendar_1 = Button(text="Group 1")
        # self.group_calendar_1.bind(on_press=self.group_1_pressed)

        # self.group_calendar_2 = Button(text="Group 2")
        # self.group_calendar_2.bind(on_press=self.group_2_pressed)

        # self.inside.add_widget(Label(text="Group Calendars"))
        # self.inside.add_widget(self.group_calendar_1)
        # self.inside.add_widget(self.group_calendar_2)

        # self.add_widget(self.inside)


    def my_calendar_pressed(self):
        print("pressed")
    
    # def group_1_pressed(self):
    #     print("pressed", self.button_1.text)
    
    # def group_2_pressed(self, instance):
    #     print("pressed")

    def add_group_calendar_pressed(self):
        print("add calendar test")

        self.count += 1
        new_group_calendar_button = RemovableButton(text='Group Calendar '+ str(self.count))
        self.group_calendar_box.add_widget(new_group_calendar_button, index=0)

        print(self.count)





    # def on_touch_down(self, touch):
    #     pass
    
    # def on_touch_move(self, touch):
    #     pass

    # def on_touch_up(self, touch):
    #     self.my_calendar.opacity = 1




    # pass


class MyApp(App):
    def build(self):
        return MyLayout()
    
        # return MyGrid()


if __name__ == "__main__":
    MyApp().run()

