# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/FreeServer/outils/MyDynaTextScreen.py
Version_1 = '7.0.3'
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap
from Components.Input import Input
from Screens.InputBox import InputBox
from Tools.Directories import fileExists
from Screens.Screen import Screen
import re
from Plugins.Plugin import PluginDescriptor
from Tools.Directories import fileExists
from Screens.Screen import Screen
from Screens.Standby import *
from Tools.Directories import *
from Components.Sources.List import List
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Label import Label
from Components.Button import Button
from Components.Sources.StaticText import StaticText
from Components.ScrollLabel import ScrollLabel
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from Components.config import config, ConfigSelection, getConfigListEntry, ConfigSubsection, configfile
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, getDesktop, loadPNG, eConsoleAppContainer
from enigma import *
from enigma import eTimer
from datetime import date, datetime
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Screens.Standby import TryQuitMainloop
from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console
from Components.MenuList import MenuList
from Components.ActionMap import ActionMap
from Components.ActionMap import NumberActionMap, ActionMap
from Plugins.Plugin import PluginDescriptor 
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
from Plugins.Extensions.FreeServer.outils.Showinfo import *
import os
from struct import pack
from enigma import *
from Screens.MessageBox import MessageBox
from Screens.InputBox import InputBox
from Screens.ChoiceBox import ChoiceBox
from Components.ActionMap import ActionMap, NumberActionMap
from Components.ScrollLabel import ScrollLabel
from Components.Label import Label, MultiColorLabel
from Components.GUIComponent import *
from Components.MenuList import MenuList
from Components.Input import Input
from Components.ConfigList import ConfigList
from Screens.Console import Console
from Plugins.Plugin import PluginDescriptor
from Screens.ServiceInfo import *
from Plugins.Plugin import PluginDescriptor
from Tools import Notifications
from Components.config import *

session = None

from time import *
import time
import datetime
###########################################################################
from Tools.Directories import fileExists
def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

class MyDynaTextScreen2(Screen):
	skin = """
		<screen position="70,40" size="100,60" title="Radio " >
			<widget name="myText" position="10,10" size="400,100" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;22"/>
                        <widget name="myRedBtn" position="10,110" size="100,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
			<widget name="myGreenBtn" position="120,110" size="100,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
			<widget name="myYellowBtn" position="230,110" size="100,40" backgroundColor="yellow" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
			<widget name="myBlueBtn" position="340,110" size="100,40" backgroundColor="blue" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>			
		</screen>
                """

	def __init__(self, session, args = 0):
		self.session = session
		Screen.__init__(self, session)
		self.text=""                           
		self["myText"] = Label()
		self["go"] = Label()	
		self["goto"] = Label()		
		self["prombt"] = Label()	      
		self["myRedBtn"] = Label(_("Cancel"))
		self["myGreenBtn"] = Label(_("OSCAM"))
		self["myYellowBtn"] = Label(_("NCAM"))
		self["myBlueBtn"] = Label(_("info"))                		
                self['actions'] = ActionMap(["SetupActions", "ColorActions"], 
		{
                        "0": self.key0,                                      
                        "green": self.go,                       
			"yellow": self.goto,
			"blue": self.gotoa,                          			
			"red": self.close,
                        #"ok": self.restartenigma,
                        "cancel": self.close,
		}, -1)
		self.onShown.append(self.setMyText)
		self.Tilawa
                self.go               
		self.goto
		self.prombt
		#self.onShown.append(self.setMyText)
        	self.onChangedEntry = []
		#self['actions'] = ActionMap(['SetupActions'], {'ok': self.go,
		self.timer_list = []
		self.processed_timers = [] 
		self.timer = eTimer()
		self.initialservice = session.nav.getCurrentlyPlayingServiceReference()
		self.updateTimer = eTimer()
		self.timer.callback.append(self.disappear)
		self.timer.start(2000, True)
### EDit By RAED To DreamOS OE2.5/2.6
                if fileExists('/var/lib/dpkg/status'):
                     self.wget = "/usr/bin/wget2 --no-check-certificate"
                else:   
	             self.wget = "/usr/bin/wget"
### End
                import sys,os  
                os.system("sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/picturecimages.sh'") 

	def Tilawa(self):

            from enigma import eServiceReference
            from Plugins.Extensions.FreeServer.outils.InfoBar import ALAJREStream5
            #url = "https://ia600704.us.archive.org/31/items/PremierLeague_201812/0010.mp3"
            #url = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Audio/009.mp3'
            url = 'http://178.33.178.204:9322/index.htm'
            #url = 'https://ia601507.us.archive.org/22/items/PremierLeague_201812/Premier_League.mp3'
            ref = eServiceReference(4097, 0, url)
            ref.setName(Version_1)
            self.session.openWithCallback(self.backToIntialService, ALAJREStream5, ref)

       
	def backToIntialService(self, ret = None):
            self.session.nav.stopService()
            self.session.nav.playService(self.initialservice)
            self.fast()

	def fast(self):   
            self.timer.stop()
            #self.session.openWithCallback(self.close, ALAJREStream6, ref)
            #self.session.close(ALAJREStream5)
             
	def disappear(self):
            self.Tilawa()
            
	#def info(self):
            #self.session.open(Showinfo)           
            
        def Update(self):
            Update = "afile"
            afile = open('/tmp/monfichier.txt', 'w')
            #afile.write(Update)
            #self.session.open(MessageBox,_("Enigma2 update" + str(Update) + "Message test"), MessageBox.TYPE_INFO, timeout=20)
            self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + str(Update) + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)            
            
	def setMyText(self):
            self["myText"].setText(self.text)
                 
	def go(self):
	        from Plugins.Extensions.FreeServer.outils.MyShPrombt import MyShPrombt
                com = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/OSCamEmus_all.ipk.sh'                
		self.session.open(Console,_("Executing: %s") % (com),["%s" % com])	                
	        self.prombt("/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/OSCamEmus_all.ipk.sh")            
                                                
	def goto(self):
	        from Plugins.Extensions.FreeServer.outils.MyShPrombt import MyShPrombt
                com = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/NCamEmus_all.ipk.sh'
        	self.session.open(Console,_("Executing: %s") % (com),["%s" % com])
                self.prombt("/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/NCamEmus_all.ipk.sh") 
                            
	def gotoa(self):
                from Plugins.Extensions.FreeServer.outils.MyShPrombt import MyShPrombt
                com = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/FreeServerinfo.sh'
                self.session.open(Console,_("Executing: %s") % (com),["%s" % com])
                self.prombt("/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/FreeServerinfo.sh") 

	def prombt(self, com):
	        scripts = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/"
                os.chmod(scripts, 755)
		self.session.open(Console,_("Executing: %s") % (com), ["%s" % com])
                                		
        def key0(self):
            self.session.openWithCallback(self.restartenigma, MessageBox, _('Restart Enigma2 To Load New Update?'), MessageBox.TYPE_YESNO, timeout=20)            
        
        def restartenigma(self, result):
            if result:
                self.session.open(TryQuitMainloop, 3)

		
	def cancel(self):
		print "\n[MyShPrombt] cancel\n"
		self.close(None)
                	
def main(session, **kwargs):
	session.open(MyDynaTextScreen)

