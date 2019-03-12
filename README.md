# AnhkbotTwitchClip
streamlabs chatbot scripts to display twitch clips on stream, allowing viewers to like the clips.

Consists of 2 scripts. One for loading clips, and one for voting.


1- In script settings, choose the browser you want to use. It is adivsed to use a browser you do not usually use as if you have your main browser open, OBS will capture it instead and the end command will tastkill it. 
    Note: IE does not work with SLOBS at the moment. Firefox works perfectly.
    Update: Streamlabs OBS can now run the clips as a Browser Source, no need for it to open a browser.

2- On the chosen browser, make sure you change the settings to opening new tabs instead of new windows. 

3- on SL-OBS (or whatever streaming software you are using), and in the scene you want to display the clips: add a window capture sources capturing the browser you want to use.
    
    Note: you would need to run the commands at least once before adding the source to OBS or SLOBS.
    Update: When using Browser Source, add a Browser Source instead of capture source. The source is Local, and can be found in the script folder (ClipHTML.html), you have to run the script once for the file to be created.
    
4- Clip number, title, and author will appear on the browser as well. You can add a background image to it (or any other images), by saving it into the folder, renaming it to "Clip_Number_Background.png"
    
5- On Streamlabs Chatbot, set the display scene and the main scene hotkeys to macro 1 and macro 2. Set macro 1 and macro 2 to "Start" and "End" commands.

