# AnhkbotTwitchClip
streamlabs chatbot scripts to display twitch clips on stream, allowing viewers to like the clips.

Consists of 2 scripts. One for loading clips, and one for voting.


1- In script settings, choose the browser you want to use. It is adivsed to use a browser you do not usually use as if you have your main browser open, OBS will capture it instead and the end command will tastkill it. 
    Note: IE does not work with SLOBS at the moment. Firefox works perfectly.

2- On the chosen browser, make sure you change the settings to opening new tabs instead of new windows. 

3- on SL-OBS (or whatever streaming software you are using), and in the scene you want to display the clips: add 2 sources:

    a- a window capture: capturing the browser you want to use.
    
    b- a Text(GDI+): set to "Read from file", and choose ClipNo.txt in ClipVote folder - this displays the clip number.
    
    Note: you would need to run the commands at least once before adding the sources to OBS or SLOBS.
    
4- On Streamlabs Chatbot, set the display scene and the main scene hotkeys to macro 1 and macro 2. Set macro 1 and macro 2 to "Start" and "End" commands.

