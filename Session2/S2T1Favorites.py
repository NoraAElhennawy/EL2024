import webbrowser
MyFavorite=[0,'www.google.com','www.bing.com','www.facebook.com']
def GetFavorite():
    UrlInd=int(input("Choose from list your favorite url to open:  1-Google    2-Bing    3-FaceBook \n"))
    webbrowser.open(MyFavorite[UrlInd])