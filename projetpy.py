import lvgl as lv

from imagetools import get_png_info, open_png


from lv_colors import lv_colors

lv.init()
import SDL
SDL.init()
disp_buf1 = lv.disp_buf_t()
buf1_1 = bytearray(480*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.buffer = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 480
disp_drv.ver_res = 320
disp_drv.register()

# Regsiter SDL mouse driver

indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER;
indev_drv.read_cb =SDL.mouse_read;
indev_drv.register();


# Register PNG image decoder
decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png
##### main script #####
LV_HOR_RES=240
LV_VER_RES=240
#var dark
LV_DEMO_WIDGETS_SLIDESHOW = 0
LV_THEME_DEFAULT_COLOR_PRIMARY=lv.color_hex(0x01a2b1)
LV_THEME_DEFAULT_COLOR_SECONDARY=lv.color_hex(0x44d1b6)
from lv_colors import lv_colors   #linux tp9a ou j'enleve
############################# main script #################
#create 2 screen *************************************************************
def event0_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn0 :
            print("Btn0 Clicked")
            lv.scr_load_anim(screen2,lv.SCR_LOAD_ANIM.MOVE_LEFT, 500, 500, False)
        else:
          if source == btn9:
            print("Btn9 Clicked")
            lv.scr_load_anim(screen1,lv.SCR_LOAD_ANIM.MOVE_RIGHT, 500, 500, False) #screen 1 to 2
##### main script screen 1 #####(create btn0 to log in to scrreen 2 and bnt01 for help)############"
# screen number 1
print('\n'.join(dir(lv.SCR_LOAD_ANIM)))
screen1 = lv.obj(None,None)

#//////////////     Image    /////////////////////////////////////////
# Register PNG image decoder   in screen 1 
with open('aaa.png','rb') as f:  #image green
  png_data = f.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})

img1 = lv.img(screen1,None)
lv.img.cache_set_size(2)
img1.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
img1.set_src(png_img_dsc)
img1.set_zoom(800)

with open('alma74.png','rb') as g: #image2 greenhouse
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
# pic greenhouse
img2 = lv.img(screen1,None)
lv.img.cache_set_size(2)
img2.align(lv.scr_act(), lv.ALIGN.CENTER, -30, -28)
img2.set_src(png_img_dsc)
img2.set_zoom(350)




# barre wifi et blututh et languages.......................................
style_shadow = lv.style_t()
style_shadow.init()
style_shadow.set_shadow_width(lv.STATE.DEFAULT, 10)
style_shadow.set_shadow_spread(lv.STATE.DEFAULT, 2)
LV_COLOR_GREEN=lv.color_hex3(0x00)  #black 0X00 ici si je veux changer la couleur 
style_shadow.set_shadow_color(lv.STATE.DEFAULT,LV_COLOR_GREEN)
obj1 = lv.obj(screen1,None)
obj1.set_size(460,35)
obj1.align(None,lv.ALIGN.CENTER, 0, -135)
obj1.add_style(obj1.PART.MAIN,style_shadow)
label002=lv.label(obj1,None)
label002.set_text("15:30")
label002.align(None,lv.ALIGN.CENTER,200,0)

#png wifi
with open('wifi1.png','rb') as k: #image3
  png_data = k.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
# pic wifi
img3 = lv.img(obj1,None)
lv.img.cache_set_size(2)
img3.align(obj1, lv.ALIGN.CENTER,-78,10)
img3.set_src(png_img_dsc)
img3.set_zoom(350)

#battery 

#png wifi
with open('battery.png','rb') as l: #image4
  png_data = l.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
# pic battery
img4 = lv.img(obj1,None)
lv.img.cache_set_size(2)
img4.align(obj1, lv.ALIGN.CENTER,175,0)
img4.set_src(png_img_dsc)
img4.set_zoom(200)

#audio
#png wifi
with open('audio.png','rb') as m: #image5
  png_data = m.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
# pic battery
img5 = lv.img(obj1,None)
lv.img.cache_set_size(2)
img5.align(obj1, lv.ALIGN.CENTER,135,0)
img5.set_src(png_img_dsc)
img5.set_zoom(155)

#bluetooth

with open('bluetooth.png','rb') as w: #image6
  png_data = w.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img6 = lv.img(obj1,None)
lv.img.cache_set_size(2)
img6.align(obj1, lv.ALIGN.CENTER,100,0)
img6.set_src(png_img_dsc)
img6.set_zoom(135)

#update
with open('mise.png','rb') as c: #image7
  png_data = c.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img7 = lv.img(obj1,None)
lv.img.cache_set_size(2)
img7.align(obj1, lv.ALIGN.CENTER,-55,0)
img7.set_src(png_img_dsc)
img7.set_zoom(145)


#share between pc and phone
with open('share.png','rb') as c: #image8
  png_data = c.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img8 = lv.img(obj1,None)
lv.img.cache_set_size(2)
img8.align(obj1, lv.ALIGN.CENTER,64,0)
img8.set_src(png_img_dsc)
img8.set_zoom(145)

#antivirus
with open('update.png','rb') as v: #image9
  png_data = v.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img9 = lv.img(obj1,None)
lv.img.cache_set_size(2)
img9.align(obj1, lv.ALIGN.CENTER,20,0)
img9.set_src(png_img_dsc)
img9.set_zoom(145)

#rotation
with open('rotation.png','rb') as v: #image10
  png_data = v.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img10= lv.img(obj1,None)
lv.img.cache_set_size(2)
img10.align(obj1, lv.ALIGN.CENTER,-14,2)
img10.set_src(png_img_dsc)
img10.set_zoom(170)


#//////////////////////////////////////////////////////
#les langues 
def event001_handler(obj, event):
    if event == lv.EVENT.VALUE_CHANGED:
        option = " "*10 # should be large enough to store the option
        obj.get_selected_str(option, len(option))
        # .strip() removes trailing spaces
        print("Option: \"%s\"" % option.strip())

# Create a drop down list
ddlist = lv.dropdown(obj1)
ddlist.set_options("\n".join([
                    "English",
                    "French",
                    "Arab",
                    "other"]))

ddlist.align(None, lv.ALIGN.IN_TOP_MID,-166, 3)
ddlist.set_event_cb(event001_handler)
ddlist.set_size(100,30)
#.............................

