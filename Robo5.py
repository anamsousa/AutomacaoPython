import pyautogui as p

p.hotkey('win','r')
p.sleep(1)
p.write('C:\RPA.pbix')
p.sleep(1)
p.press('enter')
p.sleep(30)
p.click(x=768, y=101)
p.sleep(7)
p.click(x=1343, y=20)
p.sleep(3)
p.click(x=694, y=401)


# p.sleep(3)
# print(p.position())