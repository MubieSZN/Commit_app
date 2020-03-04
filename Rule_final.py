from kivy.app import  App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
import os
import sys
import webbrowser
from kivy.effects.scroll import ScrollEffect
from kivy.uix.scrollview import ScrollView
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty,NumericProperty,ListProperty
from kivy.uix.modalview import ModalView
from kivy.utils import get_hex_from_color
from kivy import platform
from kivymd.uix.menu import MDDropdownMenu
#from kivymd.uix.fanscreenmanager import MDFanScreen
#from kivymd.uix.popupscreen import MDPopupScreen
from kivymd.uix.list import IRightBodyTouch, OneLineIconListItem
#from kivymd.uix.selectioncontrol import MDCheckbox
#from kivymd.uix.card import MDCard
#from kivymd.utils.cropimage import crop_image
from kivymd.utils import asynckivy
from kivymd.theming import ThemeManager
from kivymd.icon_definitions import md_icons
from kivymd.uix.card import MDCardPost
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.button import MDIconButton
from random import sample
from string import ascii_lowercase
from kivy.clock import Clock
import json
from os.path import join,exists
import time
from kivy.uix.widget import Widget
from kivymd.uix.snackbar import Snackbar
from kivy.storage.jsonstore import JsonStore
from kivymd.toast.kivytoast import toast
from kivymd.app import MDApp
kv='''
#:import Window  kivy.core.window.Window       
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:include FirebaseLoginScreen/firebaseloginscreen.kv
#:import FirebaseLoginScreen FirebaseLoginScreen.firebaseloginscreen.FirebaseLoginScreen
#:import MDBottomAppBar kivymd.uix.toolbar.MDBottomAppBar
#:import utils kivy.utils

<Salat_Widget@AnchorLayout+MDLabel>
    
    anchor_y:"bottom"
    anchor_x:"right"
    font_size:40
    halign:"center"
    font_style:"H2"
    theme_text_color: 'Primary'
   
        
   
    

<SelectableLabel>:
# Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (0,0,0,.25) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size

    text_size:root.width, None
    #size:self.texture_size

    halign:"center"


                        
<ContentNavigationDrawer@MDNavigationDrawer>        
    drawer_logo: 'rule.jpg'
    NavigationDrawerSubheader:
        text: "Tools"
        
    NavigationDrawerIconButton:
        text: app.user_name
        id:username
        icon: 'account-box-outline'
        on_release:
            app.change_username()
            
    NavigationDrawerIconButton:
        text: "Salat"
        icon: 'human-handsdown'
        on_release:
            app.screen_transition("left")    
            app.goto_screen("Salat")  
      
    NavigationDrawerIconButton:
        text: "Tasbih"
        icon: 'counter'
        on_release:
            app.screen_transition("left")    
            app.goto_screen("Tasbih")  
            
    
    NavigationDrawerDivider:  
              
    NavigationDrawerSubheader:
        text: "Preferences"
        
    NavigationDrawerIconButton:
        text: "Settings"
        icon: 'settings'
        on_release:
            app.goto_screen("Settings")
            app.screen_transition("left")
            
    NavigationDrawerIconButton:
        text: "About"
        icon: 'information'
        on_release:
            app.screen_transition("left")
            app.goto_screen("About")

Root_Widget:
    NavigationLayout:
        id: nav_layout
        
        
        ContentNavigationDrawer:
            id: nav_drawer
            
                
        FloatLayout:
            id: float_box
            BoxLayout:
                id: box_for_manager
                orientation: 'vertical'
                MDToolbar:
                    id: toolbar
                    title: app.app_title
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'Primary'
                    background_hue: '200'
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_layout.toggle_nav_drawer()]]
                    right_action_items:
                        [['account-circle', lambda x: app.login()]]
                ScreenManager:
                    id: scr_mngr
                    Screen:
                        name: 'Home'                       
                        BoxLayout:
                            orientation:"vertical"                           
                            RecycleView:
                                id: rv
                                data : [{'text': "Tap the + button to add "}]
                                scroll_type: ['bars', 'content']
                                scroll_wheel_distance: dp(200)
                                bar_width: dp(5)
                                viewclass: 'SelectableLabel'
                                SelectableRecycleBoxLayout:                          
                                    multiselect:False
                                    touch_multiselect: True                          
                                    cols:2
                                    #tweak this make it random 
                                    default_size: None, dp(200)
                                    default_size_hint: 1, None
                                    size_hint_y: None
                                    height: self.minimum_height
                                    orientation: 'vertical'
                                    spacing: dp(3)   
                                                         
                        FloatLayout:
                            size_hint_y:.2
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .15, 'center_y': .5}
                                icon:"delete"
                                on_release:
                                    app.delete()
                                    app.save()
                 
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .85, 'center_y': .5}
                                icon:"plus"
                                on_release:
                                    app.goto_screen("Edit")                                                  
                                    app.screen_transition("up")
                    Screen:
                        name:"Salat"
                        ScrollView:                        
                            do_scroll_x: False
                            BoxLayout:
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height
                                padding: dp(20)
                                spacing: dp(100)
                                NavigationDrawerDivider:
                                    
                                MDLabel:
                                    id:tasbih_label
                                    pos_hint: {'center_x': .5, 'center_y':.7 }
                                    font_size:dp(70)
                                    halign:"center"
                                    text:"Day :"+ app.today
                                    font_style:"H2"
                                    theme_text_color: 'Primary'   
                                Salat_Widget:
                                    
                                    text:"Nafila"
                                    
                                    MDIconButton:
                                        id:nafila
                                        icon:"close"
                                        on_release:
                                            self.icon="check"
                                            app.salat_save()
                                   
                                Salat_Widget:
                                    
                                   
                                    text:"Fajr"
                                    MDIconButton:
                                        id:fajr
                                        icon:"close"
                                        on_release:
                                            self.icon="check"
                                            app.salat_save()
                                Salat_Widget:
                                    
                                    
                                    text:"Subh"
                                    
                                    MDIconButton:
                                        
                                        id:subh
                                        icon:"close"
                                        on_release:
                                            self.icon="check"
                                            app.salat_save()
                                Salat_Widget:
                                    
                                    text:"Zuhr"
                                    MDIconButton:
                                        id:zuhr
                                        icon:"close"
                                        on_release:
                                            self.icon="check"
                                            app.salat_save()
                                Salat_Widget:
                                 
                                    text:"Asr"
                                    
                                    MDIconButton:
                                        id:asr
                                        icon:"close"
                                        on_release:
                                            self.icon="check"
                                            app.salat_save()
                                Salat_Widget:
                                 
                                    text:"Magrib"
                                    MDIconButton:
                                        id:magrib
                                        icon:"close"
                                        on_release:
                                            self.icon="check"
                                            app.salat_save()
                                Salat_Widget:
                                   
                                    text:"Isha"
                                    MDIconButton:
                                        id:isha
                                        icon:"close"
                                        on_release:
                                            self.icon="check"
                                            app.salat_save()
                                NavigationDrawerDivider:
                                    
                                
                        FloatLayout:
                            size_hint_y:.2      
                            
                                                                
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .5, 'center_y': .65}
                                icon:"close"
                                on_release:                              
                                    app.go_home()                                  
                                    app.screen_transition("down")                    
                            
                            
                                           
                        
                    Screen:
                        name:"Tasbih"                      
                        FloatLayout:
                      
                            
                            MDLabel:
                                id:tasbih_label
                                pos_hint: {'center_x': .5, 'center_y':.7 }
                                font_size:dp(70)
                                halign:"center"
                                text:"0"
                                font_style:"H2"
                                theme_text_color: 'Primary'                            
                            MDLabel:                           
                                pos_hint: {'center_x': .5, 'center_y':.4}
                                font_size:dp(1)
                                halign:"center"
                                text:"Tap +1 to count"
                                font_style:"Caption"
                                theme_text_color: 'Hint'
                                
                        FloatLayout:
                            size_hint_y:.2                        
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .23, 'center_y': .75}
                                icon:"close"
                                on_release:                              
                                    app.go_home()                                  
                                    app.screen_transition("down")                    
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .78, 'center_y': .75}
                                icon:"refresh"
                                on_release:
                                    app.reset_tasbih()                                                           
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .5, 'center_y': 1.5}
                                icon:"plus-one"
                                on_release:
                                    app.add_tasbih()
                                                                                               
                    Screen:
                        name:"Login"
                        BoxLayout:                            
                            orientation:"vertical"
                            size_hint_y:1
                            FirebaseLoginScreen:
                                pos_hint: {'center_x': .5, 'center_y': .3}                                
                                id: firebase_login_screen
                                name: "firebase_login_screen"
                                web_api_key: "your_web_api_key_from_firebase"
                                primary_color: app.theme_cls.primary_color 
                                secondary_color: utils.get_color_from_hex("#060809")
                                tertiary_color: (.25, .25, .25, 1)
                                
                                
                                on_login_success:
                                    app.toast("Login successful")
                                    # Defining this function lets you program what to do when the
                                    # user has logged in (probably you'll want to change screens)!
                                    # Get the important user info
                                    #app.user_localId = self.localId
                                    #app.user_idToken = self.idToken
                        FloatLayout:                            
                            size_hint_y:.2
                            MDFloatingActionButton:                               
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                icon:"close"
                                on_release:                                    
                                    app.go_home()
                                    app.screen_transition("right")             
                           
                    Screen:
                        name: 'Edit'
                        BoxLayout:
                            padding:120                            
                            MDTextField:
                                pos_hint: {'center_x': .5, 'center_y': .87}
                                id:rule_textfield
                                hint_text: "Tap to add new"
                                helper_text: "Eg:Five daily salat, Code ,Pushups"
                                helper_text_mode: "on_focus"
                                color_mode: 'accent'
                                multiline:True
                            MDIconButton:
                                icon:"close"
                                pos_hint: {'center_x': .15, 'center_y': .95}    
                                on_press:rule_textfield.text=""
    
                        FloatLayout:
                            size_hint_y:.2
                            
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .2, 'center_y': 2}
                                icon:"close"
                                on_release:                              
                                    app.go_home()
                                    
                                    app.screen_transition("down")
                                    
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .8, 'center_y': 2}
                                icon:"check"
                                on_release:
                                    
                                    app.go_home()
                                    app.screen_transition("down")
                                    app.root.insert(rule_textfield.text)
                                    rule_textfield.text=""
                                    app.save()
                                          
                    Screen:
                        name:"Settings"
                        BoxLayout:
                            orientation:"vertical"
                            StackLayout:
                                size_hint_y:.8
                                                     
                                TwoLineIconListItem:
                                    text: "Theme"
                                    on_press:
                                        app.theme_picker_open()
                                    secondary_text:
                                        "[color=%s]Change theme[/color]" \
                                        % get_hex_from_color(app.theme_cls.primary_color)
                                    IconLeftWidget:
                                        icon: 'palette'
                                                                                                         
                                TwoLineIconListItem:
                                    text: "Reset app"
                                    on_press:
                                        app.reset_dialog()
                                    secondary_text:
                                        "[color=%s]Reset all app settings[/color]" \
                                        % get_hex_from_color(app.theme_cls.primary_color)
                                    IconLeftWidget:
                                        icon: 'backup-restore'
                            FloatLayout:
                                size_hint_y:.2
                                MDFloatingActionButton:
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    icon:"close"
                                    on_release:
                                        app.go_home()                                        
                                        app.screen_transition("down")
                                        app.theme_saver()
                                         
                    Screen:
                        name:"About"
                        StackLayout:
                            BoxLayout:
                                orientation:"vertical"
                                size_hint_y:.4                            
                                MDLabel:
                                    text:"Rule "
                                    font_size:150
                                    #size_hint_y: None
                                    #height: self.texture_size[1]
                                    font_style: 'H1'
                                    theme_text_color: 'Primary'
                                    markup: True
                                    halign: 'center'
                                    #text_size: self.width - 20, None
                                MDLabel:
                                    text:"1.0.0"
                                    #size_hint_y: None
                                    #height: self.texture_size[1]
                                    font_style: 'H5'
                                    theme_text_color: 'Primary'
                                    markup: True
                                    halign: 'center'
                                    #text_size: self.width - 20, None
                            BoxLayout:
                                orientation:"vertical"
                                size_hint_y:.4                               
                                TwoLineIconListItem:
                                    text: "Contact us"
                                    on_press:
                                        app.open_address("https://gmail.com/Mubarklawal52@gmail.com")
                                    secondary_text:
                                        "[color=%s]Swoopiness@gmail.com[/color]" \
                                        % get_hex_from_color(app.theme_cls.primary_color)
                                    IconLeftWidget:
                                        icon: 'gmail'
                                           
                                TwoLineIconListItem:
                                    text: "Twitter"
                                    on_press:
                                        app.open_address( "https://twitter.com/@Tall_Mubie" )
                                    secondary_text:
                                        "[color=%s]@Tall_Mubie" \
                                        % get_hex_from_color(app.theme_cls.primary_color)
                                    IconLeftWidget:
                                        icon: 'twitter'
                                
                                TwoLineIconListItem:
                                    text: "Connect with us on Quora"
                                    on_press:
                                        app.open_address("https://quora.com/Mubaraklawal_1"  )
                                    secondary_text:
                                        "[color=%s]Mubarak Lawal[/color]" \
                                        % get_hex_from_color(app.theme_cls.primary_color)
                                    IconLeftWidget:
                                        icon: 'quora'
                        FloatLayout:
                            size_hint_y:.2
                            MDFloatingActionButton:
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                icon:"close"
                                on_release:
                                    app.go_home()
                                    app.screen_transition("down")         
'''

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
RecycleGridLayout):
    pass

