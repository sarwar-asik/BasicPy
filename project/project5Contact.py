# print("Contact Project-5")
from win10toast import ToastNotifier
import time
Toast = ToastNotifier()

Toast.show_toast("!!!!Hellow  User!!!", "Are you Asik . If not .pLease left now", duration=3)
Toast.show_toast("!! Danger , Virus! Virus!","Kepp the Laptop ,Please.and go to Asik ", duration=10)
Toast.show_toast("Hellow  Asik","Time waste korisna", duration=15)
Toast.show_toast("Hey Asik","SHudo Laptop tiple hbe ? podashuna korte hbe .",duration=18)
Toast.show_toast("Mr. Asik","AJ k job apply korcho ?", duration=20)
Toast.show_toast("Hey Asik","Thank you a lot for update me.",duration=25)

while Toast.notification_active(): time.sleep(0.1)