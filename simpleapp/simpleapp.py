#!/usr/bin/env python

from flask import Flask
import sys
import optparse
import time

app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def hello_world():

    curtime = int(round(time.time()))
    elapsed = curtime - start
    seconds = int((elapsed) % 60)
    minutes = int(((elapsed / (60)) % 60))
    hours   = int(((elapsed / (60*60)) % 24));

    return "<h1>Hello, World from Python and Distelli!</h1><i>Uptime: %02d:%02d:%02d" % (hours, minutes, seconds)

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p <port>")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
