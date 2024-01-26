from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.utils import rgba
from kivymd.uix.screen import MDScreen

from kivymd.uix.screenmanager import MDScreenManager

from kivy.lang import Builder
Builder.load_file('main.kv')

# screen names
_home = "home"

class SideBar(MDBoxLayout):
    pass

class CenterBar(MDBoxLayout):
    pass

class HomeScreen(MDScreen):
    pass



class ITX_AD(MDApp):
    
    def build(self):
        super().build()
        self.box = MDBoxLayout(md_bg_color=rgba("#3333CC"))
        self.box.padding = "20dp","10dp","20dp","0dp"
        self.box
        self.sm = MDScreenManager()
        self.sm.pos_hint={'center_x':0.5,'bottom':1}
        self.sm.add_widget(HomeScreen(name=_home))
        self.box.add_widget(self.sm)
        return self.box
    


if __name__ =="__main__":
    app = ITX_AD()
    app.run()
    