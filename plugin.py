# -*- coding: utf-8 -*-
Path_1 = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/author.txt'
line = open(Path_1).read()
version = '7.0.3'
session = None
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ScrollLabel import ScrollLabel
from enigma import eTimer, getDesktop
from Components.ActionMap import ActionMap
import time
import re
import os
from Screens.MessageBox import MessageBox
from Screens.TextBox import TextBox
from Components.MultiContent import MultiContentEntryText
from enigma import *
from Screens.Screen import Screen
from Screens.HelpMenu import HelpableScreen
from Components.ActionMap import ActionMap, HelpableActionMap
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Components.config import config, ConfigSubsection, ConfigYesNo, ConfigText, getConfigListEntry
from skin import loadSkin
from Plugins.Extensions.FreeServer.outils.CronTimers import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam import *
from Plugins.Extensions.FreeServer.outils.LiseScreencccam2 import *
from Plugins.Extensions.FreeServer.outils.Input import *
from Plugins.Extensions.FreeServer.outils.MyShPrombt import *
from Screens.Standby import TryQuitMainloop
from Tools.Directories import fileExists, pathExists
from datetime import date, datetime
from Components.Pixmap import Pixmap
from Components.ConfigList import ConfigList, ConfigListScreen
from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console
from Screens.Screen import Screen
from enigma import eTimer
from Components.Label import Label
from Components.ActionMap import NumberActionMap, ActionMap
from Plugins.Extensions.FreeServer.outils.configServer import ConfigIP
from Components.config import config, ConfigSelection, getConfigListEntry, ConfigSubsection, configfile
from Components.Sources.StaticText import StaticText
from Components.ScrollLabel import ScrollLabel
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, getDesktop, loadPNG, eConsoleAppContainer
from enigma import *
import os
import sys
import re
from xml.dom import Node, minidom
from twisted.web.client import getPage
import urllib
import base64
### EDit By RAED To DreamOS OE2.5/2.6 and To new Keymap
from Components.ActionMap import HelpableActionMap
from Tools.Directories import fileExists
#### End
config.plugins.FreeServerminoo = ConfigSubsection()
config.plugins.FreeServerminoo.notification = ConfigSelection(default='disabled', choices=[('disabled', _('Disabled')), ('enabled', _('Enabled'))])
#config.plugins.FreeServerminoo.Updattime = ConfigIP(default=[(0, 0), (0, 0)], auto_jump=False)
config.plugins.FreeServerminoo.Updattime = ConfigIP(default=[0, 0, 0, 0], auto_jump = False)
## Add By RAED
config.plugins.FreeServerminoo.lang = ConfigSelection(default = "EN", choices = [
      ("EN", _("English")),
      ("AR", _("Arabic")),
      ("FR", _("French"))
      ])
PLUGIN_PATH = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Skin'

data_xml = 'aHR0cHM6Ly9pYTYwMDcwMi51cy5hcmNoaXZlLm9yZy8yNi9pdGVtcy9kcmVhbW9zYXQvY2Ftc3RhcnQudHh0Cg=='
xml_path = base64.b64decode(data_xml)
import os
path='/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/'
for root, dirs,files in os.walk(path):
    for filename in files:
        scriptfile=os.path.join(path,filename)
        os.chmod(scriptfile,755)

currversion = '7.0.2'        

#### Add By RAED

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280

####################################################################################################        
class FreeServermino(Screen, ConfigListScreen):

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
### EDit By RAED To DreamOS OE2.5/2.6
        if DreamOS():
		self.wget = "/usr/bin/wget2 --no-check-certificate"
        else:
		self.wget = "/usr/bin/wget"
        if isHD():
            skin = loadSkin(PLUGIN_PATH + '/skin.xml')
        else:
            if DreamOS():
                skin = loadSkin(PLUGIN_PATH + '/skinfhdOS.xml')
            else:
                skin = loadSkin(PLUGIN_PATH + '/skinfhd.xml')
### End
        self.onChangedEntry = []
        self.list = []
        ConfigListScreen.__init__(self, self.list, session=self.session, on_change=self.changedEntry)
### EDit By RAED To Add privet keymap.xml
        self["actions"] = HelpableActionMap(self, "FreeServerminoActions",
        {
            'menu': self.KeyMenu,
            'info': self.KeyInfo,
            'blue': self.KeyBlue,
            'yellow': self.KeyYellow,
            'green': self.keySave,
            'red': self.keyClose,
            'cancel': self.keyClose,
            'ok': self.keySave,
            'left': self.keyLeft,
            'right': self.keyRight
        }, -1)
