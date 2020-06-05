#!/bin/sh
#@mino60 By RAED 2020
#### EDit By RAED To DreamOS OE2.5/2.6
if [ -f /var/lib/dpkg/status ]; then
      WGET='/usr/bin/wget2 --no-check-certificate'
else
      WGET='/usr/bin/wget'
fi         
#### End Edit  
LINE="************************************************************"
FreeServer3=/usr/keys/CCcam.cfg
FreeServer2=/tmp/FreeServer.txt
FreeServer2=FreeServer.txt
FreeServer=/etc/CCcam.cfg
EmuServer='/etc/CCcam.cfg'
FreeServertmpa=/tmp/freeservra*
FreeServertmpb=/tmp/freeservrb*
rm -f $FreeServer > /dev/null 2>&1
rm -f $FreeServer2 > /dev/null 2>&1
rm -f $FreeServertmpa* > /dev/null 2>&1
rm -f $FreeServertmpb* > /dev/null 2>&1
#HOST             
HTTPSERV1="http://ia601509.us.archive.org/5/items/dreamosat/CCCAM.txt"  
HTTPSERV24="http://ia601509.us.archive.org/5/items/dreamosat/free-server1.txt"
HTTPSERV25="http://ia601509.us.archive.org/5/items/dreamosat/free-server2.txt"   
HTTPSERV26="http://ia601509.us.archive.org/5/items/dreamosat/free-server3.txt"  
HTTPSERV27="http://ia601509.us.archive.org/5/items/dreamosat/free-server4.txt"       
HTTPSERV28="http://ia601509.us.archive.org/5/items/dreamosat/free-server5.txt"                 
HTTPSERV29="http://ia601509.us.archive.org/5/items/dreamosat/free-server6.txt"                
HTTPSERV30="http://ia601509.us.archive.org/5/items/dreamosat/free-server7.txt"              
HTTPSERV31="http://ia601509.us.archive.org/5/items/dreamosat/free-server8.txt"                                     
HTTPSERV32="http://ia601509.us.archive.org/5/items/dreamosat/free-server9.txt"                            
HTTPSERV33="http://ia601509.us.archive.org/5/items/dreamosat/free-server10.txt"                                      
#HTTPSERV34="https://www.freecamtv.com/trial1.php"  
#HTTPSERV35="http://cccamstore.tv/free-server.php"
HTTPSERV36="https://thecccam.com/cccam-free.php"
HTTPSERV37="http://bosscccam.co/Test.php" 
HTTPSERV38="https://cccamsiptv.com/cccamfree/get.php"
HTTPSERV39="https://cccamiptvs.com/freecccam/get.php"
HTTPSERV40="https://mycccam.shop/free-cccam.php" 
#HTTPSERV41="http://cccamgood.com/free/get2.php"
HTTPSERV42="https://cccam.zone/FREEN12/new0.php"
HTTPSERV43="https://premium-cccam.com/sv1.php"
HTTPSERV44="http://buyiptvcode.com/free6/get2.php"
#HTTPSERV45="https://cccamxfree.com/free/get.php" 
#HTTPSERV46="https://cccameasy.com/free/get.php"
#HTTPSERV47="https://cccamup.com/free/get.php" 
#HTTPSERV48="https://www.freecamtv.com/tss1.php"
#HTTPSERV49="https://www.topcamd.com/get1.php"
#HTTPSERV50="https://www.topcamd.com/get2.php"
#HTTPSERV51="https://www.bluecccam.com/cline1.php"
#HTTPSERV52="http://cccamstore.tv/free-server.php"
HTTPSERV53="https://cccam.zone/FREEN12/new0.php"  
HTTPSERV54="https://cccam.zone/FREEN12/new0.php"
HTTPSERV55="https://cccam.zone/FREEN12/new0.php"
HTTPSERV56="https://cccam.zone/FREEN12/new0.php"
HTTPSERV57="http://cccammania.com/free4/get2.php" 
HTTPSERV58="http://cccamgenerador.com/gratis/get2.php"   
#HTTPSERV59="https://oscamlive.com/cccam-server-test/cccam-free-2019/"
#HTTPSERV60="https://s.cccamkey.com/cccam24.php"
HTTPSERV61="http://infosat.satunivers.tv/cgn/generatejdid.php"
#HTTPSERV62="https://iptvfree.ch/cccamfree/get.php"
#HTTPSERV63="https://www.realcccam.com/freecccam/index.php"
HTTPSERV64="https://www.cccambird.com/freecccam.php"
#HTTPSERV65="https://cccamon.com/free/get.php"
#HTTPSERV66="https://vipcccam.net/freetest.php"
#HTTPSERV67="http://eurohd.ddns.us/Tv/price.php"
#HTTPSERV68="http://chandcccam.cf/get.php?user=6897654&pass=8654798"
HTTPSERV69="http://cccam24h.com/lik1.php"
#HTTPSERV70="https://fcccam.com/index.php"
HTTPSERV71="http://cccamnice.com/free5/get2.php"
HTTPSERV72="https://www.cccamtiger.com/freecccam48h.php"
#HTTPSERV73="https://clinepk.com/index.php"
#HTTPSERV74="http://sky.king4tv.com/index.php/free-test/"
#HTTPSERV75="https://www.freecamtv.com/server2.php"
#HTTPSERV76="https://www.freecamtv.com/server3.php"
#TMP FILES 
FreeServertmpb1=/tmp/freeservrb1
FreeServertmpb2=/tmp/freeservrb2
FreeServertmpb3=/tmp/freeservrb3
FreeServertmpb4=/tmp/freeservrb4
FreeServertmpb5=/tmp/freeservrb5
FreeServertmpb6=/tmp/freeservrb6
FreeServertmpb7=/tmp/freeservrb7
FreeServertmpb8=/tmp/freeservrb8
FreeServertmpb9=/tmp/freeservrb9
FreeServertmpb10=/tmp/freeservrb10
FreeServertmpb11=/tmp/freeservrb11
FreeServertmpb12=/tmp/freeservrb12
FreeServertmpb13=/tmp/freeservrb13
FreeServertmpb14=/tmp/freeservrb14
FreeServertmpb15=/tmp/freeservrb15
FreeServertmpb16=/tmp/freeservrb16
FreeServertmpb17=/tmp/freeservrb17
FreeServertmpb18=/tmp/freeservrb18
FreeServertmpb19=/tmp/freeservrb19
FreeServertmpb20=/tmp/freeservrb20
FreeServertmpb21=/tmp/freeservrb21
FreeServertmpb22=/tmp/freeservrb22
FreeServertmpb23=/tmp/freeservrb23
FreeServertmpb24=/tmp/freeservrb24
FreeServertmpb25=/tmp/freeservrb25
FreeServertmpb26=/tmp/freeservrb26
FreeServertmpb27=/tmp/freeservrb27
FreeServertmpb28=/tmp/freeservrb28
FreeServertmpb29=/tmp/freeservrb29
FreeServertmpb30=/tmp/freeservrb30
FreeServertmpb31=/tmp/freeservrb31
FreeServertmpb32=/tmp/freeservrb32
FreeServertmpb33=/tmp/freeservrb33
#FreeServertmpb34=/tmp/freeservrb34
#FreeServertmpb35=/tmp/freeservrb35
FreeServertmpb36=/tmp/freeservrb36
FreeServertmpb37=/tmp/freeservrb37
FreeServertmpb38=/tmp/freeservrb38
FreeServertmpb39=/tmp/freeservrb39
FreeServertmpb40=/tmp/freeservrb40
#FreeServertmpb41=/tmp/freeservrb41
FreeServertmpb42=/tmp/freeservrb42
FreeServertmpb43=/tmp/freeservrb43
FreeServertmpb44=/tmp/freeservrb44
#FreeServertmpb45=/tmp/freeservrb45
#FreeServertmpb46=/tmp/freeservrb46
#FreeServertmpb47=/tmp/freeservrb47
#FreeServertmpb48=/tmp/freeservrb48
#FreeServertmpb49=/tmp/freeservrb49
#FreeServertmpb50=/tmp/freeservrb50
#FreeServertmpb51=/tmp/freeservrb51
#FreeServertmpb52=/tmp/freeservrb52
FreeServertmpb53=/tmp/freeservrb53
FreeServertmpb54=/tmp/freeservrb54
FreeServertmpb55=/tmp/freeservrb55
FreeServertmpb56=/tmp/freeservrb56
FreeServertmpb57=/tmp/freeservrb57
FreeServertmpb58=/tmp/freeservrb58
#FreeServertmpb59=/tmp/freeservrb59
#FreeServertmpb60=/tmp/freeservrb60
FreeServertmpb61=/tmp/freeservrb61
#FreeServertmpb62=/tmp/freeservrb62
#FreeServertmpb63=/tmp/freeservrb63
FreeServertmpb64=/tmp/freeservrb64
#FreeServertmpb65=/tmp/freeservrb65
#FreeServertmpb66=/tmp/freeservrb66
#FreeServertmpb67=/tmp/freeservrb67
#FreeServertmpb68=/tmp/freeservrb68
FreeServertmpb69=/tmp/freeservrb69
#FreeServertmpb70=/tmp/freeservrb70
FreeServertmpb71=/tmp/freeservrb71
FreeServertmpb72=/tmp/freeservrb72
#FreeServertmpb73=/tmp/freeservrb73
#FreeServertmpb74=/tmp/freeservrb74
#FreeServertmpb75=/tmp/freeservrb75
#FreeServertmpb76=/tmp/freeservrb76
#TMP FILES
FreeServertmpa1=/tmp/freeservra1
FreeServertmpa2=/tmp/freeservra2
FreeServertmpa3=/tmp/freeservra3
FreeServertmpa4=/tmp/freeservra4
FreeServertmpa5=/tmp/freeservra5
FreeServertmpa6=/tmp/freeservra6
FreeServertmpa7=/tmp/freeservra7
FreeServertmpa8=/tmp/freeservra8
FreeServertmpa9=/tmp/freeservra9
FreeServertmpa10=/tmp/freeservra10
FreeServertmpa11=/tmp/freeservra11
FreeServertmpa12=/tmp/freeservra12
FreeServertmpa13=/tmp/freeservra13
FreeServertmpa14=/tmp/freeservra14
FreeServertmpa15=/tmp/freeservra15
FreeServertmpa16=/tmp/freeservra16
FreeServertmpa17=/tmp/freeservra17
FreeServertmpa18=/tmp/freeservra18
FreeServertmpa19=/tmp/freeservra19
FreeServertmpa20=/tmp/freeservra20
FreeServertmpa21=/tmp/freeservra21
FreeServertmpa22=/tmp/freeservra22
FreeServertmpa23=/tmp/freeservra23
FreeServertmpa24=/tmp/freeservra24
FreeServertmpa25=/tmp/freeservra25
FreeServertmpa26=/tmp/freeservra26
FreeServertmpa27=/tmp/freeservra27
FreeServertmpa28=/tmp/freeservra28
FreeServertmpa29=/tmp/freeservra29
FreeServertmpa30=/tmp/freeservra30
FreeServertmpa31=/tmp/freeservra31
FreeServertmpa32=/tmp/freeservra32
FreeServertmpa33=/tmp/freeservra33
#FreeServertmpa34=/tmp/freeservra34
#FreeServertmpa35=/tmp/freeservra35
FreeServertmpa36=/tmp/freeservra36
FreeServertmpa37=/tmp/freeservra37
FreeServertmpa38=/tmp/freeservra38
FreeServertmpa39=/tmp/freeservra39
FreeServertmpa40=/tmp/freeservra40
#FreeServertmpa41=/tmp/freeservra41
FreeServertmpa42=/tmp/freeservra42
FreeServertmpa43=/tmp/freeservra43
FreeServertmpa44=/tmp/freeservra44
#FreeServertmpa45=/tmp/freeservra45
#FreeServertmpa46=/tmp/freeservra46
#FreeServertmpa47=/tmp/freeservra47
#FreeServertmpa48=/tmp/freeservra48
#FreeServertmpa49=/tmp/freeservra49
#FreeServertmpa50=/tmp/freeservra50
#FreeServertmpa51=/tmp/freeservra51
#FreeServertmpa52=/tmp/freeservra52
FreeServertmpa53=/tmp/freeservra53
FreeServertmpa54=/tmp/freeservra54
FreeServertmpa55=/tmp/freeservra55
FreeServertmpa56=/tmp/freeservra56
FreeServertmpa57=/tmp/freeservra57
FreeServertmpa58=/tmp/freeservra58
#FreeServertmpa59=/tmp/freeservra59
#FreeServertmpa60=/tmp/freeservra60
FreeServertmpa61=/tmp/freeservra61
#FreeServertmpa62=/tmp/freeservra62
#FreeServertmpa63=/tmp/freeservra63
FreeServertmpa64=/tmp/freeservra64
#FreeServertmpa65=/tmp/freeservra65
#FreeServertmpa66=/tmp/freeservra66
#FreeServertmpa67=/tmp/freeservra67
#FreeServertmpa68=/tmp/freeservra68
FreeServertmpa69=/tmp/freeservra69
#FreeServertmpa70=/tmp/freeservra70
FreeServertmpa71=/tmp/freeservra71
FreeServertmpa72=/tmp/freeservra72
#FreeServertmpa73=/tmp/freeservra73
#FreeServertmpa74=/tmp/freeservra74
#FreeServertmpa75=/tmp/freeservra75
#FreeServertmpa76=/tmp/freeservra76
#Download Files
$WGET -O $FreeServertmpa1 $HTTPSERV1 > /dev/null 2>&1
$WGET -O $FreeServertmpa24 $HTTPSERV24 > /dev/null 2>&1
$WGET -O $FreeServertmpa25 $HTTPSERV25 > /dev/null 2>&1
$WGET -O $FreeServertmpa26 $HTTPSERV26 > /dev/null 2>&1
$WGET -O $FreeServertmpa27 $HTTPSERV27 > /dev/null 2>&1
$WGET -O $FreeServertmpa28 $HTTPSERV28 > /dev/null 2>&1
$WGET -O $FreeServertmpa29 $HTTPSERV29 > /dev/null 2>&1
$WGET -O $FreeServertmpa30 $HTTPSERV30 > /dev/null 2>&1
$WGET -O $FreeServertmpa31 $HTTPSERV31 > /dev/null 2>&1
$WGET -O $FreeServertmpa32 $HTTPSERV32 > /dev/null 2>&1
$WGET -O $FreeServertmpa33 $HTTPSERV33 > /dev/null 2>&1
#$WGET -O $FreeServertmpa34 $HTTPSERV34 > /dev/null 2>&1
#$WGET -O $FreeServertmpa35 $HTTPSERV35 > /dev/null 2>&1
$WGET -O $FreeServertmpa36 $HTTPSERV36 > /dev/null 2>&1
$WGET -O $FreeServertmpa37 $HTTPSERV37 > /dev/null 2>&1
$WGET -O $FreeServertmpa38 $HTTPSERV38 > /dev/null 2>&1
$WGET -O $FreeServertmpa39 $HTTPSERV39 > /dev/null 2>&1
$WGET -O $FreeServertmpa40 $HTTPSERV40 > /dev/null 2>&1
#$WGET -O $FreeServertmpa41 $HTTPSERV41 > /dev/null 2>&1
$WGET -O $FreeServertmpa42 $HTTPSERV42 > /dev/null 2>&1
$WGET -O $FreeServertmpa43 $HTTPSERV43 > /dev/null 2>&1
$WGET -O $FreeServertmpa44 $HTTPSERV44 > /dev/null 2>&1
#$WGET -O $FreeServertmpa45 $HTTPSERV45 > /dev/null 2>&1
#$WGET -O $FreeServertmpa46 $HTTPSERV46 > /dev/null 2>&1
#$WGET -O $FreeServertmpa47 $HTTPSERV47 > /dev/null 2>&1
#$WGET -O $FreeServertmpa48 $HTTPSERV48 > /dev/null 2>&1
#$WGET -O $FreeServertmpa49 $HTTPSERV49 > /dev/null 2>&1
#$WGET -O $FreeServertmpa50 $HTTPSERV50 > /dev/null 2>&1
#$WGET -O $FreeServertmpa51 $HTTPSERV51 > /dev/null 2>&1
#$WGET -O $FreeServertmpa52 $HTTPSERV52 > /dev/null 2>&1
$WGET -O $FreeServertmpa53 $HTTPSERV53 > /dev/null 2>&1
$WGET -O $FreeServertmpa54 $HTTPSERV54 > /dev/null 2>&1
$WGET -O $FreeServertmpa55 $HTTPSERV55 > /dev/null 2>&1
$WGET -O $FreeServertmpa56 $HTTPSERV56 > /dev/null 2>&1
$WGET -O $FreeServertmpa57 $HTTPSERV57 > /dev/null 2>&1
$WGET -O $FreeServertmpa58 $HTTPSERV58 > /dev/null 2>&1
#$WGET -O $FreeServertmpa59 $HTTPSERV59 > /dev/null 2>&1
#$WGET -O $FreeServertmpa60 $HTTPSERV60 > /dev/null 2>&1
$WGET -O $FreeServertmpa61 $HTTPSERV61 > /dev/null 2>&1
#$WGET -O $FreeServertmpa62 $HTTPSERV62 > /dev/null 2>&1
#$WGET -O $FreeServertmpa63 $HTTPSERV63 > /dev/null 2>&1
$WGET -O $FreeServertmpa64 $HTTPSERV64 > /dev/null 2>&1
#$WGET -O $FreeServertmpa65 $HTTPSERV65 > /dev/null 2>&1
#$WGET -O $FreeServertmpa66 $HTTPSERV66 > /dev/null 2>&1
#$WGET -O $FreeServertmpa67 $HTTPSERV67 > /dev/null 2>&1
#$WGET -O $FreeServertmpa68 $HTTPSERV68 > /dev/null 2>&1
$WGET -O $FreeServertmpa69 $HTTPSERV69 > /dev/null 2>&1
#$WGET -O $FreeServertmpa70 $HTTPSERV70 > /dev/null 2>&1
$WGET -O $FreeServertmpa71 $HTTPSERV71 > /dev/null 2>&1
curl -k $HTTPSERV72 -o $FreeServertmpa72 > /dev/null 2>&1
#$WGET -O $FreeServertmpa73 $HTTPSERV73 > /dev/null 2>&1
#$WGET -O $FreeServertmpa74 $HTTPSERV74 > /dev/null 2>&1
#$WGET -O $FreeServertmpa75 $HTTPSERV75 > /dev/null 2>&1
#$WGET -O $FreeServertmpa76 $HTTPSERV76 > /dev/null 2>&1
#Copy Lines
sed -ne '/SERVER LISTEN PORT :/ p' $FreeServertmpa1 > $FreeServertmpb1
sed -ne '/ALLOW TELNETINFO:/ p' $FreeServertmpa1 > $FreeServertmpb2
sed -ne '/ALLOW WEBINFO:/ p' $FreeServertmpa1 > $FreeServertmpb3
sed -ne '/WEBINFO LISTEN PORT :/ p' $FreeServertmpa1 > $FreeServertmpb4
sed -ne '/#WEBINFO USERNAME :/ p' $FreeServertmpa1 > $FreeServertmpb5
sed -ne '/#WEBINFO PASSWORD :/ p' $FreeServertmpa1 > $FreeServertmpb6
sed -ne '/SMARTCARD WRITE DELAY:/ p' $FreeServertmpa1 > $FreeServertmpb7
sed -ne '/SMARTCARD CLOCK FREQUENCY:/ p' $FreeServertmpa1 > $FreeServertmpb8
sed -ne '/CAMKEY:/ p' $FreeServertmpa1 > $FreeServertmpb9
sed -ne '/CAMDATA:/ p' $FreeServertmpa1 > $FreeServertmpb10
sed -ne '/TRY ALL CHIDS:/ p' $FreeServertmpa1 > $FreeServertmpb11
sed -ne '/EXTRA EMM LEVEL :/ p' $FreeServertmpa1 > $FreeServertmpb12
sed -ne '/B:/ p' $FreeServertmpa1 > $FreeServertmpb13
sed -ne '/B:/ p' $FreeServertmpa1 > $FreeServertmpb14
sed -ne '/CAID PRIO FILE :/ p' $FreeServertmpa1 > $FreeServertmpb15
sed -ne '/PROVIDERINFO FILE :/ p' $FreeServertmpa1 > $FreeServertmpb16
sed -ne '/CHANNELINFO FILE :/ p' $FreeServertmpa1 > $FreeServertmpb17
sed -ne '/SOFTKEY FILE :/ p' $FreeServertmpa1 > $FreeServertmpb18
sed -ne '/AUTOROLL FILE :/ p' $FreeServertmpa1 > $FreeServertmpb19
sed -ne '/SECA HANDLER :/ p' $FreeServertmpa1 > $FreeServertmpb20
sed -ne '/DEBUG:/ p' $FreeServertmpa1 > $FreeServertmpb21
sed -ne '/SHOW TIMING:/ p' $FreeServertmpa1 > $FreeServertmpb22
sed -ne '/#LOG WARNINGS :/ p' $FreeServertmpa1 > $FreeServertmpb23
sed -ne '/C:/ p' $FreeServertmpa24 > $FreeServertmpb24  
sed -ne '/C:/ p' $FreeServertmpa25 > $FreeServertmpb25
sed -ne '/C:/ p' $FreeServertmpa26 > $FreeServertmpb26
sed -ne '/C:/ p' $FreeServertmpa27 > $FreeServertmpb27 
sed -ne '/C:/ p' $FreeServertmpa28 > $FreeServertmpb28
sed -ne '/C:/ p' $FreeServertmpa29 > $FreeServertmpb29
sed -ne '/C:/ p' $FreeServertmpa30 > $FreeServertmpb30
sed -ne '/C:/ p' $FreeServertmpa31 > $FreeServertmpb31
sed -ne '/C:/ p' $FreeServertmpa32 > $FreeServertmpb32
sed -ne '/C:/ p' $FreeServertmpa33 > $FreeServertmpb33
#sed -ne '/C:/ p' $FreeServertmpa34 > $FreeServertmpb34
#sed -ne '/C:/ p' $FreeServertmpa35 > $FreeServertmpb35
sed -ne '/C:/ p' $FreeServertmpa36 > $FreeServertmpb36
sed -ne '/c:/ p' $FreeServertmpa37 > $FreeServertmpb37
sed -ne '/C:/ p' $FreeServertmpa38 > $FreeServertmpb38
sed -ne '/C:/ p' $FreeServertmpa39 > $FreeServertmpb39
sed -ne '/C:/ p' $FreeServertmpa40 > $FreeServertmpb40
#sed -ne '/C:/ p' $FreeServertmpa41 > $FreeServertmpb41
sed -ne '/C:/ p' $FreeServertmpa42 > $FreeServertmpb42
sed -ne '/C:/ p' $FreeServertmpa43 > $FreeServertmpb43
sed -ne '/C:/ p' $FreeServertmpa44 > $FreeServertmpb44
#sed -ne '/C:/ p' $FreeServertmpa45 > $FreeServertmpb45
#sed -ne '/C:/ p' $FreeServertmpa46 > $FreeServertmpb46
#sed -ne '/C:/ p' $FreeServertmpa47 > $FreeServertmpb47
#sed -ne '/C:/ p' $FreeServertmpa48 > $FreeServertmpb48
#sed -ne '/C:/ p' $FreeServertmpa49 > $FreeServertmpb49
#sed -ne '/C:/ p' $FreeServertmpa50 > $FreeServertmpb50
#sed -ne '/C:/ p' $FreeServertmpa51 > $FreeServertmpb51
#sed -ne '/C:/ p' $FreeServertmpa52 > $FreeServertmpb52
sed -ne '/C:/ p' $FreeServertmpa53 > $FreeServertmpb53
sed -ne '/C:/ p' $FreeServertmpa54 > $FreeServertmpb54
sed -ne '/C:/ p' $FreeServertmpa55 > $FreeServertmpb55
sed -ne '/C:/ p' $FreeServertmpa56 > $FreeServertmpb56
sed -ne '/C:/ p' $FreeServertmpa57 > $FreeServertmpb57  
sed -ne '/C:/ p' $FreeServertmpa58 > $FreeServertmpb58
#sed -ne '/C:/ p' $FreeServertmpa59 > $FreeServertmpb59
#sed -ne '/C:/ p' $FreeServertmpa60 > $FreeServertmpb60
sed -ne '/C:/ p' $FreeServertmpa61 > $FreeServertmpb61
#sed -ne '/C:/ p' $FreeServertmpa62 > $FreeServertmpb62
#sed -ne '/C:/ p' $FreeServertmpa63 > $FreeServertmpb63
sed -ne '/C:/ p' $FreeServertmpa64 > $FreeServertmpb64
#sed -ne '/C:/ p' $FreeServertmpa65 > $FreeServertmpb65
#sed -ne '/C:/ p' $FreeServertmpa66 > $FreeServertmpb66
#sed -ne '/C:/ p' $FreeServertmpa67 > $FreeServertmpb67
#sed -ne '/C:/ p' $FreeServertmpa68 > $FreeServertmpb68
sed -ne '/C:/ p' $FreeServertmpa69 > $FreeServertmpb69
#sed -ne '/C:/ p' $FreeServertmpa70 > $FreeServertmpb70
sed -ne '/C:/ p' $FreeServertmpa71 > $FreeServertmpb71
sed -ne '/C :/ p' $FreeServertmpa72 > $FreeServertmpb72
#sed -ne '/C:/ p' $FreeServertmpa73 > $FreeServertmpb73
#sed -ne '/C:/ p' $FreeServertmpa74 > $FreeServertmpb74
#sed -ne '/C:/ p' $FreeServertmpa75 > $FreeServertmpb75
#sed -ne '/C:/ p' $FreeServertmpa76 > $FreeServertmpb76
#Find
FreeServertmpc1=`cat $FreeServertmpb1`
FreeServertmpc2=`cat $FreeServertmpb2`
FreeServertmpc3=`cat $FreeServertmpb3`
FreeServertmpc4=`cat $FreeServertmpb4`
FreeServertmpc5=`cat $FreeServertmpb5`
FreeServertmpc6=`cat $FreeServertmpb6`
FreeServertmpc7=`cat $FreeServertmpb7`
FreeServertmpc8=`cat $FreeServertmpb8`
FreeServertmpc9=`cat $FreeServertmpb9`
FreeServertmpc10=`cat $FreeServertmpb10`
FreeServertmpc11=`cat $FreeServertmpb11`
FreeServertmpc12=`cat $FreeServertmpb12`
FreeServertmpc13=`cat $FreeServertmpb13`
FreeServertmpc14=`cat $FreeServertmpb14`
FreeServertmpc15=`cat $FreeServertmpb15`
FreeServertmpc16=`cat $FreeServertmpb16`
FreeServertmpc17=`cat $FreeServertmpb17`
FreeServertmpc18=`cat $FreeServertmpb18`
FreeServertmpc19=`cat $FreeServertmpb19`
FreeServertmpc20=`cat $FreeServertmpb20`
FreeServertmpc21=`cat $FreeServertmpb21`
FreeServertmpc22=`cat $FreeServertmpb22`
FreeServertmpc23=`cat $FreeServertmpb23`
FreeServertmpc24=`cat $FreeServertmpb24`
FreeServertmpc25=`cat $FreeServertmpb25`
FreeServertmpc26=`cat $FreeServertmpb26`
FreeServertmpc27=`cat $FreeServertmpb27`
FreeServertmpc28=`cat $FreeServertmpb28`
FreeServertmpc29=`cat $FreeServertmpb29`
FreeServertmpc30=`cat $FreeServertmpb30`
FreeServertmpc31=`cat $FreeServertmpb31`
FreeServertmpc32=`cat $FreeServertmpb32`
FreeServertmpc33=`cat $FreeServertmpb33`
#FreeServertmpc34=`cat $FreeServertmpb34`
#FreeServertmpc35=`cat $FreeServertmpb35`
FreeServertmpc36=`cat $FreeServertmpb36`
FreeServertmpc37=`cat $FreeServertmpb37`
FreeServertmpc38=`cat $FreeServertmpb38`
FreeServertmpc39=`cat $FreeServertmpb39`
FreeServertmpc40=`cat $FreeServertmpb40`
#FreeServertmpc41=`cat $FreeServertmpb41`
FreeServertmpc42=`cat $FreeServertmpb42`
FreeServertmpc43=`cat $FreeServertmpb43`
FreeServertmpc44=`cat $FreeServertmpb44`
#FreeServertmpc45=`cat $FreeServertmpb45`
#FreeServertmpc46=`cat $FreeServertmpb46`
#FreeServertmpc47=`cat $FreeServertmpb47`
#FreeServertmpc48=`cat $FreeServertmpb48`
#FreeServertmpc49=`cat $FreeServertmpb49`
#FreeServertmpc50=`cat $FreeServertmpb50`
#FreeServertmpc51=`cat $FreeServertmpb51`
#FreeServertmpc52=`cat $FreeServertmpb52`
FreeServertmpc53=`cat $FreeServertmpb53`
FreeServertmpc54=`cat $FreeServertmpb54`
FreeServertmpc55=`cat $FreeServertmpb55`
FreeServertmpc56=`cat $FreeServertmpb56`
FreeServertmpc57=`cat $FreeServertmpb57`
FreeServertmpc58=`cat $FreeServertmpb58`
#FreeServertmpc59=`cat $FreeServertmpb59`
#FreeServertmpc60=`cat $FreeServertmpb60`
FreeServertmpc61=`cat $FreeServertmpb61`
#FreeServertmpc62=`cat $FreeServertmpb62`
#FreeServertmpc63=`cat $FreeServertmpb63`
FreeServertmpc64=`cat $FreeServertmpb64`
#FreeServertmpc65=`cat $FreeServertmpb65`
#FreeServertmpc66=`cat $FreeServertmpb66`
#FreeServertmpc67=`cat $FreeServertmpb67`
#FreeServertmpc68=`cat $FreeServertmpb68`
FreeServertmpc69=`cat $FreeServertmpb69`
#FreeServertmpc70=`cat $FreeServertmpb70`
FreeServertmpc71=`cat $FreeServertmpb71`
FreeServertmpc72=`cat $FreeServertmpb72`
#FreeServertmpc73=`cat $FreeServertmpb73`
#FreeServertmpc74=`cat $FreeServertmpb74`
#FreeServertmpc75=`cat $FreeServertmpb75`
#FreeServertmpc76=`cat $FreeServertmpb76`
#Created Final file
echo $FreeServertmpc1 >> $FreeServer2
echo $FreeServertmpc2 >> $FreeServer2
echo $FreeServertmpc3 >> $FreeServer2
echo $FreeServertmpc4 >> $FreeServer2
echo $FreeServertmpc5 >> $FreeServer2
echo $FreeServertmpc6 >> $FreeServer2
echo $FreeServertmpc7 >> $FreeServer2
echo $FreeServertmpc8 >> $FreeServer2
echo $FreeServertmpc9 >> $FreeServer2
echo $FreeServertmpc10 >> $FreeServer2
echo $FreeServertmpc11 >> $FreeServer2
echo $FreeServertmpc12 >> $FreeServer2
echo $FreeServertmpc13 >> $FreeServer2
echo $FreeServertmpc14 >> $FreeServer2
echo $FreeServertmpc15 >> $FreeServer2
echo $FreeServertmpc16 >> $FreeServer2
echo $FreeServertmpc17 >> $FreeServer2
echo $FreeServertmpc18 >> $FreeServer2
echo $FreeServertmpc19 >> $FreeServer2
echo $FreeServertmpc20 >> $FreeServer2
echo $FreeServertmpc21 >> $FreeServer2
echo $FreeServertmpc22 >> $FreeServer2
echo $FreeServertmpc23 >> $FreeServer2
echo $FreeServertmpc24 >> $FreeServer2
echo $FreeServertmpc25 >> $FreeServer2
echo $FreeServertmpc26 >> $FreeServer2
echo $FreeServertmpc27 >> $FreeServer2
echo $FreeServertmpc28 >> $FreeServer2
echo $FreeServertmpc29 >> $FreeServer2
echo $FreeServertmpc30 >> $FreeServer2
echo $FreeServertmpc31 >> $FreeServer2
echo $FreeServertmpc32 >> $FreeServer2
echo $FreeServertmpc33 >> $FreeServer2
#echo $FreeServertmpc34 >> $FreeServer2
#echo $FreeServertmpc35 >> $FreeServer2
echo $FreeServertmpc36 >> $FreeServer2
echo $FreeServertmpc37 >> $FreeServer2
echo $FreeServertmpc38 >> $FreeServer2
echo $FreeServertmpc39 >> $FreeServer2
echo $FreeServertmpc40 >> $FreeServer2
#echo $FreeServertmpc41 >> $FreeServer2
echo $FreeServertmpc42 >> $FreeServer2
echo $FreeServertmpc43 >> $FreeServer2
echo $FreeServertmpc44 >> $FreeServer2
#echo $FreeServertmpc45 >> $FreeServer2
#echo $FreeServertmpc46 >> $FreeServer2
#echo $FreeServertmpc47 >> $FreeServer2
#echo $FreeServertmpc48 >> $FreeServer2
#echo $FreeServertmpc49 >> $FreeServer2
#echo $FreeServertmpc50 >> $FreeServer2
#echo $FreeServertmpc51 >> $FreeServer2
#echo $FreeServertmpc52 >> $FreeServer2
echo $FreeServertmpc53 >> $FreeServer2
echo $FreeServertmpc54 >> $FreeServer2
echo $FreeServertmpc55 >> $FreeServer2
echo $FreeServertmpc56 >> $FreeServer2
echo $FreeServertmpc57 >> $FreeServer2
echo $FreeServertmpc58 >> $FreeServer2
#echo $FreeServertmpc59 >> $FreeServer2
#echo $FreeServertmpc60 >> $FreeServer2
echo $FreeServertmpc61 >> $FreeServer2
#echo $FreeServertmpc62 >> $FreeServer2
#echo $FreeServertmpc63 >> $FreeServer2
echo $FreeServertmpc64 >> $FreeServer2
#echo $FreeServertmpc65 >> $FreeServer2
#echo $FreeServertmpc66 >> $FreeServer2
#echo $FreeServertmpc67 >> $FreeServer2
#echo $FreeServertmpc68 >> $FreeServer2
echo $FreeServertmpc69 >> $FreeServer2
#echo $FreeServertmpc70 >> $FreeServer2
echo $FreeServertmpc71 >> $FreeServer2
echo $FreeServertmpc72 >> $FreeServer2
#echo $FreeServertmpc73 >> $FreeServer2
#echo $FreeServertmpc74 >> $FreeServer2  
#echo $FreeServertmpc75 >> $FreeServer2
#echo $FreeServertmpc76 >> $FreeServer2
#Clean     
sed -i 's|.*<FONT COLOR="#75D246"> ||' $FreeServer2 
sed -i 's|<br> <p> and.*||' $FreeServer2
sed -i 's|.*<FONT COLOR="#104b99">||' $FreeServer2
sed -i 's|<br></FONT></B></font><br>||' $FreeServer2 
sed -i 's/<h1>//' $FreeServer2
sed -i 's|</h1>||' $FreeServer2
sed -i 's/    <h1>//' $FreeServer2
sed -i 's|.*style="display:none;">C ||' $FreeServer2 
sed -i 's|</textarea><textarea.*||' $FreeServer2   
sed -i 's*^:*C:*' $FreeServer2
sed -i 's|.*style="display: none"><center><strong>||' $FreeServer2
sed -i 's|</strong></center></div><div.*||' $FreeServer2
sed -i 's|.*value="||' $FreeServer2
sed -i 's|" id="prince"></input>||' $FreeServer2 
sed -i "s|.*color='violet'>||" $FreeServer2 
sed -i "s|.*color='red'>||" $FreeServer2 
sed -i "s|</font></B>||" $FreeServer2
sed -i "s|.*showline'>||" $FreeServer2
sed -i "s|</div>||" $FreeServer2
sed -i "s|</a></font></h3></center>||" $FreeServer2
sed -i "s|.*><center><strong>||" $FreeServer2 
sed -i "s|</strong></center></div><div.*||" $FreeServer2
sed -i "s|<br><br><a.*||" $FreeServer2
sed -i 's/ <font color="#5F8A10"> //' $FreeServer2
sed -i 's| </font>||' $FreeServer2
sed -i 's|.*style="color: #99cc00;">||' $FreeServer2
sed -i 's|</span></strong></em></h3>||' $FreeServer2
sed -i 's|.*class="tg-ahn8">Cline</th><th class="tg-juwk">||' $FreeServer2
sed -i 's|</th></tr><tr><td.*||' $FreeServer2
sed -i 's|<li>||' $FreeServer2
sed -i 's/    <h1>//' $FreeServer2
sed -i 's|</FONT>.*||' $FreeServer2
sed -i 's|</FONT><br>.*||' $FreeServer2
sed -i 's/.*COLOR="#00FF0D"> //' $FreeServer2 
sed -i 's/.*<FONT COLOR="#75D246"> //' $FreeServer2   
sed -i 's|</strong></p>||' $FreeServer2
sed -i 's/<center><h1><div class="label label-success"><strong>//' $FreeServer2
sed -i 's|</strong></a></font></div></h1></center>||' $FreeServer2
sed -i 's|</strong></a></font></div></center>||' $FreeServer2
sed -i 's/Your Free Test line : <strong>//' $FreeServer2
sed -i 's|</strong>||' $FreeServer2
sed -i 's/.*<strong>//' $FreeServer2
sed -i 's/Your Free Test line : <strong>//' $FreeServer2
sed -i 's/.*<br> //' $FreeServer2
sed -i 's| <h2><FONT.*||' $FreeServer2 
sed -i 's|<h5 id="text-val">||' $FreeServer2 
sed -i 's|</h5>||' $FreeServer2
sed -i 's/<p><font color="red">//' $FreeServer2
sed -i 's|.*COLOR="#75D246"> ||' $FreeServer2 
sed -i 's|</FONT><br>.*||' $FreeServer2
sed -i 's/Copy Your Free cccam : <strong>//' $FreeServer2
sed -i 's|<center><strong>||' $FreeServer2
sed -i 's| <br><h6>.*||' $FreeServer2
sed -i 's|</font><br />||' $FreeServer2
sed -i 's|.*<h2>||' $FreeServer2
sed -i 's| <br><br><span.*||' $FreeServer2
sed -i 's|.*CCCAM</font><br><br></center>||' $FreeServer2
sed -i 's|<h3><strong class="bg-primary">||' $FreeServer2
sed -i 's|</H3><br><br>||' $FreeServer2
sed -i 's|</h6></strong></center>||' $FreeServer2
sed -i 's/                                    <h4><p style="text-align: center;"><span class="id-color">//' $FreeServer2
sed -i 's|<center><div class="label label-success"><strong>||' $FreeServer2
sed -i 's|<a href="http://cccamstore.tv">www.cccamstore.tv</a></li>||' $FreeServer2
sed -i 's/								<center><h1><div class="label label-success"><strong>//' $FreeServer2
sed -i 's|</strong></a></font></div></h1></center>||' $FreeServer2
sed -i 's/<h1 class="wow fadeInDown" data-wow-delay="0.4s"> //' $FreeServer2
sed -i 's|</p> <!--edit here-->||' $FreeServer2
sed -i 's/<h4 style="background-color:MediumSeaGreen;"> //' $FreeServer2                                   
sed -i 's/<center><h3><div class="panel panel-success" ><div class="panel-heading">Your Free Cline is <br><br>//' $FreeServer2
sed -i 's/<div class="panel-heading">Your Free Cline is <br><br>//' $FreeServer2
sed -i 's/			<h4 style="background-color:MediumSeaGreen;">   <center><strong>//' $FreeServer2
sed -i 's/<p class="text-center">Your Free Test line : <strong>//' $FreeServer2
sed -i 's/<p class="text-center//' $FreeServer2
sed -i 's|</strong></p>||' $FreeServer2 
sed -i 's/<p class="text-center">Your Free Test line : <strong>//' $FreeServer2
sed -i 's|<h4 style="background-color:MediumSeaGreen;">   <center><strong>||' $FreeServer2
sed -i 's/<h4><p style="text-align: center;"><span class="id-color">//' $FreeServer2
sed -i 's/<h2><p style="text-align: center;"><span class="id-color">//' $FreeServer2
sed -i 's/<center><p style="text-align: center;" color="green"> <b class="c-pink"> //' $FreeServer2
sed -i 's|</b></p></center>||' $FreeServer2
sed -i 's/<p>//' $FreeServer2
sed -i 's|</p>||' $FreeServer2
sed -i 's|</p></span></h4>||' $FreeServer2
sed -i 's|<p style="text-align: center;"><strong>||' $FreeServer2
sed -i 's|">||' $FreeServer2
sed -i 's/">//' $FreeServer2  
sed -i 's|<br />||' $FreeServer2
sed -i 's|<span class="generalBorder</span>||' $FreeServer2
sed -i 's/.*<font size="8"><FONT COLOR="#00FF0D">//' $FreeServer2
sed -i 's/<font color="blue//' $FreeServer2 
sed -i 's|</a></font></div></h3></center>||' $FreeServer2 
sed -i 's/<h4><font size="4" color="lime//' $FreeServer2 
sed -i 's|</font></h4>||' $FreeServer2
sed -i 's|</p></h4>||' $FreeServer2
sed -i 's|</span>||' $FreeServer2
sed -i 's|<span class="text-blue||' $FreeServer2
sed -i 's|</span>||' $FreeServer2
sed -i 's/<h2> //' $FreeServer2
sed -i 's|</h2>||' $FreeServer2
sed -i 's|</h4>||' $FreeServer2
sed -i 's/<h2><p style="text-align: center;"><span class="id-color">//' $FreeServer2
sed -i 's|\n||' $FreeServer2
sed -i 's|\t||' $FreeServer2
sed -i 's|\r||' $FreeServer2
sed -i 's|  ||' $FreeServer2
sed '/^$/d' $FreeServer2 > $FreeServer 
cat $FreeServer > $FreeServer3 
rm -f $FreeServer2
rm -f $FreeServertmpa* $FreeServertmpb*
sed '/^\s*$/d' $EmuServer
echo "$LINE"
echo "*                        Finished                          *"
echo "*                   mino60 - RAED - Fairbird               *"
echo "*   You can find Servers lines in (/etc/CCcam.cfg)         *"
echo "$LINE"
#OScam Path
cd /etc/tuxbox/config
OUTPUT=/etc/tuxbox/config/oscam.server
OUTPUT2=/etc/tuxbox/config/oscam.server
SERVER=/tmp/oscam.options
SERVER=oscam.options
#function convert_servers 
OUTPUT="/etc/tuxbox/config/oscam.server"
OUTPUT2=/etc/tuxbox/config/oscam.server
HTTPSERV="http://ia601509.us.archive.org/5/items/dreamosat/server.txt"         
$WGET -O $SERVER $HTTPSERV > /dev/null 2>&1 
echo -n "Converting C lines"        
cat oscam.server > $OUTPUT
cat oscam.options >> $OUTPUT
grep -i "^C:.*" $FreeServer > conv.tmp
FS=" " 
while read line
do
F1=$(echo $line|cut -d"$FS" -f1)
SERVER=$(echo $line|cut -d"$FS" -f2)
PORT=$(echo $line|cut -d"$FS" -f3)
USER=$(echo $line|cut -d"$FS" -f4)
PASS=$(echo $line|cut -d"$FS" -f5)
#echo "SERVER: $SERVER PORT: $PORT USER: $USER PASS: $PASS"
echo -n "."
echo "[reader]" >> $OUTPUT2
echo "label = $SERVER" >> $OUTPUT2
echo "protocol = cccam" >> $OUTPUT2
echo "device = $SERVER,$PORT" >> $OUTPUT2
echo "user = $USER" >> $OUTPUT2		
echo "password = $PASS" >> $OUTPUT2		
echo "disablecrccws_only_for = 0E00:000000,0500:030B00,050F00;098C:000000;09C4:000000" >> $OUTPUT2
echo "inactivitytimeout = 30" >> $OUTPUT2
echo "group = 1" >> $OUTPUT2
echo "cccversion = 2.3.2" >> $OUTPUT2
echo "ccckeepalive = 1" >> $OUTPUT2
echo "audisabled = 1" >> $OUTPUT2
echo "disablecrccws = 1" >> $OUTPUT2 				
echo "" >> $OUTPUT
done < conv.tmp
rm conv.tmp
echo ""
#NCam Path
cd /etc/tuxbox/config
OUTPUT=/etc/tuxbox/config/ncam.server
OUTPUT2=/etc/tuxbox/config/ncam.server
SERVER=/tmp/ncam.options
SERVER=ncam.options
#function convert_servers 
OUTPUT="/etc/tuxbox/config/ncam.server"
OUTPUT2=/etc/tuxbox/config/ncam.server
HTTPSERV="http://ia601509.us.archive.org/5/items/dreamosat/server.txt"         
$WGET -O $SERVER $HTTPSERV > /dev/null 2>&1 
echo -n "Converting C lines"        
cat ncam.server > $OUTPUT
cat ncam.options >> $OUTPUT
grep -i "^C:.*" $FreeServer > conv.tmp
FS=" " 
while read line
do
F1=$(echo $line|cut -d"$FS" -f1)
SERVER=$(echo $line|cut -d"$FS" -f2)
PORT=$(echo $line|cut -d"$FS" -f3)
USER=$(echo $line|cut -d"$FS" -f4)
PASS=$(echo $line|cut -d"$FS" -f5)
#echo "SERVER: $SERVER PORT: $PORT USER: $USER PASS: $PASS"
echo -n "."
echo "[reader]" >> $OUTPUT2
echo "label = $SERVER" >> $OUTPUT2
echo "protocol = cccam" >> $OUTPUT2
echo "device = $SERVER,$PORT" >> $OUTPUT2
echo "user = $USER" >> $OUTPUT2		
echo "password = $PASS" >> $OUTPUT2		
echo "disablecrccws_only_for = 0E00:000000,0500:030B00,050F00;098C:000000;09C4:000000" >> $OUTPUT2
echo "inactivitytimeout = 30" >> $OUTPUT2
echo "group = 1" >> $OUTPUT2
echo "cccversion = 2.3.2" >> $OUTPUT2
echo "ccckeepalive = 1" >> $OUTPUT2
echo "audisabled = 1" >> $OUTPUT2
echo "disablecrccws = 1" >> $OUTPUT2 				
echo "" >> $OUTPUT
done < conv.tmp
rm conv.tmp
echo ""
#GCam Path
cd /etc/tuxbox/config
OUTPUT=/etc/tuxbox/config/gcam.server
OUTPUT2=/etc/tuxbox/config/gcam.server
SERVER=/tmp/gcam.options
SERVER=gcam.options
#function convert_servers 
OUTPUT="/etc/tuxbox/config/gcam.server"
OUTPUT2=/etc/tuxbox/config/gcam.server
HTTPSERV="http://ia601509.us.archive.org/5/items/dreamosat/server.txt"         
$WGET -O $SERVER $HTTPSERV > /dev/null 2>&1 
echo -n "Converting C lines"        
cat gcam.server > $OUTPUT
cat gcam.options >> $OUTPUT
grep -i "^C:.*" $FreeServer > conv.tmp
FS=" " 
while read line
do
F1=$(echo $line|cut -d"$FS" -f1)
SERVER=$(echo $line|cut -d"$FS" -f2)
PORT=$(echo $line|cut -d"$FS" -f3)
USER=$(echo $line|cut -d"$FS" -f4)
PASS=$(echo $line|cut -d"$FS" -f5)
#echo "SERVER: $SERVER PORT: $PORT USER: $USER PASS: $PASS"
echo -n "."
echo "[reader]" >> $OUTPUT2
echo "label = $SERVER" >> $OUTPUT2
echo "protocol = cccam" >> $OUTPUT2
echo "device = $SERVER,$PORT" >> $OUTPUT2
echo "user = $USER" >> $OUTPUT2		
echo "password = $PASS" >> $OUTPUT2		
echo "disablecrccws_only_for = 0E00:000000,0500:030B00,050F00;098C:000000;09C4:000000" >> $OUTPUT2
echo "inactivitytimeout = 30" >> $OUTPUT2
echo "group = 1" >> $OUTPUT2
echo "cccversion = 2.3.2" >> $OUTPUT2
echo "ccckeepalive = 1" >> $OUTPUT2
echo "audisabled = 1" >> $OUTPUT2
echo "disablecrccws = 1" >> $OUTPUT2 				
echo "" >> $OUTPUT
done < conv.tmp
rm conv.tmp
echo ""

exit 0
