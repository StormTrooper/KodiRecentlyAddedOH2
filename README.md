# KodiRecentlyAddedOH2

Syncronization of Kodi recently added episodes to OpenHab2 items

This script was tested with Kodi 18 Leia nightly and OpenHab2 2.1 running on the Raspberry Pi 2

# Usage

Copy files:
mkdir /etc/openhab2/scripts/Kodi-Episodes/
cp kodi-episodes.py to /etc/openhab2/scripts/Kodi-Episodes/
cp kodi-episodes.sh to /etc/openhab2/scripts
sudo chmod +x /etc/openhab2/scripts/kodi-episodes.sh 


Edit kodi-episodes.py and change the values for:

```
OH2_Host
OH2_Port
Kodi_Host
Kodi_Port
Kodi_user
Kodi_pass
```

If you do not have Kodi password configured then comment these lines out:

```
#Kodi_user
#Kodi_pass 
```

Create a items file for Kodi:

```
String          Kodi_title1 "Title1: [%s]"
String          Kodi_episode1 "Episode1: [%s]"
String          Kodi_title2 "Title2: [%s]"
String          Kodi_episode2 "Episode2: [%s]"
String          Kodi_title3 "Title3: [%s]"
String          Kodi_episode3 "Episode3: [%s]"
String          Kodi_title4 "Title4: [%s]"
String          Kodi_episode4 "Episode4: [%s]"
String          Kodi_title5 "Title5: [%s]"
String          Kodi_episode5 "Episode5: [%s]"
```

Create rules file to schedule /etc/openhab2/scripts/kodi-episodes.sh to be run:

```
rule "GetKodiEpisodes"
when
        Time cron "0 0/15 * 1/1 * ? *"
then
        var String results = executeCommandLine("/etc/openhab2/scripts/kodi-episodes.sh",5*1000)
        logInfo("KodiEpisodes", results)
end
```


# License

Software licensed under GPL version 3 available on http://www.gnu.org/licenses/gpl.txt