label001 = lv.label(screen1,None)
label001.set_text("Welcome to my Greenhouse")
label001.align(None,lv.ALIGN.CENTER,0,-80)
btn0 = lv.btn(screen1,None)
btn0.set_event_cb(event0_handler)
btn0.align(None,lv.ALIGN.CENTER,-160,135)
btn0.set_size(143,35)
btn0.add_style(btn0.PART.MAIN,style_shadow)
label0=lv.label(btn0,None)
label0.set_text("Log in")   #Go to screen2 
label0.align(None,lv.ALIGN.CENTER,10,50)
#button exit   .....0..........................
def eventexit_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn009:
            print("Btn1 Clicked")
            lv.scr_load_anim(screenexit,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            if source == btnexit:
                print("Btn2 Clicked")
                lv.scr_load_anim(screen1,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
btn009 = lv.btn(screen1,None)
btn009.align(None,lv.ALIGN.CENTER,+156,135)
btn009.set_size(141,35)
btn009.add_style(btn009.PART.MAIN,style_shadow)
btn009.set_event_cb(eventexit_handler)
label009=lv.label(btn009,None)
label009.set_text("Power") 

screenexit = lv.obj(None,None)
#labelexit0 = lv.label(screenexit,None)
#labelexit0.set_text("screenexit")
#labelexit0.align(None,lv.ALIGN.CENTER,0,-40)
btnexit = lv.btn(screenexit,None)
btnexit.set_event_cb(eventexit_handler)
btnexit.align(None,lv.ALIGN.CENTER,-160,-130)
btnexit.set_size(30,25)
labelexit=lv.label(btnexit,None)
labelexit.set_text("<-")
            
# create a simple bar
barfin = lv.bar(screenexit,None)
barfin.set_size(430,5)
barfin.align(None,lv.ALIGN.CENTER,0,-110)
barfin.set_anim_time(14000)
barfin.set_value(100,lv.ANIM.ON)



#my photooo 78961685465323654361332232122++++++++++++

##### main script #####

label1 = lv.label(screenexit,None)
label1.set_long_mode(lv.label.LONG.BREAK)  # Break the long lines
label1.set_recolor(True)                   # Enable re-coloring by commands in the text
label1.set_align(lv.label.ALIGN.CENTER)        # Center aligned lines
label1.set_text(
""" #0000ff Please feel free to contact me if you need any further#
#0000ff information. I'll be there.#
#0000ff Thank you for  this opportunity# 
 """)
label1.set_width(400)
label1.align(None,lv.ALIGN.CENTER, 0, -50)
#mails
label3 = lv.label(screenexit,None)
label3.set_long_mode(lv.label.LONG.BREAK)  # Break the long lines
label3.set_recolor(True)                   # Enable re-coloring by commands in the text
label3.set_align(lv.label.ALIGN.CENTER)        # Center aligned lines
label3.set_text(
"""#ff0000 mahmoudialma96@gmail.com# 
 """)
label3.set_width(300)
label3.align(None,lv.ALIGN.CENTER, 0, 110)
label4 = lv.label(screenexit,None)   #other mail
label4.set_long_mode(lv.label.LONG.BREAK)  # Break the long lines
label4.set_recolor(True)                   # Enable re-coloring by commands in the text
label4.set_align(lv.label.ALIGN.CENTER)  
label4.set_text(
"""#ff0000 alma.mahmoudi@enicar.u-carthage.tn# 
 """)
label4.set_width(500)
label4.align(None,lv.ALIGN.CENTER,26, 130)   

#pic mail
with open('mymail.png','rb') as g: #mail
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img17 = lv.img(screenexit,None)
lv.img.cache_set_size(2)
img17.align(screenexit, lv.ALIGN.CENTER, -140,100)
img17.set_src(png_img_dsc)
img17.set_zoom(150)


#picture in obj
stylepicfin_shadow = lv.style_t()
stylepicfin_shadow.init()
stylepicfin_shadow.set_shadow_width(lv.STATE.DEFAULT, 10)
stylepicfin_shadow.set_shadow_spread(lv.STATE.DEFAULT, 1)
LV_COLOR_BLUE=lv.color_hex3(0xF)
stylepicfin_shadow.set_shadow_color(lv.STATE.DEFAULT,LV_COLOR_BLUE)

objpic = lv.obj(screenexit,None)
objpic.set_size(90,90)
objpic.align(None,lv.ALIGN.CENTER, 0, 30)
objpic.add_style(objpic.PART.MAIN,stylepicfin_shadow)

#1111111111    ligne n'est pas en repos    1111111111111
label2 = lv.label(screenexit, None)
label2.set_long_mode(lv.label.LONG.SROLL_CIRC)
label2.set_width(380)
label2.set_text(" I hope you like it so good bye and good luck for you ")
label2.align(None, lv.ALIGN.CENTER,20,-136)


with open('mypic1.png','rb') as g: #my pic 16
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img16 = lv.img(objpic,None)
lv.img.cache_set_size(2)
img16.align(objpic, lv.ALIGN.CENTER, -55, -80)
img16.set_src(png_img_dsc)
img16.set_zoom(121)


# create a screen 0 for any help 
def event01_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn01 :
            print("Btn01 Clicked")
            lv.scr_load_anim(screen0,lv.SCR_LOAD_ANIM.MOVE_TOP, 500, 500, False)
        else:
          if source == btn02:
            print("Btn02 Clicked")
            lv.scr_load_anim(screen1,lv.SCR_LOAD_ANIM.MOVE_BOTTOM, 500, 500, False) #screen 0 to 1
btn01 = lv.btn(screen1,None)
btn01.set_event_cb(event01_handler)
btn01.align(None,lv.ALIGN.CENTER,0,135)
btn01.set_size(143,35)
btn01.add_style(btn01.PART.MAIN,style_shadow)
label01=lv.label(btn01,None)
label01.set_text("Help")  # go to help where we found a number to call for help 

#screen 0 
screen0 = lv.obj(None,None)
label03 = lv.label(screen0,None)
label03.align(None,lv.ALIGN.CENTER,-120,-130)
label03.set_text('''I hope everything is going well for you 
If you have any problem don't hesitate 
to call us in our numbers :

     +21671963475
     +21676321478''')

btn02 = lv.btn(screen0,None)   #help us to go(return) to screen 1
btn02.set_event_cb(event01_handler)
btn02.align(None,lv.ALIGN.CENTER,-160,-130)
btn02.set_size(30,25)
label02=lv.label(btn02,None)
label02.set_text("<-")  
#create keybord (number) in screen 0 
LV0_HOR_RES = 240
LV0_VER_RES = 240
def ta0_event_cb(ta,event):
    if  event == lv.EVENT.VALUE_CHANGED:
        txt = ta.get_text()
        pos = ta.get_cursor_pos()
        # find position of ":" in text
        colon_pos= txt.find(":")
        # if there are more than 2 digits before the colon, remove the last one entered
        if colon_pos == 3:
            ta.del_char()
        if colon_pos != -1:
            # if there are more than 3 digits after the ":" remove the last one entered
            rest = txt[colon_pos:]
            if len(rest) > 3:
                ta.del_char()
# create a textarea (where we create the number phone)
ta = lv.textarea(screen0,None)
ta.set_event_cb(ta0_event_cb)
ta.set_accepted_chars("0123456789:")
ta.set_max_length(8)  #lenght of number is 8 
ta.set_one_line(True)
ta.set_text(" ");
ta.align(None,lv.ALIGN.CENTER,15,-10)
ta.set_size(170,35)
kb_map = ["1","2", "3", " ","\n",
          "4", "5", "6", " ", "\n",
          "7", "8", "9",lv.SYMBOL.BACKSPACE,"\n",
          "0",lv.SYMBOL.LEFT,lv.SYMBOL.RIGHT," ",""]

kb_ctlr_map = [lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.HIDDEN,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.HIDDEN,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.NO_REPEAT,
               lv.btnmatrix.CTRL.HIDDEN]
# Create a keyboard of number (phone number)
kb = lv.keyboard(screen0, None)
kb.set_size(LV0_HOR_RES, LV0_VER_RES // 2)
kb.set_mode(lv.keyboard.MODE.SPECIAL)
kb.set_map(lv.keyboard.MODE.SPECIAL,kb_map)
kb.set_ctrl_map(lv.keyboard.MODE.SPECIAL,kb_ctlr_map)
kb.set_textarea(ta)
kb.align(None,lv.ALIGN.CENTER,0,80)



with open('phone.png','rb') as h: #image phone red
  png_data = h.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
# pic greenhouse
img12 = lv.img(screen0,None)
lv.img.cache_set_size(2)
img12.align(screen0, lv.ALIGN.CENTER, 108, 60)
img12.set_src(png_img_dsc)



with open('phonev.png','rb') as h: #image phone green
  png_data = h.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
# pic greenhouse
img13 = lv.img(screen0,None)
lv.img.cache_set_size(2)
img13.align(screen0, lv.ALIGN.CENTER, 94, -18)
img13.set_src(png_img_dsc)
img13.set_zoom(138)
##### main script screen 2 #####(bt1 sign in to go to screen 3 and btn9 to ruturn to screen 1)
screen2 = lv.obj(None,None)

def event1_handler(source,evt):  #screen 1 and 3 
    if evt == lv.EVENT.CLICKED:
        if source == btn1 :
            print("Btn1 Clicked")
            lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
          if source == btn5:
            print("Btn5 Clicked")
            lv.scr_load_anim(screen1,lv.SCR_LOAD_ANIM.MOVE_TOP, 500, 500, False) #screen 3 to 1
##### ((((((((((((( main script screen 3 ))))))))))))))####
screen3 = lv.obj(None,None)
#pic screen3 
with open('fin123.png','rb') as f:
  png_data = f.read()
png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})


img20 = lv.img(screen3,None)
lv.img.cache_set_size(2)
img20.align(screen3, lv.ALIGN.CENTER, -170, -105)
img20.set_src(png_img_dsc)
img20.set_zoom(326)


#create a button to reutuern from screen 3 to screen 1 (exit)
btn5 = lv.btn(screen3,None)
btn5.set_event_cb(event1_handler)
btn5.align(None,lv.ALIGN.CENTER,-169,154)
btn5.set_size(56,20)
label5=lv.label(btn5,None)
label5.set_text("EXIT") #return to screen number one 



#screen advices+-+-+-+-+--+-+-+-+-+-+-+-+-+-+
def eventad_handler(source,evt):  #screen 1 and 3 
    if evt == lv.EVENT.CLICKED:
        if source == btn50 :
            print("Btn50 Clicked")
            lv.scr_load_anim(screenad,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            if source == btn501:
                print("Btn501 Clicked")
                lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.MOVE_TOP, 500, 500, False) #screen 3 to 1

btn50 = lv.btn(screen3,None)
btn50.set_event_cb(eventad_handler)
btn50.align(None,lv.ALIGN.CENTER,-105,154)
btn50.set_size(80,20)
label50=lv.label(btn50,None)
label50.set_text("Advices") #go to screen advices screenad

screenad = lv.obj(None,None)

btn501 = lv.btn(screenad,None)
btn501.set_event_cb(eventad_handler)
btn501.align(None,lv.ALIGN.CENTER,-138,-140)
btn501.set_size(29,25)
label501=lv.label(btn501,None)
label501.set_text("<-") #return to screen number one 

#screen advices
objad = lv.obj(screenad,None)
objad.set_size(400,250)
objad.align(None,lv.ALIGN.CENTER, 0,0)

labelsell = lv.label(objad,None)
labelsell.set_text(''' Open door, window and tarpaulin to maintain an
ideal growing temperature.

Screen the sun's rays with a shade net in order to
 reduce the temperature and limit the impact
 of sunshine.
Insulate your greenhouse using plastic a bubble
 inside.

Anticipate the weather thanks to a weather station 
to prevent sudden drops in temperature.''')
labelsell.align(objad,lv.ALIGN.CENTER,10,0)


#**************************************************************************************


def event_handler(source,evt):
    if  evt == lv.EVENT.VALUE_CHANGED:
        if source.is_checked():
            print("State: checked")
        else:
            print("State: unchecked")   #settings augmenter et diminuer 

def event_handler(source,evt):   #calendrier
    if  evt == lv.EVENT.VALUE_CHANGED:
        date = lv.calendar.get_pressed_date(source)
        if date:
            print("Clicked date: %02d.%02d.%02d"%(date.day, date.month, date.year))
def ta_event_cb(ta,event):
    if  event == lv.EVENT.CLICKED:
        # Focus on the clicked text area 
       if kb != None:
           kb.set_textarea(ta)
       elif event == LV_EVENT_INSERT:
        string = lv.event.get_data()
        if string[0] == '\n':
            print("Ready")
def event_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn1:
            # treat "clicked" events only for btn1
            print("Clicked")
        elif evt == lv.EVENT.VALUE_CHANGED:
            print("Toggled")
# Create a Tab view object******************
tabview = lv.tabview(screen2, None)


# Add 3 tabs (the tabs are page (lv_page) and can be scrolled
tab1=tabview.add_tab("Home")  #tab1
tab2=tabview.add_tab("Setting")
tab3=tabview.add_tab("12/05/2021")  #calendreier 


# Add content to the tabs
label = lv.label(tab1,None)
label.set_text('''.''')
label.align(None,lv.ALIGN.CENTER,50,50)

label = lv.label(tab2,None)
label.set_text("")

label = lv.label(tab3, None)
label.set_text("");

#***************************************************************
# Create the password box (password)
pwd_ta = lv.textarea(tab1, None)
pwd_ta.set_text("")
pwd_ta.set_pwd_mode(True)
pwd_ta.set_one_line(True)
pwd_ta.set_cursor_hidden(True)
pwd_ta.set_width(LV_HOR_RES // 2 - 10)
pwd_ta.set_pos(270, 70)
pwd_ta.set_event_cb(ta_event_cb)
# Create a label and position it above the text box 
pwd_label = lv.label(tab1, None)
pwd_label.set_text("Password:")
pwd_label.align(pwd_ta, lv.ALIGN.OUT_TOP_LEFT, -90,30)
#**********************************tab1 Home**************************
# Create the one-line mode text area (nom)
oneline_ta = lv.textarea(tab1, pwd_ta)
oneline_ta.set_pwd_mode(False)
oneline_ta.set_cursor_hidden(True)
oneline_ta.set_pos(270, 30)
oneline_ta.set_event_cb(ta_event_cb)

# Create a label and position it above the text box 
oneline_label = lv.label(tab1, None)
oneline_label.set_text("User:")
oneline_label.align(oneline_ta, lv.ALIGN.OUT_TOP_LEFT, -90, 30)


#pic of user   

objuser = lv.obj(tab1,None)
objuser.set_size(80,80)
objuser.align(None,lv.ALIGN.CENTER, -130, -67)


with open('user.png','rb') as g: #image19 user
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
# pic greenhouse
img19 = lv.img(objuser,None)
lv.img.cache_set_size(2)
img19.align(objuser, lv.ALIGN.CENTER, 9, -5)
img19.set_src(png_img_dsc)
img19.set_zoom(300)

#*************************************************************

# create a simple button
btn1 = lv.btn(tab1,None)
# attach the callback
btn1.set_event_cb(event1_handler)
btn1.set_size(100,30)
btn1.align(None,lv.ALIGN.CENTER,146,-5)
label=lv.label(btn1,None)
label.set_text("Sign in")
label.set_size(100,30)
label.align(None,lv.ALIGN.CENTER,0,0)    #if we click in sign in we go to screen 3



#create a button to reutuern to screen 1 
btn9 = lv.btn(tab1,None)
btn9.set_event_cb(event0_handler)
btn9.align(None,lv.ALIGN.CENTER,-160,-105)
btn9.set_size(30,25)
label9=lv.label(btn9,None)
label9.set_text("<-") #return to screen number one 

lv.scr_load(screen1)

# creatz  i agree to the termes check
def event22_handler(source,evt):
    if  evt == lv.EVENT.VALUE_CHANGED:
        if source.is_checked():
            print("State: checked")
        else:
            print("State: unchecked")
            
# create a checkbox
cb = lv.checkbox(tab1,None)
cb.set_text("I agree to the terms and conditions.")
cb.set_size(200,30)
cb.align(None,lv.ALIGN.CENTER, -60, -6)
# attach the callback
cb.set_event_cb(event22_handler)

##### main script screen 3 #####*********************************************************


# *********** button 10 for the light (light temperature....)***********************
def event310_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn10:
            print("Btn10 Clicked")
            lv.scr_load_anim(screen31,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            print("Btn310 Clicked")
            lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False) 
btn10 = lv.btn(screen3,None)
# attach the callback
btn10.set_event_cb(event310_handler)
btn10.set_size(110,60)
btn10.align(None,lv.ALIGN.CENTER,31,-80)
btn10.add_style(btn10.PART.MAIN,style_shadow)


label10=lv.label(btn10,None)
label10.set_text("Light")
label10.set_size(100,30)
label10.align(None,lv.ALIGN.CENTER,0,0)  
#create screen31 for light  
screen31 = lv.obj(None,None)
btn310 = lv.btn(screen31,None)
btn310.set_event_cb(event310_handler)
btn310.align(None,lv.ALIGN.CENTER,-165,-135)
btn310.set_size(30,25)
label310=lv.label(btn310,None)
label310.set_text("<-")
#temperature + pic++++++++++++++------------------------- 
with open('temp.png','rb') as g: #pic for button
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img30 = lv.img(screen31,None)
lv.img.cache_set_size(2)
img30.align(screen31, lv.ALIGN.CENTER,-45, -55)
img30.set_src(png_img_dsc)
img30.set_zoom(350)
#+++++++++++++++++++++++++++++++++++++++++++++++++
def increment_event_cb(source,evt):   #pour augmenter ou bien diminuer la temperature
    if evt == lv.EVENT.SHORT_CLICKED or evt == lv.EVENT.LONG_PRESSED_REPEAT:
        spinbox.increment()        
def decrement_event_cb(source,evt):
    if evt == lv.EVENT.SHORT_CLICKED or evt == lv.EVENT.LONG_PRESSED_REPEAT:
        spinbox.decrement()
spinbox = lv.spinbox(screen31,None)
spinbox.set_range(-1000,90000)
spinbox.set_digit_format(3,2)
spinbox.step_prev()
spinbox.set_width(100)
spinbox.align(None,lv.ALIGN.CENTER,0,100)
h = spinbox.get_height()
btn310 = lv.btn(screen31,None)
btn310.set_size(h,h)
btn310.align(spinbox,lv.ALIGN.OUT_RIGHT_MID, 5, 0)
lv.theme_apply(btn310,lv.THEME.SPINBOX_BTN)
btn310.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.PLUS)
btn310.set_event_cb(increment_event_cb)
btn310 = lv.btn(screen31, btn310)
btn310.align(spinbox, lv.ALIGN.OUT_LEFT_MID, -5, 0)
btn310.set_event_cb(decrement_event_cb)
btn310.set_style_local_value_str(lv.btn.PART.MAIN, lv.STATE.DEFAULT, lv.SYMBOL.MINUS)

labeltemp = lv.label(screen31,None)
labeltemp.set_text("Temperature")
labeltemp.align(None,lv.ALIGN.CENTER,-15, -124)

#****************** but 2 water  ******************************
def event320_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn11:
            print("Btn11 Clicked")
            lv.scr_load_anim(screen32,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            print("Btn320 Clicked")
            lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False) #from screen 32 to screen 3


#  buttons creen 3 
btn11 = lv.btn(screen3,None)
btn11.set_event_cb(event320_handler)
btn11.set_size(110,60)
btn11.align(None,lv.ALIGN.CENTER,165,-80)
btn11.add_style(btn11.PART.MAIN,style_shadow)
label11=lv.label(btn11,None)
label11.set_text("Water")
label11.set_size(100,30)
label11.align(None,lv.ALIGN.CENTER,0,0) 
 
#create screen31 for light  
screen32 = lv.obj(None,None)
btn320 = lv.btn(screen32,None)  #to return to screen3
btn320.set_event_cb(event320_handler)
btn320.align(None,lv.ALIGN.CENTER,-165,-135)
btn320.set_size(30,25)
label320=lv.label(btn320,None)
label320.set_text("<-")
#____________>
obj1water = lv.obj(screen32,None)
obj1water.set_size(100,100)
obj1water.align(None,lv.ALIGN.CENTER, -130, 70)

def eventwater_handler(obj,evt):
    if evt == lv.EVENT.VALUE_CHANGED:
        state = obj.get_state()
        if state:
            print("State: On")
        else:
            print("State: Off")            

#Create a switch and apply the styles
sw1water = lv.switch(obj1water, None)
sw1water.align(None, lv.ALIGN.CENTER, 0, +20)
sw1water.set_event_cb(eventwater_handler)


labelwater= lv.label(obj1water,None)
labelwater.set_text("OFF | ON")
labelwater.align(None,lv.ALIGN.CENTER,0,-20)

# create the gauge
gauge1=lv.gauge(screen32,None)
gauge1.set_needle_count(1, lv_colors.BLUE)
gauge1.set_size(180,180)
gauge1.align(None,lv.ALIGN.CENTER,90,0)

# Set the values
gauge1.set_value(0, 50)

def eventagree_handler(source,evt):
    if  evt == lv.EVENT.VALUE_CHANGED:
        if source.is_checked():
            print("State: agree")
        else:
            print("State: not agree")
            
# create a checkbox
cb = lv.checkbox(screen32,None)
cb.set_text("I agree to this vitesse.")
cb.align(None,lv.ALIGN.CENTER, 90, 110)
# attach the callback
cb.set_event_cb(eventagree_handler)

labelsell = lv.label(screen32,None)
labelsell.set_text("Water Velocity")
labelsell.align(None,lv.ALIGN.CENTER,90,-110)
#img water
with open('water1.png','rb') as g: 
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img31 = lv.img(screen32,None)
lv.img.cache_set_size(2)
img31.align(screen32, lv.ALIGN.CENTER, -120, -80)
img31.set_src(png_img_dsc)
img31.set_zoom(600)
#*********************  but 3 alimentation minerale  *****************************
def event330_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn12:
            print("Btn12 Clicked")
            lv.scr_load_anim(screen33,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            print("Btn320 Clicked")
            lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False) #from screen 32 to screen 3

btn12 = lv.btn(screen3,None)
# attach the callback
btn12.set_event_cb(event330_handler)
btn12.set_size(110,60)
btn12.align(None,lv.ALIGN.CENTER,31,35)
btn12.add_style(btn12.PART.MAIN,style_shadow)
label12=lv.label(btn12,None)
label12.set_text('''Alimentation 
   minerale''')
label12.set_size(100,30)
label12.align(None,lv.ALIGN.CENTER,0,0) 
#create screen33 for light  
screen33 = lv.obj(None,None)
btn330 = lv.btn(screen33,None)  #to return to screen3
btn330.set_event_cb(event330_handler)
btn330.align(None,lv.ALIGN.CENTER,-165,-135)
btn330.set_size(30,25)
label330=lv.label(btn330,None)
label330.set_text("<-")
#here i create alimentation 

table = lv.table(screen33, None)
table.set_col_cnt(2)
table.set_row_cnt(6)
table.set_size(300,200)
table.align(lv.scr_act(), lv.ALIGN.CENTER, -11, -40)

# Make the cells of the first row center aligned 
table.set_col_width(0,200)
table.set_cell_align(0, 0, lv.label.ALIGN.CENTER)
table.set_cell_align(0, 1, lv.label.ALIGN.CENTER)

# Align the price values to the right in the 2nd column
table.set_col_width(1,110)
table.set_cell_align(1, 1, lv.label.ALIGN.RIGHT)
table.set_cell_align(2, 1, lv.label.ALIGN.RIGHT)
table.set_cell_align(3, 1, lv.label.ALIGN.RIGHT)
table.set_cell_align(4, 1, lv.label.ALIGN.RIGHT)
table.set_cell_align(5, 1, lv.label.ALIGN.RIGHT)
table.set_cell_type(0, 0, 2)
table.set_cell_type(0, 1, 2)

# Fill the first column
table.set_cell_value(0, 0, "Name")
table.set_cell_value(1, 0, "Azote(N)")
table.set_cell_value(2, 0, "Phosphore(P)")
table.set_cell_value(3, 0, "Potassium(K)")
table.set_cell_value(4, 0, "Calcium(Ca)")
table.set_cell_value(5, 0, "Magnésium(Mg)")


# Fill the second column
table.set_cell_value(0, 1, "Percentage")
table.set_cell_value(1, 1, "20 %")
table.set_cell_value(2, 1, "19.8 %")
table.set_cell_value(3, 1, "18.61 %")
table.set_cell_value(4, 1, "12.7 %")
table.set_cell_value(5, 1, "10.98 %")
#***********************       but 4 Pesticides     ***************************
def event34_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn13:
            print("Btn14 Clicked")
            lv.scr_load_anim(screen34,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            print("Btn350 Clicked")
            lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False) #to go from screen 36 to screen 3
btn13 = lv.btn(screen3,None)
btn13.set_event_cb(event34_handler)
btn13.set_size(110,60)
btn13.align(None,lv.ALIGN.CENTER,165,35)
btn13.add_style(btn13.PART.MAIN,style_shadow)
label13=lv.label(btn13,None)
label13.set_text("Pesticides")
label13.set_size(100,30)
label13.align(None,lv.ALIGN.CENTER,0,0) 


screen34 = lv.obj(None,None)
#label34 = lv.label(screen34,None)
#label34.set_text(" Pesticides ??????")
#label34.align(None,lv.ALIGN.CENTER,0,-117)
btn340 = lv.btn(screen34,None)       #button to return from screen34 to screen3
btn340.set_event_cb(event34_handler)
btn340.align(None,lv.ALIGN.CENTER,-165,-135)
btn340.set_size(30,25)
label340=lv.label(btn340,None)
label340.set_text("<-")
#---------------------->
# Create a drop down list
ddlist0 = lv.dropdown(screen34)
ddlist0.set_options("\n".join([
                    "Carbaryl",
                    "Deltamethrine",
                    "Malathion",
                    "Chlorpyrifos",
                    "herbicides"]))

ddlist0.set_dir(lv.dropdown.DIR.LEFT);
ddlist0.set_show_selected(False)
ddlist0.set_text("Pesticides")
# It will be called automatically when the size changes
ddlist0.align(None, lv.ALIGN.IN_TOP_RIGHT, 0, 20)

label345 = lv.label(screen34,None)
label345.set_text("Insect detection")
label345.align(None,lv.ALIGN.CENTER,0,-100)

lmeter0 = lv.linemeter(screen34,None)
lmeter0.set_range(0,100)         # Set the range
lmeter0.set_value(80)            # Set the current value
lmeter0.set_scale(240,21)        # Set the angle and number of lines
lmeter0.set_size(150,150)
lmeter0.align(None,lv.ALIGN.CENTER,0,0)
# create a Preloader object
preload = lv.spinner(screen34, None)
preload.set_size(50, 50)
preload.align(None, lv.ALIGN.CENTER, 0, 0)
#img insectes
with open('in1.png','rb') as g: #pic for button
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img33 = lv.img(screen34,None)
lv.img.cache_set_size(2)
img33.align(screen34, lv.ALIGN.CENTER, -140, 0)
img33.set_src(png_img_dsc)
img33.set_zoom(400)
#other copy
img34= lv.img(screen34,None)
lv.img.cache_set_size(2)
img34.align(screen34, lv.ALIGN.CENTER,221,130)
img34.set_src(png_img_dsc)
img34.set_zoom(400)
with open('in2.png','rb') as g: #pic for button
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img35 = lv.img(screen34,None)
lv.img.cache_set_size(2)
img35.align(screen34, lv.ALIGN.CENTER, -140,-120)
img35.set_src(png_img_dsc)
img35.set_zoom(300)
#other copy
img36= lv.img(screen34,None)
lv.img.cache_set_size(2)
img36.align(screen34, lv.ALIGN.CENTER, 150, 30)
img36.set_src(png_img_dsc)
img36.set_zoom(300)

with open('in3.png','rb') as g: #pic for button
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img37 = lv.img(screen34,None)
lv.img.cache_set_size(2)
img37.align(screen34, lv.ALIGN.CENTER, -140,100)
img37.set_src(png_img_dsc)
img37.set_zoom(300)
#other copy
img38= lv.img(screen34,None)
lv.img.cache_set_size(2)
img38.align(screen34, lv.ALIGN.CENTER, 170, -50)
img38.set_src(png_img_dsc)
img38.set_zoom(300)

with open('in4.png','rb') as g: #pic for button
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img39 = lv.img(screen34,None)
lv.img.cache_set_size(2)
img39.align(screen34, lv.ALIGN.CENTER,0,100)
img39.set_src(png_img_dsc)
img39.set_zoom(250)
#************************     btn 14 sell &buy     ***********************************
def event35_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn14:
            print("Btn14 Clicked")
            lv.scr_load_anim(screen35,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            print("Btn350 Clicked")
            lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False) #to go from screen 36 to screen 3
btn14 = lv.btn(screen3,None)
btn14.set_event_cb(event35_handler)
btn14.set_size(100,20)
btn14.align(None,lv.ALIGN.CENTER,180,145)
label14=lv.label(btn14,None)
label14.set_text("Sell & Buy")
label14.set_size(100,30)
label14.align(None,lv.ALIGN.CENTER,0,0) 


screen35 = lv.obj(None,None)
#img 
with open('button.png','rb') as g: 
  png_data = g.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})
