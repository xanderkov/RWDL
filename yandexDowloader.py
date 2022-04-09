import yadisk
from constants import YANDEX_TOKEN

def upload():
    y = yadisk.YaDisk(token=YANDEX_TOKEN)
    y.upload("Database/wm-nowm.zip", "Database/wm-nowm.zip")
    

def download():
    y = yadisk.YaDisk(token=YANDEX_TOKEN)
    y.download("Database/wm-nowm.zip", "Database/wm-nowm.zip")

y = yadisk.YaDisk(token=YANDEX_TOKEN)
