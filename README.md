# AnhkbotTwitchClip
streamlabs chatbot scripts to display twitch clips on stream, allowing viewers to like the clips.

Consists of 2 scripts. One for loading clips, and one for voting.

1- Make sure your Windows user is one word with no spaces. Otherwise, change line 199 "os.system("start {}.exe {}\ClipHTML.html".format(MySettings.Browser,path))" to os.system("start {}.exe C:\ClipHTML.html".format(MySettings.Browser)) or any path with no spaces.
2- Make sure the scripts folder is called ClipVote.
3- on OBS (or whatever streaming software you are using), and in the scene you want to display the clips: add 2 sources:
    a- a window capture: capturing the browser you want to use, setting the matching setting to same executable.
    b- a Text(GDI+): set to "Read from file", and choose ClipNo.txt in ClipVote folder.
4- On Streamlabs Chatbot, set the display scene and the main scene hotkeys to macro 1 and macro 2. Set macro 1 and macro 2 to "Start" and "End" commands.