img45 = lv.img(screen35,None)
lv.img.cache_set_size(2)
img45.align(screen35, lv.ALIGN.CENTER,-50,-30)
img45.set_src(png_img_dsc)
img45.set_zoom(500)

btn350 = lv.btn(screen35,None)       #button to return from screen35 to screen3
btn350.set_event_cb(event35_handler)
btn350.align(None,lv.ALIGN.CENTER,-165,-135)
btn350.set_size(30,25)
label350=lv.label(btn350,None)
label350.set_text("<-")
# 111111111111111111111111   screen of sell and buy

def eventsellbuy_handler(obj, event):
    list_btn = lv.list.__cast__(obj)
    if event == lv.EVENT.CLICKED:
        print("Clicked: %s" % list_btn.get_btn_text())

# ççççççç      list sell        çççç
labelsell = lv.label(screen35,None)
labelsell.set_text("SELL")
labelsell.align(None,lv.ALIGN.CENTER,-105,-65)

list1 = lv.list(screen35)
list1.set_size(160, 200)
list1.align(None, lv.ALIGN.CENTER, -100,50)

# Add buttons to the list
list_btn = list1.add_btn(lv.SYMBOL.DIRECTORY, "Vegetables")
list_btn.set_event_cb(eventsellbuy_handler)

