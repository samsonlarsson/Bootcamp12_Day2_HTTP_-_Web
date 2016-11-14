import urllib2
import json

def render_output_data(data):
    # Use the json module to load the string data into a dictionary
    json_response = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in json_response["metadata"]:
        print json_response["metadata"]["title"]
        print "=" * 50

    # print the events that only have a magnitude greater than 4
    for i in json_response["features"]:
        if i["properties"]["mag"] >= 4.1:
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

    # print blank line to create spacing
    print

    # print status events
    events_status = "Events that were Reviewed"
    print events_status.center(50)
    print "=" * 50
    for i in json_response["features"]:
        statusReports = i["properties"]["status"]
        if (statusReports != None) & (statusReports > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(statusReports) + " times"


    # print blank line to create spacing
    print

    # print only the events where at least 1 person reported feeling something
    events_felt = "Events that were Felt:"
    print events_felt.center(50)
    print "=" * 50
    for i in json_response["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None) & (feltReports > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"

    # print blank line to create spacing
    print

    # output the number of events, plus the magnitude and each event name
    count = json_response["metadata"]["count"]
    events_recorded = str(count) + " Total Events Recorded"
    print events_recorded.center(50)
    print "_" * 50


def main():
    """
        define a variable to hold endpoint
        In this case we'll use the free data feed from the USGS
        This feed lists all earthquakes for the last day larger than Mag 2.5
    """
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        # print out our customized results
        render_output_data(data)
    else:
        print "Results could not be retrieved. Server responded with an error" + str(webUrl.getcode())


if __name__ == "__main__":
    main()