class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass   

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        
        return super(SelectableLabel, self).refresh_view_attrs(
rv, index, data)
    def on_touch_down(self, touch):       
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return False        
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch) 
                   
    def get_index(self,index):
        global rule_index
        rule_index=index
        
        
          
    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        
        self.selected = is_selected
        index_num=index
        if is_selected :
            
          
            self.get_index(index)
            
            
class Root_Widget(BoxLayout):
    
     
     
    def __init__(self,**kwargs):
       super(Root_Widget,self).__init__(**kwargs)
      
       Clock.schedule_once(self.loader)
       
        
     
    def new(self):
       self.ids.scr_mngr.current="Edit"
        
       
    def loader(self,*args):
       os.chdir(RuleApp.path)
       if not exists("rule.json" ):
           
           fd=open("rule.json","wb+")
           fd.close()    
       with open("rule.json","r") as fd:
           try:
           
               data=json.load(fd)
                 
           except:
               print("rules not loaded")
       #the habit list is populated here   
       try:
           self.ids.rv.data=data["rules"]
      
       except:
           print("rv data not loaded ")
            
    
         
    
    def insert(self, value):
       txt=self.ids.rule_textfield.text        
       self.ids.rv.data.insert(0, {"text"  :txt})
       RuleApp().toast(str(txt)+" Added")
 

    