list_btn = list1.add_btn(lv.SYMBOL.DIRECTORY, "Fruits")
list_btn.set_event_cb(eventsellbuy_handler)

list_btn = list1.add_btn(lv.SYMBOL.DIRECTORY, "Flowers")
list_btn.set_event_cb(eventsellbuy_handler)


list_btn = list1.add_btn(lv.SYMBOL.EDIT, "Edit")
list_btn.set_event_cb(eventsellbuy_handler)

list_btn = list1.add_btn(lv.SYMBOL.CLOSE, "Delete")
list_btn.set_event_cb(eventsellbuy_handler)


list_btn = list1.add_btn(lv.SYMBOL.SAVE, "Save")
list_btn.set_event_cb(eventsellbuy_handler)

list_btn = list1.add_btn(lv.SYMBOL.BELL, "Notify")
list_btn.set_event_cb(eventsellbuy_handler)

# çççççççç      list buy        ççççç
labelbuy = lv.label(screen35,None)
labelbuy.set_text("BUY")
labelbuy.align(None,lv.ALIGN.CENTER,90,-65)

listbuy = lv.list(screen35)
listbuy.set_size(160, 200)
listbuy.align(None, lv.ALIGN.CENTER, 100,50)

# Add buttons to the list
listbuy_btn = listbuy.add_btn(lv.SYMBOL.DIRECTORY, "Pesticides")
listbuy_btn.set_event_cb(eventsellbuy_handler)