### End
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
                self.update = False
            else:  
                self.update()
        except:
            if self.update == False:
                return
                
        self.__changed = self.changedEntry
        self['Box_1'] = Label('FreeServer V_' + version)
        self['Box_2'] = Label(line)
        self['Box_3'] = Label()
        self['Box_4'] = Label()
        self['text'] = Label('')
        self['logo'] = Pixmap()
        self['aime'] = Pixmap()
        self['logo'].hide()
        self['Box_2'].hide()
        self['Box_4'].setText('Last Update Servers  ' + ImportWritetimes())
        self['text'].hide()
        self['aime'].hide()
        self.showhide = False
        config.plugins.FreeServerminoo.Updattime.value = self.Verif_1(config.plugins.FreeServerminoo.Updattime.value)
        self.runSetup()

    def Verif_1(self, Valist):
        if Valist[0] < 10:
            if Valist[1] < 10:
                Valist = ['0' + str(Valist[0]), '0' + str(Valist[1])]
            else:
                Valist = ['0' + str(Valist[0]), Valist[1]]
        elif Valist[1] < 10:
            Valist = [Valist[0], '0' + str(Valist[1])]
        else:
            Valist = [Valist[0], Valist[1]]
        return Valist

    def Verif(self, Valist):
        if Valist[0] < 10:
            if Valist[1] < 10:
                Valist = '%02d' % Valist[0] + ':' + '%02d' % Valist[1]
            else:
                Valist = '%02d' % Valist[0] + ':' + str(Valist[1])
        elif Valist[1] < 10:
            Valist = str(Valist[0]) + ':' + '%02d' % Valist[1]
        else:
            Valist = str(Valist[0]) + ':' + str(Valist[1])
        return Valist
  
    def update(self):
        import sys,os  
