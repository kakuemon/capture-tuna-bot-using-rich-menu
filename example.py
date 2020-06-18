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

# Setup RichMenu to register
rm = RichMenu(name="Test menu", chat_bar_text="menu1")
rm.add_area(0, 0, 2500, 1686, "message", "hoge")

# Register
res = rmm.register(rm, "C:\\Users\\t-kakuta\\Documents\\study3\\richmenu\\image.png")
richmenu_id1 = res["richMenuId"]

print(res)

rm = RichMenu(name="Test menu", chat_bar_text="menu2")
rm.add_area(0, 0, 2500, 1686, "message", "unko")

# Register
res = rmm.register(rm, "C:\\Users\\t-kakuta\\Documents\\study3\\richmenu\\image.png")
richmenu_id2 = res["richMenuId"]

print(res)

# Apply to user

if args[1] == '1':
    rmm.apply(user_id, richmenu_id1)
    print("menu 1")
    
elif args[1] == '2':
    rmm.apply(user_id, richmenu_id2)
    print("menu 2")
    
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
