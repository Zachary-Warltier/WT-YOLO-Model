import os
import pyautogui
import time
from PIL import Image

def capture_screenshot(folder_path, filename):
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot to the specified folder
    screenshot.save(os.path.join(folder_path, filename))

def main():
    # Define the folder where screenshots will be saved
    folder_path = "./screenshots"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    count = 195
    while True:
        # Generate a unique filename for each screenshot
        filename = f"screenshot_{count}.png"
        
        # Capture and save the screenshot to the folder
        capture_screenshot(folder_path, filename)
        print(f"Screenshot saved as {os.path.join(folder_path, filename)}")
        
        # Wait for 15 seconds before taking the next screenshot
        time.sleep(15)
        
        # Increment the screenshot counter
        count += 1

if __name__ == "__main__":
    main()