# Edit By RAED To DreamPOS
        os.system("%s https://ia600702.us.archive.org/26/items/dreamosat/freecc.sh -qO - | /bin/sh" % self.wget)
                 
    def runSetup66(self):
        self.list = []
        self.list.append(getConfigListEntry(_('Select Language TO list Menu'), config.plugins.FreeServerminoo.lang))
        self.list.append(getConfigListEntry(_('Notify on_off'), config.plugins.FreeServerminoo.notification))
        self['config'].list = self.list
        self['config'].setList(self.list)
        self['Box_3'].setText('')
        if not isHD() and DreamOS():
               self["config"].l.setValueFont(gFont("Regular", 30)) ## set font to config menu (DreamOS images Need it)
               self["config"].l.setItemHeight(40) ## set ItemHeight to config menu (DreamOS images Need it)

    def runSetup(self):
        self.list.append(getConfigListEntry(_('Select Language TO list Menu'), config.plugins.FreeServerminoo.lang))
        self.list.append(getConfigListEntry(_('Notify on_off'), config.plugins.FreeServerminoo.notification))
        self.list = []
        self.list.append(getConfigListEntry(_('Select Language TO list Menu'), config.plugins.FreeServerminoo.lang))
        self.list.append(getConfigListEntry(_('Notify on_off'), config.plugins.FreeServerminoo.notification))
        if config.plugins.FreeServerminoo.notification.value == 'enabled':
            self.list.append(getConfigListEntry(_('AutoUpdat'), config.plugins.FreeServerminoo.Updattime))
            self['config'].list = self.list
            self['config'].setList(self.list)
            Updattime = self.Verif(config.plugins.FreeServerminoo.Updattime.value)
            self['Box_3'].setText('You Have Chosen..Time\n' + str(Updattime) + '\n To Update Your Servers\nCongratulations')
        if not isHD() and DreamOS():
            self["config"].l.setValueFont(gFont("Regular", 30)) ## set font to config menu (DreamOS images Need it)
            self["config"].l.setItemHeight(40) ## set ItemHeight to config menu (DreamOS images Need it)

    def KeyMenu(self):
        cmdlist = []
	cmdlist.append("%s -qO - '" % self.wget + "'")
	cmdlist.append("%s https://ia601506.us.archive.org/33/items/freecccamserver_201906/firecccam.sh -qO - | /bin/sh" % self.wget)
	self.session.open(Consolo, title='Free CCcam 7 days', cmdlist=cmdlist, finishedCallback=None)
	return    
	
    def KeyInfo(self):
        self.session.open(Consolo, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/scripts/FreeServer.sh'"], closeOnSuccess=True)
       
    def keyLeft(self):
        if self.showhide:
            pass
        else:
            ConfigListScreen.keyLeft(self)
            if config.plugins.FreeServerminoo.notification.value == 'enabled':
                self.runSetup()
            else:
                self.runSetup66()

    def keyRight(self):
        if self.showhide:
            pass
        else:
            ConfigListScreen.keyRight(self)
            if config.plugins.FreeServerminoo.notification.value == 'enabled':
                self.runSetup()
            else:
                self.runSetup66()

    def keySave(self):
        if self.showhide:
            pass
        else:
            for x in self['config'].list:
                x[1].save()
            configfile.save()
            if config.plugins.FreeServerminoo.notification.value == 'enabled':
                Updattime = self.Verif(config.plugins.FreeServerminoo.Updattime.value)
                f = file('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt', 'w')
                f.write(Updattime)
                f.close()
                self['Box_3'].setText('You Have Chosen..Time\n' + str(Updattime) + '\n To Update Your Servers\nCongratulations')
                self.session.openWithCallback(self.restartenigma, MessageBox, _('Free Server V_' + version + '\nRestart Enigma2 To Load New Settings?'), MessageBox.TYPE_YESNO)
            else:
                f = file('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt', 'w')
                f.write('Disabled')
                f.close()
                self['Box_3'].setText('')
                self.close()

    def restartenigma(self, result):
        if result:
            self.session.open(TryQuitMainloop, 3)
            
    def LiseScreencccam(self):
        self.session.open(LiseScreencccam)         
        
    def LiseScreencccam2(self):
        self.session.open(LiseScreencccam2)

    def KeyBlue(self):
        self.session.open(Input)

    def KeyYellow(self):
        if self.showhide:
            pass
        else:
            self.session.open(Consolo, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/FreeServer.sh'"], finishedCallback=self.installRun)

    def installRun(self):
        timeimop = Importtimes()
        NServer = NumbreServers()
        self['Box_4'].setText('Last Update Servers  Nbr_s = ' + str(NServer) + '\n\t' + timeimop)
        self['Box_4'].show()

    def keyClose(self):
        if self.showhide:
            self['Box_2'].hide()
            self['text'].hide()
            self['logo'].hide()
            self['aime'].hide()
            self['config'].show()
            self['Box_3'].show()
            self['Box_4'].show()
            self.showhide = False
        else:
            for x in self['config'].list:
                x[1].cancel()

            self.close()
        return
        
    def changedEntry(self):
        for x in self.onChangedEntry:
            x()

def Nmbrs_linesdatastxt():
    n = ''
    file_0 = ''
    if fileExists('/etc/CCcam.cfg'):
        file_0 = '/etc/CCcam.cfg'
        n = sum((1 for _ in open(file_0)))
    else:
        n = 'makach'
    return n


def NumbreServers():
    n = Nmbrs_linesdatastxt()
    if n != 'makach':
        counter = 0
        if fileExists('/etc/CCcam.cfg'):
            ptfile = open('/etc/CCcam.cfg', 'r')
            msg = ptfile.readlines()
            for i in range(n):
                if 'c:' in msg[i].lower():
                    counter = counter + 1

            print counter
        else:
            counter = 'Nooo'
    else:
        counter = 'Nooo'
    return counter


def Importtimes():
    msgtimes = ''
    hr1 = ''
    minute1 = ''
    Jour1 = ''
    mois1 = ''
    now = datetime.now()
    hr = str(now.hour)
    minute = str(now.minute)
    Nomdujour = time.strftime('%A')
    Jour = str(now.day)
    mois = str(now.month)
    Annee = str(now.year)
    if len(hr) == 1:
        hr1 = '0' + str(hr)
    else:
        hr1 = str(hr)
    if len(minute) == 1:
        minute1 = '0' + str(minute)
    else:
        minute1 = str(minute)
    if len(Jour) == 1:
        Jour1 = '0' + str(Jour)
    else:
        Jour1 = str(Jour)
    if len(mois) == 1:
        mois1 = '0' + str(mois)
    else:
        mois1 = str(mois)
    msgtimes = hr1 + ':' + minute1 + ' ' + Nomdujour + ' ' + Jour1 + ':' + mois1 + ':' + str(Annee)
    Writetimes(msgtimes)
    return msgtimes


def Writetimes(timeserv):
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Runtimes.txt', 'w')
    f.write(timeserv)
    f.close()


def ImportWritetimes():
    f = ''
    Path_1 = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Runtimes.txt'
    if fileExists(Path_1):
        f = open(Path_1).read()
    else:
        f = '......'
    return f


def comparetimes_2():
    msgestr_2 = ''
    try:
        now = datetime.now()
        hr = str(now.hour)
        minute = str(now.minute)
        if len(hr) == 1:
            hr = '0' + hr
        if len(minute) == 1:
            minute = '0' + minute
        hrminute = hr + minute
        hrminute = hrminute.replace(':', '')
        hrminute = hrminute.strip()
        ptimesfile = '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt'
        ptfile = open(ptimesfile, 'r')
        data = ptfile.readlines()
        ptfile.close()
        updat_time = data[0]
        if updat_time == 'Disabled' or updat_time == '':
            msgestr_2 = ''
        else:
            updat_time1 = data[0].replace('\n', '').replace('\t', '').replace('\r', '')
            f = []
            f = updat_time.split(':')
            fhour = f[0]
            fminute = f[1]
            if len(fhour) == 1:
                fhour = '0' + fhour
            if len(fminute) == 1:
                fminute = '0' + fminute
            updat_time = str(fhour) + str(fminute)
            updat_time = updat_time.strip()
            if hrminute == updat_time:
                msgestr_2 = 'Wait For The Download Time Of Your Free Servers....' + str(updat_time1) + ' You Can Find Servers Lines In (/etc/CCcam.cfg)'
        return msgestr_2
    except:
        return msgestr_2


class DoFreeServerminooScreen(Screen):
    skin = '<screen position="100,100" size="300,300" title="Free Server" ></screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        self.msg = ''
        self.minutecount = 30000
        self.FreeServerminoo = eTimer()
        self.FreeServerminoo.stop()
### Edit By RAED To DreamOS
        try:
            self.FreeServerminoo.timeout.get().append(self.CheckFreeServerminoo)
        except:
            self.FreeServerminoo_conn = self.FreeServerminoo.timeout.connect(self.CheckFreeServerminoo)
### End
        self.FreeServerminoo.start(self.minutecount, True)

    def repeat(self, result = None):
        self.FreeServerminoo = eTimer()
        self.FreeServerminoo.stop()
### Edit By RAED To DreamOS
        try:
            self.FreeServerminoo.timeout.get().append(self.CheckFreeServerminoo)
        except:
            self.FreeServerminoo_conn = self.FreeServerminoo.timeout.connect(self.CheckFreeServerminoo)
### End
        self.FreeServerminoo.start(self.minutecount, True)

    def CheckFreeServerminoo(self):
        msg_2 = comparetimes_2()
        now = datetime.now()
        if not msg_2 == 'Disabled' and not msg_2 == '':
            self.minutecount = 3600000
            if config.plugins.FreeServerminoo.notification.value == 'enabled':
                self.session.openWithCallback(self.repeat, CheckFreeServerminooscreen_2, msg_2)
        else:
            self.minutecount = 30000
            self.repeat()


class CheckFreeServerminooscreen_2(Screen):

    def __init__(self, session, msg = None):
        Screen.__init__(self, session)
### Edit By RAED To FHD Skin
        if isHD():
            skin = loadSkin(PLUGIN_PATH + '/skin.xml')
        else:
            if DreamOS():
                skin = loadSkin(PLUGIN_PATH + '/skinfhdOS.xml')
            else:
                skin = loadSkin(PLUGIN_PATH + '/skinfhd.xml')
### End
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.disappear,
         'cancel': self.disappear}, -1)
        self.messageupdat = msg
        self['info'] = Label()
        self['info'].setText(msg)
        self.timer = eTimer()
