import os
from datetime import datetime, timedelta


def file_disp(path, thresh, base=True):
    if os.path.isdir(path):
        for inte in os.listdir(path):
            file_disp(path + "/" + inte, thresh, False)

        if (not base) and (len(os.listdir(path) == 0)):
            os.remove(path)
        return

    mod = os.path.getmtime(path)
    if thresh > mod:
        os.remove(path)


threshold = (datetime.now() - timedelta(minutes=4)).timestamp()
file_disp("fol1", threshold)
