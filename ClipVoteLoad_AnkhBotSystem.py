#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, sys, json, os, codecs
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
import time, threading, datetime
from ast import literal_eval

#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "ClipVoteLoad"
Website = ""
Creator = "Yaz12321"
Version = "1.1"
Description = "Load clips on stream, and let viewers like their favourites"

settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

# Version: 


# > 1.1 <
    # Added a feature to log winners.

# > 1.0 < 
    # Official Release - Joined Voting and Loading scripts

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
            self.FinalWarning = "You have {0} seconds left to like the clips"
            self.VoteResponse = "{0}, thanks for liking Clip {1}"
            self.PayoutCreator = 30
            self.PayoutVoter = 10
            self.Delay = 30
            self.NotInChat = "{0} did not receive their winnings because they are not in chat!"
            self.NClips = 10
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
            self.CDColour = "red"
            self.CDFont = "Arial"
            self.CDSize = 3
            self.CDB = False
            self.CDI = False
            self.CDU = False
            self.BGIW = 550
            self.BGIH = 50
            self.BGIT = 0
            self.BGIL = 0
            self.CNT = 0 
            self.CNL = 150
            self.CDT = 0 
            self.CDL = 150
            self.CDP = "relative"
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

    global tl

    global endl
    endl = 0
    global Triggerl
    Triggerl = 0
    global nl
    nl = 0
    global loaded
    loaded = 0
    # Globals
    global MySettings
    

    # Load in saved settings
    MySettings = Settings(settingsFile)
    global NClipsd
    NClipsd = MySettings.NClips

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

global Trigger
global Clips
global Clip1,Clip2,Clip3,Clip4,Clip5,Clip6,Clip7,Clip8,Clip9,Clip10,Clip11,Clip12,Clip13,Clip14,Clip15,Clip16,Clip17,Clip18,Clip19,Clip20,Clip21,Clip22,Clip23,Clip24,Clip25,Clip26,Clip27,Clip28,Clip29,Clip30,Clip31,Clip32,Clip33,Clip34,Clip35,Clip36,Clip37,Clip38,Clip39,Clip40,Clip41,Clip42,Clip43,Clip44,Clip45,Clip46,Clip47,Clip48,Clip49,Clip50
global t
global end
try:
    end
except NameError:
    end = 0


def Execute(data):
    path = os.path.dirname(os.path.abspath(__file__))

    if MySettings.LiveOnly == False:
        live = True 
    else:
        live = Parent.IsLive()
    
    #Start Voting
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.StartCommand:
        global Trigger
        Trigger = 1
        Parent.SendTwitchMessage(MySettings.StartAnnounce.format(MySettings.VoteCommand))
        global Clip1,Clip2,Clip3,Clip4,Clip5,Clip6,Clip7,Clip8,Clip9,Clip10,Clip11,Clip12,Clip13,Clip14,Clip15,Clip16,Clip17,Clip18,Clip19,Clip20,Clip21,Clip22,Clip23,Clip24,Clip25,Clip26,Clip27,Clip28,Clip29,Clip30,Clip31,Clip32,Clip33,Clip34,Clip35,Clip36,Clip37,Clip38,Clip39,Clip40,Clip41,Clip42,Clip43,Clip44,Clip45,Clip46,Clip47,Clip48,Clip49,Clip50
        Clip1=Clip2=Clip3=Clip4=Clip5=Clip6=Clip7=Clip8=Clip9=Clip10=Clip11=Clip12=Clip13=Clip14=Clip15=Clip16=Clip17=Clip18=Clip19=Clip20=Clip21=Clip22=Clip23=Clip24=Clip25=Clip26=Clip27=Clip28=Clip29=Clip30=Clip31=Clip32=Clip33=Clip34=Clip35=Clip36=Clip37=Clip38=Clip39=Clip40=Clip41=Clip42=Clip43=Clip44=Clip45=Clip46=Clip47=Clip48=Clip49=Clip50= []
        global Clips
        Clips = [Clip1,Clip2,Clip3,Clip4,Clip5,Clip6,Clip7,Clip8,Clip9,Clip10,Clip11,Clip12,Clip13,Clip14,Clip15,Clip16,Clip17,Clip18,Clip19,Clip20,Clip21,Clip22,Clip23,Clip24,Clip25,Clip26,Clip27,Clip28,Clip29,Clip30,Clip31,Clip32,Clip33,Clip34,Clip35,Clip36,Clip37,Clip38,Clip39,Clip40,Clip41,Clip42,Clip43,Clip44,Clip45,Clip46,Clip47,Clip48,Clip49,Clip50]
        try:
            data.GetParam(1)
            global NClipsd
            NClipsd = int(data.GetParam(1))
        except:
            global NClipsd
            NClipsd = MySettings.NClips
            
        global loaded
        loaded = 0

