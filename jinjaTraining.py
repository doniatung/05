from flask import Flask
from flask import render_template
import random

my_app = Flask(__name__)

def read(csv):
    thefile = open(csv, 'r')
    l = thefile.readlines()
    thefile.close()
    return l
#reads the file into a list with each entry as a separate line in the csv

def makeDictionary(l):
    d = {}
    del l[0]
    del l[-1]
    for x in l:
        if x.count(",") > 1:
            quote = x.find('"', 1, len(x))
            k = x[1 : quote]
            v = float(x[quote + 2: -1])
            d[k] = v
        else:
            comma = x.find(",")
            k = x[: comma]
            v = float(x[comma + 1: -1])
            d[k] = v
    return d
#creates a dictionary of the entries in a given list by using the ',' as the separation character between the key and value of the dictionary entry

def pickOne(d):
    l = []
    for key in d:
        v = d[key] * 10
        counter = 0
        while counter < v:
            l.append(key)
            counter = counter + 1
    return l[random.randint(0,len(l)-1)]

def htmlOutput():
    return render_template('hw.html', d = makeDictionary(read("occupations.csv")))

@my_app.route("/occupations")
def root():
    return htmlOutput()

if __name__ == '__main__':
    my_app.debug = "true"
    my_app.run()
