from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDRoundFlatButton,MDFlatButton
from kivy.utils import rgba
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivymd.uix.list import ILeftBodyTouch,TwoLineIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.properties import StringProperty



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

class SearchBar(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class ListItemWithCheckbox(TwoLineIconListItem):
    pass

class LeftCheckBox(ILeftBodyTouch,MDCheckbox):
    pass

# ListItemWithCheckbox:
#     text:"[size=14]Text[/size]"
#     secondary_text: "[size=14]Secondary text here[/size]"
# ListItemWithCheckbox:
#     text: "[size=14]Two-line item[/size]"
#     secondary_text: "[size=14]Secondary text here[/size]"
# ListItemWithCheckbox:
#     text: "[size=14]Two-line item[/size]"
#     secondary_text: "[size=14]Secondary text here[/size]"


class FilterDialog(MDDialog):
    def add_items(self,_list):
        for item in _list:
            temp=ListItemWithCheckbox(text=item.get("name"),secondary_text="DN: "+item.get("dn"))
            self.content_cls.ids.list_container.add_widget(temp)
        

    def ok_click(self):
        print("okay clicked")

class FilterItem(MDBoxLayout):
    hint_text = StringProperty()

class HomeScreen(MDScreen):
    # item = ListItemWithCheckbox()
    ou_dialog=None
    group_dialog=None
    users_dialog = None

    def OU_click(self):
        if not self.ou_dialog:
            self.ou_dialog = FilterDialog(
                                        title="Filter OU",
                                        size_hint=(0.5,None),
                                        content_cls=FilterItem(hint_text = "Search OU")
                                        ,type="custom",
                                        buttons=[
                                                MDFlatButton(
                                                    text="OK",
                                                    theme_text_color="Custom",
                                                    text_color=rgba("#3333CC"),
                                                    on_release=lambda x: self.ok_click(1)
                                                ),
                                            ],
                                        )
            temp_list = [{"name":"HR","dn":"CN=HR,DC=ITX,DC=com"},{"name":"Admin","dn":"CN=Admin,DC=ITX,DC=com"},{"name":"Finance","dn":"CN=Finance,DC=ITX,DC=com"},
                         {"name":"Security","dn":"CN=Security,DC=ITX,DC=com"},{"name":"IT","dn":"CN=IT,DC=ITX,DC=com"},{"name":"Management","dn":"CN=Management,DC=ITX,DC=com"}]
            self.ou_dialog.add_items(temp_list)
        self.ou_dialog.open()

    def group_click(self):
        if not self.group_dialog:
            self.group_dialog = FilterDialog(
                size_hint=(0.5,None),
                content_cls=FilterItem(hint_text = "Search group"),
                type="custom",
                title="Filter Group",
                buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=rgba("#3333CC"),
                            on_release=lambda x: self.ok_click(2)
                        ),
                    ],
                )
            temp_list = [{"name":"G1","dn":"CN=G1,DC=ITX,DC=com"},{"name":"G2","dn":"CN=G2,DC=ITX,DC=com"},{"name":"G3","dn":"CN=G3,DC=ITX,DC=com"}]
            self.group_dialog.add_items(temp_list)
            
        self.group_dialog.open()

    def users_click(self):
        pass

    def ok_click(self,flag):
        if flag==1:
            self.ou_dialog.ok_click()
        elif flag==2:
            self.group_dialog.ok_click()
        elif flag==3:
            self.users_dialog.ok_click()

class UsersScreen(MDScreen):
    pass


class ITX_AD(MDApp):
    
    def build(self):
        super().build()
        Window.set_icon('images/icon.png')
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
    