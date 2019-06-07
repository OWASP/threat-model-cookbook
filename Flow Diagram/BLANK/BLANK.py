#!/usr/bin/env python3

from pytm import *

tm = TM("Example Flow Diagram")
tm.description = "This is a sample threat model for the Threat Modeling Workshop."

internet = Boundary(" ")

user = Actor("Actor<br/>(user)")

web = Server("Process")
web.inBoundary = internet

api = Server("Another<br/>Process")
api.inBoundary = internet

db = Datastore("Datastore")
db.inBoundary = internet

another = SetOfProcesses("Multiples<br/>Process")
another.inBoundary = internet

user_to_web = Dataflow(user, web, "HTTPS")
web_to_api = Dataflow(web, api, "HTTP")
api_to_db = Dataflow(api, db, " ")
web_to_another = Dataflow(web, another, "?")

tm.process()