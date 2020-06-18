# -*- coding: utf-8 -*-

""" Usage of RichMenu Manager """
from richmenu import RichMenu, RichMenuManager
import sys

args = sys.argv
print(args)
print(args[1])

# Setup RichMenuManager
user_id = "your user id"
channel_access_token = "your access token"
rmm = RichMenuManager(channel_access_token)
image0 = "/path/to/maguro0.png"
image1 = "/path/to/maguro1.png"
image2 = "/path/to/maguro2.png"
image3 = "/path/to/maguro3.png"

# menu0
rm = RichMenu(name="Test menu", chat_bar_text="menu 0")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "message", "逃す")
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image0)
richmenu_id0 = res["richMenuId"]
print(res)

# menu1
rm = RichMenu(name="Test menu", chat_bar_text="menu 1")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "message", "逃す")
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image1)
richmenu_id1 = res["richMenuId"]
print(res)

# menu2
rm = RichMenu(name="Test menu", chat_bar_text="menu 2")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "message", "逃す")
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image2)
richmenu_id2 = res["richMenuId"]
print(res)

# menu3
rm = RichMenu(name="Test menu", chat_bar_text="menu 3")
rm.add_area(0, 0, 2500, 843, "message", "マグロ")
rm.add_area(0, 843, 830, 840, "message", "捕獲")
rm.add_area(833, 843, 830, 840, "message", "逃す")
rm.add_area(1666, 843, 830, 840, "message", "マグロ一丁")
res = rmm.register(rm, image3)
richmenu_id3 = res["richMenuId"]
print(res)

# Apply to user

if args[1] == '0':
    rmm.apply(user_id, richmenu_id0)
    print("menu 0")
    
elif args[1] == '1':
    rmm.apply(user_id, richmenu_id1)
    print("menu 1")

elif args[1] == '2':
    rmm.apply(user_id, richmenu_id2)
    print("menu 2")

elif args[1] == '3':
    rmm.apply(user_id, richmenu_id3)
    print("menu 3")

elif args[1] == 'r':
    rmm.remove_all()
    print("remove all donne")
    
else: 
    print("not setting")



# # Check
# res = rmm.get_applied_menu(user_id)
# print(res)
#print(user_id  + ":" + res["richMenuId"])

# # Others
# res = rmm.get_list()
# rmm.download_image(richmenu_id, "/path/to/downloaded_image.png")
# res = rmm.detach(user_id)
# res = rmm.remove(richmenu_id)
# rmm.remove_all()
# res = rmm.get_list()
