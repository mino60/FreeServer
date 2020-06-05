# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ScrollLabel import ScrollLabel
from datetime import date, datetime
from Components.Label import Label, MultiColorLabel
from Screens.Standby import TryQuitMainloop
from Screens.Console import Console
from Components.MenuList import MenuList
from Components.ActionMap import NumberActionMap, ActionMap
from Plugins.Extensions.FreeServer.outils.Update import Consolo
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
from Components.MediaPlayer import *
from struct import pack
from enigma import *
from Screens.MessageBox import MessageBox
from Screens.InputBox import InputBox
from Screens.ChoiceBox import ChoiceBox
from Components.Pixmap import Pixmap  
from Components.GUIComponent import *
from Components.Input import Input
from Components.ConfigList import ConfigList
from Screens.ServiceInfo import *
from Tools import Notifications
from Components.config import *
from enigma import eServiceReference
from Tools.Directories import fileExists
from time import *
import time
import datetime
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, getDesktop, loadPNG, eConsoleAppContainer
from enigma import *
import os, sys, re
from xml.dom import Node, minidom
from twisted.web.client import getPage
import urllib
import base64

session = None
data_xml = 'aHR0cHM6Ly9pYTYwMDcwMi51cy5hcmNoaXZlLm9yZy8yNi9pdGVtcy9kcmVhbW9zYXQvY2Ftc3RhcnQwLnR4dA=='
xml_path = base64.b64decode(data_xml)
version = '7710'    
currversion = '7710'   
###################################################################################################### 
Name_001= "RMC 1 FHD"
Name_002= "RMC 2 FHD"
Name_003= "RMC 3 FHD"
Name_004= "RMC 4 FHD"
Name_1= "BEINFR 1 FHD"
Name_2= "BEINFR 2 FHD"
Name_3= "BEINFR 3 FHD"
Name_01= "BEIN 1 FHD"
Name_02= "BEIN 2 FHD"
Name_03= "BEIN 3 FHD"
Name_04= "BEIN 4 FHD"
Name_05= "BEIN 5 FHD"
Name_06= "BEIN 6 FHD"
Name_07= "BEIN 7 FHD"
Name_08= "BEIN 8 FHD"
Name_09= "BEIN 9 FHD"
Name_10= "BEIN 10 FHD"
Name_11= "BEIN 11 FHD"
Name_12= "DAZN 1 BAR HD"
Name_13= "DAZN 2 BAR HD"
Name_14= "SKY SELECT HD"
Name_15= "SKY SELECT 1 HD"
Name_16= "SKY SELECT 2 HD"
Name_17= "SKY SELECT 3 HD"
Name_18= "SKY SELECT 4 HD"
Name_19= "SKY SELECT 5 HD"
Name_20= "SKY SELECT 6 HD"
Name_21= "SKY SELECT 7 HD"
Name_22= "SKY SELECT 8 HD"
Name_23= "SKY SELECT 9 HD"
Name_24= "BOXE OFFICE 1 HD"
Name_25= "BOXE OFFICE 2 HD"
Name_26= "BOXE OFFICE 3 HD"
Name_27= "BOXE OFFICE 4 HD"
Name_28= "BOXE OFFICE 5 HD"
Name_29= "BOXE OFFICE 6 HD"
Name_30= "BOXE OFFICE 7 HD"
Name_31= "BOXE OFFICE 8 HD"
Name_32= "BOXE OFFICE 9 HD"
Name_33= "A LA CARTE 1 HD"
Name_34= "A LA CARTE 2 HD"
Name_35= "A LA CARTE 3 HD"
Name_36= "A LA CARTE 4 HD"
Name_37= "A LA CARTE 5 HD"
Name_38= "A LA CARTE 6 HD"
Name_39= "A LA CARTE 7 HD"
Name_40= "A LA CARTE 8 HD"
Name_41= "A LA CARTE 9 HD"
Name_42= "CANAL PLAY 1 HD"
Name_43= "CANAL PLAY 2 HD"
Name_44= "CANAL PLAY 3 HD"
Name_45= "CANAL PLAY 4 HD"
Name_46= "CANAL PLAY 5 HD"
Name_47= "CANAL PLAY 6 HD"
Name_48= "CANAL PLAY 7 HD"
Name_49= "LOCAL SKY SELECT 1 HD"
Name_50= "LOCAL SKY SELECT 2 HD"
Name_51= "LOCAL SKY SELECT 3 HD"
Name_52= "LOCAL SKY SELECT 4 HD"
Name_53= "LOCAL SKY SELECT 5 HD"
Name_54= "LOCAL SKY SELECT 6 HD"
Name_55= "LOCAL SKY SELECT 7 HD"
Name_56= "LOCAL SKY SELECT 8 HD"
Name_57= "LOCAL SKY SELECT 9 HD"
Name_58= "SKY SELECT 1 HD"
Name_59= "SKY SELECT 2 HD"
Name_60= "SKY SELECT 3 HD"
Name_61= "SKY SELECT 4 HD"
Name_62= "SKY SELECT 5 HD"
Name_63= "SKY SELECT 6 HD"
Name_64= "SKY SELECT 7 HD"
Name_65= "SKY SELECT 8 HD"
Name_66= "SKY SELECT 9 HD"
Name_67= "SKY SELECT 10 HD"
Name_68= "DAZN 1 BAR HD"
Name_69= "DAZN 2 BAR HD"
######################################################################################################
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin/'
p_path = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer'   
from enigma import addFont
try:
    #addFont('%s/Raleway-Black.ttf' % plugin_path, 'Rale', 100, 1)
    #addFont('%s/PlayfairDisplay-Black.otf' % plugin_path, 'Play', 100, 1)
    addFont('%s/bpmono.ttf' % plugin_path, 'bpmo', 100, 1)
except Exception as ex:
    print ex

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280

#########################################################################################################
class MyKoraScreen(Screen):
#### Edit By RAED
        if isHD():
 	    skin = """
		 <screen position="40,50" size="1200,636" title="IPTV WORLD SPORT MOVIES        CHANNELS" flags="wfNoBorder" backgroundColor="#20000000">
		      <widget source="Title" render="Label" position="0,3" size="1200,28" zPosition="3" halign="center" valign="center" font="Regular;26" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329"/>	
		      <widget name="myRedBtn" position="10,556" size="100,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
		      <widget name="myGreenBtn" position="120,556" size="100,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
		      <!--widget name="myYellowBtn" position="230,556" size="100,40" backgroundColor="yellow" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20">
		      <widget name="myBlueBtn" position="340,556" size="100,40" backgroundColor="blue" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>			
		      <widget font="Regular; 16" halign="center" name="tries" position="856,175" size="680,150" zPosition="1" /-->
                      <widget name="myMenu" position="0,40" size="620,500" foregroundColor="#FEFEFE" transparent="1" zPosition="2" />
                      <!--ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/mainbj.jpg" alphatest="blend" transparent="1" />
		      <widget name="myMenu2" position="0,0" size="620,500" flags="wfNoBorder" backgroundColor="#00000000" halign="right"/-->
		 </screen>"""
	else:
 	    skin = """
		 <screen position="0,0" size="1920,1080" title="IPTV WORLD SPORT MOVIES        CHANNELS" flags="wfNoBorder" backgroundColor="#20000000">
		      <widget source="Title" render="Label" position="0,3" size="1920,32" zPosition="3" halign="center" valign="center" font="Regular;30" backgroundColor="#20000000" transparent="1" foregroundColor="#bab329" />	
		      <widget name="myRedBtn" position="30,1030" size="130,40" backgroundColor="red" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;33"/>
		      <widget name="myGreenBtn" position="170,1030" size="130,40" backgroundColor="green" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;33"/>
		      <!--widget name="myYellowBtn" position="260,556" size="130,40" backgroundColor="yellow" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>
		      <widget name="myBlueBtn" position="340,556" size="100,40" backgroundColor="blue" valign="center" halign="center" zPosition="2"  foregroundColor="white" font="Regular;20"/>			
		      <widget font="Regular; 26" halign="center" name="tries" position="856,175" size="680,150" zPosition="1" /-->
                      <widget name="myMenu" position="5,40" size="1690,1000" foregroundColor="#FEFEFE" transparent="1" zPosition="2" />
                      <!--ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/mainbjfhd.jpg" alphatest="blend" transparent="1" />
		      <widget name="myMenu2" position="0,0" size="620,500" flags="wfNoBorder" backgroundColor="#00000000" halign="right"/-->
		 </screen>"""

	def __init__(self, session, picPath = None, args = 0):
		Screen.__init__(self, session)	
		#self.text="IPTV WORLD SPORT MOVIES        CHANNELS"
### EDit By RAED To DreamOS OE2.5/2.6
		if DreamOS():
		     self.wget = "/usr/bin/wget2 --no-check-certificate"
		else:
		     self.wget = "/usr/bin/wget"