class RuleApp(MDApp):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_theme_picker = None
        
    today=str((time.localtime().tm_yday))
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "Teal"
    theme_cls.accent_palette = "DeepOrange"
    theme_cls.theme_style="Dark"
    main_widget=None
    ok_cancel_dialog=None
    user_dialog=None
    path="/storage/emulated/0/commit_app_final/Rule"
    app_title="Commit"
    my_snackbar=None
    user_name=StringProperty("User")
    
    
    def save(self):
       data={}

       data['rules']=self.root.ids.rv.data
       with open("rule.json", 'w+') as fd:
           json.dump(data, fd)
          
       print("saved rule")
             
    def undo(self):
        self.root.ids.rv.data.insert(rule_index, undo_text)
        self.save()
        self.toast("Item restored")
       
    def undo_snackbar(self,snack_type):       
        Snackbar(text="Item removed! ", button_text="UNDO", button_callback=lambda *x: self.undo()).show()
         
    
    def delete(self):
        try:
            
            touched_item=self.root.ids.rv.data[rule_index]
            global undo_text
            undo_text=touched_item
            self.root.ids.rv.data.remove(touched_item)
            #id=None
            self.undo_snackbar("button")
        
        except:
            print("rv.data is empty")
     
        
    
    def add_tasbih(self):
        value=int(self.root.ids.tasbih_label.text)
        self.root.ids.tasbih_label.text=str(value+1)
        
    def reset_tasbih(self):
        self.root.ids.tasbih_label.text="0"
                
    def toast(self,text):
        
        toast(text)
           
 
    
    def login(self):        
        self.root.ids.toolbar.title="Log in"
        self.root.ids.scr_mngr.current="Login"
        self.root.ids.scr_mngr.transition.direction="left"   
    
    def account_callback(self,text_of_selection,popup_widget):
        name=popup_widget.text_field.text
        print(name)      
    
    input_dialog=None
    def change_username(self):      
        if not self.input_dialog:
            from kivymd.uix.dialog import MDInputDialog
            self.input_dialog = MDInputDialog(
                title="Change Username",
                hint_text="Enter new user name",
                size_hint=(0.8, 0.3),
                text_button_ok="Save",
                text_button_cancel="Cancel",
                events_callback=self.username_callback,
            )
        self.input_dialog.open()
        
    def username_callback(self,text_of_selection,popup_widget):       
        if text_of_selection=="Save":            
            self.user_name=popup_widget.text_field.text
            new_name=popup_widget.text_field.text
            self.config.set("theme","username",new_name)
            self.config.write()
            
    def callback_for_reset(self,text_of_selection,popup_widget):
        if text_of_selection=="Yes": 
            self.reset_app()
        else:
            print("cant call reset function")           
     
    def reset_dialog(self):
        if not self.ok_cancel_dialog:
            from kivymd.uix.dialog import MDDialog
            self.ok_cancel_dialog = MDDialog(
                title="Reset",
                size_hint=(0.8, 0.3),
                text_button_ok="Yes",
                text="Do you want to reset all app settings",
                text_button_cancel="No",
                events_callback=self.callback_for_reset,
            )
        self.ok_cancel_dialog.open()
        
    def theme_saver(self):
        self.config.set("theme","primary_palette",self.theme_cls.primary_palette)
        self.config.set("theme","accent_palette",self.theme_cls.accent_palette)
        self.config.set("theme","theme_style",self.theme_cls.theme_style)
        self.config.write()
        
    def new_day(self):
        try:
            store = JsonStore(self.path+'salat_state.json')
            today= store.get('Today')['Day']
            print(today)
            self.today
            if today==self.today:
                print("same day")
                self.load_salat()
            else:
                print("new day")
        except:
            print("cant print today")
        
    def salat_save(self):
       
        try:
            store = JsonStore(self.path+'salat_state.json')
            store.put('Nafila', state=self.root.ids.nafila.icon)
            store.put('Fajr', state=self.root.ids.fajr.icon)
            store.put('Subh', state=self.root.ids.subh.icon)
            store.put('Zuhr', state=self.root.ids.zuhr.icon)
            store.put('Asr', state=self.root.ids.asr.icon)
            store.put('Magrib', state=self.root.ids.magrib.icon)
            store.put('Isha', state=self.root.ids.isha.icon)
            store.put('Today', Day=self.today)
        except:
            
            print("cant store salat parameters")
        
        toast("Salat completed")
    def load_salat(self):
        try:
            store = JsonStore(self.path+'salat_state.json')
            nafila_state= store.get('Nafila')['state']
            self.root.ids.nafila.icon=nafila_state
            fajr_state= store.get('Fajr')['state']
            self.root.ids.fajr.icon=fajr_state
            subh_state= store.get('Subh')['state']
            self.root.ids.subh.icon=subh_state
            zuhr_state= store.get('Zuhr')['state']
            self.root.ids.zuhr.icon=zuhr_state
            asr_state= store.get('Asr')['state']
            self.root.ids.asr.icon=asr_state
            magrib_state= store.get('Magrib')['state']
            self.root.ids.magrib.icon=magrib_state
            isha_state= store.get('Isha')['state']
            self.root.ids.isha.icon=isha_state
        except:
            print("cant load salat parameters")
        
    
    
        
    
           
             
    def on_start(self):
        try:           
            self.theme_cls.primary_palette=self.config.get("theme","primary_palette")
            self.user_name=self.config.get("theme","username")
            self.theme_cls.accent_palette=self.config.get("theme","accent_palette")
            self.theme_cls.theme_style =self.config.get("theme","theme_style")
            #self.theme_cls.theme_style =self.config.get("theme","theme_style")
            self.new_day()
        except:
            print(" cant load on_start parameters")
            
    def build(self):
        self.main_widget=Builder.load_string(kv)
        return self.main_widget
        
    def build_config(self,config):
        config.setdefaults("theme",{"primary_palette":"Indigo",
        "accent_palette":"Purple",
        "theme_style":"Dark",
        "username":str.capitalize(self.user_name)})
     
    def theme_picker_open(self):
        if not self.md_theme_picker:
            from kivymd.uix.picker import MDThemePicker

            self.md_theme_picker = MDThemePicker()
        self.md_theme_picker.open() 
    def goto_screen(self,ScreenName):
        self.root.ids.toolbar.title=ScreenName
        self.root.ids.scr_mngr.current=ScreenName
        
    def screen_transition(self,direction):
        self.root.ids.scr_mngr.transition.direction=direction     
   
    def go_home(self):
        self.root.ids.toolbar.title=self.app_title
        self.root.ids.scr_mngr.current="Home"
        
    def open_address(self,address):
        webbrowser.open(address)
          
    def reset_app(self):               
        try:
            
            os.chdir(self.path)
            os.remove("rule.json")
            os.remove("/storage/sdcard0/.rule.ini")
            os.remove("salat_state.json")
            self.toast("Restart app for changes to take effect")            
            Clock.schedule_once(self.stop,3)
            print("app resetted")
        except:
            print("cant reset app")
    
if __name__=="__main__":
    RuleApp().run()
        
        
        
        