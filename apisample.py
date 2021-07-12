# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:44:00 2021

@author: Admin
"""

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()