### End
		list = []
		list.append(("  SPORT IPTV CHANNELS", "com_***"))
		list.append(("  RMC1 FHD", "com_001"))
		list.append(("  RMC2 FHD", "com_002"))
		list.append(("  RMC3 FHD", "com_003"))
		list.append(("  RMC4 FHD", "com_004"))		
		list.append(("  BEINSPORTS FR 1FHD", "com_005"))		
		list.append(("  BEINSPORTS FR 2FHD", "com_006"))
		list.append(("  BEINSPORTS FR 3FHD", "com_007"))		
		list.append(("  BEINSPORTS 1FHD", "com_01"))		
		list.append(("  BEINSPORTS 2FHD", "com_02"))
		list.append(("  BEINSPORTS 3FHD", "com_03"))
		list.append(("  BEINSPORTS 4FHD", "com_04"))		
		list.append(("  BEINSPORTS 5FHD", "com_05")) 	
		list.append(("  BEINSPORTS 6FHD", "com_06"))
		list.append(("  BEINSPORTS 7FHD", "com_07"))		
		list.append(("  BEINSPORTS 8FHD", "com_08")) 	
		list.append(("  BEINSPORTS 9FHD", "com_09"))
		list.append(("  BEINSPORTS 10FHD", "com_010")) 	
		list.append(("  BEINSPORTS 11FHD", "com_011"))
		list.append(("  DAZN 1 BAR HD", "com_012")) 	
		list.append(("  DAZN 2 BAR HD", "com_013"))
		list.append(("  SKYSELECT HD", "com_014")) 	
		list.append(("  SKYSELECT 1 HD", "com_015"))
		list.append(("  SKYSELECT 2 HD", "com_016")) 	
		list.append(("  SKYSELECT 3 HD", "com_017")) 	
		list.append(("  SKYSELECT 4 HD", "com_018"))
		list.append(("  SKYSELECT 5 HD", "com_019")) 	
		list.append(("  SKYSELECT 6 HD", "com_020"))		
		list.append(("  SKYSELECT 7 HD", "com_021")) 	
		list.append(("  SKYSELECT 8 HD", "com_022"))
		list.append(("  SKYSELECT 9 HD", "com_023")) 	
		list.append(("  BOXE OFFICE 1 HD", "com_024"))
		list.append(("  BOXE OFFICE 2 HD", "com_025")) 	
		list.append(("  BOXE OFFICE 3 HD", "com_026")) 	
		list.append(("  BOXE OFFICE 4 HD", "com_027"))
		list.append(("  BOXE OFFICE 5 HD", "com_028")) 	
		list.append(("  BOXE OFFICE 6 HD", "com_029"))		
		list.append(("  BOXE OFFICE 7 HD", "com_030")) 	
		list.append(("  BOXE OFFICE 8 HD", "com_031"))
		list.append(("  BOXE OFFICE 9 HD", "com_032")) 
		list.append(("  A LA CARTE 1 HD", "com_033"))
		list.append(("  A LA CARTE 2 HD", "com_034")) 	
		list.append(("  A LA CARTE 3 HD", "com_035")) 	
		list.append(("  A LA CARTE 4 HD", "com_036"))
		list.append(("  A LA CARTE 5 HD", "com_037")) 	
		list.append(("  A LA CARTE 6 HD", "com_038"))		
		list.append(("  A LA CARTE 7 HD", "com_039")) 	
		list.append(("  A LA CARTE 8 HD", "com_040"))
		list.append(("  A LA CARTE 9 HD", "com_041"))
		list.append(("  CANAL PLAY 1 HD", "com_042"))
		list.append(("  CANAL PLAY 2 HD", "com_043")) 	
		list.append(("  CANAL PLAY 3 HD", "com_044")) 	
		list.append(("  CANAL PLAY 4 HD", "com_045"))
		list.append(("  CANAL PLAY 5 HD", "com_046")) 	
		list.append(("  CANAL PLAY 6 HD", "com_047"))		
		list.append(("  CANAL PLAY 7 HD", "com_048"))
		list.append(("  LOCAL SKY SELECT 1 HD", "com_049"))
		list.append(("  LOCAL SKY SELECT 2 HD", "com_050"))
		list.append(("  LOCAL SKY SELECT 3 HD", "com_051"))
		list.append(("  LOCAL SKY SELECT 4 HD", "com_052")) 	
		list.append(("  LOCAL SKY SELECT 5 HD", "com_053")) 	
		list.append(("  LOCAL SKY SELECT 6 HD", "com_054"))
		list.append(("  LOCAL SKY SELECT 7 HD", "com_055")) 	
		list.append(("  LOCAL SKY SELECT 8 HD", "com_056"))		
		list.append(("  LOCAL SKY SELECT 9 HD", "com_057")) 	
		list.append(("  SKYSELECT 1 HD", "com_058"))
		list.append(("  SKYSELECT 2 HD", "com_059")) 	
		list.append(("  SKYSELECT 3 HD", "com_060")) 	
		list.append(("  SKYSELECT 4 HD", "com_061"))
		list.append(("  SKYSELECT 5 HD", "com_062")) 	
		list.append(("  SKYSELECT 6 HD", "com_063"))		
		list.append(("  SKYSELECT 7 HD", "com_064")) 	
		list.append(("  SKYSELECT 8 HD", "com_065"))
		list.append(("  SKYSELECT 9 HD", "com_066"))
		list.append(("  SKYSELECT 10 HD", "com_067"))                
		list.append(("  DAZN 1 BAR HD", "com_068")) 	
		list.append(("  DAZN 2 BAR HD", "com_069"))		
		list.append(("  LISTS IPTV SPORTS", "com_***"))		
                list.append(("  IPTVFree001", "com_1"))
                list.append(("  IPTVFree002", "com_2"))	
                list.append(("  IPTVFree003", "com_3"))
                list.append(("  IPTVFree004", "com_4")) 
                list.append(("  IPTVFree005", "com_5"))
                list.append(("  IPTVFree006", "com_6"))             
                list.append(("  IPTVFree007", "com_7"))
                list.append(("  IPTVFree008", "com_8"))          
                list.append(("  IPTVFree009", "com_9"))
                list.append(("  IPTVFree010", "com_10"))
                list.append(("  IPTVFree011", "com_11"))
                list.append(("  IPTVFree012", "com_12"))  
                list.append(("  IPTVFree013", "com_13"))
                list.append(("  IPTVFree014", "com_14"))
                list.append(("  IPTVFree015", "com_15"))                              
                list.append(("  IPTVFree016", "com_16"))		
		list.append(("  IPTVFree017", "com_17"))
		list.append(("  IPTVFree018", "com_18"))       		
  		list.append(("  IPTVFree019", "com_19"))
		list.append(("  IPTVFree020", "com_20"))
		list.append(("  IPTVFree021", "com_21"))
		list.append(("  IPTVFree022", "com_22"))
		list.append(("  IPTVFree023", "com_23"))
		list.append(("  IPTVFree024", "com_24"))
		list.append(("  IPTVFree025", "com_25"))
		list.append(("  IPTVFree026", "com_26"))       		
  		list.append(("  IPTVFree027", "com_27"))
		list.append(("  IPTVFree028", "com_28"))
		list.append(("  IPTVFree029", "com_29"))
		list.append(("  IPTVFree030", "com_30"))
		list.append(("  IPTVFree031", "com_31"))
		list.append(("  IPTVFree032", "com_32"))
		list.append(("  IPTVFree033", "com_33"))       		
  		list.append(("  IPTVFree034", "com_34"))
		list.append(("  IPTVFree035", "com_35"))
		list.append(("  IPTVFree036", "com_36"))
		list.append(("  IPTVFree037", "com_37"))
		list.append(("  IPTVFree038", "com_38"))
		list.append(("  IPTVFree039", "com_39"))
		list.append(("  IPTVFree040", "com_40"))
		list.append(("  IPTVFree041", "com_41"))
		list.append(("  IPTVFree042", "com_42"))
		list.append(("  IPTVFree043", "com_43"))
		list.append(("  IPTVFree044", "com_44"))  
		list.append(("  IPTVFree045", "com_45"))  
		list.append(("  IPTVFree046", "com_46"))
		list.append(("  IPTVFree047", "com_47"))  
		list.append(("  IPTVFree048", "com_48"))
		list.append(("  IPTVFree049", "com_49"))                  
		list.append(("  IPTVFree050", "com_50"))
		list.append(("  IPTVFree051", "com_51"))
		list.append(("  IPTVFree052", "com_52"))
		list.append(("  IPTVFree053", "com_53"))
		list.append(("  IPTVFree054", "com_54"))
		list.append(("  IPTVFree055", "com_55"))  
		list.append(("  IPTVFree056", "com_56"))  
		list.append(("  IPTVFree057", "com_57"))
		list.append(("  IPTVFree058", "com_58"))  
		list.append(("  IPTVFree059", "com_59"))
		list.append(("  IPTVFree060", "com_60"))                                 	
                list.append(("  IPTVFree061", "com_61"))
                list.append(("  IPTVFree062", "com_62"))	
                list.append(("  IPTVFree063", "com_63"))
                list.append(("  IPTVFree064", "com_64")) 
                list.append(("  IPTVFree065", "com_65"))
                list.append(("  IPTVFree066", "com_66"))             
                list.append(("  IPTVFree067", "com_67"))
                list.append(("  IPTVFree068", "com_68"))          
                list.append(("  IPTVFree069", "com_69"))
                list.append(("  IPTVFree070", "com_70"))
                list.append(("  IPTVFree071", "com_71"))
                list.append(("  IPTVFree072", "com_72"))  
                list.append(("  IPTVFree073", "com_73"))
                list.append(("  IPTVFree074", "com_74"))
                list.append(("  IPTVFree075", "com_75"))                              
                list.append(("  IPTVFree076", "com_76"))		
		list.append(("  IPTVFree077", "com_77"))
		list.append(("  IPTVFree078", "com_78"))       		
  		list.append(("  IPTVFree079", "com_79"))
		list.append(("  IPTVFree080", "com_80"))
		list.append(("  IPTVFree081", "com_81"))
		list.append(("  IPTVFree082", "com_82"))
		list.append(("  IPTVFree083", "com_83"))
		list.append(("  IPTVFree084", "com_84"))
		list.append(("  IPTVFree085", "com_85"))
		list.append(("  IPTVFree086", "com_86"))       		
  		list.append(("  IPTVFree087", "com_87"))
		list.append(("  IPTVFree088", "com_88"))
		list.append(("  IPTVFree089", "com_89"))
		list.append(("  IPTVFree090", "com_90"))
		list.append(("  IPTVFree091", "com_91"))
		list.append(("  IPTVFree092", "com_92"))
		list.append(("  IPTVFree093", "com_93"))       		
  		list.append(("  IPTVFree094", "com_94"))
		list.append(("  IPTVFree095", "com_95"))
		list.append(("  IPTVFree096", "com_96"))
		list.append(("  IPTVFree097", "com_77"))
		list.append(("  IPTVFree098", "com_98"))
		list.append(("  IPTVFree099", "com_99"))
		list.append(("  IPTVFree100", "com_100"))
		list.append(("  IPTVFree101", "com_101"))
		list.append(("  IPTVFree102", "com_102"))
		list.append(("  IPTVFree103", "com_103"))
		list.append(("  IPTVFree104", "com_104"))  
		list.append(("  IPTVFree105", "com_105"))  
		list.append(("  IPTVFree106", "com_106"))
		list.append(("  IPTVFree107", "com_107"))  
		list.append(("  IPTVFree108", "com_108"))
		list.append(("  IPTVFree109", "com_109"))                  
		list.append(("  IPTVFree110", "com_110"))
		list.append(("  IPTVFree111", "com_111"))
		list.append(("  IPTVFree112", "com_112"))
		list.append(("  IPTVFree113", "com_113"))
		list.append(("  IPTVFree114", "com_114"))
		list.append(("  IPTVFree115", "com_115"))  
		list.append(("  IPTVFree116", "com_116"))  
		list.append(("  IPTVFree117", "com_117"))
		list.append(("  IPTVFree118", "com_118"))  
		list.append(("  IPTVFree119", "com_119"))
		list.append(("  IPTVFree120", "com_120")) 
		list.append(("  IPTVFree121", "com_121"))
		list.append(("  IPTVFree122", "com_122"))
		list.append(("  IPTVFree123", "com_123"))
		list.append(("  IPTVFree124", "com_124"))
		list.append(("  IPTVFree125", "com_125"))  
		list.append(("  IPTVFree126", "com_126"))  
		list.append(("  IPTVFree127", "com_127"))
		list.append(("  IPTVFree128", "com_128"))  
		list.append(("  IPTVFree129", "com_129"))
		list.append(("  IPTVFree130", "com_130")) 
		list.append(("  IPTVFree131", "com_131"))
		list.append(("  IPTVFree132", "com_132"))
		list.append(("  IPTVFree133", "com_133"))
		list.append(("  IPTVFree134", "com_134"))
		list.append(("  IPTVFree135", "com_135"))  
		list.append(("  IPTVFree136", "com_136"))  
		list.append(("  IPTVFree137", "com_137"))
		list.append(("  IPTVFree138", "com_138"))  
		list.append(("  IPTVFree139", "com_139"))
		list.append(("  IPTVFree140", "com_140")) 
		list.append(("  IPTVFree141", "com_141"))
		list.append(("  IPTVFree142", "com_142"))
		list.append(("  IPTVFree143", "com_143"))
		list.append(("  IPTVFree144", "com_144"))
		list.append(("  IPTVFree145", "com_145"))  
		list.append(("  IPTVFree146", "com_146"))  
		list.append(("  IPTVFree147", "com_147"))
		list.append(("  IPTVFree148", "com_148"))  
		list.append(("  IPTVFree149", "com_149"))
		list.append(("  IPTVFree150", "com_150"))                 		
		list.append(("  ***** ARABE *****", "com_***"))
		list.append(("  IPTVWORLDAR001", "com_151"))
		list.append(("  IPTVWORLDAR002", "com_152"))	
		list.append(("  IPTVWORLDAR003", "com_153"))
		list.append(("  IPTVWORLDAR004", "com_154")) 
		list.append(("  IPTVWORLDAR005", "com_155"))
		list.append(("  IPTVWORLDAR006", "com_156"))
		list.append(("  IPTVWORLDAR007", "com_157"))
		list.append(("  IPTVWORLDAR008", "com_158"))
		list.append(("  IPTVWORLDAR009", "com_159"))
		list.append(("  IPTVWORLDAR010", "com_160"))
		list.append(("  IPTVWORLDAR011", "com_161"))
		list.append(("  IPTVWORLDAR012", "com_162"))  
		list.append(("  IPTVWORLDAR013", "com_163"))
		list.append(("  IPTVWORLDAR014", "com_164"))
		list.append(("  IPTVWORLDAR015", "com_165"))
		list.append(("  IPTVWORLDAR016", "com_166"))		
		list.append(("  IPTVWORLDAR017", "com_167"))
		list.append(("  IPTVWORLDAR018", "com_168"))
  		list.append(("  IPTVWORLDAR019", "com_169"))
		list.append(("  IPTVWORLDAR020", "com_170"))
		list.append(("  IPTVWORLDAR021", "com_171"))
		list.append(("  IPTVWORLDAR022", "com_172"))
		list.append(("  IPTVWORLDAR023", "com_173"))
		list.append(("  IPTVWORLDAR024", "com_174"))
		list.append(("  IPTVWORLDAR025", "com_175"))
		list.append(("  IPTVWORLDAR026", "com_176"))
  		list.append(("  IPTVWORLDAR027", "com_177"))
		list.append(("  IPTVWORLDAR028", "com_178"))
		list.append(("  IPTVWORLDAR029", "com_179"))
		list.append(("  IPTVWORLDAR030", "com_180"))
		list.append(("  IPTVWORLDAR031", "com_181"))
		list.append(("  IPTVWORLDAR032", "com_182"))
		list.append(("  IPTVWORLDAR033", "com_183"))
  		list.append(("  IPTVWORLDAR034", "com_184"))
		list.append(("  IPTVWORLDAR035", "com_185"))
		list.append(("  IPTVWORLDAR036", "com_186"))
		list.append(("  IPTVWORLDAR037", "com_187"))
		list.append(("  IPTVWORLDAR038", "com_188"))
		list.append(("  IPTVWORLDAR039", "com_189"))
		list.append(("  IPTVWORLDAR040", "com_190"))
		list.append(("  IPTVWORLDAR041", "com_191"))
		list.append(("  IPTVWORLDAR042", "com_192"))
		list.append(("  IPTVWORLDAR043", "com_193"))
		list.append(("  IPTVWORLDAR044", "com_194"))  
		list.append(("  IPTVWORLDAR045", "com_195"))  
		list.append(("  IPTVWORLDAR046", "com_196"))
		list.append(("  IPTVWORLDAR047", "com_197"))  
		list.append(("  IPTVWORLDAR048", "com_198"))
		list.append(("  IPTVWORLDAR049", "com_199"))  
		list.append(("  IPTVWORLDAR050", "com_200"))
		list.append(("  IPTVWORLDAR051", "com_201"))
		list.append(("  IPTVWORLDAR052", "com_202"))	
		list.append(("  IPTVWORLDYU053", "com_203"))
		list.append(("  IPTVWORLDAR054", "com_204")) 
		list.append(("  IPTVWORLDAR055", "com_205"))
		list.append(("  IPTVWORLDAR056", "com_206"))
		list.append(("  IPTVWORLDAR057", "com_207"))
		list.append(("  IPTVWORLDAR058", "com_208"))
		list.append(("  IPTVWORLDAR059", "com_209"))
		list.append(("  IPTVWORLDAR060", "com_210"))
		list.append(("  IPTVWORLDAR061", "com_211"))
		list.append(("  IPTVWORLDAR062", "com_212"))  
		list.append(("  IPTVWORLDAR063", "com_213"))
		list.append(("  IPTVWORLDAR064", "com_214"))
		list.append(("  IPTVWORLDAR065", "com_215"))
		list.append(("  IPTVWORLDAR066", "com_216"))		
		list.append(("  IPTVWORLDAR067", "com_217"))
		list.append(("  IPTVWORLDAR068", "com_218"))
  		list.append(("  IPTVWORLDAR069", "com_219"))
		list.append(("  IPTVWORLDAR070", "com_220"))
		list.append(("  IPTVWORLDAR071", "com_221"))
		list.append(("  IPTVWORLDAR072", "com_222"))
		list.append(("  IPTVWORLDAR073", "com_223"))
		list.append(("  IPTVWORLDAR074", "com_234"))
		list.append(("  IPTVWORLDAR075", "com_235"))
		list.append(("  IPTVWORLDAR076", "com_236"))
  		list.append(("  IPTVWORLDAR077", "com_237"))
		list.append(("  IPTVWORLDAR078", "com_238"))
		list.append(("  IPTVWORLDAR079", "com_239"))
		list.append(("  IPTVWORLDAR080", "com_240"))
		list.append(("  IPTVWORLDAR081", "com_241"))
		list.append(("  IPTVWORLDAR082", "com_242"))
		list.append(("  IPTVWORLDAR083", "com_243"))
  		list.append(("  IPTVWORLDAR084", "com_244"))
		list.append(("  IPTVWORLDAR085", "com_245"))
		list.append(("  IPTVWORLDAR086", "com_246"))
		list.append(("  IPTVWORLDAR087", "com_247"))
		list.append(("  IPTVWORLDAR088", "com_248"))
		list.append(("  IPTVWORLDAR089", "com_249"))
		list.append(("  IPTVWORLDAR090", "com_240"))
		list.append(("  IPTVWORLDAR091", "com_241"))
		list.append(("  IPTVWORLDAR092", "com_242"))
		list.append(("  IPTVWORLDAR093", "com_243"))
		list.append(("  IPTVWORLDAR094", "com_244"))  
		list.append(("  IPTVWORLDAR095", "com_245"))  
		list.append(("  IPTVWORLDAR096", "com_246"))
		list.append(("  IPTVWORLDAR097", "com_247"))  
		list.append(("  IPTVWORLDAR098", "com_248"))
		list.append(("  IPTVWORLDAR099", "com_249"))  
		list.append(("  IPTVWORLDAR100", "com_250"))
		list.append(("  ***** FRANCE ******", "com_***"))		
		list.append(("  IPTVWORLDFR001", "com_251"))
		list.append(("  IPTVWORLDFR002", "com_252"))	
		list.append(("  IPTVWORLDFR003", "com_253"))
		list.append(("  IPTVWORLDFR004", "com_254")) 
		list.append(("  IPTVWORLDFR005", "com_255"))
		list.append(("  IPTVWORLDFR006", "com_256"))
		list.append(("  IPTVWORLDFR007", "com_257"))
		list.append(("  IPTVWORLDFR008", "com_258"))
		list.append(("  IPTVWORLDFR009", "com_259"))
		list.append(("  IPTVWORLDFR010", "com_260"))
		list.append(("  IPTVWORLDFR011", "com_261"))
		list.append(("  IPTVWORLDFR012", "com_262"))  
		list.append(("  IPTVWORLDFR013", "com_263"))
		list.append(("  IPTVWORLDFR014", "com_264"))
		list.append(("  IPTVWORLDFR015", "com_265"))
		list.append(("  IPTVWORLDFR016", "com_266"))		
		list.append(("  IPTVWORLDFR017", "com_267"))
		list.append(("  IPTVWORLDFR018", "com_268"))
  		list.append(("  IPTVWORLDFR019", "com_269"))
		list.append(("  IPTVWORLDFR020", "com_270"))
		list.append(("  IPTVWORLDFR021", "com_271"))
		list.append(("  IPTVWORLDFR022", "com_272"))
		list.append(("  IPTVWORLDFR023", "com_273"))
		list.append(("  IPTVWORLDFR024", "com_274"))
		list.append(("  IPTVWORLDFR025", "com_275"))
		list.append(("  IPTVWORLDFR026", "com_276"))
  		list.append(("  IPTVWORLDFR027", "com_277"))
		list.append(("  IPTVWORLDFR028", "com_278"))
		list.append(("  IPTVWORLDFR029", "com_279"))
		list.append(("  IPTVWORLDFR030", "com_280"))	
		list.append(("  IPTVWORLDFR031", "com_281"))
		list.append(("  IPTVWORLDFR032", "com_282"))
		list.append(("  IPTVWORLDFR033", "com_283"))
  		list.append(("  IPTVWORLDFR034", "com_284"))
		list.append(("  IPTVWORLDFR035", "com_285"))
		list.append(("  IPTVWORLDFR036", "com_286"))
		list.append(("  IPTVWORLDFR037", "com_287"))
		list.append(("  IPTVWORLDFR038", "com_288"))
		list.append(("  IPTVWORLDFR039", "com_289"))
		list.append(("  IPTVWORLDFR040", "com_290"))	
		list.append(("  IPTVWORLDFR041", "com_291"))
		list.append(("  IPTVWORLDFR042", "com_292"))
		list.append(("  IPTVWORLDFR043", "com_293"))
		list.append(("  IPTVWORLDFR044", "com_294"))  
		list.append(("  IPTVWORLDFR045", "com_295"))  
		list.append(("  IPTVWORLDFR046", "com_296"))
		list.append(("  IPTVWORLDFR047", "com_297"))  
		list.append(("  IPTVWORLDFR048", "com_298"))
		list.append(("  IPTVWORLDFR049", "com_299"))  
		list.append(("  IPTVWORLDFR050", "com_300")) 
		list.append(("  ****** GREEK *****", "com_***"))	
		list.append(("  IPTVWORLDGR001", "com_301"))
		list.append(("  IPTVWORLDGR002", "com_302"))
		list.append(("  IPTVWORLDGR003", "com_303"))
		list.append(("  IPTVWORLDGR004", "com_304"))  
		list.append(("  IPTVWORLDGR005", "com_305"))  
		list.append(("  IPTVWORLDGR006", "com_306"))
		list.append(("  IPTVWORLDGR007", "com_307"))  
		list.append(("  IPTVWORLDGR008", "com_308"))
		list.append(("  IPTVWORLDGR009", "com_309"))  
		list.append(("  IPTVWORLDHR010", "com_310"))
		list.append(("  IPTVWORLDGR011", "com_311"))
		list.append(("  IPTVWORLDGR012", "com_312"))  
		list.append(("  IPTVWORLDGR013", "com_313"))
		list.append(("  IPTVWORLDGR014", "com_314"))  
		list.append(("  IPTVWORLDGR015", "com_315")) 		
		list.append(("  ***** TURKE *****", "com_***"))
		list.append(("  IPTVWORLDTR001", "com_316"))
		list.append(("  IPTVWORLDTR002", "com_317"))
		list.append(("  IPTVWORLDTR003", "com_318"))
		list.append(("  IPTVWORLDTR004", "com_319"))  
		list.append(("  IPTVWORLDTR005", "com_320"))  
		list.append(("  IPTVWORLDTR006", "com_321"))
		list.append(("  IPTVWORLDTR007", "com_322"))  
		list.append(("  IPTVWORLDTR008", "com_323"))
		list.append(("  IPTVWORLDTR009", "com_324"))  
		list.append(("  IPTVWORLDTR010", "com_325"))
		list.append(("  IPTVWORLDTR011", "com_326"))
		list.append(("  IPTVWORLDTR012", "com_327"))	
		list.append(("  IPTVWORLDTR013", "com_328"))
		list.append(("  IPTVWORLDTR014", "com_329")) 
		list.append(("  IPTVWORLDTR015", "com_330"))
		list.append(("  IPTVWORLDTR016", "com_331"))
		list.append(("  IPTVWORLDTR017", "com_332"))
		list.append(("  IPTVWORLDTR018", "com_333"))
		list.append(("  IPTVWORLDTR019", "com_334"))
		list.append(("  IPTVWORLDTR020", "com_335"))
		list.append(("  ***** USA *****", "com_***"))
		list.append(("  IPTVWORLDUS001", "com_336"))
		list.append(("  IPTVWORLDUS002", "com_337"))
		list.append(("  IPTVWORLDUS003", "com_338"))
		list.append(("  IPTVWORLDUS004", "com_339"))  
		list.append(("  IPTVWORLDUS005", "com_340"))  
		list.append(("  IPTVWORLDUS006", "com_341"))
		list.append(("  IPTVWORLDUS007", "com_342"))  
		list.append(("  IPTVWORLDUS008", "com_343"))
		list.append(("  IPTVWORLDUS009", "com_344"))  
		list.append(("  IPTVWORLDUS010", "com_345"))
		list.append(("  IPTVWORLDUS011", "com_346"))
		list.append(("  IPTVWORLDUS012", "com_347"))	
		list.append(("  IPTVWORLDUS013", "com_348"))
		list.append(("  IPTVWORLDUS014", "com_349")) 
		list.append(("  IPTVWORLDUS015", "com_350"))
		list.append(("  IPTVWORLDUS016", "com_351"))
		list.append(("  IPTVWORLDUS017", "com_352"))
		list.append(("  IPTVWORLDUS018", "com_353"))
		list.append(("  IPTVWORLDUS019", "com_354"))
		list.append(("  IPTVWORLDUS020", "com_355"))
		list.append(("  IPTVWORLDUS021", "com_356"))
		list.append(("  IPTVWORLDUS022", "com_357"))
		list.append(("  IPTVWORLDUS023", "com_358"))
		list.append(("  IPTVWORLDUS024", "com_359"))  
		list.append(("  IPTVWORLDUS025", "com_360"))  
		list.append(("  IPTVWORLDUS026", "com_361"))
		list.append(("  IPTVWORLDUS027", "com_362"))  
		list.append(("  IPTVWORLDUS028", "com_363"))
		list.append(("  IPTVWORLDUS029", "com_364"))  
		list.append(("  IPTVWORLDUS030", "com_365"))
		list.append(("  IPTVWORLDUS031", "com_366"))
		list.append(("  IPTVWORLDUS032", "com_367"))	
		list.append(("  IPTVWORLDUS033", "com_368"))
		list.append(("  IPTVWORLDUS034", "com_369")) 
		list.append(("  IPTVWORLDUS035", "com_370"))
		list.append(("  IPTVWORLDUS036", "com_371"))
		list.append(("  IPTVWORLDUS037", "com_372"))
		list.append(("  IPTVWORLDUS038", "com_373"))
		list.append(("  IPTVWORLDUS039", "com_374"))
		list.append(("  IPTVWORLDUS040", "com_375"))
		list.append(("  ***** RUSSE *****", "com_***"))
		list.append(("  IPTVWORLDRU001", "com_376"))
		list.append(("  IPTVWORLDRU002", "com_377"))	
		list.append(("  IPTVWORLDRU003", "com_378"))
		list.append(("  IPTVWORLDRU004", "com_379")) 
		list.append(("  IPTVWORLDRU005", "com_380"))
		list.append(("  IPTVWORLDRU006", "com_381"))
		list.append(("  IPTVWORLDRU007", "com_382"))
		list.append(("  IPTVWORLDRU008", "com_383"))
		list.append(("  IPTVWORLDRU009", "com_384"))
		list.append(("  IPTVWORLDRU010", "com_385"))
		list.append(("  IPTVWORLDRU011", "com_386"))
		list.append(("  IPTVWORLDRU012", "com_387"))
		list.append(("  IPTVWORLDRU013", "com_388"))
		list.append(("  IPTVWORLDRU014", "com_389"))  
		list.append(("  IPTVWORLDRU015", "com_390"))  
		list.append(("  IPTVWORLDRU016", "com_391"))
		list.append(("  IPTVWORLDRU017", "com_392"))  
		list.append(("  IPTVWORLDRU018", "com_393"))
		list.append(("  IPTVWORLDRU019", "com_394"))  
		list.append(("  IPTVWORLDRU020", "com_395"))
		list.append(("  IPTVWORLDRU021", "com_396"))
		list.append(("  IPTVWORLDRU022", "com_397"))	
		list.append(("  IPTVWORLDRU023", "com_398"))
		list.append(("  IPTVWORLDRU024", "com_399")) 
		list.append(("  IPTVWORLDRU025", "com_400"))
		list.append(("  IPTVWORLDRU026", "com_401"))
		list.append(("  IPTVWORLDRU027", "com_402"))
		list.append(("  IPTVWORLDRU028", "com_403"))
		list.append(("  IPTVWORLDRU029", "com_404"))
		list.append(("  IPTVWORLDRU030", "com_405"))                			
		list.append(("  IPTV WORLD CHANNELS", "com_***"))  
		list.append(("  IPTVWORLD001", "com_406"))
		list.append(("  IPTVWORLD002", "com_407"))	
		list.append(("  IPTVWORLD003", "com_408"))
		list.append(("  IPTVWORLD004", "com_409")) 
		list.append(("  IPTVWORLD005", "com_410"))
		list.append(("  IPTVWORLD006", "com_411"))
		list.append(("  IPTVWORLD007", "com_412"))
		list.append(("  IPTVWORLD008", "com_413"))
		list.append(("  IPTVWORLD009", "com_414"))
		list.append(("  IPTVWORLD010", "com_415"))
		list.append(("  IPTVWORLD011", "com_416"))
		list.append(("  IPTVWORLD012", "com_417"))  
		list.append(("  IPTVWORLD013", "com_418"))
		list.append(("  IPTVWORLD014", "com_419"))
		list.append(("  IPTVWORLD015", "com_420"))
		list.append(("  IPTVWORLD016", "com_421"))		
		list.append(("  IPTVWORLD017", "com_422"))
		list.append(("  IPTVWORLD018", "com_423"))
  		list.append(("  IPTVWORLD019", "com_424"))
		list.append(("  IPTVWORLD020", "com_425"))
		list.append(("  IPTVWORLD021", "com_426"))
		list.append(("  IPTVWORLD022", "com_427"))
		list.append(("  IPTVWORLD023", "com_428"))
		list.append(("  IPTVWORLD024", "com_429"))
		list.append(("  IPTVWORLD025", "com_430"))
		list.append(("  IPTVWORLD026", "com_431"))
  		list.append(("  IPTVWORLD027", "com_432"))
		list.append(("  IPTVWORLD028", "com_433"))
		list.append(("  IPTVWORLD029", "com_434"))
		list.append(("  IPTVWORLD030", "com_435"))
		list.append(("  IPTVWORLD031", "com_436"))
		list.append(("  IPTVWORLD032", "com_437"))
		list.append(("  IPTVWORLD033", "com_438"))
  		list.append(("  IPTVWORLD034", "com_439"))
		list.append(("  IPTVWORLD035", "com_440"))
		list.append(("  IPTVWORLD036", "com_441"))
		list.append(("  IPTVWORLD037", "com_442"))
		list.append(("  IPTVWORLD038", "com_443"))
		list.append(("  IPTVWORLD039", "com_444"))
		list.append(("  IPTVWORLD040", "com_445"))
		list.append(("  IPTVWORLD041", "com_446"))
		list.append(("  IPTVWORLD042", "com_447"))
		list.append(("  IPTVWORLD043", "com_448"))
		list.append(("  IPTVWORLD044", "com_449"))  
		list.append(("  IPTVWORLD045", "com_450"))  
		list.append(("  IPTVWORLD046", "com_451"))
		list.append(("  IPTVWORLD047", "com_452"))  
		list.append(("  IPTVWORLD048", "com_453"))
		list.append(("  IPTVWORLD049", "com_454"))  
		list.append(("  IPTVWORLD050", "com_455")) 
		list.append(("  IPTVWORLD051", "com_456"))
		list.append(("  IPTVWORLD052", "com_457"))  
		list.append(("  IPTVWORLD053", "com_458"))
		list.append(("  IPTVWORLD054", "com_459"))
		list.append(("  IPTVWORLD055", "com_460"))
		list.append(("  IPTVWORLD056", "com_461"))		
		list.append(("  IPTVWORLD057", "com_462"))
		list.append(("  IPTVWORLD058", "com_463"))
  		list.append(("  IPTVWORLD059", "com_464"))
		list.append(("  IPTVWORLD060", "com_465"))
		list.append(("  ***** DEUTSHLAND *****", "com_***"))				
		list.append(("  IPTVWORLDDE001", "com_466"))
		list.append(("  IPTVWORLDDE002", "com_467"))  
		list.append(("  IPTVWORLDDE003", "com_468"))
		list.append(("  IPTVWORLDDE004", "com_469"))
		list.append(("  IPTVWORLDDE005", "com_470"))
		list.append(("  IPTVWORLDDE006", "com_471"))		
		list.append(("  IPTVWORLDDE007", "com_472"))
		list.append(("  IPTVWORLDDE008", "com_473"))
  		list.append(("  IPTVWORLDDE009", "com_474"))
		list.append(("  IPTVWORLDDE010", "com_475"))
		list.append(("  IPTVWORLDDE011", "com_476"))
		list.append(("  IPTVWORLDDE012", "com_477"))  
		list.append(("  IPTVWORLDDE013", "com_478"))
		list.append(("  IPTVWORLDDE014", "com_479"))
		list.append(("  IPTVWORLDDE015", "com_480"))
		list.append(("  IPTVWORLDDE016", "com_481"))		
		list.append(("  IPTVWORLDDE017", "com_482"))
		list.append(("  IPTVWORLDDE018", "com_483"))
  		list.append(("  IPTVWORLDDE019", "com_484"))
		list.append(("  IPTVWORLDDE020", "com_485"))
		list.append(("  ***** ENGLAND *****", "com_***"))			
		list.append(("  IPTVWORLDUK001", "com_486"))
		list.append(("  IPTVWORLDUK002", "com_487"))
		list.append(("  IPTVWORLDUK003", "com_488"))
		list.append(("  IPTVWORLDUK004", "com_489"))
		list.append(("  IPTVWORLDUK005", "com_490"))
		list.append(("  IPTVWORLDUK006", "com_491"))
  		list.append(("  IPTVWORLDUK007", "com_492"))
		list.append(("  IPTVWORLDUK008", "com_493"))
		list.append(("  IPTVWORLDUK009", "com_494"))
		list.append(("  IPTVWORLDUK010", "com_495"))
		list.append(("  ***** ESPANIA *****  ", "com_***"))  
		list.append(("  IPTVWORLDES001", "com_496")) 
		list.append(("  IPTVWORLDES002", "com_497"))
		list.append(("  IPTVWORLDES003", "com_498"))
		list.append(("  IPTVWORLDES004", "com_499"))
		list.append(("  IPTVWORLDES005", "com_500"))
		list.append(("  IPTVWORLDES006", "com_501"))  
		list.append(("  IPTVWORLDES007", "com_502"))  
		list.append(("  IPTVWORLDES008", "com_503"))
		list.append(("  IPTVWORLDES009", "com_504"))  
		list.append(("  IPTVWORLDES010", "com_505"))
		list.append(("  IPTVWORLDES011", "com_506")) 
		list.append(("  IPTVWORLDES012", "com_507"))
		list.append(("  IPTVWORLDES013", "com_508"))
		list.append(("  IPTVWORLDES014", "com_509"))
		list.append(("  IPTVWORLDES015", "com_510"))
		list.append(("  IPTVWORLDES016", "com_511"))  
		list.append(("  IPTVWORLDES017", "com_512"))  
		list.append(("  IPTVWORLDES018", "com_513"))
		list.append(("  IPTVWORLDES019", "com_514"))  
		list.append(("  IPTVWORLDES020", "com_515"))
		list.append(("  IPTVWORLDES021", "com_516")) 		                 
		list.append(("  IPTVWORLDPO022", "com_517"))
		list.append(("  IPTVWORLDPO023", "com_518"))
		list.append(("  IPTVWORLDES024", "com_519"))  
		list.append(("  IPTVWORLDES025", "com_520"))
		list.append(("  IPTVWORLDES026", "com_521"))  
		list.append(("  IPTVWORLDES027", "com_522"))
		list.append(("  IPTVWORLDES028", "com_523")) 		                 
		list.append(("  IPTVWORLDES029", "com_524"))
		list.append(("  IPTVWORLDES030", "com_525"))		
		list.append(("  ***** EX-YOUGOSLAVIE *****", "com_***"))		
		list.append(("  IPTVWORLDYU001", "com_526"))
		list.append(("  IPTVWORLDYU002", "com_527"))
		list.append(("  IPTVWORLDYU003", "com_528"))
		list.append(("  IPTVWORLDYU004", "com_529"))  
		list.append(("  IPTVWORLDYU005", "com_530"))  
		list.append(("  IPTVWORLDYU006", "com_531"))
		list.append(("  IPTVWORLDYU007", "com_532"))  
		list.append(("  IPTVWORLDYU008", "com_533"))
		list.append(("  IPTVWORLDYU009", "com_534"))  
		list.append(("  IPTVWORLDYU010", "com_535"))
		list.append(("  ***** ITALIA *****", "com_***"))		
		list.append(("  IPTVWORLDIT001", "com_536"))
		list.append(("  IPTVWORLDIT002", "com_537"))
		list.append(("  IPTVWORLDIT003", "com_538"))
		list.append(("  IPTVWORLDIT004", "com_539"))  
		list.append(("  IPTVWORLDIT005", "com_540"))  
		list.append(("  IPTVWORLDIT006", "com_541"))
		list.append(("  IPTVWORLDIT007", "com_542"))  
		list.append(("  IPTVWORLDIT008", "com_543"))
		list.append(("  IPTVWORLDIT009", "com_544"))  
		list.append(("  IPTVWORLDIT010", "com_545"))
		list.append(("  ***** PORTUGAL *****", "com_***"))		
		list.append(("  IPTVWORLDPO001", "com_546"))
		list.append(("  IPTVWORLDPO002", "com_547"))
		list.append(("  IPTVWORLDPO003", "com_548"))
		list.append(("  IPTVWORLDPO004", "com_549"))  
		list.append(("  IPTVWORLDPO005", "com_550"))  
		list.append(("  IPTVWORLDPO006", "com_551"))
		list.append(("  IPTVWORLDPO007", "com_552"))  
		list.append(("  IPTVWORLDPO008", "com_553"))
		list.append(("  IPTVWORLDPO009", "com_554"))  
		list.append(("  IPTVWORLDPO010", "com_555"))  
		list.append(("  ***** ALBANIE *****", "com_***"))		
		list.append(("  IPTVWORLDAL001", "com_556"))
		list.append(("  IPTVWORLDAL002", "com_557"))
		list.append(("  IPTVWORLDAL003", "com_558"))
		list.append(("  IPTVWORLDAL004", "com_559"))  
		list.append(("  IPTVWORLDAL005", "com_560"))  
		list.append(("  IPTVWORLDAL006", "com_561"))
		list.append(("  IPTVWORLDAL007", "com_562"))  
		list.append(("  IPTVWORLDAL008", "com_563"))
		list.append(("  IPTVWORLDAL009", "com_564"))  
		list.append(("  IPTVWORLDAL010", "com_565"))
		list.append(("  ***** ROMANIA *****", "com_***"))		
		list.append(("  IPTVWORLDRO001", "com_566"))
		list.append(("  IPTVWORLDRO002", "com_567"))
		list.append(("  IPTVWORLDRO003", "com_568"))
		list.append(("  IPTVWORLDRO004", "com_569"))  
		list.append(("  IPTVWORLDRO005", "com_570"))  
		list.append(("  IPTVWORLDRO006", "com_571"))
		list.append(("  IPTVWORLDRO007", "com_572"))  
		list.append(("  IPTVWORLDRO008", "com_573"))
		list.append(("  IPTVWORLDRO009", "com_574"))  
		list.append(("  IPTVWORLDRO010", "com_575"))
		list.append(("  ***** BRAZIL *****", "com_***"))		
		list.append(("  IPTVWORLDBR001", "com_576"))
		list.append(("  IPTVWORLDBR002", "com_577"))
		list.append(("  IPTVWORLDBR003", "com_578"))
		list.append(("  IPTVWORLDBR004", "com_579"))  
		list.append(("  IPTVWORLDBR005", "com_580"))  
		list.append(("  IPTVWORLDBR006", "com_581"))
		list.append(("  IPTVWORLDBR007", "com_582"))  
		list.append(("  IPTVWORLDBR008", "com_583"))
		list.append(("  IPTVWORLDBR009", "com_584"))  
		list.append(("  IPTVWORLDBR010", "com_585"))
		list.append(("  ***** CANADA *****", "com_***"))
		list.append(("  IPTVWORLDCA001", "com_586"))
		list.append(("  IPTVWORLDCA002", "com_587"))
		list.append(("  IPTVWORLDCA003", "com_588"))
		list.append(("  IPTVWORLDCA004", "com_589"))  
		list.append(("  IPTVWORLDCA005", "com_590"))  
		list.append(("  IPTVWORLDCA006", "com_591"))
		list.append(("  IPTVWORLDCA007", "com_592"))  
		list.append(("  IPTVWORLDCA008", "com_593"))
		list.append(("  IPTVWORLDCA009", "com_594"))  
		list.append(("  IPTVWORLDCA010", "com_595"))		
		list.append(("  IPTVWORLDCA011", "com_596"))
		list.append(("  IPTVWORLDCA012", "com_597"))
		list.append(("  IPTVWORLDCA013", "com_598"))
		list.append(("  IPTVWORLDCA014", "com_599"))  
		list.append(("  IPTVWORLDCA015", "com_600"))  
		list.append(("  ***** ASIE *****", "com_***"))
		list.append(("  IPTVWORLDAS001", "com_601"))  
		list.append(("  IPTVWORLDAS002", "com_602"))  
		list.append(("  IPTVWORLDAS003", "com_603"))
		list.append(("  IPTVWORLDAS004", "com_604"))  
		list.append(("  IPTVWORLDAS005", "com_605"))
		list.append(("  IPTVWORLDAS006", "com_606")) 
		list.append(("  IPTVWORLDAS007", "com_607"))
		list.append(("  IPTVWORLDAS008", "com_608"))
		list.append(("  IPTVWORLDAS009", "com_609"))
		list.append(("  IPTVWORLDAS010", "com_610"))
		list.append(("  IPTVWORLDAS011", "com_611"))  
		list.append(("  IPTVWORLDAS012", "com_612"))  
		list.append(("  IPTVWORLDAS013", "com_613"))
		list.append(("  IPTVWORLDAS014", "com_614"))  
		list.append(("  IPTVWORLDAS015", "com_615"))
		list.append(("  IPTVWORLDAS016", "com_616")) 		                 
		list.append(("  IPTVWORLDAS017", "com_617"))
		list.append(("  IPTVWORLDAS018", "com_618"))
		list.append(("  IPTVWORLDAS019", "com_619"))  
		list.append(("  IPTVWORLDAS020", "com_620"))
		list.append(("  IPTVWORLDAS021", "com_621"))  
		list.append(("  IPTVWORLDAS022", "com_622"))
		list.append(("  IPTVWORLDAS023", "com_623")) 		                 
		list.append(("  IPTVWORLDAS024", "com_624"))
		list.append(("  IPTVWORLDAS025", "com_625"))				
		list.append(("  IPTVWORLDAS026", "com_626"))
		list.append(("  IPTVWORLDAS027", "com_627"))
		list.append(("  IPTVWORLDAS028", "com_628"))
		list.append(("  IPTVWORLDAS029", "com_629"))  
		list.append(("  IPTVWORLDAS030", "com_630"))  
		list.append(("  IPTVWORLDAS031", "com_631"))
		list.append(("  IPTVWORLDAS032", "com_632"))  
		list.append(("  IPTVWORLDAS033", "com_633"))
		list.append(("  IPTVWORLDAS034", "com_634"))  
		list.append(("  IPTVWORLDAS035", "com_635"))		
		list.append(("  IPTVWORLDAS036", "com_636"))
		list.append(("  IPTVWORLDAS037", "com_637"))
		list.append(("  IPTVWORLDAS038", "com_638"))
		list.append(("  IPTVWORLDAS039", "com_639"))  
		list.append(("  IPTVWORLDAS040", "com_640"))  
		list.append(("  IPTVWORLDAS041", "com_641"))
		list.append(("  IPTVWORLDAS042", "com_642"))  
		list.append(("  IPTVWORLDAS043", "com_643"))
		list.append(("  IPTVWORLDAS044", "com_644"))  
		list.append(("  IPTVWORLDAS045", "com_645"))		
		list.append(("  IPTVWORLDAS046", "com_646"))
		list.append(("  IPTVWORLDAS047", "com_647"))
		list.append(("  IPTVWORLDAS048", "com_648"))
		list.append(("  IPTVWORLDAS049", "com_649"))  
		list.append(("  IPTVWORLDAS050", "com_650"))  
		list.append(("  IPTVWORLDAS051", "com_651"))
		list.append(("  IPTVWORLDAS052", "com_652"))  
		list.append(("  IPTVWORLDAS053", "com_653"))
		list.append(("  IPTVWORLDAS054", "com_654"))  
		list.append(("  IPTVWORLDAS055", "com_655"))  		
		list.append(("  IPTVWORLDAS056", "com_656"))
		list.append(("  IPTVWORLDAS057", "com_657"))
		list.append(("  IPTVWORLDAS058", "com_658"))
		list.append(("  IPTVWORLDAS059", "com_659"))  
		list.append(("  IPTVWORLDAS060", "com_660"))                                               		
		list.append((_("Exit"), "exit"))
		Screen.__init__(self, session)
		self['icon3'] = Pixmap()		
		#self['icon'] = Pixmap() 
		self['icon2'] = Pixmap() 
		self["go"] = Label()	
		#self["goto"] = Label()		
		self["prombt"] = Label()
		self["myRedBtn"] = Label(_("Cancel"))
		self["myGreenBtn"] = Label(_("IPTV"))
		#self["myYellowBtn"] = Label(_("restart"))
		#self["myBlueBtn"] = Label(_("Preview"))
		self.cmdlist = []
		self.onChangedEntry = []
		self.initialservice = session.nav.getCurrentlyPlayingServiceReference()		
		self["myMenu"] = MenuList(list)
		self['setupActions'] = ActionMap(['SetupActions', 'ColorActions', 'DirectionActions'], {'green': self.IPTV,
                 #'yellow': self.goto,
                 #'blue': self.gotoa,
                 'red': self.close,
                 'ok': self.go,
                 'cancel': self.close}, -2)
		self.timer = eTimer()
