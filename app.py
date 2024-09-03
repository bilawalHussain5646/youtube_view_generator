from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

import json
import multiprocessing
import tkinter as tk
import tkinter.font as tkFont
import threading
import os
import concurrent.futures

# Define the YouTube video URL




VIDEO_URL = 'https://www.youtube.com/watch?v=iIGDHG5GDFI'  # Replace with your video URL

def VPN_Connection(driver):
   

    driver.switch_to.window(driver.window_handles[0])

    driver.get("chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html")

    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,".next").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,".next").click()
    x = 170.625
    time.sleep(5)
    elem = driver.find_element(By.CSS_SELECTOR,"button.button svg g:nth-child(2)")

    y = 200
    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # # Move the mouse to the specified point
    actions.move_to_element(elem)
    actions.click().perform()
    # driver.get("chrome://extensions/shortcuts")
    # time.sleep(1500)
    time.sleep(15)




def watch_youtube_video(driver,df):

    
    total_time = 0
    try:
        for index, row in df.iterrows():
            row["Links"]
        
            try:
                if index == 0:

                    # Open the YouTube video URL
                    driver.get(row["Links"])
                    time.sleep(30)
                else:
                    # Open a new tab and switch to it
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[index])
                    driver.get(row["Links"])
                # Get the video's duration
                video_duration = driver.execute_script(
                    "return document.querySelector('video').duration;"
                )
                total_time = total_time + video_duration + 10
                # Wait for the video to complete
                
            except:
                pass
    finally:
        time.sleep(total_time + 10)  
        # Close the WebDriver
        driver.quit()

# Call the function with the video URL

def Run():

    excel_file_path = 'youtube_links.xlsx'
    df = pd.read_excel(excel_file_path, engine='openpyxl')

    
    options = webdriver.ChromeOptions()
    options.add_extension("veepn.crx")
    driver = webdriver.Chrome(options=options)
    time.sleep(5)
    # Open the vpn and run that vpn first
    VPN_Connection(driver)
    # Run this video
    watch_youtube_video(driver,df)


class App:

    def __init__(self, root):
        #setting title
        root.title("Youtube Video Watcher")
        ft = tkFont.Font(family='Arial Narrow',size=13)
        #setting window size
        width=640
        height=480
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='black')

        ClickBtnLabel=tk.Label(root)
       
      
        
        ClickBtnLabel["font"] = ft
        
        ClickBtnLabel["justify"] = "center"
        ClickBtnLabel["text"] = "Youtube Video Watcher"
        ClickBtnLabel["bg"] = "black"
        ClickBtnLabel["fg"] = "white"
        ClickBtnLabel.place(x=120,y=190,width=150,height=70)
    

        
        Lulu=tk.Button(root)
        Lulu["anchor"] = "center"
        Lulu["bg"] = "#009841"
        Lulu["borderwidth"] = "0px"
        
        Lulu["font"] = ft
        Lulu["fg"] = "#ffffff"
        Lulu["justify"] = "center"
        Lulu["text"] = "START"
        Lulu["relief"] = "raised"
        Lulu.place(x=375,y=190,width=150,height=70)
        Lulu["command"] = self.start_func




  

    def ClickRun(self):

        running_actions = [Run]

        thread_list = [threading.Thread(target=func) for func in running_actions]

        # start all the threads
        for thread in thread_list:
            thread.start()

        # wait for all the threads to complete
        for thread in thread_list:
            thread.join()
    
    def start_func(self):
        thread = threading.Thread(target=self.ClickRun)
        thread.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()