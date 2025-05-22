from tools import container
from tools.helper import shell
from tools.logger import Logger


class AndroidId:
   def get_id(self):
        if container.is_running():
            try:
                queryout = shell(
                    arg="sqlite3 /data/data/com.google.android.gsf/databases/gservices.db \"select * from main where name = 'android_id';\"",
                    env="ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n"
                )
            except:
                return
        else:
            Logger.error("Make sure Waydroid session is running and has installed GAPPS images!")
            return
        print(queryout.replace("android_id|", "").strip())
        print("   ^----- Access this link --------> https://google.com/android/uncertified/")
        print("          Login with your Google account and Submit the Android GSF ID there")