####
        htmlf = open("{}/ClipHTML.html".format(path),"w+")
        htmlf.write("<!DOCTYPE html> <html><head> <meta http-equiv=\"refresh\" content=\"1\"> </head> <body> </body> </html>")
        htmlf.close()
        if MySettings.Browser != "BrowserSource":
            os.system("start \"\" \"{}.exe\" \"{}\ClipHTML.html\"".format(MySettings.Browser,path)) #test
        time.sleep(MySettings.NextClip)
        global Triggerl
        Triggerl = 1
        global nl
        nl = 0

        
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
        while i < NClipsd:
            chosenclips.append(randomiser.pop(Parent.GetRandom(0,len(randomiser))))
            i = i + 1

        #Save needed details of clips on a .txt file
        global ClipsDetails
        ClipsDetails = []
        i = 0
        while i < NClipsd:
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
#####

    #End Voting
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.EndCommand and Trigger == 1:
        ##Inform viewers that voting will be over
        Parent.SendTwitchMessage(MySettings.FinalWarning.format(MySettings.Delay)) 
        # Wait Delay
        global t
        t = time.time()
        global end
        end = 1

###
    #Stop Loading
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.EndCommand:
        global Triggerl
        Triggerl = 0
        global endl
        endl = 0

        #kill browser
        if MySettings.Browser != "BrowserSource":
            os.system("taskkill /IM {}.exe".format(MySettings.Browser))
####
    #Voting    
    if live == True and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.VoteCommand and Trigger == 1:
        try:
            if 0 < int(data.GetParam(1)) <= loaded:
            
                ##Check if user already liked the clip
                if data.User not in Clips[int(data.GetParam(1))-1]:
                    ##add voter name to voted clip
                    global Clips
                    Clips[int(data.GetParam(1))-1] = Clips[int(data.GetParam(1))-1] +[data.User]
                    Parent.SendTwitchMessage(MySettings.VoteResponse.format(data.UserName,data.GetParam(1)))
        except:
            Parent.SendTwitchMessage("{}, NO! Just NO!".format(data.UserName))
          
    return



def Check():
    path = os.path.dirname(os.path.abspath(__file__))
    if end == 1 and time.time() > t + MySettings.Delay:
        global end
        end = 0        
        global Trigger
        Trigger = 0
        Counts = []
        for i in Clips:
            #Parent.SendTwitchMessage(str(i))
            Counts.append(len(i))
        WinCount = max(Counts)
        Winners = [i for i, j in enumerate(Counts) if j == WinCount]
        n = Winners[Parent.GetRandom(0,len(Winners))]
        
        ClipDetails = []
        f = open("{}/f.txt".format(path),"r")
        from ast import literal_eval
        ClipDetails = literal_eval(f.read())
        f.close()

        try:
            ##Get details of winning clip
            CWinner =  ClipDetails[n][4].lower()
            WinnerURL = "https://clips.twitch.tv/{}".format(ClipDetails[n][0])
            WinnerTitle = ClipDetails[n][1]
            WinnerTime = ClipDetails[n][3]
            ## pick a random voter of the winning clip
            VWinner = Clips[n][Parent.GetRandom(0,len(Clips[n]))]
            ## Add points to creator
            Parent.AddPoints(CWinner.lower(),MySettings.PayoutCreator)
            ##Add points to voter
            Parent.AddPoints(VWinner.lower(),MySettings.PayoutVoter) 
            Parent.SendTwitchMessage(MySettings.Response.format(n+1,WinCount,CWinner.upper(),MySettings.PayoutCreator,Parent.GetCurrencyName(),VWinner.upper(),MySettings.PayoutVoter,WinnerURL,WinnerTitle,WinnerTime))  #Announce winners
            if CWinner not in Parent.GetViewerList():
                Parent.SendTwitchMessage(MySettings.NotInChat.format(CWinner))

            path = os.path.dirname(os.path.abspath(__file__))

            try:
                Winnerslog = open("{}/WinList.txt".format(path),"a+")
            except:
                Winnerslog = open("{}/WinList.txt".format(path),"w+")

            winclip = str(datetime.datetime.now()) + ": " + CWinner + " (" + WinnerTitle + "), " + WinnerURL + "\n"
            Winnerslog.write(winclip)
            Winnerslog.close()

            try:
                Winsum = open("{}/WinLog.txt".format(path),"r+")
                Winnerssum = Winsum.read()
                Winsum.close()
                ws = literal_eval(Winnerssum)
            except:
                ws = {}
            
            try:
                ws[CWinner] = ws[CWinner] + 1
            except:
                ws[CWinner] = 1
            Winsum = open("{}/WinLog.txt".format(path),"w+")
            Winsum.write(str(ws))
            Winsum.close()
        except:
            Parent.SendTwitchMessage("No one has liked any clips")
        
        global Clip1,Clip2,Clip3,Clip4,Clip5,Clip6,Clip7,Clip8,Clip9,Clip10,Clip11,Clip12,Clip13,Clip14,Clip15,Clip16,Clip17,Clip18,Clip19,Clip20,Clip21,Clip22,Clip23,Clip24,Clip25,Clip26,Clip27,Clip28,Clip29,Clip30,Clip31,Clip32,Clip33,Clip34,Clip35,Clip36,Clip37,Clip38,Clip39,Clip40,Clip41,Clip42,Clip43,Clip44,Clip45,Clip46,Clip47,Clip48,Clip49,Clip50
        Clip1=Clip2=Clip3=Clip4=Clip5=Clip6=Clip7=Clip8=Clip9=Clip10=Clip11=Clip12=Clip13=Clip14=Clip15=Clip16=Clip17=Clip18=Clip19=Clip20=Clip21=Clip22=Clip23=Clip24=Clip25=Clip26=Clip27=Clip28=Clip29=Clip30=Clip31=Clip32=Clip33=Clip34=Clip35=Clip36=Clip37=Clip38=Clip39=Clip40=Clip41=Clip42=Clip43=Clip44=Clip45=Clip46=Clip47=Clip48=Clip49=Clip50= []




