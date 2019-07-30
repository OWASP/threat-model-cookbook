#!/usr/bin/env python3

from pytm import *

tm = TM("Battle Royale Game Flow Diagram")
tm.description = "This is a threat model made in the Threat Modeling Workshop."

playerlocal = Boundary("player's local machine")
corp = Boundary("corp network")
prod = Boundary("prod network")

player = Actor("Player")
anon = Actor("Anonymous<br/>WWW User-Agent")

cs = Actor("Customer Support")
cs.inBoundary = corp

gameclient = Server("Game<br/>Client")
browser = Server("Browser")

for process in [browser, gameclient, anon, player]:
	process.inBoundary = playerlocal
	
wwwstats = Server("Website<br/>Stats")
lobby = Server("Lobby")
gameservers = SetOfProcesses("Game<br/>Servers")
wwwmod = Server("Moderation<br/>Website")
apirest = Server("API REST")


playerdb = Datastore("Player Database")
statsdb = Datastore("Stats Database")


for process in [wwwstats, lobby, gameservers, wwwmod, apirest, playerdb, statsdb]:
	process.inBoundary = prod


player_to_gameclient = Dataflow(player, gameclient, "Uses/Launch")
player_to_browser = Dataflow(player, browser, "Uses/Launch")
anon_to_wwwstats = Dataflow(anon, wwwstats, " ")
browser_to_wwwstats = Dataflow(browser, wwwstats, "HTTPS")
wwwstats_to_apirest = Dataflow(wwwstats, apirest, " ")
wwwstats_to_playerdb = Dataflow(wwwstats, playerdb, " ")

gameclient_to_lobby = Dataflow(gameclient, lobby, "TCP 1234")
gameclient_to_gameservers = Dataflow(gameclient, gameservers, "TCP 1235")

lobby_to_gameservers = Dataflow(lobby, gameservers, " ")
lobby_to_playerdb = Dataflow(lobby, playerdb, " ")
lobby_to_apirest = Dataflow(lobby, apirest, " ")

wwwmod_to_playerdb = Dataflow(wwwmod, playerdb, " ")
cs_to_wwwmod = Dataflow(cs, wwwmod, " ")

gameservers_to_statsdb = Dataflow(gameservers, statsdb, "r/w")
gameservers_to_playerdb = Dataflow(gameservers, playerdb, " ")

apirest_to_statsdb = Dataflow(apirest, statsdb, "r/o")
apirest_to_playerdb = Dataflow(apirest, playerdb, " ")


tm.process()