### Edit By RAED To DreamOS
        try:
            self.timer.callback.append(self.disappear_0)
        except:
            self.timer_conn = self.timer.timeout.connect(self.disappear_0)
### End
        self.timer.start(10000, True)

    def disappear_0(self):
        self.timer.stop()
        Importtimes()
        self.session.open(Consolo, title='Free Server', cmdlist=["sh '/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/FreeServer.sh'"], finishedCallback=self.installservers, closeOnSuccess=True)

    def installservers(self):
        ChServers = NumbreServers()
        if ChServers != 'Nooo':
            self['info'].setText('Congratulations......... You Received  ' + str(ChServers) + ' Servers\n\tFree Server  V_' + version + '\n\t   mino60')

    def disappear(self):
        self.timer.stop()
        self.close()


class FreeServerminoosBackgroundWorkerScreen(Screen):

    def __init__(self, session, args = 0):
        self.session = session
        Screen.__init__(self, session)
### Edit By RAED To FHD Skin
        if isHD():
            skin = loadSkin(PLUGIN_PATH + '/skin.xml')
        else:
            if DreamOS():
                skin = loadSkin(PLUGIN_PATH + '/skinfhdOS.xml')
            else:
                skin = loadSkin(PLUGIN_PATH + '/skinfhd.xml')
