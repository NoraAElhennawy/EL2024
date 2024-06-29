import pyautogui
import time
#Ext_Cord=pyautogui.locateCenterOnScreen("Ext_Pic.png")
#print(Ext_Cord)
#pyautogui.moveTo(Ext_Cord)

pyautogui.hotkey("ctrl","shift","x")
def  LocOnScr_Ext(image):
    Ext_Cord=None
    while(Ext_Cord is None):
        Ext_Cord=pyautogui.locateCenterOnScreen(image)  
    if(Ext_Cord is not None):
        print(Ext_Cord)
        pyautogui.moveTo(Ext_Cord)
        pyautogui.click()
    return Ext_Cord    

LocOnScr_Ext("clr_ext2.png")
pyautogui.write("clangd")
pyautogui.moveTo(100,100)
time.sleep(2)
print("locating clang")
Install_Cord=LocOnScr_Ext("clang.png")
pyautogui.moveTo(Install_Cord.x+75,Install_Cord.y+20)
pyautogui.click()
 

 