listbuy_btn = listbuy.add_btn(lv.SYMBOL.DIRECTORY, "Seeds")
listbuy_btn.set_event_cb(eventsellbuy_handler)

listbuy_btn = listbuy.add_btn(lv.SYMBOL.DIRECTORY, "Machines")
listbuy_btn.set_event_cb(eventsellbuy_handler)


listbuy_btn = listbuy.add_btn(lv.SYMBOL.EDIT, "Edit")
listbuy_btn.set_event_cb(eventsellbuy_handler)

listbuy_btn = listbuy.add_btn(lv.SYMBOL.CLOSE, "Delete")
listbuy_btn.set_event_cb(eventsellbuy_handler)


listbuy_btn = listbuy.add_btn(lv.SYMBOL.SAVE, "Save")
listbuy_btn.set_event_cb(eventsellbuy_handler)

listbuy_btn = listbuy.add_btn(lv.SYMBOL.BELL, "Notify")
listbuy_btn.set_event_cb(eventsellbuy_handler)

#......
style_shadow = lv.style_t()
style_shadow.init()
style_shadow.set_shadow_width(lv.STATE.DEFAULT, 10)
style_shadow.set_shadow_spread(lv.STATE.DEFAULT, 1)
LV_COLOR_BLUE=lv.color_hex3(0xF)
style_shadow.set_shadow_color(lv.STATE.DEFAULT,LV_COLOR_BLUE)

