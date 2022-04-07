import pyautogui
import tkinter as tk



pyautogui.PAUSE= 1
for i in range(64):
    pyautogui.rightClick()
    pyautogui.PAUSE= 0.03
