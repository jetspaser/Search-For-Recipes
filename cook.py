import eel
eel.init('src')

@eel.expose
def exx(x):
    print(x)

eel.start("cook.html", size = (634, 951))