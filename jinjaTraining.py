from flask import Flask, render_template
from util import occupations

my_app = Flask(__name__)

#print occupations.read('data/occupations.csv')
dictOfJobs = occupations.makeDictionary(occupations.read('data/occupations.csv'))


def htmlOutput():
    return render_template('hw.html', dictionary = dictOfJobs, randJob = occupations.pickOne(dictOfJobs))

@my_app.route("/")
def root():
    return "Hey there!" 
              

@my_app.route("/occupations")
def table():
    return htmlOutput()

if __name__ == '__main__':
    my_app.debug = "true"
    my_app.run()
