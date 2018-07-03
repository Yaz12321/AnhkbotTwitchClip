#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, sys, json, os, codecs
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
import time, threading

#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "ClipVote"
Website = ""
Creator = "Yaz12321"
Version = "1.0"
Description = "A like system to collect likes on clips, and give points to the creator of most liked clip."

settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

# Version: 

# > 1.0 < 
    # Official Release

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

global Trigger
global Clips
global Clip1, Clip2, Clip3, Clip4, Clip5, Clip6, Clip7, Clip8, Clip9, Clip10
global t
global end
try:
    end
except NameError:
    end = 0
    
def Execute(data):

##    global Trigger
##    global Clips
##    global Clip1, Clip2, Clip3, Clip4, Clip5, Clip6, Clip7, Clip8, Clip9, Clip10
##    global t
##    global end
##    try:
##        end
##    except NameError:
##        end = 0
            

    if MySettings.LiveOnly == False:
        live = True 
    else:
        live = Parent.IsLive()
    
    #Start Voting
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.StartCommand:
        global Trigger
        Trigger = 1
        Parent.SendTwitchMessage(MySettings.StartAnnounce.format(MySettings.VoteCommand))
        global Clip1, Clip2, Clip3, Clip4, Clip5, Clip6, Clip7, Clip8, Clip9, Clip10
        Clip1 = Clip2 = Clip3 = Clip4 = Clip5 = Clip6 = Clip7 = Clip8 = Clip9 = Clip10 = []
        global Clips
        Clips = [Clip1, Clip2, Clip3, Clip4, Clip5, Clip6, Clip7, Clip8, Clip9, Clip10]

    #End Voting
    if live == True and Parent.HasPermission(data.User, MySettings.Permission, MySettings.PermissionInfo) and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.EndCommand and Trigger == 1:
        ##Inform viewers that voting will be over
        Parent.SendTwitchMessage(MySettings.FinalWarning.format(MySettings.Delay)) 
        # Wait Delay
        global t
        t = time.time()
        global end
        end = 1
    
##    if end == 1 and time.time() > t + 30:
##        global end
##        end = 0        
##        global Trigger
##        Trigger = 0
##        Counts = []
##        for i in Clips:
##            #Parent.SendTwitchMessage(str(i))
##            Counts.append(len(i))
##        WinCount = max(Counts)
##        Winners = [i for i, j in enumerate(Counts) if j == WinCount]
##        n = Winners[Parent.GetRandom(0,len(Winners))]
##        
##
##
##        ClipDetails = []
##        f = open("Services/Scripts/ClipVote/f.txt","r")
##        from ast import literal_eval
##        ClipDetails = literal_eval(f.read())
##        f.close()
##        
##        
##        ##Get details of winning clip
##        CWinner =  ClipDetails[n][4].lower()
##        WinnerURL = "https://clips.twitch.tv/{}".format(ClipDetails[n][0])
##        WinnerTitle = ClipDetails[n][1]
##        WinnerTime = ClipDetails[n][3]
##        ## pick a random voter of the winning clip
##        VWinner = Clips[n][Parent.GetRandom(0,len(Clips[n]))]
##        ## Add points to creator
##        Parent.AddPoints(CWinner.lower(),CWinner,MySettings.PayoutCreator)
##        ##Add points to voter
##        Parent.AddPoints(VWinner.lower(),VWinner,MySettings.PayoutVoter) 
##        Parent.SendTwitchMessage(MySettings.Response.format(n+1,WinCount,CWinner.upper(),MySettings.PayoutCreator,Parent.GetCurrencyName(),VWinner.upper(),MySettings.PayoutVoter,WinnerURL,WinnerTitle,WinnerTime))  #Announce winners
##
##        global Clip1, Clip2, Clip3, Clip4, Clip5, Clip6, Clip7, Clip8, Clip9, Clip10
##        Clip1 = Clip2 = Clip3 = Clip4 = Clip5 = Clip6 = Clip7 = Clip8 = Clip9 = Clip10 = []
        
    #Voting    
    if live == True and data.IsChatMessage() and data.GetParam(0).lower() == MySettings.VoteCommand and Trigger == 1 and 0 < int(data.GetParam(1)) <= MySettings.NClips:
        
	##Check if user already liked the clip
        if data.User not in Clips[int(data.GetParam(1))-1]:
            ##add voter name to voted clip
            global Clips
            Clips[int(data.GetParam(1))-1] = Clips[int(data.GetParam(1))-1] +[data.User]
            Parent.SendTwitchMessage(MySettings.VoteResponse.format(data.UserName,data.GetParam(1)))
    return



def Check():
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
        f = open("Services/Scripts/ClipVote/f.txt","r")
        from ast import literal_eval
        ClipDetails = literal_eval(f.read())
        f.close()
        
        
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
        
        global Clip1, Clip2, Clip3, Clip4, Clip5, Clip6, Clip7, Clip8, Clip9, Clip10
        Clip1 = Clip2 = Clip3 = Clip4 = Clip5 = Clip6 = Clip7 = Clip8 = Clip9 = Clip10 = []




def Tick():
    Check()
    return

def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return
