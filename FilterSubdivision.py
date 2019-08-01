'''
A translation function for Spartanburg county shp subdivision data (subdivision.*). 


The following fields are used:    

Field           Used For            Reason

SUBDIVNAME      name


Constant fields:
landuse=residential
place=neighbourhood

'''

import re

    
def filterTags(attrs):
    if not attrs:
        return

    tags = {}
    
    if 'SUBDIVNAME' in attrs:
        name = attrs['SUBDIVNAME'].strip().title()
        if "industrial" in name.lower():
            tags['landuse'] = 'industrial'
        elif "commercial" in name.lower():
            tags['landuse'] = 'commercial'
        else:
            tags['place'] = 'neighbourhood'
            tags['landuse'] = 'residential'

    return tags