obj1 = lv.obj(screen35,None)
obj1.set_size(200,30)
obj1.align(None,lv.ALIGN.CENTER,100,-135)
obj1.add_style(obj1.PART.MAIN,style_shadow)

labelbuy = lv.label(obj1,None)
labelbuy.set_text("Consumption | Profit")
labelbuy.align(None,lv.ALIGN.CENTER,0,0)

#*************************     btn 15 evaluation      ******************************
def event36_handler(source,evt):
    if evt == lv.EVENT.CLICKED:
        if source == btn15:
            print("Btn15 Clicked")
            lv.scr_load_anim(screen36,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False)
        else:
            print("Btn360 Clicked")
            lv.scr_load_anim(screen3,lv.SCR_LOAD_ANIM.FADE_ON, 500, 500, False) #to go from screen 36 to screen 3
screen36 = lv.obj(None,None)
label36 = lv.label(screen36,None)
label36.set_text("Rating of this year compared to rating from last year")
label36.align(None,lv.ALIGN.CENTER,0,-117)

btn15 = lv.btn(screen3,None) #button evalutaion to go to screen36
# attach the callback
btn15.set_event_cb(event36_handler)
btn15.set_size(200,20)
btn15.align(None,lv.ALIGN.CENTER,20,145)
btn15.add_style(btn15.PART.MAIN,style_shadow)
label15=lv.label(btn15,None)
label15.set_text("Evaluation")
label15.set_size(100,30)
label15.align(None,lv.ALIGN.CENTER,0,0) 

