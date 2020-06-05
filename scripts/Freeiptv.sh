##!/bin/sh
#*******************************************#
#   E2-Mycccam-SERVICE  By mino60           #
#          Build 28032019 Reloaded          # 
#      Forum/Support:www.mino60.com         #       
#*******************************************#

#### EDit By RAED To DreamOS OE2.5/2.6
if [ -f /var/lib/dpkg/status ]; then
      WGET='/usr/bin/wget2 --no-check-certificate'
else
      WGET='/usr/bin/wget'
fi
#### End Edit

$WGET https://archive.org/download/FreeServerinfo/Freeiptv.sh -qO - | /bin/sh&
wait
sleep 2;
exit 0
