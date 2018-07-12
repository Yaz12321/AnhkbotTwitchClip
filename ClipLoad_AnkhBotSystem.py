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
Version = "1.1"
Description = "Load twitch clips to browser (to be captured by OBS)"

settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

# Version: 
# > 1.1 <
    # Changed clip upload: Clips now upload on a single browser page
    # Added Clip Number and Details to clip on browser
    # Added colours
    # fixed bugs
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
            self.NClips = 10
            self.NextClip = 5
            self.BGColour = "blue"
            self.CNColour = "red"
            self.CNFont = "Arial"
            self.CNSize = 3
            self.CNB = False
            self.CNI = False
            self.CNU = False
            self.BGIW = 550
            self.BGIH = 50
            self.BGIT = 0
            self.BGIL = 0
            self.CNT = 0 
            self.CNL = 150
            self.VT = 0
            self.VL = 10
            
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
    path = os.path.dirname(os.path.abspath(__file__))

            
    if MySettings.LiveOnly == False:
        live = True
    else:
        live = Parent.IsLive()
    
    #Start Loading
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.StartCommand:
        htmlf = open("{}/ClipHTML.html".format(path),"w+")
        htmlf.write("<!DOCTYPE html> <html><head> <meta http-equiv=\"refresh\" content=\"1\"> </head> <body> </body> </html>")
        htmlf.close()
        os.system("start \"\" \"{}.exe\" \"{}\ClipHTML.html\"".format(MySettings.Browser,path)) #test
        time.sleep(MySettings.NextClip)
        global Trigger
        Trigger = 1
        global n
        n = 0

        
        # Get clips through API    
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

        #Pick 10 clips to be displayed
        randomiser = range(int(MySettings.Limit))
        global chosenclips
        chosenclips = []
        i = 0
        while i < 10:
            chosenclips.append(randomiser.pop(Parent.GetRandom(0,len(randomiser))))
            i = i + 1

        #Save needed details of clips on a .txt file
        global ClipsDetails
        ClipsDetails = []
        i = 0
        while i < 10:
            clipi = []
            
            clipi.append(allclips[chosenclips[i]]['slug']) #ClipsDetails[0]
            clipi.append(allclips[chosenclips[i]]['title']) #ClipsDetails[1]
            clipi.append(allclips[chosenclips[i]]['duration']) #ClipsDetails[2]
            clipi.append(allclips[chosenclips[i]]['created_at']) #ClipsDetails[3]
            clipi.append(allclips[chosenclips[i]]['curator']['name']) #ClipsDetails[4]
            clipi.append(allclips[chosenclips[i]]['tracking_id']) #ClipsDetails[5]
            clipi.append(allclips[chosenclips[i]]['thumbnails']['small']) #ClipsDetails[6]
            #clipi.append(allclips[chosenclips[i]]['vod']['id']) #ClipsDetails[7]
            
            
            ClipsDetails.append(clipi)
            i=i+1      
           
        f = open("{}/f.txt".format(path),"w+")
        f.write(str(ClipsDetails))
        f.close()

        
    #Stop Loading
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.EndCommand:
        global Trigger
        Trigger = 0
        global end
        end = 0

        #kill browser
        os.system("taskkill /IM {}.exe".format(MySettings.Browser))
        

    return


def Tick():
    # Load Clip n
    if Trigger == 1:
        path = os.path.dirname(os.path.abspath(__file__))

        global Trigger
        Trigger = 0

        ## LOADING THE CLIP, Clip slug: ClipsDetails[n][0]
        
        offsetleft = ClipsDetails[n][6].split("-preview")
        vidurl = offsetleft[0]
        fontstyle = ""
        fontstyleend = ""
        if MySettings.CNB:
            fontstyle = fontstyle + "<b>"
            fontstyleend = "</b>" + fontstyleend
        if MySettings.CNI:
            fontstyle = fontstyle + "<i>"
            fontstyleend = "</i>" + fontstyleend
        if MySettings.CNU:
            fontstyle = fontstyle + "<u>"
            fontstyleend = "</u>" + fontstyleend
            
        

        

        #Save clip URL (here using embedded URL) to .html file
        html = str("<iframe src=\"https://clips.twitch.tv/embed?clip={}\" frameborder=\"0\" allowfullscreen=\"true\" height=\"{}\" width=\"{}\"></iframe>".format(ClipsDetails[n][0],MySettings.height,MySettings.width))
        htmlf = open("{}/ClipHTML.html".format(path),"w+")
        htmlf.write("<!DOCTYPE html> \n <html> \n <head> \n <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> \n <meta http-equiv=\"refresh\" content=\"{}\"> \n <style> \n .img {{position: fixed;top:{}px;left:{}px;z-index:1}} \n body{{background-color:{}}}\n .Clipno{{color: {};font-family: \"{}\";font-size: {}px;position: fixed;top: {}px;left: {}px;z-index: 2 }} \n .vid {{position: fixed;top: {}px;left:{}px;z-index: 0}} \n </style> \n </head> \n <body> \n <div class=\"img\"> <image src=\"Clip_Number_Background.png\" width= {}px height = {}px></image> </div> \n <div class= \"Clipno\"> <p> {} Clip {}: {} by {} {}</p>  </div> \n <div class=\"vid\"> \n <video width=\"{}\" height=\"{}\" controls autoplay >   \n <source src=\"{}.mp4\" type=\"video/mp4\" autoplay=\"true\"> \n Your browser does not support the video tag. \n </video> \n </div> \n <div class=\"clearfix\"></div> \n </body> \n </html> \n".format(ClipsDetails[n][2],MySettings.BGIT,MySettings.BGIL,MySettings.BGColour,MySettings.CNColour,MySettings.CNFont,int(MySettings.CNSize),MySettings.CNT,MySettings.CNL,MySettings.VT,MySettings.VL,MySettings.BGIW,MySettings.BGIH,fontstyle,n+1,ClipsDetails[n][1],ClipsDetails[n][4],fontstyleend,MySettings.width,MySettings.height,vidurl))
        htmlf.close()
        #Open browser and load html file.
##        os.system("start \"\" \"{}.exe\" \"{}\ClipHTML.html\"".format(MySettings.Browser,path))
        

        ## END OF LOADING THE CLIP
        
        #Load n to ClipNo.txt to be displayed on SLOBS
        Clipno = open("{}/ClipNo.txt".format(path),"w+")
        Clipno.write(str("Clip {}".format(n+1)))
        Clipno.close()
        Details = open("{}/ClipDetails.txt".format(path),"w+")
        Details.write("{} by {}".format(ClipsDetails[n][1],ClipsDetails[n][4]))
        Details.close()

        #Set current time  
        global t
        t = time.time()
        
        #Go to next clip. Loop when reaching number of clips to be displayed.
        if n < MySettings.NClips - 1:
            global n
            n = n+1
        else:
            global n
            n = 0
        global end
        end = 1

    #After duration of clip + delay
    if end == 1 and time.time() > t + ClipsDetails[n-1][2]:   
        
        #Allow loading a new clip
        global Trigger
        Trigger = 1
        
        global end
        end = 0
    return 

def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return