btn360 = lv.btn(screen36,None)       #button to return from screen36 to screen3
btn360.set_event_cb(event36_handler)
btn360.align(None,lv.ALIGN.CENTER,-165,-135)
btn360.set_size(30,25)
btn360.add_style(btn360.PART.MAIN,style_shadow)
label360=lv.label(btn360,None)
label360.set_text("<-")
#create the function in screen 36 evaluation''''''''''''''''''''''''
# create a chart
chart = lv.chart(screen36,None)
chart.set_size(350,200)
chart.align(None,lv.ALIGN.CENTER,0,0)
chart.set_type(lv.chart.TYPE.LINE)
# Add a faded are effect
chart.set_style_local_bg_opa(lv.chart.PART.SERIES, lv.STATE.DEFAULT, lv.OPA._50)               # Max. opa.
chart.set_style_local_bg_grad_dir(lv.chart.PART.SERIES, lv.STATE.DEFAULT, lv.GRAD_DIR.VER)
chart.set_style_local_bg_main_stop(lv.chart.PART.SERIES, lv.STATE.DEFAULT, 255)                # Max opa on the top
chart.set_style_local_bg_grad_stop(lv.chart.PART.SERIES, lv.STATE.DEFAULT, 0)                  # Transparent on the bottom
ser1=chart.add_series(lv_colors.RED)
ser2=chart.add_series(lv_colors.GREEN)
#les courbes
# Set next points on ser1  #red
chart.set_next(ser1,31)
chart.set_next(ser1,66)
chart.set_next(ser1,10)
chart.set_next(ser1,89)
chart.set_next(ser1,63)
chart.set_next(ser1,56)
chart.set_next(ser1,32)
chart.set_next(ser1,35)
chart.set_next(ser1,57)
chart.set_next(ser1,85)
# Set points on ser2 #green
chart.set_points(ser2, [38, 71, 61, 15, 21, 35, 35, 58, 31, 53])
#~~~~~~  who are ~the red and the green  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
line0_points = [ {"x":0, "y":0}, 
                {"x":1, "y":0},
                {"x":70, "y":0},]
style360_line = lv.style_t()   # Create new style (thick dark red)
style360_line.init()
style360_line.set_line_width(lv.STATE.DEFAULT, 5)
style360_line.set_line_color(lv.STATE.DEFAULT, lv_colors.RED)
style360_line.set_line_rounded(lv.STATE.DEFAULT, True)

# Copy the previous line and apply the new style
line360 = lv.line(screen36)
line360.set_points(line0_points, len(line0_points))      # Set the points RED
line360.add_style(lv.line.PART.MAIN, style360_line)
line360.align(None, lv.ALIGN.CENTER, -120, 120)

label3600 = lv.label(screen36,None)   #to write rating of 2021
label3600.set_text("Rating of this year 2021 ")
label3600.align(None,lv.ALIGN.CENTER,10,120)

style361_line = lv.style_t()  # Create new style (thick dark Green)
style361_line.init()
style361_line.set_line_width(lv.STATE.DEFAULT, 5)
style361_line.set_line_color(lv.STATE.DEFAULT, lv_colors.GREEN)
style361_line.set_line_rounded(lv.STATE.DEFAULT, True)

line361 = lv.line(screen36)
line361.set_points(line0_points, len(line0_points))      # Set the points GREEN
line361.add_style(lv.line.PART.MAIN, style361_line)
line361.align(None, lv.ALIGN.CENTER, -120,140)

label3601 = lv.label(screen36,None)   #to write rating of 2020
label3601.set_text("Rating of the last year 2020")
label3601.align(None,lv.ALIGN.CENTER,25,140)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     
#__________________________create (termes and conditions) __________________________________
# create a window
win = lv.win(screen2,None)
win.set_size(250,250)
win.align(None,lv.ALIGN.CENTER,0,0)
win.set_title("Terms and conditions ")                   # Set the title

