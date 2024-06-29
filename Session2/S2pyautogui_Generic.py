import pyautogui
import time
#Ext_Cord=pyautogui.locateCenterOnScreen("Ext_Pic.png")
#print(Ext_Cord)
#pyautogui.moveTo(Ext_Cord)


def  LocOnScr_Ext(image):
    Ext_Cord=None
    while(Ext_Cord is None):
        Ext_Cord=pyautogui.locateCenterOnScreen(image,confidence=0.7)  
    if(Ext_Cord is not None):
        print(Ext_Cord)
        pyautogui.moveTo(Ext_Cord)
        pyautogui.click()
    return Ext_Cord  
Ext_Name=input("please enter extension name")
Ext_Image=input("please enter file name that contain ext image")
pyautogui.hotkey("ctrl","shift","x")
LocOnScr_Ext("clr_ext2.png")
pyautogui.write(Ext_Name)# Ext_Name ""
pyautogui.moveTo(20,20)
time.sleep(2)
print("locating clang")
Install_Cord=LocOnScr_Ext(Ext_Image)#""
#Install_Cord=pyautogui.locate(Ext_Image,"install.png",confidence=0.7)
pyautogui.moveTo(Install_Cord.x+65,Install_Cord.y+40)
pyautogui.click()
 

 