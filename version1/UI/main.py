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
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty



from kivy.lang import Builder
Builder.load_file('main.kv')

# constants
_name = "name"
_dn = "dn"


# screen names
_export_adusers = "export_adusers"
_adusers = "adusers"

class CheckedItem(MDBoxLayout):
    name = StringProperty()
    dn = StringProperty()

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

class ListItemWithCheckbox(TwoLineIconListItem):
    pass

class LeftCheckBox(ILeftBodyTouch,MDCheckbox):
    def on_check(self):
        flag =self.active
        name_=self.parent.parent.text
        dn_=self.parent.parent.secondary_text
        if flag:
            self.parent.parent.parent.parent.parent.add_checked_item(name_,dn_)
        else:
            self.parent.parent.parent.parent.parent.remove_checked_item(dn_)





class FilterDialog(MDDialog):
    def open(self):
        self.content_cls.remove_items()
        self.content_cls.add_items()
        super().open()        

    def ok_click(self):
        print("okay clicked")

    def get_checked_item(self):
        return self.content_cls.checked_data

    

class FilterItem(MDBoxLayout):
    text = StringProperty()
    hint_text = StringProperty()
    checked_data=None # this list contains checked data only
    data = None

    def add_checked_item(self,name_,dn_):
        temp_dict = {}
        temp_dict[_name]=name_
        temp_dict[_dn]=dn_
        self.checked_data.append(temp_dict)

    def remove_checked_item(self,dn):
        for item in self.checked_data:
            if item.get(_dn)==dn:
                self.checked_data.remove(item)
                # print(self.checked_data)
                return
                
    def remove_items(self):
        self.ids.list_container.clear_widgets()

    def add_items(self,_list=None):
        temp_list =self.data

        if _list:
            temp_list = _list

        for item in temp_list:
            temp=ListItemWithCheckbox(text=item.get("name"),secondary_text=item.get("dn"))
            self.ids.list_container.add_widget(temp)
    
    def search_item(self,search_word:str=None):
        temp_list =[]
        if search_word:
            temp_list.append(item for item in self.data if item.get("name").upper().startswith(search_word.upper()))
            return temp_list[0] ## it gives the generator object
        return temp_list
    
    def on_text_changed(self):
        text =self.ids.search_bar.text
        self.remove_items()
        gen_obj =self.search_item(text)
        self.add_items(gen_obj)



class HomeScreen(MDScreen):
    # item = ListItemWithCheckbox()
    ou_dialog=None
    group_dialog=None
    users_dialog = None

    def OU_click(self):
        temp_list = [{"name":"HR","dn":"CN=HR,DC=ITX,DC=com"},{"name":"Admin","dn":"CN=Admin,DC=ITX,DC=com"},{"name":"Finance","dn":"CN=Finance,DC=ITX,DC=com"},
                         {"name":"Security","dn":"CN=Security,DC=ITX,DC=com"},{"name":"IT","dn":"CN=IT,DC=ITX,DC=com"},{"name":"Management","dn":"CN=Management,DC=ITX,DC=com"},
                         {"name":"Staff","dn":"CN=Staff,DC=ITX,DC=com"},{"name":"Technical","dn":"CN=Technical,DC=ITX,DC=com"}]
        if not self.ou_dialog:

            filter_item = FilterItem(hint_text = "Search OU")
            self.ou_dialog = FilterDialog(
                                        title="Filter OU",
                                        size_hint=(0.5,None),
                                        content_cls=filter_item,
                                        type="custom",
                                        buttons=[
                                                MDFlatButton(
                                                    text="OK",
                                                    theme_text_color="Custom",
                                                    text_color=rgba("#3333CC"),
                                                    on_release=lambda x: self.ok_click(1)
                                                ),
                                            ],
                                        )
            self.ou_dialog.content_cls.data=temp_list
            self.ou_dialog.content_cls.checked_data=list()  
        self.ou_dialog.open()

    def group_click(self):
        temp_list = [{"name":"G1","dn":"CN=G1,DC=ITX,DC=com"},{"name":"G2","dn":"CN=G2,DC=ITX,DC=com"},{"name":"G3","dn":"CN=G3,DC=ITX,DC=com"}]
        filter_item = FilterItem(hint_text = "Search group")
        if not self.group_dialog:
            self.group_dialog = FilterDialog(
                size_hint=(0.5,None),
                content_cls=filter_item,
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
            self.group_dialog.content_cls.data=temp_list 
            self.group_dialog.content_cls.checked_data=list() 
        self.group_dialog.open()
        

    def users_click(self):
        pass

    def ok_click(self,flag):
        if flag==1:### ok click of ou dialog
            self.add_checked_OU()
            print(self.ou_dialog.content_cls.checked_data)
            self.ou_dialog.dismiss()
        elif flag==2: ### ok click of group dialog
            self.add_checked_group()
            print(self.group_dialog.content_cls.checked_data)
            self.group_dialog.dismiss()
        elif flag==3:### ok click of user dialog
            self.users_dialog.ok_click()

    def add_checked_OU(self):
        self.ids.ou_checked_item_box.clear_widgets()
        list_ = self.ou_dialog.get_checked_item()
        if list_:
            self.ids.ou_checked_item_box.add_widget(
                MDLabel(
                            text="OU",
                            size_hint=(None,None),
                            adaptive_size=True,
                            font_style ="H6",
                            bold = True)
            )
        for item in list_:
            self.ids.ou_checked_item_box.add_widget(CheckedItem(name=item.get(_name),dn=item.get(_dn)))

    def add_checked_group(self):
        self.ids.group_checked_item_box.clear_widgets()
        list_=self.group_dialog.get_checked_item()
        if list_:
            self.ids.group_checked_item_box.add_widget(
                MDLabel(
                        text="Group",
                        size_hint=(None,None),
                        adaptive_size=True,
                        font_style ="H6",
                        bold = True)
            )
        for item in list_:
            self.ids.group_checked_item_box.add_widget(CheckedItem(name=item.get(_name),dn=item.get(_dn)))

   
        
        
    
            
                


    def add_heading(self,heading):
        self.ids.scroll_checked_item.add_widget(
            MDLabel(
                text=heading,
                size_hint=(None,None),
                adaptive_size=True,
                font_style ="H6",
                bold = True
            )
        )
        
        

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
    



# ListItemWithCheckbox:
#     text:"[size=14]Text[/size]"
#     secondary_text: "[size=14]Secondary text here[/size]"
# ListItemWithCheckbox:
#     text: "[size=14]Two-line item[/size]"
#     secondary_text: "[size=14]Secondary text here[/size]"
# ListItemWithCheckbox:
#     text: "[size=14]Two-line item[/size]"
#     secondary_text: "[size=14]Secondary text here[/size]"