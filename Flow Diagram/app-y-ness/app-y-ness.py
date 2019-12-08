#!/usr/bin/env python3

from pytm.pytm import TM, Server, Datastore, Dataflow, Boundary, Actor, Lambda

tm = TM("my test tm")
tm.description = "another test tm"

Web = Boundary("Internal Web")
external_web = Boundary("External Web")

user = Actor("App-y-Tenant")

app = Server("Mobile App")

buy_api = Server("Buy<br/>API-y")
buy_api.inBoundary = Web

rent_api = Server("Rent<br/>API-y")
rent_api.inBoundary = Web

alert_api = Server("Alert<br/>API-y")
alert_api.inBoundary = Web

cloud = Server("Phone Provider Cloud")
cloud.inBoundary = external_web
alert_api_to_cloud = Dataflow(alert_api, cloud, "push")
cloud_to_app = Dataflow(cloud, app, " ")

db_b = Datastore("Oracle Table B")
db_b.inBoundary = Web
buy_api_to_db = Dataflow(buy_api, db_b, " ")

db_r = Datastore("Oracle Table R")
db_r.inBoundary = Web
rent_api_to_db = Dataflow(rent_api, db_r, " ")

db_t = Datastore("Oracle Table Tenants")
db_t.inBoundary = Web
rent_api_to_db_t = Dataflow(rent_api, db_t, " ")
buy_api_to_db_t = Dataflow(buy_api, db_t, " ")
alert_api_to_db_t = Dataflow(alert_api, db_t, " ")

auth = Server("Auth<br/>API-y")
auth.inBoundary = Web
Dataflow(auth, db_t, 'auth')
Dataflow(app, auth, 'https')

user_to_app = Dataflow(user, app, "use")
app_to_buy_api = Dataflow(app, buy_api, "https")
app_to_rent_api = Dataflow(app, rent_api, "https")
buy_api_to_cloud = Dataflow(buy_api, cloud, " ")

gov = Server("Fire 'n' Stuff .gov")
gov.inBoundary = external_web
alert_api_to_gov = Dataflow(alert_api, gov, "https")
Dataflow(gov, alert_api, "callback")

operator = Actor("Operator<br/>Employee")
Dataflow(operator, db_t, "admin")

tm.process()
