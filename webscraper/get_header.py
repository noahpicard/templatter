import urllib2
import re
import random

bag = []

class urlnode:

    def __init__(self, url):
        self._url = url
        self._html = ""
        self._title = ""
        self._links = []
        self._paragraphs = []
        self._headers = []

    def get_html(self):
        try:
            response = urllib2.urlopen(self._url)
            self._html = response.read()
        except:
            print "Could not connect to website"


    def get_title(self):
        if self._title != "":
            return self._title
        if self._html == "":
            self.get_html()
        print "getting title!"
        rs = re.search('\<title\>([^<>]*)\<\/title\>', self._html)
        print "search complete!"
        if rs:
            print rs.group(1)
        else:
            print "no title"
            self._title = self._url
        return self._title



    def get_links(self):
        if self._links != []:
            return self._links
        if self._html == "":
            self.get_html()
        print "getting links"
        rs = re.findall('\<a[^\>]*href[^\=\>]*=[^\=\>\"]*"(https?\:\/\/[^\"]*)"', self._html)
        for r in rs:
            self._links.append(r)
        print "search complete!"
        return self._links

    def get_headers(self):
        if self._headers != []:
            return self._headers
        if self._html == "":
            self.get_html()
        print "getting headers"
        rs = re.findall('\<h[1-9][^\>]*\>(.*)\<\/h[1-9]\>', self._html)
        for r in rs:
            self._headers.append(r)
        print "search complete!"
        return self._headers

    def get_paragraphs(self):
        if self._paragraphs != []:
            return self._paragraphs
        if self._html == "":
            self.get_html()
        print "getting paragraphs"

        rs = re.findall('\<p[^\>]*\>(.*?)\<\/p[^\>]*\>', self._html)
        for r in rs:
            self._paragraphs.append(r.split())
        print "search complete!"
        return self._paragraphs

    def get_words(self, word_count):
        if self._paragraphs == []:
            self.get_paragraphs()
        words = []
        for i in range(word_count):
            p = get_rand_choice(self._paragraphs, [])
            word = get_rand_choice(p, "")
            words.append(word)
        return words

def get_rand_choice(lstr, err):
    try:
        value = random.choice(lstr)
    except IndexError:
        return err
    return value


def list_ind_print(l):
    for i in range(len(l)):
        print i, l[i]

def get_user_int(s, minval=0, maxval=0):
    while True:
        value = raw_input(s)
        try:
           value = int(value)
        except ValueError:
           print 'Not a valid index'
           continue
        if ((not minval) and (not maxval)) or (value < maxval and value >= minval):
            break
        else:
            print "Value out of range!", minval, maxval
    return value

def interact(n):
    print n.get_title()

    list_ind_print(n.get_headers())

    #list_ind_print(n.get_links())
    return


def main():
    history = []
    n = urlnode(raw_input("Enter a URL:"))
    n.get_html()
    print(n._html)

    interact(n)

    i = get_user_int('Where next? (index): ')

    while (i > -2):

        if i == -1:
            if len(history) > 0:
                n = history.pop()
            else:
                print "History is empty!"
                i = get_user_int('Where next? (index): ')
                continue
        elif i < len(n._links):
            history.append(n)
            next = n._links[i]
            n = urlnode(next)

        interact(n)
        i = get_user_int('Where next? (index, or -1 to go back): ', -2, len(n._links))


    print "Here's your bag!"
    print " ".join(bag)


if __name__ == "__main__":
    main()