### End
        self.menu = args
        self.session = session
        self.loop = eTimer()
### Edit By RAED To DreamOS
        try:
            self.loop.callback.append(self.ExecTest)
        except:
            self.loop_conn = self.loop.timeout.connect(self.ExecTest)
### End

    def stopTimer(self):
        self.loop.stop()

    def startTimer(self):
        self.loop.start(1, 1)

    def ExecTest(self):
        self.loop.stop()
        self.DebugToLog()
        self.loop.start(3600000, 1)

    def DebugToLog(self):
        now = datetime.now()
        timenow = str(now)

StayLoop = FreeServerminoosBackgroundWorkerScreen(session)

def openfile():
    try:
        fp = open('/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/config/Times.txt', 'r')
        line = fp.read()
        fp.close()
        return line
    except:
        cname = 'none'
        return cname

def autostartFreeServerminoo(reason, **kwargs):
    global session
    try:
        if config.plugins.FreeServerminoo.notification.value == 'disabled':
            return
    except:
        pass

    if reason == 0:
        if openfile() == 'none':
            StayLoop.stopTimer
        else:
            StayLoop.startTimer()
    if reason == 0 and kwargs.has_key('session'):
        session = kwargs['session']
        session.open(DoFreeServerminooScreen)

class Consolo(Screen):

    def __init__(self, session, title = 'Consolo', cmdlist = None, finishedCallback = None, closeOnSuccess = False):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'zdfHD.xml'
        else:
            skin = skin_path + 'zdfFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.finishedCallback = finishedCallback
        self.closeOnSuccess = closeOnSuccess
        self['text'] = ScrollLabel('')
        self['actions'] = ActionMap(['WizardActions', 'DirectionActions'], {'ok': self.cancel,
         'back': self.cancel,
         'up': self['text'].pageUp,
         'down': self['text'].pageDown}, -1)
        self.cmdlist = cmdlist
        self.newtitle = title
        self.container = eConsoleAppContainer()
        self.run = 0
        self.onShown.append(self.updateTitle)
### Edit By RAED To DreamOS
        try:
            self.container.appClosed.append(self.runFinished)
            self.container.dataAvail.append(self.dataAvail)
        except:
            self.container.appClosed_conn = self.container.appClosed.connect(self.runFinished)
            self.container.dataAvail_conn = self.container.dataAvail.connect(self.dataAvail)
### End
        self.onLayoutFinish.append(self.startRun)

    def updateTitle(self):
        self.setTitle(self.newtitle)

    def startRun(self):
        self['text'].setText(_('Execution Progress:') + '\n\n')
        print 'Console: executing in run', self.run, ' the command:', self.cmdlist[self.run]
        if self.container.execute(self.cmdlist[self.run]):
            self.runFinished(-1)

    def runFinished(self, retval):
        self.run += 1
        if self.run != len(self.cmdlist):
            if self.container.execute(self.cmdlist[self.run]):
                self.runFinished(-1)
        else:
            str = self['text'].getText()
            str += _('Execution finished!!')
            self['text'].setText(str)
            self['text'].lastPage()
            if self.finishedCallback is not None:
                self.finishedCallback()
            if not retval and self.closeOnSuccess:
                self.cancel()
        return

    def cancel(self):
        if self.run == len(self.cmdlist):
            self.close()
### Edit By RAED To DreamOS
            try:
                  self.container.appClosed.remove(self.runFinished)
                  self.container.dataAvail.remove(self.dataAvail)
            except:
                  self.container.appClosed_conn = None
                  self.container.dataAvail_conn = None
### End

    def dataAvail(self, str):
        self['text'].setText(self['text'].getText() + str)

def menu(menuid, **kwargs):
    if menuid == 'mainmenu':
        return [('FreeServer',
          main,
          'FreeServer',
          1)]
    return []


def main(session, **kwargs):
    session.open(FreeServermino)


def Plugins(**kwargs):
    return [PluginDescriptor(name='FreeServer ', description='CCcam Free Servers for online Generator', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main, icon='/usr/lib/enigma2/python/Plugins/Extensions/FreeServer/Deco/plugin.png'), PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART, PluginDescriptor.WHERE_AUTOSTART], fnc=autostartFreeServerminoo)]