### Edit By RAED To DreamOS & Fix update notification restart warrning
		try:
		       self.timer.callback.append(self.update)
		except:
		       self.timer_conn = self.timer.timeout.connect(self.update)
		self.timer.start(2, 1)
		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		self.setTitle("IPTV WORLD SPORT MOVIES        CHANNELS")

	def update(self):
		try:
                    fp = urllib.urlopen(xml_path)
                    count = 0
                    self.labeltext = ''
                    s1 = fp.readline()
                    s2 = fp.readline()
                    s3 = fp.readline()
                    s1 = s1.strip()
                    s2 = s2.strip()
                    s3 = s3.strip()
                    self.link = s2
                    self.version = s1
                    self.info = s3
                    fp.close()
                    cstr = s1 + ' ' + s2
                    if s1 <= currversion:
                        return
                        print '[No Update Avilable]'
                    else:  
                        self.session.openWithCallback(self.install, MessageBox, _('New update available.\n\nDo you want ot install now.'), MessageBox.TYPE_YESNO)
                        print '[New Update Avilable]'
		except:
                    return '[New Update Avilable]'

	def install(self, *retval):
            os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/freecc4.sh -qO - | /bin/sh" % self.wget)
            self.session.openWithCallback(self.restartenigma, MessageBox, _('** Nedd Restart Enigma2 To Load New Update ?!! **'), MessageBox.TYPE_YESNO, timeout=10)
