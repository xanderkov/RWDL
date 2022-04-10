import yadisk
from src.constants import YANDEX_TOKEN

def upload():
    y = yadisk.YaDisk(token=YANDEX_TOKEN)
    y.upload("Database/wm-nowm.zip", "Database/wm-nowm.zip")
    

def download():
    y = yadisk.YaDisk(token=YANDEX_TOKEN)
    y.download("Database/wm-nowm.zip", "Database/wm-nowm.zip")
    from zipfile import ZipFile
    with ZipFile('Database/wm-nowm.zip', 'r') as zipObj:
        zipObj.extractall()

y = yadisk.YaDisk(token=YANDEX_TOKEN)
