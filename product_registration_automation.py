import pyautogui
import time
import webbrowser
import pandas as pd

pyautogui.PAUSE = 0.3 # Sets a delay of 0.3 seconds after each pyautogui function is executed.

webbrowser.open("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # Open the user's default browser at the system link
time.sleep(3) # Wait 3 seconds for the browser to open and the site to load

pyautogui.click(x=774, y=388) # Select the email field (use the file get_position.py to know the correct coordinates)

# Write your email and password (In this example, any email and password will work)
pyautogui.write("your@email.com")
pyautogui.press("tab") # Move to the next field
pyautogui.write("your password")
pyautogui.click(x=972, y=560) # Click on the login button (use the get_position.py file to find the correct coordinates)
time.sleep(3)

table = pd.read_csv("products.csv")

print(table)

# Step 4: Register the products
for line in table.index:
    pyautogui.click(x=782, y=293) # click on the code field (use the get_position.py file to find the correct coordinates)
    
    pyautogui.write(str(table.loc[line, "codigo"])) # fill in the field with the value from the table
    pyautogui.press("tab") # move to the next field
    
    # Repeat the process for all the columns in the table
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    if str(table.loc[line, "obs"]) != "nan":
        pyautogui.write(str(table.loc[line, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # register the product (send button)
    # scroll all the way up
    pyautogui.scroll(500000)
    # Step 5: Repeat the registration process until the end