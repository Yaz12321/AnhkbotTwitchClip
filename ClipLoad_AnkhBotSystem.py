#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, sys, json, os, codecs
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
import time



#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "ClipLoad"
Website = ""
Creator = "Yaz12321"
Version = "1.0"
Description = "Load twitch clips to browser (to be captured by OBS)"

settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

# Version: 

# > 1.0 < 
    # Official Release

# Future Version:
    # Replace the use of browser to direct use of SLOBS

class Settings:
    # Tries to load settings from file if given 
    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile = None):
        if settingsFile is not None and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig',mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig') 
        else: #set variables if no settings file
            self.LiveOnly = True
            self.StartCommand = "!break"
            self.EndCommand = "!endbreak"
            self.VoteCommand = "!like"
            self.Permission = "Caster"
            self.PermissionInfo = ""
            self.Response = "The winning clip was Clip {0} with {1} likes. {2} has received {3} {4} for creating the clips. And {5} has received {6} {4} for liking it!"
            self.StartAnnounce = "Send {0} followed by the number to give a like to the clip you like"
            self.FinalWarning = "You have 30 seconds left to like the clips"
            self.VoteResponse = "{0}, thanks for liking Clip {1}"
            self.PayoutCreator = 30
            self.PayoutVoter = 10
            self.Period = "month"
            self.Limit = 50
            self.Channel = ""
            self.height = 378
            self.width = 620
            self.Browser = "firefox"
            
    # Reload settings on save through UI
    def ReloadSettings(self, data):
        self.__dict__ = json.loads(data, encoding='utf-8-sig')
        return

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        with codecs.open(settingsFile,  encoding='utf-8-sig',mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig',mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
        return


#---------------------------------------
# Initialize Data on Load
#---------------------------------------
def Init():
    # Globals
    

    global t

    global end
    end = 0
    global Trigger
    Trigger = 0
    global n
    n = 0 

    global MySettings
    # Load in saved settings
    MySettings = Settings(settingsFile)

    # End of Init
    return

#---------------------------------------
# Reload Settings on Save
#---------------------------------------
def ReloadSettings(jsonData):
    # Globals
    global MySettings

    # Reload saved settings
    MySettings.ReloadSettings(jsonData)

    # End of ReloadSettings
    return




def Execute(data):

            
    if MySettings.LiveOnly == False:
        live = True
    else:
        live = Parent.IsLive()
    
    #Start Loading
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.StartCommand:
        global Trigger
        Trigger = 1
        global n
        n = 0 
        

        

            
        header = {'Accept': 'application/vnd.twitchtv.v5+json','Client-ID': '4l912jdf5x78xwe5l096mxti4tkzv3'}
        if MySettings.Channel == "":
            Channel = Parent.GetChannelName()
        else:
            Channel = MySettings.Channel
        api = "https://api.twitch.tv/kraken/clips/top?channel={}&period={}&trending=false&limit={}".format(Channel,MySettings.Period,int(MySettings.Limit))
        
        result = dict()
        result = json.loads(Parent.GetRequest(api, header))
        global path
        path = os.path.dirname(os.path.abspath(__file__))
        
 
        
        global allclips
        allclips = json.loads(result['response'])['clips']
        randomiser = range(int(MySettings.Limit))
        global chosenclips
        chosenclips = []
        i = 0
        while i < 10:
            chosenclips.append(randomiser.pop(Parent.GetRandom(0,len(randomiser))))
            i = i + 1
        global ClipsDetails
        ClipsDetails = []
        i = 0
        while i < 10:
            clipi = []
            
            clipi.append(allclips[chosenclips[i]]['slug'])
            clipi.append(allclips[chosenclips[i]]['title'])
            clipi.append(allclips[chosenclips[i]]['duration'])
            clipi.append(allclips[chosenclips[i]]['created_at'])
            clipi.append(allclips[chosenclips[i]]['curator']['name'])
            ClipsDetails.append(clipi)
            i=i+1
            
           

            
        f = open("Services/Scripts/ClipVote/f.txt","w+")
        f.write(str(ClipsDetails))
        f.close()

        


        
    #Stop Loading
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.EndCommand:
        global Trigger
        Trigger = 0
        global end
        end = 0
        os.system("taskkill /IM {}.exe".format(MySettings.Browser))
        

    return


def Tick():
    # Load Clip n
    if Trigger == 1:

        global Trigger
        Trigger = 0

        
        html = str("<iframe src=\"https://clips.twitch.tv/embed?clip={}\" frameborder=\"0\" allowfullscreen=\"true\" height=\"{}\" width=\"{}\"></iframe>".format(ClipsDetails[n][0],MySettings.height,MySettings.width))
        htmlf = open("Services/Scripts/ClipVote/ClipHTML.html","w+")
        htmlf.write(html)
        htmlf.close()
        os.system("start {}.exe {}\ClipHTML.html".format(MySettings.Browser,path))
        


        Clipno = open("Services/Scripts/ClipVote/ClipNo.txt","w+")
        Clipno.write(str("Clip {}".format(n+1)))
        Clipno.close()
        



        # Set current time
        
        global t
        t = time.time()
        
        #go to next clip, up to n = 9 . Loop when reaching 10 clips.
        if n < 9:
            global n
            n = n+1
        else:
            global n
            n = 0
        

        global end
        end = 1

    if end == 1 and time.time() > t + ClipsDetails[n-1][2] + 5:   
        

        global Trigger
        Trigger = 1
        
        global end
        end = 0
    return 

def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return
