from pytm.pytm import TM, Boundary, Server, Actor, Datastore, Dataflow, SetOfProcesses

tm = TM("Generic CMS example")
tm.description = "This is a sample threat model for the Threat Model Cookbook."

internet = Boundary("Internet")

user = Actor("Generic/Privilege User")

webserver = Server("Web Server")
webserver.inBoundary = internet

user_to_webserver = Dataflow(user, webserver, "HTTPS")

db = Datastore("db")
db.inBoundary = internet
db_to_webserver = Dataflow(webserver, db, " ")

adminuser = Actor(" admin ")
admin_to_webserver = Dataflow(adminuser, db, "unsecure<br/>mysql<br/>connection")

cdn = SetOfProcesses("CDN network")
user_to_cdn = Dataflow(user, cdn, "HTTP")
webserver_to_cdn = Dataflow(webserver, cdn, "Push to Bucket")

tm.process()
