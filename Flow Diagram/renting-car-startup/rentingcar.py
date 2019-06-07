#!/usr/bin/env python3

from pytm import *

tm = TM("Renting Car Startup Flow Diagram")
tm.description = "This is a threat model made in the Threat Modeling Workshop."

owner = Actor("Owner Phone")
customer = Actor("Customer Phone")

ownz = Server("Ownz Mobile")
cadz = Server("Cadz Mobile")
	
apigw = Server("API Gateway")
auth = Server("Auth")
conncar = SetOfProcesses("Connected Car")
abc = Server("ABC")

api = Server("API")
apiar = Server("API AR")
apiai = Server("API AI")
apiamfm = Server("API AM/FM")

unsure = Process("?")
# todo change this for a cloud?
watson = ExternalEntity("Watson")

flatfile = Datastore("Flatfile radio stations")
carsdb = Datastore("Cars DB")

insidecar = Boundary("Inside the car")
dmz = Boundary("DMZ")
prod = Boundary(" ")

for process in [conncar, cadz, abc, customer]:
	process.inBoundary = insidecar

apiai.inBoundary = dmz

for process in [apigw, api, apiar, apiamfm, auth, flatfile, carsdb, unsure]:
	process.inBoundary = prod

owner2ownz = Dataflow(owner, ownz, "Launch")
customer2cadz = Dataflow(customer, cadz, "Launch")
ownz2apigw = Dataflow(ownz, apigw, "HTTPS")
cadz2apigw = Dataflow(cadz, apigw, "HTTPS")

apigw2apiai = Dataflow(apigw, apiai, "HTTP")
apigw2apiamfm = Dataflow(apigw, apiamfm, "SSH")
apigw2apiar = Dataflow(apigw, apiar, "HTTP/2")
apigw2api = Dataflow(apigw, api, "HTTP")

api2carsdb = Dataflow(api, carsdb, " ")
apiaamfm2flatfile = Dataflow(apiamfm, flatfile, " ")
apiai2watson = Dataflow(apiai, watson, " ")
apigw2auth = Dataflow(apigw, auth, "Kerberos")

apiar2unsure = Dataflow(apiar, unsure, " ")

conncar2abc = Dataflow(conncar, abc, " ")
abc2carsdb = Dataflow(abc, carsdb, " ")
conncar2cadz = Dataflow(conncar, cadz, "Bluetooth")


tm.process()
