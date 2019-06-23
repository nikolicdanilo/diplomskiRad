"""An example program that uses the elsapy module"""

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json
    
## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

## Initialize client
client = ElsClient(config['apikey'])

## Author example
# Initialize author with uri
my_auth = ElsAuthor(
        uri = 'https://api.elsevier.com/content/author/author_id/7004367821')
# Read author data, then write to disk
if my_auth.read(client):
    print ("my_auth.full_name: ", my_auth.full_name)
    my_auth.write()
else:
    print ("Read author failed.")

## Affiliation example
# Initialize affiliation with ID as string
my_aff = ElsAffil(affil_id = '60101411')
if my_aff.read(client):
    print ("my_aff.name: ", my_aff.name)
    my_aff.write()
else:
    print ("Read affiliation failed.")

## Scopus (Abtract) document example
# Initialize document with Scopus ID.
scp_doc = AbsDoc('gene')
if scp_doc.read(client):
    print ("scp_doc.title: ", scp_doc.title)
    scp_doc.write()   
else:
    print ("Read document failed.")

