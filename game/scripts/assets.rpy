﻿# ============================================================
# BACKGROUNDS
# ============================================================
image bg blank = "images/bg/blank.png"
image bg white = "images/bg/white.png"
image bg fieldsofisis = "images/bg/fields_of_isis.png"  #im.Scale("images/bg/fields_of_isis.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg fieldsofisis sky = "images/bg/fields_of_isis_sky.png" #im.Scale("images/bg/fields_of_isis_sky.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg glacies = "images/bg/glacies.png"
image bg glacies sky = "images/bg/glacies_sky.png"
image bg fullmoon = "images/bg/fullmoon.png"
image bg fullmoon sky = "images/bg/fullmoon_sky.png"
image bg fullmoon sky semisepia = "images/bg/fullmoon_sky_semisepia.png"

# ============================================================
# CG
# ============================================================   
image cg mainmenu = "images/cg/mainmenu.png"
image cg mainmenu video = Movie(channel="mainmenuvid", play="videos/mainmenu.avi")
image cg mainmenu grayscale = im.Grayscale("images/cg/mainmenu.png")

image cg prologue1 ada = "images/cg/prologue1_ada_intro.png"
image cg prologue1 rebelvehicles = "images/cg/prologue1_rebelvehicles.png"
image cg prologue1 transport1 = "images/cg/prologue1_transport_1.png"
image cg prologue1 transport2 = "images/cg/prologue1_transport_2.png"
image cg prologue1 transport3 = "images/cg/prologue1_transport_3_alt.png"

image cg prologue2 desertbase = "images/cg/prologue2_desertbase.png"
image cg prologue2 desertbase2 = "images/cg/prologue2_desertbase2.png"
image cg prologue2 ada = "images/cg/prologue2_ada_water.png"

image cg episode1 promethean = "images/cg/episode1_promethean_flames.png"
image cg episode1 promethean semisepia = "images/cg/episode1_promethean_flames_semisepia.png"
image cg episode1 crippledpyro = "images/cg/episode1_crippledpyro.png"
image cg episode1 crippledpyro2 = "images/cg/episode1_crippledpyro2.png"

# ============================================================
# ITEM IMAGES
# ============================================================
image map episode1 = "images/items/map_ep1.png"
image edenblueprints = "images/items/eden_blueprints.png"

# ============================================================
# ICONS
# ============================================================
image factionicon empire = im.FactorScale("images/icons/Empire3.png", 2)

# ============================================================
# UI
# ============================================================


# ============================================================
# CHARACTERS
# ============================================================
define ada = Character("Ada", color = '#0df5f3')
define sophia = Character("Sophia", color = '#60b0b0')
define imperial = Character("Imperial Unit", color = '#9600FF')
define imperialColonel = Character("Imperial Colonel", color = '#9600FF')
define rebels = Character("Rebel Units", color = '#FF4141')
define nvlChar = Character("", kind=nvl)

# ============================================================
# ANIMATIONS
# ============================================================
transform chapterTitlePos:
    xalign 0.45 yalign 0.36
    
transform chapterTitlePos2:
    xalign 0.55 yalign 0.5

transform chapterTitleAnim(dt = 0.5):
    on show:
        alpha 0 xzoom 4 yzoom 2
        linear dt alpha 1 xzoom 1 yzoom 1
    on hide:
        alpha 1 xzoom 1 yzoom 1
        linear dt alpha 0 xzoom 4 yzoom 2
    
transform spinY(dt = 1):
    xzoom 1
    block:
        easeout dt xzoom 0
        easein dt xzoom -1
        easeout dt xzoom 0
        easein dt xzoom 1
        repeat

transform foldOutY(dt = 0.1):
    yzoom 0
    linear dt yzoom 1

transform foldInY(dt = 0.2):
    linear dt yzoom 0

define fadeWhite = Fade(0.5,0,0.5,color='#ffffff')
define fadeWhiteSlow = Fade(1,0.5,1,color='#ffffff')
define flashWhite = Fade(0.1,0,0.1,color='#ffffff')
define dissolveUp = ImageDissolve("images/gfx/dissolvegradient.png", 0.5)
define dissolveBars = ImageDissolve("images/gfx/dissolvebars.png", 0.5)

# ============================================================
# TITLE TEXTS
# ============================================================
init python:
    def MakeTitleText(text, size=48):
        return Text(text=text, size=size, outlines={(2,"#222",3,3)})

image zklogo = "images/zk_logo.png"

image zklogo mainmenu:
    "images/zk_logo.png"
    xalign 0.3 ypos 0.2 yanchor 0.5 #alpha 0 xzoom 0
    #linear 0.2 xalign 0.5 alpha 1 xzoom 1
    xalign 0.5

image titleSunrise:
    #0.4
    Text("sunrise", size=64, outlines={(2,"#222",3,3)})
    xalign 0.8 ypos 0.32 yanchor 0.5 #alpha 0 xzoom 0 
    #linear 0.2 xalign 0.7 alpha 1 xzoom 1
    xalign 0.7

image gameOverText = Text("game over", size=48, outlines={(2,"#222",3,3)})
    
image preBattleText = Text("PREPARE FOR BATTLE", size=64, outlines={(3,"#222",2,2)})

image chapterTitle prologue1 = MakeTitleText("Prologue 1")
image chapterTitle2 prologue1 = MakeTitleText("Blood Dawn", 60)

image chapterTitle prologue2 = MakeTitleText("Prologue 2")
image chapterTitle2 prologue2 = MakeTitleText("Cold Path", 60)

image chapterTitle episode1 = MakeTitleText("Episode 1")
image chapterTitle2 episode1 = MakeTitleText("Awakening", 60)

# ============================================================
# MUSIC
# ============================================================
init python:
    soundtracks = {
        "Evacuation (Action)" : "<to 103>music/Evacuation (Action).mp3",
        "Inspiring" : "<to 106>music/Inspiring.mp3",
        "Inspiring 2" : "<to 153>music/Inspiring 2.mp3",
        "Intro" : "<to 71>music/Intro.mp3",
        "Intense" : "<to 86.5>music/Intense.mp3",
        "March" : "<to 66>music/March.mp3",
        "March (alt)" : "<to 146.3>music/March (alt).mp3",
        "Sentimental" : "<to 182.5>music/Sentimental.mp3",
        "Suspense" : "<to 113.3>music/Suspense.mp3",
        "Tension" : "<to 71.6>music/Tension.mp3",
    }

# ============================================================
# OTHER STUFF
# ============================================================
