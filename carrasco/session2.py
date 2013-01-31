import untangle

def getting_data():
    """Fetch data from the status of escalators in the NYC subway system and
    calculate the fraction of this outages that needs to be repaired
    """

    NYC_STATE = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    doc = untangle.parse(NYC_STATE)
    outages = doc.NYCOutages.outage
    to_repair = float(len(filter(lambda o: o.reason.cdata == "REPAIR", outages)))
    print "Fraction of outages with the reason REPAIR: {}".format(to_repair/len(outages))