win_style = lv.style_t()
win_style.init()
win_style.set_margin_right(lv.STATE.DEFAULT, 50)
win.add_style(lv.win.PART.CONTENT_SCROLLABLE,win_style)

# Add control button to the header
close_btn = win.add_btn_right(lv.SYMBOL.CLOSE)
close_btn.set_event_cb(lambda obj,e:  lv.win.close_event_cb(lv.win.__cast__(obj), e))


win.add_btn_right(lv.SYMBOL.SETTINGS)           # Add a setup button

# Add some dummy content
txt = lv.label(win)
txt.set_text(
"""You agree not to alter or modify any part of the 
service . You agree not to distribute in any medium
any part of the service or the content. You agree to 
protect copyrighted material. As a user of this service,
you may be asked to register with us and provide private
information.You are responsible for ensuring the accuracy
of this information ,and you are responible for maintining 
the safety and security of you identifying information.
You are also responsable for all actiities that occur under your account or password 
if you think there are any possible isssus regarding the security of your account on 
this service , inform us immediately so we may adress them accordingly.
We reserve all rights to terminate accounts , edit or remove content and cancel
 orders at our sole discrection  !""")

#tab2 (help )____________________________________________________________________________
mbox1 = lv.msgbox(tab2)
mbox1.set_text(" Theme   | Volume   | Update  |  Maintenance ");

mbox1.set_width(420)
mbox1.set_event_cb(event_handler)
mbox1.align(None, lv.ALIGN.CENTER,-20,-100)  # Align to the corner


#creer les dans tab2 +++++++++++++++++++++++++++++++++++++
objtab21 = lv.obj(tab2,None) #dark theme 
objtab21.set_size(180,90)
objtab21.align(None,lv.ALIGN.CENTER, -110, -20)
objtab23 = lv.obj(tab2,None)    #volume
objtab23.set_size(180,90)
objtab23.align(None,lv.ALIGN.CENTER, 100, -20)

objtab22 = lv.obj(tab2,None)     #update
objtab22.set_size(180,90)
objtab22.align(None,lv.ALIGN.CENTER, -110, 80)
objtab20 = lv.obj(tab2,None)  #maintenace & procetection
objtab20.set_size(180,90)
objtab20.align(None,lv.ALIGN.CENTER, 100, 80)
#volume 
def eventvolume_handler(source,evt):
    if  evt == lv.EVENT.VALUE_CHANGED:
        print("Value:",slider.get_value())      
slider = lv.slider(objtab23,None)
slider.set_width(100)
slider.align(None,lv.ALIGN.CENTER,0,20)
slider.set_event_cb(eventvolume_handler)
labelvolume=lv.label(objtab23,None)
labelvolume.set_text("Volume")
labelvolume.align(None,lv.ALIGN.CENTER,0,-10)
#maintenace &protection
labelfichier=lv.label(objtab20,None)
labelfichier.set_text('''Maintenance 
& protection''')
labelfichier.align(None,lv.ALIGN.CENTER,0,0)
#update
barupdate = lv.bar(objtab22,None)
barupdate.set_size(150,10)
barupdate.align(None,lv.ALIGN.CENTER,0,20)
barupdate.set_anim_time(500)
barupdate.set_value(50,lv.ANIM.ON)
labelupdate=lv.label(objtab22,None)
labelupdate.set_text("Update")
labelupdate.align(None,lv.ALIGN.CENTER,0,-10)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

#*****************************************calendrier tab3***************************
# create a calendar
calendar = lv.calendar(tab3,None)
calendar.set_size(300,250)
calendar.align(None,lv.ALIGN.CENTER,0,0)
calendar.set_event_cb(event_handler)

# Make the date number smaller to be sure they fit into their area
calendar.set_style_local_text_font(lv.calendar.PART.DATE,lv.STATE.DEFAULT,lv.theme_get_font_small())
today = lv.calendar_date_t()
today.year = 2021;
today.month = 05;
today.day = 24

calendar.set_today_date(today)
calendar.set_showed_date(today)

# Highlight a few days
highlighted_days=[]
for i in range(3):
    highlighted_days.append(lv.calendar_date_t())

highlighted_days[0].year=2021
highlighted_days[0].month=5
highlighted_days[0].day=1

highlighted_days[1].year=2021
highlighted_days[1].month=5
highlighted_days[1].day=24

highlighted_days[2].year=2021
highlighted_days[2].month=5
highlighted_days[2].day=31

calendar.set_highlighted_dates(highlighted_days,3)





#setting **************   Tabbbbb2   *****************************************
def color_chg_event_cb(sw, e):
    if e == lv.EVENT.VALUE_CHANGED:
        flag = lv.THEME_MATERIAL_FLAG.LIGHT
        if sw.get_state():
            flag=lv.THEME_MATERIAL_FLAG.DARK
        theme = lv.theme_material_init(LV_THEME_DEFAULT_COLOR_PRIMARY,LV_THEME_DEFAULT_COLOR_SECONDARY,flag,
                                       lv.theme_get_font_small(), lv.theme_get_font_normal(), lv.theme_get_font_subtitle(),
                                       lv.theme_get_font_title())   
def LV_DPX(n):
    if n == 0:
        return n
    scr=lv.scr_act()
    display = scr.get_disp()
    dpi = display.get_dpi()
    # print("dpi: ",dpi)
    tmp = (dpi*n+80)//160
    # print("tmp: ",tmp)
    if tmp > 1:
        return tmp
    else:
        return 1           #les fonctions (dark)

sw = lv.switch(objtab21, None)      #dark switch 
sw.align(None, lv.ALIGN.CENTER,0,0)
if lv.theme_get_flags() & lv.THEME_MATERIAL_FLAG.DARK:
   sw.on(LV_ANIM_OFF)
sw.set_event_cb(color_chg_event_cb)   
sw.set_pos(LV_DPX(50), LV_DPX(40))
sw.set_style_local_value_str(lv.switch.PART.BG, lv.STATE.DEFAULT, "  Dark")
sw.set_style_local_value_align(lv.switch.PART.BG, lv.STATE.DEFAULT, lv.ALIGN.OUT_RIGHT_MID)
#sw.set_style_local_value_ofs_x(lv.switch.PART.BG, lv.STATE.DEFAULT, LV_DPI//35)
#**************************************************************************************
# Create a keyboard 
kb = lv.keyboard(tab1, None)
kb.set_textarea(pwd_ta)      #Focus it on one of the text areas to start 
kb.set_cursor_manage(True)   # Automatically show/hide cursors on text areas */



#*****************************************************************************************************
#//////////////Image/////////////////////////////////////////




#////////////////////////////////////////////////////////////