def Tick():
    Check()
    # Load Clip n
    if Triggerl == 1:
        path = os.path.dirname(os.path.abspath(__file__))

        global Triggerl
        Triggerl = 0

        ## LOADING THE CLIP, Clip slug: ClipsDetails[n][0]
        
        offsetleft = ClipsDetails[nl][6].split("-preview")
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

        fontdstyle = ""
        fontdstyleend = ""
        if MySettings.CDB:
            fontdstyle = fontdstyle + "<b>"
            fontdstyleend = "</b>" + fontdstyleend
        if MySettings.CDI:
            fontdstyle = fontstyle + "<i>"
            fontdstyleend = "</i>" + fontdstyleend
        if MySettings.CDU:
            fontdstyle = fontdstyle + "<u>"
            fontdstyleend = "</u>" + fontdstyleend
            
        

        

        #Save clip URL (here using embedded URL) to .html file
        htmlf = open("{}/ClipHTML.html".format(path),"w+")
        try:
            htmlf.write("<!DOCTYPE html> \n <html> \n <head> \n <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> \n <meta http-equiv=\"refresh\" content=\"{}\"> \n <style> \n .img {{position: fixed;top:{}px;left:{}px;z-index:1}} \n body{{background-color:{}}}\n .Clipno{{color: {};font-family: \"{}\";font-size: {}px;position: fixed;top: {}px;left: {}px;z-index: 2 }} \n ClipD{{color: {};font-family: \"{}\";font-size: {}px;position: {};top: {}px;left: {}px;z-index: 2 }} \n .vid {{position: fixed;top: {}px;left:{}px;z-index: 0}} \n </style> \n </head> \n <body> \n <div class=\"img\"> <image src=\"Clip_Number_Background.png\" width= {}px height = {}px></image> </div> \n <div class= \"Clipno\"> <p> {} Clip {} {} <ClipD> {} {} by {} {}  </ClipD>  </div> \n <div class=\"vid\"> \n <video width=\"{}\" height=\"{}\" controls autoplay >   \n <source src=\"{}.mp4\" type=\"video/mp4\" autoplay=\"true\"> \n Your browser does not support the video tag. \n </video> \n </div> \n <div class=\"clearfix\"></div> \n </body> \n </html> \n".format(ClipsDetails[nl][2],MySettings.BGIT,MySettings.BGIL,MySettings.BGColour,MySettings.CNColour,MySettings.CNFont,int(MySettings.CNSize),MySettings.CNT,MySettings.CNL,MySettings.CDColour,MySettings.CDFont,int(MySettings.CDSize),MySettings.CDP,MySettings.CDT,MySettings.CDL,MySettings.VT,MySettings.VL,MySettings.BGIW,MySettings.BGIH,fontstyle,nl+1,fontstyleend,fontdstyle,ClipsDetails[nl][1],ClipsDetails[nl][4],fontdstyleend,MySettings.width,MySettings.height,vidurl))
        except:
            pass
        htmlf.close()
        #Open browser and load html file.
##        os.system("start \"\" \"{}.exe\" \"{}\ClipHTML.html\"".format(MySettings.Browser,path))
        

        ## END OF LOADING THE CLIP
        
        #Load n to ClipNo.txt to be displayed on SLOBS
        Clipno = open("{}/ClipNo.txt".format(path),"w+")
        Clipno.write(str("Clip {}".format(nl+1)))
        Clipno.close()
        Details = open("{}/ClipDetails.txt".format(path),"w+")
        Details.write("{} by {}".format(ClipsDetails[nl][1],ClipsDetails[nl][4]))
        Details.close()

        #Set current time  
        global tl
        tl = time.time()
        
        #Go to next clip. Loop when reaching number of clips to be displayed.
        if nl < NClipsd - 1:
            global nl
            nl = nl+1
            if nl > loaded:
                global loaded
                loaded = nl
        else:
            global loaded
            loaded = NClipsd + 1
            global nl
            nl = 0
        global endl
        endl = 1

    #After duration of clip + delay
    if endl == 1 and time.time() > tl + ClipsDetails[nl-1][2]:   
        
        #Allow loading a new clip
        global Triggerl
        Triggerl = 1
        
        global endl
        endl = 0
    return

def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return
