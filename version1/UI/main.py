from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RectangularElevationBehavior,RoundedRectangularElevationBehavior,CommonElevationBehavior
from kivymd.uix.button import MDRoundFlatButton
from kivy.utils import rgba
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import NoTransition
from kivy.core.window import Window



from kivy.lang import Builder
Builder.load_file('main.kv')

# screen names
_export_adusers = "export_adusers"
_adusers = "adusers"

class BaseShadowWidget(CommonElevationBehavior):
    pass

class FilterWidget(MDBoxLayout):
    pass

class TitleBar(BaseShadowWidget,MDBoxLayout):
    pass

class SpecificButton(CommonElevationBehavior,MDRoundFlatButton):
    pass

class SideBar(BaseShadowWidget,MDBoxLayout):
    pass

class CenterBar(MDBoxLayout):
    pass



class HomeScreen(MDScreen):
    pass

class UsersScreen(MDScreen):
    pass


class ITX_AD(MDApp):
    
    def build(self):
        super().build()
        Window.maximize()
        self.box = MDBoxLayout(md_bg_color=rgba("#3333CC"))
        self.box.padding = "20dp","10dp","20dp","0dp"
        self.subbox= MDBoxLayout(
                                md_bg_color=rgba("#FFFFFF"),
                                orientation="horizontal",
                                pos_hint={'center_x':0.5,'bottom':1}
                                 )
        self.sidebar = SideBar()
        self.subbox.add_widget(self.sidebar)
        self.centerbar = CenterBar()
        self.subbox.add_widget(self.centerbar)
        self.box.add_widget(self.subbox)
        

        return self.box
    
    def Export_ADUsers_clicked(self):
        self.centerbar.ids.sm.current = _export_adusers
        
    def ADUsers_clicked(self):
        self.centerbar.ids.sm.current = _adusers


if __name__ =="__main__":
    app = ITX_AD()
    app.run()
    