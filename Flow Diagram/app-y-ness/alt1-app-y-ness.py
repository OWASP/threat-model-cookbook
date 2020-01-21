from pytm.pytm import TM, Boundary, Server, Actor, Datastore, Dataflow, SetOfProcesses

tm = TM("App-y-ness")
tm.description = "This is a sample threat model for the Threat Modeling Workshop."

internet = Boundary("Internet")

user = Actor("App-y-tenant")

app = Server("Mobile App")

buyApi = Server("Buy<br/>API-y")
buyApi.inBoundary = internet

rentApi = Server("Rent<br/>API-y")
rentApi.inBoundary = internet

market = SetOfProcesses("Market-y")
market.inBoundary = internet

alertApi = Server("Alert<br/>API-y")
alertApi.inBoundary = internet

authApi = Server("Auth<br/>API-y")
authApi.inBoundary = internet

allAuth = Server("All Auth")
allAuth.inBoundary = internet

phoneCloud = Server("Phone<br/>Provider<br/>Cloud")

firensurfCloud = Server("Fire n' Surf .gov")

dbB = Datastore("Oracle Table B")
dbB.inBoundary = internet

dbR = Datastore("Oracle Table R")
dbR.inBoundary = internet

dbT = Datastore("Oracle Table T")
dbT.inBoundary = internet

user_to_app = Dataflow(user, app, "use")
app_to_buyapi = Dataflow(app, buyApi, "HTTPS<br/>JSON")
app_to_phonecloud = Dataflow(app, phoneCloud, " ")
app_to_rentapi = Dataflow(app, rentApi, "HTTPS<br/>JSON")
app_to_authapi = Dataflow(app, authApi, "HTTPS<br/>JSON")
app_to_dbt = Dataflow(authApi, dbT, "Token-y")
allauth_to_dbt = Dataflow(allAuth, dbT, " ")
buyapi_to_dbt = Dataflow(buyApi, dbT, " ")
buyapi_to_market = Dataflow(buyApi, market, " ")
rentapi_to_dbr = Dataflow(rentApi, dbR, " ")
rentapi_to_dbb = Dataflow(buyApi, dbB, " ")
rentapi_to_market = Dataflow(rentApi, market, " ")
alert_to_phonecloud = Dataflow(alertApi, phoneCloud, "push")
alert_to_firensurf = Dataflow(alertApi, firensurfCloud, "Kafka<br/>HTTPS")
firensurf_to_alert = Dataflow(firensurfCloud, alertApi, "push")
buyapi_to_phonecloud = Dataflow(buyApi, phoneCloud, " ")

tm.process()
