__author__ = 'Fabian'


from htmldom import htmldom
import requests
import os


class GetImgs():

    def __init__(self):
        pass

    def getthread(self):
        print(os.getcwd())
        dom = htmldom.HtmlDom("http://boards.4chan.org/e/thread/1792910/confident-gals-ii").createDom()
            # Find all the links present on a page and prints its "href" value
        div = dom.find("div")

        #GET TITLE OF THREAD
        span = dom.find("span[class=subject]")
        #wenn der titel zu lang ist macht 4chan irgend einen scheiß, darum die Unterscheidung hier nötig
        t1 = span.children(".dateTime")
        t1s = t1.html()
        if not t1s:
            title = span.first().text()
        else:
            title = span[1].text()
        #wenn kein Titel gegeben wird einer gesetzt
        if not title:
            title = "RANDOM"
        #unerlaubte zeichen aus dem titel löschen
        ft = ''
        for char in title:
            if not (char in '<>:"/\|=*'):
                if ord(char)>31:
                    ft+=char

        #GET BOARD
        board = dom.find("div[class=boardTitle]")
        boardtitle = board.first().text()
        bts = boardtitle.split(" - ")
        #unerlaubte zeichen aus dem board name löschen
        bt = ''
        for char in bts[-1]:
            if not (char in '<>:"/\|=*'):
                if ord(char)>31:
                    bt+=char


        #ordner erstellen
        path = "G:\\Download\\chanPIC\\" + bt + "\\" + ft + "\\"
        if not os.path.exists(path):
            os.makedirs(path)

        #print(div.html())
        chld = div.children(".fileText")
        a = chld.find("a")
        for link in a:
            s = link.attr("href")
            sfull = "http:" + s
            print(sfull)
            w = s.split(sep="/")
            n = w[-1]
            with open(path + n, 'wb') as handle:
                response = requests.get(sfull, stream=False)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
