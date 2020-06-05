from os import path as os_path, remove, unlink, rename, chmod, access, X_OK
from shutil import move
import time
from enigma import eTimer
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Screens.HelpMenu import HelpableScreen
from Components.Console import Console
from Components.Sources.StaticText import StaticText
from Components.Sources.Boolean import Boolean
from Components.Sources.List import List
from Components.SystemInfo import SystemInfo
from Components.Label import Label, MultiColorLabel
from Components.Input import Input
from Screens.InputBox import InputBox
from Components.ScrollLabel import ScrollLabel
from Components.Pixmap import Pixmap, MultiPixmap
from Components.MenuList import MenuList
##### Edit by RAED SCOPE_ACTIVE_SKIN  , getVersionString
from Components.config import config, ConfigSubsection, ConfigYesNo, ConfigIP, ConfigPassword, ConfigSelection, getConfigListEntry, ConfigNumber, ConfigLocations, NoSave
from About import about
from config import ConfigMacText
from Network import iNetwork
##### End edit
from Components.ConfigList import ConfigListScreen
from Components.PluginComponent import plugins
from Components.FileList import MultiFileSelectList
from Components.ActionMap import ActionMap, NumberActionMap, HelpableActionMap
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS
from Tools.LoadPixmap import LoadPixmap
from Plugins.Plugin import PluginDescriptor
from subprocess import call
import commands
import os
import glob
from Screens.Standby import TryQuitMainloop

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS
        
class NetworkMacSetup(Screen, ConfigListScreen, HelpableScreen):
    skin = """
	<screen name="NetworkMacSetup" position="center,center" size="560,400" title="MAC address setup" >
		<ePixmap pixmap="skin_default/buttons/red.png" position="0,0" size="140,40" alphatest="on" />
		<ePixmap pixmap="skin_default/buttons/green.png" position="140,0" size="140,40" alphatest="on" />
		<widget source="key_red" render="Label" position="0,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />
		<widget source="key_green" render="Label" position="140,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />
		<widget name="config" position="5,50" size="550,280" scrollbarMode="showOnDemand" />
		<widget source="introduction" render="Label" position="0,350" size="560,50" zPosition="10" font="Regular;21" halign="center" valign="center" backgroundColor="#25062748" transparent="1" />
	</screen>
"""
    def __init__(self, session):
        Screen.__init__(self, session)
        HelpableScreen.__init__(self)
        Screen.setTitle(self, _('MAC-address settings'))
        self.curMac = self.getmac('eth0')
        self.getConfigMac = NoSave(ConfigMacText(default=self.curMac))
        self['key_red'] = StaticText(_('Cancel'))
        self['key_green'] = StaticText(_('Save'))
        self['introduction'] = StaticText(_('Press OK to set the MAC-address.'))
        self['OkCancelActions'] = HelpableActionMap(self, 'OkCancelActions', {'cancel': (self.cancel, _('Exit nameserver configuration')),
         'ok': (self.ok, _('Activate current configuration'))})
        self['ColorActions'] = HelpableActionMap(self, 'ColorActions', {'red': (self.cancel, _('Exit MAC-address configuration')),
         'green': (self.ok, _('Activate MAC-address configuration'))})
        self['actions'] = NumberActionMap(['SetupActions'], {'ok': self.ok}, -2)
        self.list = []
        ConfigListScreen.__init__(self, self.list)
        self.createSetup()

    def getmac(self, iface):
        eth = about.getIfConfig(iface)
        return eth['hwaddr']

    def createSetup(self):
        self.list = []
        self.list.append(getConfigListEntry(_('MAC-address'), self.getConfigMac))
        self['config'].list = self.list
        self['config'].l.setList(self.list)

    def ok(self):
        MAC = self.getConfigMac.value
        f = open('/etc/enigma2/hwmac', 'w')
        f.write(MAC)
        f.close()
        self.restartLan()

    def run(self):
        self.ok()

    def cancel(self):
        self.close()

    def restartBox(self, answer):
        if answer is True:
            self.session.open(TryQuitMainloop, 2)
        else:
            self.close()

    def restartLan(self):
        iNetwork.restartNetwork(self.restartLanDataAvail)
        self.restartLanRef = self.session.openWithCallback(self.restartfinishedCB, MessageBox, _('Please wait while we configure your network...'), type=MessageBox.TYPE_INFO, enable_input=False)

            
    def restartLanDataAvail(self, data):
        if data is True:
            iNetwork.getInterfaces(self.getInterfacesDataAvail)

    def getInterfacesDataAvail(self, data):
        if data is True:
            self.restartLanRef.close(True)
            
    def restartfinishedCB(self, data):
        if data is True:
           if DreamOS():
               message = _('Finished configuring your network - Need Restart STB (Important)\n\nRestart your STB now?')
               mbox = self.session.openWithCallback(self.restartBox, MessageBox, message, MessageBox.TYPE_YESNO)
               mbox.setTitle(_('Restart STB'))
           else:         
               self.session.openWithCallback(self.close, MessageBox, _('Finished configuring your network'), type=MessageBox.TYPE_INFO, timeout=10, default=False)

      
