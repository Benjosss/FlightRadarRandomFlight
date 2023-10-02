from FlightRadar24 import FlightRadar24API
from random import randint

frapi=FlightRadar24API()

allflights = frapi.get_flights()
flight = allflights[randint(10,len(allflights))]
print(flight)


flightdetail = frapi.get_flight_details(flight)

# Flight
callsign = flightdetail['identification']['callsign']
print(f"Callsign : {callsign}")

# Aircraft
aircraft = flightdetail['aircraft']['model']['text']
print(f"Aircraft : {aircraft}")

registration = flightdetail['aircraft']['registration']
print(f"Registration : {registration}")

# Airline
airline = flightdetail['airline']['short']
print(f"Airline : {airline}")

airlinecode = flightdetail['airline']['code']
print(f"Airline's IATA code : {airlinecode['iata']}\nAirline's ICAO code : {airlinecode['icao']}")

# Origin Airport
airportorigin = flightdetail['airport']['origin']['name']
print(f"Origin airport : {airportorigin}")

airportorigincodes = flightdetail['airport']['origin']['code']
print(f"Origin airport's IATA code : {airportorigincodes['iata']}\nOrigin airport's ICAO code : {airportorigincodes['icao']}")

airportorigincountry = flightdetail['airport']['origin']['position']['country']['name']
print(f"Origin airport country: {airportorigincountry}")

airportorigincity = flightdetail['airport']['origin']['position']['region']['city']
print(f"Origin airport city: {airportorigincity}")

airportorigininfos = flightdetail['airport']['origin']['info']
print(f"Origin airport terminal : {airportorigininfos['terminal']}, gate : {airportorigininfos['gate']}")

# Destination Airport
airportdestination = flightdetail['airport']['destination']['name']
print(f"Destnation airport : {airportdestination}")

airportdestinationcodes = flightdetail['airport']['destination']['code']
print(f"Destination airport's IATA code : {airportdestinationcodes['iata']}\nDestination airport's ICAO code : {airportdestinationcodes['icao']}")

airportdestinationcountry = flightdetail['airport']['destination']['position']['country']['name']
print(f"Destination airport country: {airportdestinationcountry}")

airportdestinationcity = flightdetail['airport']['destination']['position']['region']['city']
print(f"Destination airport city: {airportdestinationcity}")

airportdestinationinfos = flightdetail['airport']['destination']['info']
print(f"Destination airport terminal : {airportdestinationinfos['terminal']}, gate : {airportdestinationinfos['gate']}")










