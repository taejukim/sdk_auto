import os
from APKList import apk_list

def install(apk):
    print("now install > " + apk)
    os.system("adb install " + apk)
    
def uninstall():
    print("now uninstall")
    os.system("adb uninstall com.toast.android.push.sample")
    os.system("adb uninstall com.toast.android.push.sample2")
    
if __name__ == "__main__":
    while True:
        print("0. Exit")
        for apk in apk_list:
            apk_list.index(apk)
            _index = apk_list.index(apk)+1
            print(str(_index) + ". "+apk)
        print(str(_index+1) + ". Uninstall")
        
        target_apk = ""
        while True:
            try:
                index = int(input("choose no : "))
                if index == len(apk_list)+1 or index == 0:
                    break
                target_apk = apk_list[index-1]
                break
            except:
                print("try again..")

        if target_apk:
            install(target_apk)
        elif index == len(apk_list)+1:
            uninstall()
        elif index == 0:
            print("bye")
            break
        