### End EDit
	def go(self):
		returnValue = self["myMenu"].l.getCurrentSelection()[1]
		if returnValue is not None:		
			if returnValue is "com_001":
			    self.RMCHD1()
			elif returnValue is "com_002":
			    self.RMCHD2()
			elif returnValue is "com_003":
			    self.RMCHD3()
			elif returnValue is "com_004":
			    self.RMCHD4()
			elif returnValue is "com_005":
			    self.BeinFRHD1()
			elif returnValue is "com_006":
			    self.BeinFRHD2()			    
			elif returnValue is "com_007":
			    self.BeinFRHD3()			    
			elif returnValue is "com_01":
			    self.BeinHD1()
			elif returnValue is "com_02":
			    self.BeinHD2()
			elif returnValue is "com_03":
			    self.BeinHD3()
			elif returnValue is "com_04":
			    self.BeinHD4()
			elif returnValue is "com_05":
			    self.BeinHD5()
			elif returnValue is "com_06":
			    self.BeinHD6()
			elif returnValue is "com_07":
			    self.BeinHD7()
			elif returnValue is "com_08":
			    self.BeinHD8()
			elif returnValue is "com_09":
			    self.BeinHD9()
			elif returnValue is "com_010":
			    self.BeinHD10()
			elif returnValue is "com_011":
			    self.BeinHD11()
			elif returnValue is "com_012":
			    self.DAZN1HD()
			elif returnValue is "com_013": 
			    self.DAZN2HD()
			elif returnValue is "com_014":
			    self.SKYSELECTHD()
			elif returnValue is "com_015":
			    self.SKYSELECT1HD()
			elif returnValue is "com_016":
			    self.SKYSELECT2HD()
			elif returnValue is "com_017":
			    self.SKYSELECT3HD()
			elif returnValue is "com_018":
			    self.SKYSELECT4HD()
			elif returnValue is "com_019":
			    self.SKYSELECT5HD()                            			    
			elif returnValue is "com_020":
			    self.SKYSELECT6HD()
			elif returnValue is "com_021":
			    self.SKYSELECT7HD()
			elif returnValue is "com_022":
			    self.SKYSELECT8HD()
			elif returnValue is "com_023":
			    self.SKYSELECT9HD()
			elif returnValue is "com_024":
			    self.MOVIES1HD()
			elif returnValue is "com_025":
			    self.MOVIES2HD()
			elif returnValue is "com_026":
			    self.MOVIES3HD()
			elif returnValue is "com_027":
			    self.MOVIES4HD()
			elif returnValue is "com_028":
			    self.MOVIES5HD()
			elif returnValue is "com_029":                        	
			    self.MOVIES6HD()
			elif returnValue is "com_030":
			    self.MOVIES7HD()
			elif returnValue is "com_031":
			    self.MOVIES8HD()
			elif returnValue is "com_032":
			    self.MOVIES9HD()
			elif returnValue is "com_033":
			    self.ALACARTE1HD()
			elif returnValue is "com_034":
			    self.ALACARTE2HD()
			elif returnValue is "com_035":
			    self.ALACARTE3HD()
			elif returnValue is "com_036":
			    self.ALACARTE4HD()
			elif returnValue is "com_037":
			    self.ALACARTE5HD()
			elif returnValue is "com_038":                        	
			    self.ALACARTE6HD()
			elif returnValue is "com_039":
			    self.ALACARTE7HD()
			elif returnValue is "com_040":
			    self.ALACARTE8HD()
			elif returnValue is "com_041":
			    self.ALACARTE9HD()	
			elif returnValue is "com_042":
			    self.CANALPLAY1HD()
			elif returnValue is "com_043":
			    self.CANALPLAY2HD()
			elif returnValue is "com_044":
			    self.CANALPLAY3HD()
			elif returnValue is "com_045":
			    self.CANALPLAY4HD()
			elif returnValue is "com_046":
			    self.CANALPLAY5HD()
			elif returnValue is "com_047":                        	
			    self.CANALPLAY6HD()
			elif returnValue is "com_048":
			    self.CANALPLAY7HD()
			elif returnValue is "com_049":
			    self.LOCALSKYSELECT1HD()
			elif returnValue is "com_050":
			    self.LOCALSKYSELECT2HD()	
			elif returnValue is "com_051":
			    self.LOCALSKYSELECT3HD()
			elif returnValue is "com_052":
			    self.LOCALSKYSELECT4HD()
			elif returnValue is "com_053":
			    self.LOCALSKYSELECT5HD()
			elif returnValue is "com_054":
			    self.LOCALSKYSELECT6HD()
			elif returnValue is "com_055":
			    self.LOCALSKYSELECT7HD()
			elif returnValue is "com_056":                        	
			    self.LOCALSKYSELECT8HD()
			elif returnValue is "com_057":
			    self.LOCALSKYSELECT9HD()
			elif returnValue is "com_058":
			    self.SKYSELECT1HD()
			elif returnValue is "com_059":
			    self.SKYSELECT2HD()
			elif returnValue is "com_060":
			    self.SKYSELECT3HD()
			elif returnValue is "com_061":
			    self.SKYSELECT4HD()
			elif returnValue is "com_062":
			    self.SKYSELECT5HD()                            			    
			elif returnValue is "com_063":
			    self.SKYSELECT6HD()
			elif returnValue is "com_064":
			    self.SKYSELECT7HD()
			elif returnValue is "com_065":
			    self.SKYSELECT8HD()
			elif returnValue is "com_066":
			    self.SKYSELECT9HD()
			elif returnValue is "com_067":
			    self.SKYSELECT10HD() 
			elif returnValue is "com_068":
			    self.DAZN1HD()
			elif returnValue is "com_069": 
			    self.DAZN2HD()           	    
			elif returnValue is "com_1":
				cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree001', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_2":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree002', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_3":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree003', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_4":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree004', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_5":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree005', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_6":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree006', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_7":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree007', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_8":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree008', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_9":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree009', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_10":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree010', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_11":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree011', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_12":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree012', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_13":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree013', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_14":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree014', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_15":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree015', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_16":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree016', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_17":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree017', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_18":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree018', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_19":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree019', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_20":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree020', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_21":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree021', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_22":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree022', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_23":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree023', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_24":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree024', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_25":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV025.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree025', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_26":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree026', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_27":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree027', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_28":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV028.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree028', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_29":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree029', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_30":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree030', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_31":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV031.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree031', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_32":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV032.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree032', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_33":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV033.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree033', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_34":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV034.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree034', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_35":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV035.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree035', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_36":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV036.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree036', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_37":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV037.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree037', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_38":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV038.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree038', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_39":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV039.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree039', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_40":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV040.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree040', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_41":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV041.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree041', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_42":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV042.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree042', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_43":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV043.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree043', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_44":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV044.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree044', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_45":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV045.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree045', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_46":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV046.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree046', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_47":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601501.us.archive.org/12/items/freeiptv001/FreeIPTV047.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree047', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_48":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV048.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree048', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_49":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV049.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree049', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_50":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV050.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_51":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV051.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree051', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_052":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV052.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree052', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_53":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV053.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree053', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_54":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV054.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree054', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_55":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV055.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree055', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_56":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV056.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree056', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_57":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV057.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree057', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_58":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV058.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree058', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_59":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV059.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree059', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_60":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV060.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree060', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_61":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV061.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree061', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_62":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV062.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree062', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_63":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV063.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree063', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_64":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV064.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree064', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_65":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV065.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree065', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_66":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV066.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree066', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_67":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV067.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree067', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_68":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV068.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree068', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_69":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV069.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree069', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_70":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV070.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree070', cmdlist=cmdlist, finishedCallback=None)

			elif returnValue is "com_71":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV071.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree071', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_72":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV072.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree072', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_73":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV073.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree073', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_74":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV074.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree074', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_75":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV075.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree075', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_76":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV076.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree076', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_77":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV077.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree077', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_78":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV078.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree078', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_79":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV079.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree079', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_80":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV080.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree080', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_81":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV081.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree081', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_82":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV082.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree082', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_83":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV083.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree083', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_84":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV084.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree084', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_85":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV085.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree085', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_86":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV086.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree086', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_87":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV087.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree087', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_88":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV088.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree088', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_89":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV089.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree089', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_90":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV090.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree090', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_91":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV091.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree091', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_92":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV092.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree092', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_93":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV093.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree093', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_94":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV094.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree094', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_95":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV095.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree095', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_96":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV096.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree096', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_97":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV097.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree097', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_98":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV098.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree098', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_99":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV099.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree099', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_100":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV100.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree100', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_101":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV101.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree101', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_102":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV102.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree102', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_103":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV103.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree103', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_104":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV104.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree104', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_105":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV105.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree105', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_106":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV106.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree106', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_107":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV107.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree107', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_108":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV108.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree108', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_109":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV109.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree109', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_110":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV110.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree110', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_111":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV111.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree111', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_112":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV112.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree112', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_113":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV113.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree113', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_114":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV114.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree114', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_115":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV115.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree115', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_116":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV116.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree116', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_117":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV117.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree117', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_118":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV118.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree118', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_119":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV119.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree119', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_120":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV120.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree120', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_121":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV121.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree121', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_0122":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV122.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree122', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_123":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV123.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree123', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_124":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV124.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree124', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_125":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV125.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree125', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_126":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV126.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree126', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_127":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV127.sh  -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree127', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_128":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV128.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree128', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_129":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV129.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree129', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_130":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV130.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree130', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_131":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV131.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree131', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_132":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV132.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree132', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_133":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV133.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree133', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_134":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV134.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree134', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_135":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV135.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree135', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_136":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV136.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree136', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_137":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV137.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree137', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_138":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV138.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree138', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_139":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV139.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree139', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_140":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV140.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree140', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_141":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV144.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree141', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_142":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV142.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree142', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_143":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV143.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree143', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_144":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV144.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree144', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_145":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV145.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree145', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_146":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV146.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree146', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_147":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV147.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree147', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_148":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV148.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree148', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_149":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV149.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree149', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_150":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601405.us.archive.org/33/items/freeiptv_201911/FreeIPTV150.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree150', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_151":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_152":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_153":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_154":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_155":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_156":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_157":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_158":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_159":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_160":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_161":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_162":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR012.sh  -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD SMART TV', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_163":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_164":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR014.sh  -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_165":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_166":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_167":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_168":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_69":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_170":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_171":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_172":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_173":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_174":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_175":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR025.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_176":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_177":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_178":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR028.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_179":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_180":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_181":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR031.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_182":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR032.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_183":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR033.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_184":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR034.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_185":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR035.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_186":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR036.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_187":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR037.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_188":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR038.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_189":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR039.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_190":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR040.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_191":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR041.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_192":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR042.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_193":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR043.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_194":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR044.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_195":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR045.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_196":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR046.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_197":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR047.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_198":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR048.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_199":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR049.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_200":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR050.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_201":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR051.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_202":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR052.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_203":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR053.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_204":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR054.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_205":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR055.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_206":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR056.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_207":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR057.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_208":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR058.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_209":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR059.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_210":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR060.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_211":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR061.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_212":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR062.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_213":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR063.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_214":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR064.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_215":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR065.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_216":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR066.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_217":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR067.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_218":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR068.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_219":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR069.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_220":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR070.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_221":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR071.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_222":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR072.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_223":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR073.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_224":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR074.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_225":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR075.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_226":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR076.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_227":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR077.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_228":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR078.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_229":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR079.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_230":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR080.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_231":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR081.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_232":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR082.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_233":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR083.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_234":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR084.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_235":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR085.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_236":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR086.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_237":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR087.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_238":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR088.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_239":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR089.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_240":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR090.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='Free IPTVFree050', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_241":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR091.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_242":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR092.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_243":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR093.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_244":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR094.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_245":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR095.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_246":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR096.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_247":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR097.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_248":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR098.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_249":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR099.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_250":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601403.us.archive.org/4/items/iptvworldarb/IPTVWORLDAR100.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD ARABE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_251":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_252":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_253":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_254":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_255":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_256":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_257":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_258":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_259":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_260":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_261":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_262":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_263":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_264":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_265":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_266":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_267":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_268":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_269":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_270":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_271":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_272":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_273":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_274":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_275":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR025.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_276":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_277":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_278":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR028.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_279":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_280":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD FRANCE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_281":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR031.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_282":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR032.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_283":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR033.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_284":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR034.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_285":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR035.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_286":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR036.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_287":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR037.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_288":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR038.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_289":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR039.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_290":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR040.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD GREECE', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_291":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR041.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_292":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR042.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_293":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR043.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_294":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR044.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_295":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR045.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_296":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR046.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_297":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR047.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_298":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR048.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_299":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR049.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_300":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601409.us.archive.org/7/items/iptvworldfr/IPTVWORLDFR050.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD TURKEY', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_301":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_302":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_303":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_304":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_305":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_306":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_307":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_308":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_309":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_310":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_311":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_312":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_313":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_314":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_315":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDGR015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_316":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_317":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_318":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_319":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_320":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_321":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_322":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_323":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_324":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_325":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_326":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_327":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_328":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_329":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_330":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_331":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_332":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_333":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_334":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_335":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDTR020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_336":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_337":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_338":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_339":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_340":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_341":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_342":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_343":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_344":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_345":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_346":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_347":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_348":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_349":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_350":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_351":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_352":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_353":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_354":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_355":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_356":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_357":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_358":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_359":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_360":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS025.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_361":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_362":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_363":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS028.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_364":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_365":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_366":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLD0S031.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_367":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS032.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_368":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS033.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_369":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS034.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_370":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS035.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_371":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS036.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_372":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS037.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_373":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS038.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_374":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS039.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_375":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUS040.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_376":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_377":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_378":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_379":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_380":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_381":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_382":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_383":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_384":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_385":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_386":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_387":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_388":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_389":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_390":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_391":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_392":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_393":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_394":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_395":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_396":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_397":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_398":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_399":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_400":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU025.sh-qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_401":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_402":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_403":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU028.sh-qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_404":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_405":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRU030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_406":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)

			elif returnValue is "com_407":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_408":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_409":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_410":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_411":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_412":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_413":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_414":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_415":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_416":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_417":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_418":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_419":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_420":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_421":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_422":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_423":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_424":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_425":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_426":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_427":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_428":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_429":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_430":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD025.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_431":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_432":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_433":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD028.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_434":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_435":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_436":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD031.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_437":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD032.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_438":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD033.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_439":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD034.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_440":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD035.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_441":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD036.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_442":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD037.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_443":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD038.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_444":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD039.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_445":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD040.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_446":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD041.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_447":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD042.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_448":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD043.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_449":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD044.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_450":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD045.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_451":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD046.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_452":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD047.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_453":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD048.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_454":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD049.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_455":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD050.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_456":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD051.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_457":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD052.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_458":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD053.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_459":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD054.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_460":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD055.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_461":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD056.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_462":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD057.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_463":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD058.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_464":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD059.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_465":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia601500.us.archive.org/30/items/iptvworld015/IPTVWORLD060.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_466":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_467":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_468":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_469":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_470":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_471":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_472":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_473":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_474":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_475":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_476":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_477":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_478":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_479":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_480":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_481":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_482":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_483":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_484":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_485":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDDE020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_486":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_487":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_488":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_489":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_490":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_491":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_492":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_493":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_494":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_495":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDUK010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_496":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_497":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_498":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_499":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_500":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_501":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_502":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_503":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_504":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_505":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_506":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_507":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_508":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_509":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_510":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_511":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_512":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_513":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_514":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_515":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_516":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_517":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_518":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_519":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_520":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES025.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_521":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_522":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_523":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES028.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_524":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_525":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDES030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_526":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_527":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_528":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_529":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_530":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_531":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_532":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_533":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_534":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_535":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDYU010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_536":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_537":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_538":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_539":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_540":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_541":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_542":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_543":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_544":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_545":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDIT010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_546":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_547":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_548":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_549":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_550":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_551":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_552":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_553":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_554":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_555":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDPO010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_556":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_557":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_558":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_559":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_560":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_561":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_562":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_563":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_564":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_565":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAL010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_566":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_567":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_568":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_569":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_570":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_571":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_572":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_573":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_574":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_575":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDRO010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_576":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_577":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_578":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_579":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_580":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_581":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_582":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_583":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_584":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_585":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDBR010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_586":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_587":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_588":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_589":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_590":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_591":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_592":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_593":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_594":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_595":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_596":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_597":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_598":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_599":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_600":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDCA015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_601":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS001.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_602":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS002.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_603":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS003.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_604":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS004.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_605":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS005.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_606":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS006.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_607":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS007.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_608":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS008.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_609":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS009.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_610":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS010.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_611":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS011.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_612":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS012.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_613":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS013.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_614":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS014.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_615":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS015.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_616":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS016.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_617":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS017.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_618":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS018.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_619":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS019.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_620":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS020.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_621":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS021.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_622":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS022.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_623":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS023.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_624":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS024.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_625":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS025.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_626":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS026.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_627":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS027.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_628":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS028.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_629":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS029.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_630":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS030.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_631":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS031.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_632":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS032.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_633":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS033.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_634":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS034.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_635":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS035.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_636":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS036.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_637":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS037.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_638":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS038.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_639":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS039.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_640":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS040.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_641":
                        	cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS041.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_642":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS042.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_643":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS043.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_644":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS044.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_645":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS045.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_646":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS046.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_647":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS047.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_648":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS048.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_649":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS049.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_650":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS050.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV WORLD', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_651":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS051.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_652":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS052.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_653":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS053.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_654":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'") 
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS054.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_655":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS055.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_656":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS056.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_657":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS057.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_658":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")    
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS058.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_659":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS059.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			elif returnValue is "com_660":
				cmdlist = []
				cmdlist.append("%s -qO - '" % self.wget + "'")
				cmdlist.append("%s https://ia801409.us.archive.org/29/items/iptvworld_201911/IPTVWORLDAS060.sh -qO - | /bin/sh" % self.wget)
				self.session.open(Consolo, title='IPTV USA', cmdlist=cmdlist, finishedCallback=None)
			else:
				print "\n[MyShPrombt] cancel\n"
				self.close(None)

	def Update(self):
	    Update = "afile"
	    afile = open('/tmp/monfichier.txt', 'w')
	    self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + str(Update) + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)

	def RMCHD1(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar  	    
            #url01="http://iptvpro.premium-itv.com:8789/live/31031986/31031986/32718.m3u8"  
            #url01="http://skdn.redi-vo.com/iptv/ch255?code=103131497823984&key=43852"           
            #url01="http://live.redfhd.com:8000/live/cemal/sakarya54/1729.m3u8" 
            url01="http://vvn.neoredi.com/iptv/ch255?code=1501309316704233&key=23296"
            #url01="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33365.m3u8" 
            #url01="http://www.sansat.net:25461/bRRMEeD4n5/7F09Vz4zRp/49213" 
	    #url01="http://iptvoffshore.com:80/2806892/8940691/10527" 
	    #url01="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1216.ts"
            #url01="http://linux-app.tv:6204/live/mustafa96/mustafa96/14046.m3u8"            
            #url01="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33365.m3u8" 
            #url01="http://topiptv.net:5890/live/1234567/12345/601.m3u8"
            #url01="http://showflix.org:5890/live/1234567/12345/601.m3u8"
            #url01="http://topiptv.net:5890/live/1234567/12345/601.m3u8"  
	    ref = eServiceReference(4097, 0, url01)
	    ref.setName(Name_001)
	    self.session.open(MoviePlayer, ref)
	def RMCHD2(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url02="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1264.ts"  
            #url01="http://skdn.redi-vo.com/iptv/ch253?code=103131497823984&key=43971"
	    #url02="http://iptvoffshore.com:80/2806892/8940691/341"
	    #url02="http://live.redfhd.com:8000/live/cemal/sakarya54/1728.m3u8"
	    url02="http://vvn.neoredi.com/iptv/ch253?code=1501309316704233&key=54264"
	    #url02="http://iptv-luxe.com:8789/live/1212/1212/29823.m3u8"
	    #url02="http://iptv-luxe.com:8789/live/1212/1212/29823.m3u8"
	    #url02="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33364.m3u8"
	    #url02="http://iptvpro.premium-itv.com:8789/live/31031986/31031986/32714.m3u8"
	    #url02="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39502.m3u8"
	    #url02="http://tv2iptv.com:8000/live/Faysal/faysal123/30614.m3u8"
	    #url02="http://tv.sigma-net.co:6500/live/q7iDM0wsgh/42xjrPv0tB/26130.m3u8"	    
	    #url02="http://linux-app.tv:6204/live/mustafa96/mustafa96/14045.m3u8"
	    #url02="http://topiptv.net:5890/live/1234567/12345/603.m3u8"
	    ref = eServiceReference(4097, 0, url02)
	    ref.setName(Name_002)
	    self.session.open(MoviePlayer, ref)  
	def RMCHD3(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar 
	    #url03="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33363.m3u8"
	    #url03="http://skdn.redi-vo.com/iptv/ch254?code=103131497823984&key=13496"
	    #url03="http://iptv7.premium-stv.com:25461/rmcsport3/1557539943/58"
	    #url03="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39501.m3u8"
	    #url03="http://iptv-luxe.com:8789/live/1212/1212/29824.m3u8"
	    #url03="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33363.m3u8"
	    #url03="http://iptv-luxe.com:8789/live/1212/1212/29824.m3u8"
	    #url03="http://linux-app.tv:6204/live/mustafa96/mustafa96/14044.m3u8"
            #url03="http://showflix.org:5890/live/1234567/12345/605.m3u8"            
	    #url03="http://live.redfhd.com:8000/live/cemal/sakarya54/1739.m3u8"     
	    url03="http://vvn.neoredi.com/iptv/ch253?code=1501309316704233&key=31480"	    
	    ref = eServiceReference(4097, 0, url03)
	    ref.setName(Name_003)
	    self.session.open(MoviePlayer, ref)
	def RMCHD4(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url04="http://linux-app.tv:6204/live/mustafa96/mustafa96/14043.m3u8" 
	    #url04="http://www.sansat.net:25461/zbuyen95/JZ1jh5CJV5/42338"
	    #url04="http://iptv-luxe.com:8789/live/1212/1212/29825.m3u8"
	    #url04="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1270.ts"
            #url04="http://showflix.org:5890/live/1234567/12345/607.m3u8"
	    #url04="http://iptv-luxe.com:8789/live/1212/1212/16099.m3u8"
	    #url04="http://live.redfhd.com:8000/live/cemal/sakarya54/38798.m3u8"
	    #url04="http://skdn.redi-vo.com/iptv/ch243?code=103131497823984&key=62334"
	    #url04="http://iptv6.premium-stv.com:25461/sourcefrhevcpro1/0493432475/3312"
	    #url04="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/27343.m3u8"
	    #url04="http://topiptv.net:5890/live/1234567/12345/607.m3u8" 
	    url04="http://vvn.neoredi.com/iptv/ch243?code=1501309316704233&key=15110"  
	    ref = eServiceReference(4097, 0, url04)
	    ref.setName(Name_004)
	    self.session.open(MoviePlayer, ref)   
	def BeinFRHD1(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url05="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1287.ts"	    
	    #url05="http://showflix.org:5890/live/1234567/12345/58334.m3u8"            
	    #url05="http://iptv-luxe.com:8789/live/1212/1212/10531.m3u8"
	    url05="http://skdn.redi-vo.com/iptv/ch119?code=138137164006399&key=56827"
	    #url05="http://s1.niacam.net:24621/mtg_2406_1/IyBf86mT158!1/397"	    
	    #url05="http://live.redfhd.com:8000/live/cemal/sakarya54/115.m3u8" 
	    #url05="http://skdn.redi-vo.com/iptv/ch119?code=103131497823984&key=62807"
	    #url05="http://nvkdn.redi-vo.com/iptv/ch119?code=1701273726237058&key=50356"
	    #url05="http://iptv6.premium-stv.com:25461/pro1turc/bhXdd32sd1g/1459"	    
	    #url05="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39499.m3u8"	    
	    #url05="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1287.ts"	    
	    #url05="http://linux-app.tv:6204/live/mustafa96/mustafa96/28371.m3u8"
            #url05="http://iptv-luxe.com:8789/live/1212/1212/29819.m3u8"
            #url05="http://iptv-luxe.com:8789/live/1212/1212/29819.m3u8"
	    ref = eServiceReference(4097, 0, url05)
	    ref.setName(Name_1)
	    self.session.open(MoviePlayer, ref)
	def BeinFRHD2(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url06="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1288.ts"	 
	    #url06="http://iptv-luxe.com:8789/live/1212/1212/29820.m3u8"
	    #url06="http://iptv6.premium-stv.com:25461/pro1turc/bhXdd32sd1g/1458"
	    #url06="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33380.m3u8"
            url06="http://vvn.neoredi.com/iptv/ch120?code=1501309316704233&key=51185"	
            #url06="http://live.redfhd.com:8000/live/cemal/sakarya54/114.m3u8"    
	    #url06="http://skdn.redi-vo.com/iptv/ch120?code=103131497823984&key=38010"
	    #url06="http://nvkdn.redi-vo.com/iptv/ch120?code=1701273726237058&key=51185"
	    #url06="http://www.sansat.net:25461/bRRMEeD4n5/7F09Vz4zRp/49230"
	    #url06="http://linux-app.tv:6204/live/mustafa96/mustafa96/28372.m3u8"
	    #url06="http://iptv-luxe.com:8789/live/1212/1212/29820.m3u8"
	    #url06="http://showflix.org:5890/live/1234567/12345/588.m3u8"   
            #url06="http://iptv-luxe.com:8789/live/1212/1212/10530.m3u8"	    
	    ref = eServiceReference(4097, 0, url06)
	    ref.setName(Name_2)
	    self.session.open(MoviePlayer, ref) 
	def BeinFRHD3(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url07="http://skdn.redi-vo.com/iptv/ch206?code=103131497823984&key=26341"	 
	    #url07="http://iptv6.premium-stv.com:25461/pro1turc/bhXdd32sd1g/1457"
	    #url07="http://nvkdn.redi-vo.com/iptv/ch120?code=1701273726237058&key=11755"
	    url07="http://vvn.neoredi.com/iptv/ch120?code=1501309316704233&key=11755"
	    #url07="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/27340.m3u8"
	    #url07="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/39497.m3u8"
	    #url07="http://www.sansat.net:25461/bRRMEeD4n5/7F09Vz4zRp/49231"
	    #url07="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33379.m3u8"
	    #url07="http://linux-app.tv:6204/live/mustafa96/mustafa96/28373.m3u8"
	    #url07="http://iptv-luxe.com:8789/live/1212/1212/29821.m3u8"
	    #url07="http://showflix.org:5890/live/1234567/12345/590.m3u8"   
            #url07="http://iptv-luxe.com:8789/live/1212/1212/10529.m3u8"	    
	    ref = eServiceReference(4097, 0, url07)
	    ref.setName(Name_3)
	    self.session.open(MoviePlayer, ref)
	def BeinHD1(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url1="http://showflix.org:5890/Mohamed/1234567/16"	    
            #url1="http://95.170.215.101:80/hls/m3u8/Bein-S1-a58.m3u8"
	    #url1="http://dreamtv.v90.co:2095/KASS0102/n4FhD5Id8E/52"
	    #url1="http://skdn.redi-vo.com/iptv/ch111?code=103131497823984&key=54576"
	    #url1="http://iptvpro.vision-new.org:8789/1212/1212/10517"
	    #url1="http://95.154.194.84:8000/live/DlrSUqOZ2k/lFcKAenHiB/32098.m3u8"
            #url1="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2140"
	    ref = eServiceReference(4097, 0, url1)
	    ref.setName(Name_01)
	    self.session.open(MoviePlayer, ref)
	def BeinHD2(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url2="http://iptvpro.vision-new.org:8789/1212/1212/10516"	    
	    url2="http://showflix.org:5890/Mohamed/1234567/17"
	    #url2="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32097.m3u8"
	    #url2="http://skdn.redi-vo.com/iptv/ch112?code=103131497823984&key=46098"
	    #url2="http://iptv9211.hopto.me:8000/nfzNlANvf2/HHfWU3dzWt/32097"
            #url2="http://95.154.194.84:8000/live/DlrSUqOZ2k/lFcKAenHiB/32097.m3u8"
            #url2="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2139"	    
	    ref = eServiceReference(4097, 0, url2)
	    ref.setName(Name_02)
	    self.session.open(MoviePlayer, ref)
	def BeinHD3(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url3="http://showflix.org:5890/Mohamed/1234567/18"
	    #url3="http://skdn.redi-vo.com/iptv/ch113?code=103131497823984&key=39255"
            #url3="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2138"
            #url3="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32096.m3u8"	
            #url3="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2137"   
	    ref = eServiceReference(4097, 0, url3)
	    ref.setName(Name_03)
	    self.session.open(MoviePlayer, ref) 
	def BeinHD4(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url4="http://showflix.org:5890/Mohamed/1234567/19"
	    #url4="http://skdn.redi-vo.com/iptv/ch114?code=103131497823984&key=46165"
	    #url4="http://premiumplustv.com:8000/live/user938303/G26ZM4L1gY/81759.m3u8"
            #url4="http://tv2iptv.com:8000/live/Faysal/faysal123/32.m3u8"
            #url4="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32095.m3u8"
            #url4="http://iptv-luxe.com:8789/1212/1212/11176"
            #url4="http://iptvpro.vision-new.org:8789/1212/1212/11178"	    
	    ref = eServiceReference(4097, 0, url4)
	    ref.setName(Name_04)
	    self.session.open(MoviePlayer, ref)
	def BeinHD5(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url5="http://showflix.org:5890/Mohamed/1234567/20"
	    #url5="http://skdn.redi-vo.com/iptv/ch115?code=103131497823984&key=45992"
            #url5="http://xtiptv.xyz:25461/live/PYGj0mbvYI/4fceOZuE1c/55899.ts"
            #url5="http://95.154.194.84:8000/live/DlrSUqOZ2k/lFcKAenHiB/32094.m3u8"
            #url5="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32094.m3u8"
            #url5="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2136"	 
            #url5="http://iptvpro.vision-new.org:8789/1212/1212/11176"  
	    ref = eServiceReference(4097, 0, url5)
	    ref.setName(Name_05)
	    self.session.open(MoviePlayer, ref)
	def BeinHD6(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url6="http://showflix.org:5890/Mohamed/1234567/21"
	    #url6="http://skdn.redi-vo.com/iptv/ch116?code=103131497823984&key=57392"
	    #url6="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2135"
            #url6="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32093.m3u8"
            #url6="http://iptv-luxe.com:8789/1212/1212/11172"
            #url6="http://iptvpro.vision-new.org:8789/1212/1212/11174"	    
	    ref = eServiceReference(4097, 0, url6)
	    ref.setName(Name_06)
	    self.session.open(MoviePlayer, ref)
	def BeinHD7(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url7="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2134"
	    url7="http://showflix.org:5890/Mohamed/1234567/22"
	    #url7="http://skdn.redi-vo.com/iptv/ch117?code=103131497823984&key=58844"
	    #url7="http://beryantv.com:25461/02410251710104/02410251710104/824"
            #url7="http://iptv-luxe.com:8789/1212/1212/11170"
            #url7="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32092.m3u8"	 
            #url7="http://iptvpro.vision-new.org:8789/1212/1212/11172" 
	    ref = eServiceReference(4097, 0, url7)
	    ref.setName(Name_07)
	    self.session.open(MoviePlayer, ref)
	def BeinHD8(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url8="http://showflix.org:5890/Mohamed/1234567/23"
	    #url8="http://skdn.redi-vo.com/iptv/ch118?code=103131497823984&key=43336"
            #url8="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2133"
            #url8="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1264.ts"	
            #url8="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32091.m3u8"   
            #url8="http://iptvpro.vision-new.org:8789/1212/1212/11170"
	    ref = eServiceReference(4097, 0, url8)
	    ref.setName(Name_08)
	    self.session.open(MoviePlayer, ref)
	def BeinHD9(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url9="http://iptvpro.premium-itv.com:8789/ahmed/1234/32718"
	    #url9="http://skdn.redi-vo.com/iptv/ch510?code=103131497823984&key=27398"
            #url9="http://iptv-luxe.com:8789/live/1212/1212/29822.m3u8"
            #url9="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2132"	
            #url9="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1287.ts" 
            #url9="http://iptvpro.vision-new.org:8789/1212/1212/11168"  
	    ref = eServiceReference(4097, 0, url9)
	    ref.setName(Name_09)
	    self.session.open(MoviePlayer, ref)
	def BeinHD10(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url10="http://iptvpro.premium-itv.com:8789/ahmed/1234/92"
	    #url10="http://skdn.redi-vo.com/iptv/ch511?code=103131497823984&key=51278"
            #url10="http://skdn.redi-vo.com/iptv/ch255?code=103131497823984&key=43852"
            #url10="http://iptv-luxe.com:8789/live/1212/1212/92.m3u8"
            #url10="http://iptvpro.vision-new.org:8789/1212/1212/10508"
            #url10="http://mu02.v2iptv.com:8880/HJLM1399/gOQedvLAFg/2131"
            #url10="http://best-servers.xyz:8000/3505832905415/3046728127636/14808"
            #url10="http://iptvpro.vision-new.org:8789/1212/1212/11166"  	    
	    ref = eServiceReference(4097, 0, url10)
	    ref.setName(Name_10)
	    self.session.open(MoviePlayer, ref)
	def BeinHD11(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url11="http://skdn.redi-vo.com/iptv/ch202?code=103131497823984&key=22881"
	    #url11="http://universeiptv.com:8000/live/alexaiptv/hvsfw2yfgwu/853.m3u8"
	    #url11="http://universeiptv.com:8000/alexaiptv/hvsfw2yfgwu/853"
	    #url11="http://nvkdn.redi-vo.com/iptv/ch202?code=1701273726237058&key=50378"	    
	    #url11="http://topiptv.net:5890/live/1234567/12345/553.m3u8"
            #url11="http://iptv-luxe.com:8789/live/1212/1212/17404.m3u8"
            #url11="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32088.m3u8"  
            #url11="http://topiptv.net:5890/live/1234567/12345/58334.m3u8"       
            url11="http://vvn.neoredi.com/iptv/ch203?code=1501309316704233&key=15169"	    
	    ref = eServiceReference(4097, 0, url11)
	    ref.setName(Name_11)
	    self.session.open(MoviePlayer, ref)
	def DAZN1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar	    
	    #url12="http://iptv.iptivihd.com:8000/live/cemal/sakarya54/22499.m3u8"
            url12="http://showflix.org:5890/Mohamed/1234567/1266"
            #url12="http://iptvsmarters.cc:25461/live/serkan/yilmaz/1951.ts"
            #url12="http://hemn2.xyz:8000/live/6PlHOlmM7a/gfKgQfpWED/10582.m3u8"
            #url12="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/257.m3u8"
            #url12="http://primeplus.tv:8080/YMq12IOMMi/XqJX8Mfx0i/16319" 
            #url12="http://s.igiptv.com:8000/live/abbas/112233/25652.m3u8"  
            #url12="http://linux-app.tv:6204/live/mustafa96/mustafa96/28357.m3u8" 
            #url12="http://62.210.92.2:25461/151515/151515/14378"                  	    
            #url12="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/299" 
	    ref = eServiceReference(4097, 0, url12)
	    ref.setName(Name_12)
	    self.session.open(MoviePlayer, ref)
	def DAZN2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url13="http://tv2iptv.com:8000/live/Faysal/faysal123/25653.m3u8"
            #url13="http://primeplus.tv:8080/YMq12IOMMi/XqJX8Mfx0i/16319" 
	    #url13="http://linux-app.tv:6204/live/mustafa96/mustafa96/28358.m3u8"
	    url13="http://showflix.org:5890/Mohamed/1234567/1267"
            #url13="http://iptv.iptivihd.com:8000/live/cemal/sakarya54/22500.m3u8"
	    #url13="http://turkiptv.xyz:8080/live/elena/Elena123/126970.m3u8"
            #url13="http://tv2iptv.com:8000/live/Faysal/faysal123/25652.m3u8"  
	    #url13="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2675.m3u8"
            #url13="http://topiptv.net:5890/tom01/01tom/1267"
            #url13="http://turkiptv.xyz:8080/live/elena/Elena123/126969.m3u8"	    
	    ref = eServiceReference(4097, 0, url13)
	    ref.setName(Name_13)
	    self.session.open(MoviePlayer, ref)	 
	def SKYSELECTHD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url14="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/32010.m3u8"
	    #url14="http://nvkdn.redi-vo.com/iptv/ch309?code=1701273726237058&key=16856"
            url14="http://skdn.redi-vo.com/iptv/ch309?code=103131497823984&key=19118"
            #url14="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/484.m3u8"	    
	    ref = eServiceReference(4097, 0, url14)
	    ref.setName(Name_14)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar    	    
	    #url15="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46474.m3u8" 	    
	    #url15="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17285.m3u8"
	    #url15="http://ipturkhd.biz:8000/berkbayrak/ZbwOXE1bH1/117"            	    
	    url15="http://live.redfhd.com:8000/live/cemal/sakarya54/391.m3u8"
            #url15="http://client.era-iptv.net:25461/live/Londoncafe9r8rutve/Od8e7rnsodid/1321.m3u8"	    
	    ref = eServiceReference(4097, 0, url15)
	    ref.setName(Name_15)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url16="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46473.m3u8"
            #url16="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17286.m3u8"
            #url16="http://iptv6.premium-stv.com:25461/sourcegermanypro2/0626674936/2814"
            url16="http://live.redfhd.com:8000/live/cemal/sakarya54/392.m3u8"	    
            #url16="http://vip.akiptv.biz:8000/live/faruk1/19012019/1050.ts"	    
	    ref = eServiceReference(4097, 0, url16)
	    ref.setName(Name_16)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT3HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url17="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46472.m3u8"
	    url17="http://live.redfhd.com:8000/live/cemal/sakarya54/393.m3u8"
	    #url17="http://z.iptvsubscription.org:80/live/2ucpNdKgqy/La1LlABcKd/17286.m3u8"
	    #url17="http://s.igiptv.com:8000/live/abbas/112233/23672.m3u8"
	    #url17="http://client.era-iptv.net:25461/live/Londoncafe9r8rutve/Od8e7rnsodid/1319.m3u8"
            #url17="http://vip.akiptv.biz:8000/live/faruk1/19012019/1051.ts"	    
	    ref = eServiceReference(4097, 0, url17)
	    ref.setName(Name_17)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT4HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url18="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46471.m3u8"
	    #url18="http://uye.performlive.de:80/KeremOzt/rvMUJqR5Lp/47834"
	    url18="http://live.redfhd.com:8000/live/cemal/sakarya54/394.m3u8"
	    #url18="http://s.igiptv.com:8000/live/abbas/112233/23673.m3u8"
            #url18="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17288.m3u8"	    
	    ref = eServiceReference(4097, 0, url18)
	    ref.setName(Name_18)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT5HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url19="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46470.m3u8"
	    url19="http://nvkdn.redi-vo.com/iptv/ch300?code=1701273726237058&key=15080"
	    #url19="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17289.m3u8"
            #url19="http://tv2iptv.com:8000/live/badr/badr1234/23675.m3u8"	    
	    ref = eServiceReference(4097, 0, url19)
	    ref.setName(Name_19)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT6HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url20="http://95.154.194.14:8000/live/LeGdi1tigB/DpYUNmaI8b/46472.m3u8"
	    url20="http://nvkdn.redi-vo.com/iptv/ch301?code=1701273726237058&key=44930"
	    #url20="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46469.m3u8"
            #url20="http://turkiptv.xyz:8080/live/elena/Elena123/126965.m3u8"
            #url20="http://s.igiptv.com:8000/live/abbas/112233/23675.m3u8" 
            #url20="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17290.m3u8"	    
	    ref = eServiceReference(4097, 0, url20)
	    ref.setName(Name_20)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT7HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url21="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32013.m3u8"
	    #url21="http://uye.performlive.de:80/KeremOzt/rvMUJqR5Lp/47838"
	    url21="http://nvkdn.redi-vo.com/iptv/ch302?code=1701273726237058&key=18944"
            #url21="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17291.m3u8"	    
	    ref = eServiceReference(4097, 0, url21)
	    ref.setName(Name_21)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT8HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url22="http://nvkdn.redi-vo.com/iptv/ch303?code=1701273726237058&key=49632"
	    #url22="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32010.m3u8"
	    #url22="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17292.m3u8"
	    #url22="http://turkiptv.xyz:8080/live/elena/Elena123/126963.m3u8"
            #url22="http://bestiptv2.premium-tv.info:8789/live/Naji_Derouiche/igaYR6PAtq/23728.m3u8"
            #url22="http://vip.akiptv.biz:8000/live/faruk1/19012019/1056.ts"	    
	    ref = eServiceReference(4097, 0, url22)
	    ref.setName(Name_22)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT9HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url23="http://nvkdn.redi-vo.com/iptv/ch304?code=1701273726237058&key=27939"
	    #url23="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/32011.m3u8"
	    #url23="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32014.m3u8"
	    #url23="http://z.iptvsubscription.org:80/live/2ucpNdKgqy/La1LlABcKd/17293.m3u8"   
            #url23="http://iptvpro.premium-itv.com:8789/live/31031986/31031986/13955.m3u8"	    
	    ref = eServiceReference(4097, 0, url23)
	    ref.setName(Name_23)
	    self.session.open(MoviePlayer, ref)	              
	def MOVIES1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url24="http://skdn.redi-vo.com/iptv/ch301?code=138137164006399&key=55050"	    
	    #url24="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33437.m3u8"
            #url24="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/13925.m3u8"	
            #url24="http://iptv-luxe.com:8789/live/1212/1212/213.m3u8"    
	    ref = eServiceReference(4097, 0, url24)
	    ref.setName(Name_24)
	    self.session.open(MoviePlayer, ref)
	def MOVIES2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar	    
	    #url25="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33436.m3u8"
	    #url25="http://iptv-luxe.com:8789/live/1212/1212/178.m3u8"
            #url25="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/13924.m3u8"	
            url25="http://skdn.redi-vo.com/iptv/ch300?code=138137164006399&key=50699"    
	    ref = eServiceReference(4097, 0, url25)
	    ref.setName(Name_25)
	    self.session.open(MoviePlayer, ref)
	def MOVIES3HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url26="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33435.m3u8"
	    #url26="http://iptv-luxe.com:8789/live/1212/1212/176.m3u8"
	    #url26="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/13923.m3u8"
            #url26="http://95.154.194.84:8000/live/rnvfRzOVx9/154ptVEGQR/33449.m3u8"	
            url26="http://skdn.redi-vo.com/iptv/ch302?code=138137164006399&key=10731"    
	    ref = eServiceReference(4097, 0, url26)
	    ref.setName(Name_26)
	    self.session.open(MoviePlayer, ref)
	def MOVIES4HD(self):	
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url27="http://iptv-luxe.com:8789/live/1212/1212/175.m3u8"
	    #url27="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33434.m3u8"
            #url27="http://95.154.194.84:8000/live/rnvfRzOVx9/154ptVEGQR/33448.m3u8"
            url27="http://skdn.redi-vo.com/iptv/ch303?code=138137164006399&key=34841"	    
	    ref = eServiceReference(4097, 0, url27)
	    ref.setName(Name_27)
	    self.session.open(MoviePlayer, ref)
	def MOVIES5HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url28="http://senadi.mine.nu:8000/live/O5ckVk7U1C/K91jSvYCeA/1271.ts"
            #url28="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33433.m3u8"	    
	    #url28="http://iptv-luxe.com:8789/live/1212/1212/174.m3u8"       
            #url28="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/13921.m3u8"	
            url28="http://skdn.redi-vo.com/iptv/ch304?code=138137164006399&key=11003"    
	    ref = eServiceReference(4097, 0, url28)
	    ref.setName(Name_28)
	    self.session.open(MoviePlayer, ref)
	def MOVIES6HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url29="http://iptv-luxe.com:8789/live/1212/1212/173.m3u8"
            #url29="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33432.m3u8"
            #url29="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/13920.m3u8"
            url29="http://skdn.redi-vo.com/iptv/ch305?code=138137164006399&key=60741" 	    
	    ref = eServiceReference(4097, 0, url29)
	    ref.setName(Name_29)
	    self.session.open(MoviePlayer, ref)
	def MOVIES7HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url30="http://iptv-luxe.com:8789/live/1212/1212/172.m3u8"
	    url30="http://skdn.redi-vo.com/iptv/ch306?code=138137164006399&key=56105"
	    #url30="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33431.m3u8"
	    #url30="http://iptvpro.premium-tv.media:8789/live/francesdclark/MJ5jwjknJA/13919.m3u8"   
	    ref = eServiceReference(4097, 0, url30)
	    ref.setName(Name_30)
	    self.session.open(MoviePlayer, ref)
	def MOVIES8HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url31="http://iptv-luxe.com:8789/live/1212/1212/171.m3u8"
            url31="http://skdn.redi-vo.com/iptv/ch307?code=138137164006399&key=53101"
            #url31="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33430.m3u8"
            #url31="http://iptvpro.premium-itv.com:8789/live/31031986/31031986/13969.m3u8"	    
	    ref = eServiceReference(4097, 0, url31)
	    ref.setName(Name_31)
	    self.session.open(MoviePlayer, ref)
	def MOVIES9HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url32="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33429.m3u8"
	    #url32="http://iptv-luxe.com:8789/live/1212/1212/170.m3u8"
	    url32="http://skdn.redi-vo.com/iptv/ch308?code=138137164006399&key=32595"
            #url32="http://iptvpro.premium-itv.com:8789/live/31031986/31031986/13969.m3u8"	    
	    ref = eServiceReference(4097, 0, url32)
	    ref.setName(Name_32)
	    self.session.open(MoviePlayer, ref)	
	def ALACARTE1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar 	    
	    #url33="http://linux-app.tv:6204/live/mustafa96/mustafa96/8090.m3u8"   
	    url33="http://vvn.neoredi.com/iptv/ch300?code=1501309316704233&key=15080"
	    #url33="http://nvkdn.redi-vo.com/iptv/ch300?code=1701273726237058&key=15080" 
	    #url33="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/494.m3u8"
            #url33="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33451.m3u8"
            #url33="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33451.m3u8"	    
	    ref = eServiceReference(4097, 0, url33)
	    ref.setName(Name_33)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url34="http://linux-app.tv:6204/live/mustafa96/mustafa96/8089.m3u8"
	    url34="http://vvn.neoredi.com/iptv/ch301?code=1501309316704233&key=44930"	    
	    #url34="http://nvkdn.redi-vo.com/iptv/ch302?code=1701273726237058&key=18944"
            #url34="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33450.m3u8"	
            #url34="http://tv.sigma-iptv.com:7000/live/45905/13543107/5672.m3u8"    
	    ref = eServiceReference(4097, 0, url34)
	    ref.setName(Name_34)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE3HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url35="http://linux-app.tv:6204/live/mustafa96/mustafa96/8088.m3u8"
	    url35="http://vvn.neoredi.com/iptv/ch301?code=1501309316704233&key=44944"
            #url35="http://nvkdn.redi-vo.com/iptv/ch302?code=1701273726237058&key=18944"
            #url35="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33449.m3u8"	
            #url35="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33449.m3u8"    
	    ref = eServiceReference(4097, 0, url35)
	    ref.setName(Name_35)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE4HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url36="http://vvn.neoredi.com/iptv/ch303?code=1501309316704233&key=49632"
	    #url36="http://nvkdn.redi-vo.com/iptv/ch303?code=1701273726237058&key=49632"
	    #url36="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33448.m3u8"
            #url36="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33448.m3u8"
            #url36="http://premiumplustv.com:8000/user938303/G26ZM4L1gY/88156"	    
	    ref = eServiceReference(4097, 0, url36)
	    ref.setName(Name_36)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE5HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url37="http://linux-app.tv:6204/live/mustafa96/mustafa96/8086.m3u8"
	    url37="http://vvn.neoredi.com/iptv/ch303?code=1501309316704233&key=27939"
	    #url37="http://nvkdn.redi-vo.com/iptv/ch304?code=1701273726237058&key=27939"
            #url37="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/498.m3u8"
            #url37="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33437.m3u8"	    
	    ref = eServiceReference(4097, 0, url37)
	    ref.setName(Name_37)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE6HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url38="http://vvn.neoredi.com/iptv/ch305?code=1501309316704233&key=45527"
            #url38="http://nvkdn.redi-vo.com/iptv/ch305?code=1701273726237058&key=45527"
            #url38="http://185.23.213.162:8789/live/ania/ania/13953.m3u8"	
            #url38="http://premiumplustv.com:8000/user938303/G26ZM4L1gY/88158"    
	    ref = eServiceReference(4097, 0, url38)
	    ref.setName(Name_38)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE7HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url39="http://welliptv.net:2507/walid_665395/3AGjjDnf/6928"
	    url39="http://vvn.neoredi.com/iptv/ch305?code=1501309316704233&key=50185"
	    #url39="http://nvkdn.redi-vo.com/iptv/ch307?code=1701273726237058&key=33489"
            #url39="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33433.m3u8"   
	    ref = eServiceReference(4097, 0, url39)
	    ref.setName(Name_39)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE8HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url40="http://vvn.neoredi.com/iptv/ch307?code=1501309316704233&key=33489"
	    #url40="http://nvkdn.redi-vo.com/iptv/ch306?code=1701273726237058&key=50185"
            #url40="http://tvpro.millenium-ott.com:25443/live/corine/123456/9361.m3u8"
            #url40="http://tv2iptv.com:8000/live/Faysal/faysal123/30667.m3u8"            	    
	    #url42="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/484.m3u8"
	    #url40="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/495.m3u8"
	    #url40="http://topiptv.net:5890/live/1234567/12345/696.m3u8"
            #url40="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33456.m3u8"	    
	    ref = eServiceReference(4097, 0, url40)
	    ref.setName(Name_40)
	    self.session.open(MoviePlayer, ref)
	def ALACARTE9HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url41="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/493.m3u8"	    
	    #url41="http://185.23.213.162:8789/live/ania/ania/13967.m3u8"
	    #url41="http://nvkdn.redi-vo.com/iptv/ch308?code=1701273726237058&key=41851"
            url41="http://vvn.neoredi.com/iptv/ch307?code=1501309316704233&key=41851"	    
	    ref = eServiceReference(4097, 0, url41)
	    ref.setName(Name_41)
	    self.session.open(MoviePlayer, ref)	
	def CANALPLAY1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            url42="http://vvn.neoredi.com/iptv/ch309?code=1501309316704233&key=16856"
	    #url42="http://iptv-luxe.com:8789/live/1212/1212/165.m3u8"
	    #url42="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33456.m3u8"
            #url42="http://185.233.185.248:25443/live/corine/123456/28269.m3u8"	    
	    ref = eServiceReference(4097, 0, url42)
	    ref.setName(Name_42)
	    self.session.open(MoviePlayer, ref)
	def CANALPLAY2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url43="http://topiptv.net:5890/live/1234567/12345/700.m3u8"
	    #url43="http://iptv-luxe.com:8789/live/1212/1212/166.m3u8"
	    #url43="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33455.m3u8"
	    #url43="http://iptv9211.hopto.me:8000/live/DlrSUqOZ2k/lFcKAenHiB/33455.m3u8"
            #url43="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/485.m3u8"
            url43="http://vvn.neoredi.com/iptv/ch309?code=1501309316704233&key=15080"	    
	    ref = eServiceReference(4097, 0, url43)
	    ref.setName(Name_43)
	    self.session.open(MoviePlayer, ref)
	def CANALPLAY3HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url44="http://topiptv.net:5890/live/1234567/12345/701.m3u8"
	    #url44="http://iptv-luxe.com:8789/live/1212/1212/166.m3u8"
	    #url44="http://iptv-luxe.com:8789/live/1212/1212/169.m3u8"
	    #url44="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33454.m3u8"
	    #url44="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33454.m3u8"
            url44="http://nvkdn.redi-vo.com/iptv/ch301?code=1701273726237058&key=44930"	    
	    ref = eServiceReference(4097, 0, url44)
	    ref.setName(Name_44)
	    self.session.open(MoviePlayer, ref)
	def CANALPLAY4HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url45="http://topiptv.net:5890/live/1234567/12345/702.m3u8"
	    #url45="http://iptv-luxe.com:8789/live/1212/1212/168.m3u8"
	    #url45="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/33453.m3u8"
	    #url45="http://iptv-luxe.com:8789/live/1212/1212/168.m3u8"
	    url45="http://nvkdn.redi-vo.com/iptv/ch301?code=1701273726237058&key=18944"
            #url45="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33453.m3u8"	    
	    ref = eServiceReference(4097, 0, url45)
	    ref.setName(Name_45)
	    self.session.open(MoviePlayer, ref)
	def CANALPLAY5HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            #url46="http://topiptv.net:5890/live/1234567/12345703.m3u8"
	    #url46="http://iptv-luxe.com:8789/live/1212/1212/167.m3u8"
	    #url46="http://iptv-luxe.com:8789/live/1212/1212/167.m3u8"
	    #url46="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33452.m3u8"
	    #url46="http://premiumplustv.com:8000/user938303/G26ZM4L1gY/88200"
            #url46="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/488.m3u8"
            url46="http://nvkdn.redi-vo.com/iptv/ch303?code=1701273726237058&key=49632"	    
	    ref = eServiceReference(4097, 0, url46)
	    ref.setName(Name_46)
	    self.session.open(MoviePlayer, ref)
	def CANALPLAY6HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            url47="http://nvkdn.redi-vo.com/iptv/ch304?code=1701273726237058&key=27939"
	    #url47="http://topiptv.net:5890/live/tom01/01tom/704.m3u8"
            #url47="http://premiumplustv.com:8000/user938303/G26ZM4L1gY/88201"
            #url47="http://iptv-luxe.com:8789/live/1212/1212/166.m3u8"
            #url47="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33436.m3u8"	    
	    ref = eServiceReference(4097, 0, url47)
	    ref.setName(Name_47)
	    self.session.open(MoviePlayer, ref)
	def CANALPLAY7HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
            url48="http://nvkdn.redi-vo.com/iptv/ch304?code=1701273726237058&key=45527"
	    #url48="http://topiptv.net:5890/live/tom01/01tom/700.m3u8"	    
	    #url48="http://premiumplustv.com:8000/user938303/G26ZM4L1gY/88202"
	    #url48="http://iptv-luxe.com:8789/live/1212/1212/352.m3u8"
	    #url48="http://iptv-luxe.com:8789/live/1212/1212/165.m3u8"
	    #url48="http://185.23.213.162:8789/live/ania/ania/13957.m3u8"
	    #url48="http://95.154.194.84:8000/live/14fIq4TDmE/GfCruyHz18/33434.m3u8"   
	    ref = eServiceReference(4097, 0, url48)
	    ref.setName(Name_48)
	    self.session.open(MoviePlayer, ref)	    
	def LOCALSKYSELECT1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url49="http://iptvpro.premium-itv.com:8789/31031986/31031986/23735"              	    
	    #url49="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2813.m3u8"
	    url49="http://nvkdn.redi-vo.com/iptv/ch306?code=1701273726237058&key=50185"        	    
	    #url49="http://linux-app.tv:6204/live/mustafa96/mustafa96/27728.m3u8"
            #url49="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14119"	    
	    ref = eServiceReference(4097, 0, url49)
	    ref.setName(Name_49)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar	    
	    #url50="http://xtiptv.xyz:25461/live/17094/66im8o2DpJ/56657.ts"
	    #url50="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2814.m3u8"	    
	    #url50="http://linux-app.tv:6204/live/mustafa96/mustafa96/27727.m3u8"
	    #url50="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14120"
            url50="http://nvkdn.redi-vo.com/iptv/ch306?code=1701273726237058&key=33489"	    
	    ref = eServiceReference(4097, 0, url50)
	    ref.setName(Name_50)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT3HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url51="http://nvkdn.redi-vo.com/iptv/ch308?code=1701273726237058&key=41851"
	    #url51="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14121"
	    #url51="http://tv2iptv.com:8000/live/Faysal/faysal123/23676.m3u8"
	    #url51="http://xtiptv.xyz:25461/live/17094/66im8o2DpJ/56656.ts"
            #url51="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2815.m3u8"	    
	    ref = eServiceReference(4097, 0, url51)
	    ref.setName(Name_51)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT4HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url52="http://iptv6.premium-stv.com:25461/sourcegermanypro2/0626674936/2816"
	    url52="http://nvkdn.redi-vo.com/iptv/ch308?code=1701273726237058&key=16856"
	    #url52="http://linux-app.tv:6204/live/mustafa96/mustafa96/27725.m3u8"
            #url52="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14122" 	    
	    #url52="http://tv2iptv.com:8000/live/Faysal/faysal123/23675.m3u8"
	    #url52="http://tv2iptv.com:8000/live/badr/badr1234/23675.m3u8"
            #url52="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2816.m3u8"	    
	    ref = eServiceReference(4097, 0, url52)
	    ref.setName(Name_52)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT5HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url53="http://skdn.redi-vo.com/iptv/ch309?code=138137164006399&key=51503"
	    #url53="http://linux-app.tv:6204/live/mustafa96/mustafa96/27724.m3u8"
	    #url53="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14123"
	    #url53="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/46470.m3u8"
	    #url53="http://tv2iptv.com:8000/live/Faysal/faysal123/23674.m3u8"
            #url53="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2817.m3u8"	    
	    ref = eServiceReference(4097, 0, url53)
	    ref.setName(Name_53)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT6HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar            	    
	    url54="http://skdn.redi-vo.com/iptv/ch309?code=138137164006399&key=14106"
            #url54="http://linux-app.tv:6204/live/mustafa96/mustafa96/27723.m3u8"
            #url54="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14124"
            #url54="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/46469.m3u8"
            #url54="http://185.233.185.248:25443/live/corine/123456/39226.m3u8"	    
	    ref = eServiceReference(4097, 0, url54)
	    ref.setName(Name_54)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT7HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url55="http://tv2iptv.com:8000/live/badr/badr1234/23673.m3u8"
	    #url55="http://linux-app.tv:6204/live/mustafa96/mustafa96/27722.m3u8"
	    #url55="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14125"
	    url55="http://skdn.redi-vo.com/iptv/ch300?code=138137164006399&key=13001"   
	    ref = eServiceReference(4097, 0, url55)
	    ref.setName(Name_55)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT8HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url56="http://managercw.com:8000/live/aliderdiyok/Zedv4HVdbp/83.m3u8"
	    #url56="http://linux-app.tv:6204/live/mustafa96/mustafa96/27721.m3u8"
            #url56="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14126"
            url56="http://skdn.redi-vo.com/iptv/ch301?code=138137164006399&key=52378"	    
	    ref = eServiceReference(4097, 0, url56)
	    ref.setName(Name_56)
	    self.session.open(MoviePlayer, ref)
	def LOCALSKYSELECT9HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url57="http://iptv6.premium-stv.com:25461/sourcegermanypro2/0626674936/2815"
	    #url57="http://linux-app.tv:6204/live/mustafa96/mustafa96/27720.m3u8"
	    #url57="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/14127" 
	    url57="http://skdn.redi-vo.com/iptv/ch302?code=138137164006399&key=57496"
            #url57="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17299.m3u8"	    
	    ref = eServiceReference(4097, 0, url57)
	    ref.setName(Name_57)
	    self.session.open(MoviePlayer, ref)		 
	def SKYSELECT1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar  
	    #url58="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46474.m3u8" 	    
	    #url58="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17285.m3u8"
	    #url58="http://ipturkhd.biz:8000/berkbayrak/ZbwOXE1bH1/117"            	    
	    url58="http://skdn.redi-vo.com/iptv/ch303?code=138137164006399&key=12622"
            #ur58="http://client.era-iptv.net:25461/live/Londoncafe9r8rutve/Od8e7rnsodid/1321.m3u8"	    
	    ref = eServiceReference(4097, 0, url58)
	    ref.setName(Name_58)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url59="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46473.m3u8"
            #url59="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17286.m3u8"
            #url59="http://iptv6.premium-stv.com:25461/sourcegermanypro2/0626674936/2814"
            url59="http://skdn.redi-vo.com/iptv/ch304?code=138137164006399&key=14278"	    
            #url59="http://vip.akiptv.biz:8000/live/faruk1/19012019/1050.ts"	    
	    ref = eServiceReference(4097, 0, url59)
	    ref.setName(Name_59)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT3HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url60="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46472.m3u8"
	    url60="http://skdn.redi-vo.com/iptv/ch305?code=138137164006399&key=55158"
	    #url60="http://z.iptvsubscription.org:80/live/2ucpNdKgqy/La1LlABcKd/17286.m3u8"
	    #url60="http://s.igiptv.com:8000/live/abbas/112233/23672.m3u8"
	    #url60="http://client.era-iptv.net:25461/live/Londoncafe9r8rutve/Od8e7rnsodid/1319.m3u8"
            #url60="http://vip.akiptv.biz:8000/live/faruk1/19012019/1051.ts"	    
	    ref = eServiceReference(4097, 0, url60)
	    ref.setName(Name_60)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT4HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url61="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46471.m3u8"
	    #url61="http://uye.performlive.de:80/KeremOzt/rvMUJqR5Lp/47834"
	    url61="http://skdn.redi-vo.com/iptv/ch306?code=138137164006399&key=42149"
	    #url61="http://s.igiptv.com:8000/live/abbas/112233/23673.m3u8"
            #url61="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17288.m3u8"	    
	    ref = eServiceReference(4097, 0, url61)
	    ref.setName(Name_61)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT5HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url62="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46470.m3u8"
	    url62="http://skdn.redi-vo.com/iptv/ch307?code=138137164006399&key=37723"
	    #url62="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17289.m3u8"
            #url62="http://tv2iptv.com:8000/live/badr/badr1234/23675.m3u8"	    
	    ref = eServiceReference(4097, 0, url62)
	    ref.setName(Name_62)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT6HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url63="http://95.154.194.14:8000/live/LeGdi1tigB/DpYUNmaI8b/46472.m3u8"
	    url63="http://skdn.redi-vo.com/iptv/ch308?code=138137164006399&key=18946"
	    #url63="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/46469.m3u8"
            #url63="http://turkiptv.xyz:8080/live/elena/Elena123/126965.m3u8"
            #url63="http://s.igiptv.com:8000/live/abbas/112233/23675.m3u8" 
            #url63="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17290.m3u8"	    
	    ref = eServiceReference(4097, 0, url63)
	    ref.setName(Name_63)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT7HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url64="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32013.m3u8"
	    #url64="http://uye.performlive.de:80/KeremOzt/rvMUJqR5Lp/47838"
	    url64="http://skdn.redi-vo.com/iptv/ch309?code=138137164006399&key=14106 "
            #url64="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17291.m3u8"	    
	    ref = eServiceReference(4097, 0, url64)
	    ref.setName(Name_64)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT8HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url65="http://skdn.redi-vo.com/iptv/ch309?code=138137164006399&key=14106 "
	    #url65="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32010.m3u8"
	    #url65="http://mytvonline.nl:80/live/2YQyltguql/XwEAnAWfE0/17292.m3u8"
	    #url65="http://turkiptv.xyz:8080/live/elena/Elena123/126963.m3u8"
            #url65="http://bestiptv2.premium-tv.info:8789/live/Naji_Derouiche/igaYR6PAtq/23728.m3u8"
            #url65="http://vip.akiptv.biz:8000/live/faruk1/19012019/1056.ts"	    
	    ref = eServiceReference(4097, 0, url65)
	    ref.setName(Name_65)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT9HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    url66="http://skdn.redi-vo.com/iptv/ch300?code=138137164006399&key=13001"
	    #url66="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/32011.m3u8"
	    #url66="http://iptv9211.hopto.me:8000/live/nfzNlANvf2/HHfWU3dzWt/32014.m3u8"
	    #url66="http://z.iptvsubscription.org:80/live/2ucpNdKgqy/La1LlABcKd/17293.m3u8"   
            #url66="http://185.23.213.162:8789/live/ania/ania/13925.m3u8"	    
	    ref = eServiceReference(4097, 0, url66)
	    ref.setName(Name_66)
	    self.session.open(MoviePlayer, ref)
	def SKYSELECT10HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url67="http://95.154.194.14:8000/live/3E3tfSepRV/CHoDruHskE/32010.m3u8"
	    #url67="http://uye.performlive.de:80/KeremOzt/rvMUJqR5Lp/47843"
            url67="http://showflix.org:5890/Mohamed/1234567/602"
            #url67="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/484.m3u8"	    
	    ref = eServiceReference(4097, 0, url67)
	    ref.setName(Name_67)
	    self.session.open(MoviePlayer, ref)	
	def DAZN1HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar	    
	    #url68="http://primeplus.tv:8080/YMq12IOMMi/XqJX8Mfx0i/16320"
            #url68="http://tv2iptv.com:8000/live/Faysal/faysal123/25652.m3u8"
            #url68="http://iptvsmarters.cc:25461/live/serkan/yilmaz/1951.ts"
            #url68="http://hemn2.xyz:8000/live/6PlHOlmM7a/gfKgQfpWED/10582.m3u8"
            #url68="http://45.77.65.162:80/live/SRTgsrtGsRth/7ue6hs45aerha34/257.m3u8"
            #url68="http://primeplus.tv:8080/YMq12IOMMi/XqJX8Mfx0i/16319" 
            #url68="http://s.igiptv.com:8000/live/abbas/112233/25652.m3u8"  
            #url68="http://linux-app.tv:6204/live/mustafa96/mustafa96/28357.m3u8" 
            url68="http://showflix.org:5890/Mohamed/1234567/1266"                  	    
            #url68="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/299" 
	    ref = eServiceReference(4097, 0, url68)
	    ref.setName(Name_68)
	    self.session.open(MoviePlayer, ref)
	def DAZN2HD(self):
	    from Screens.InfoBar import MoviePlayer, InfoBar
	    #url69="http://tv2iptv.com:8000/live/Faysal/faysal123/25653.m3u8"
            #url69="http://primeplus.tv:8080/YMq12IOMMi/XqJX8Mfx0i/16319" 
	    #url69="http://linux-app.tv:6204/live/mustafa96/mustafa96/28358.m3u8"
	    url69="http://showflix.org:5890/Mohamed/1234567/1267"
            #url69="http://g3m1n10.dyndns.org:2611/oB69PpuXuL/3x1zfkCdEo/300"
	    #url69="http://turkiptv.xyz:8080/live/elena/Elena123/126970.m3u8"
            #url69="http://tv2iptv.com:8000/live/Faysal/faysal123/25652.m3u8"  
	    #url69="http://iptv6.premium-stv.com:25461/live/sourcegermanypro2/0626674936/2675.m3u8"
            #url69="http://topiptv.net:5890/tom01/01tom/1267"
            #url69="http://turkiptv.xyz:8080/live/elena/Elena123/126969.m3u8"	    
	    ref = eServiceReference(4097, 0, url69)
	    ref.setName(Name_69)
	    self.session.open(MoviePlayer, ref) 
	#def goto(self):
	    #self.session.openWithCallback(self.restartenigma, MessageBox, _('Restart Enigma2 To Load New Update?'), MessageBox.TYPE_YESNO, timeout=20)

	def restartenigma(self, result):
	    if result:
	        self.session.open(TryQuitMainloop, 3)

	#def gotoa(self):
	    #cmdlist = []
### EDit By RAED To DreamOS OE2.5/2.6
	    #cmdlist.append("%s -qO - '" % self.wget + "'")
	    #cmdlist.append("%s https://ia903000.us.archive.org/30/items/FreeServerinfo/free4k.sh -qO - | /bin/sh" % self.wget)
	    #self.session.open(Console, title='Update links Bein Sport', cmdlist=cmdlist, finishedCallback=None)
	def IPTV(self):
	    cmdlist = []
	    cmdlist.append("%s -qO - '" % self.wget + "'")
	    cmdlist.append("%s https://ia903000.us.archive.org/30/items/FreeServerinfo/Freeiptv.sh -qO - | /bin/sh" % self.wget)
	    self.session.open(Console, title='Update links Bein Sport RMC', cmdlist=cmdlist, finishedCallback=None)
	def AUTOUPD(self):
	    cmdlist = []
	    cmdlist.append("%s -qO - '" % self.wget + "'")
	    cmdlist.append("%s https://ia903000.us.archive.org/30/items/FreeServerinfo/Auto_update_Freeiptv.sh -qO - | /bin/sh" % self.wget)
	    self.session.open(Console, title='AUTO Update links Bein Sport RMC', cmdlist=cmdlist, finishedCallback=None)
	def prombt(self, com):
	    scripts = "/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/"
	    os.chmod(scripts, 755)
	    self.session.open(Console,_("Executing: %s") % (com), ["%s" % com])
	def cancel(self):
	    self.close(None)
