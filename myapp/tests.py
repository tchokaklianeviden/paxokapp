from django.test import TestCase

###############################
# Create your tests here.
# EVIDEN
###############################

import cols_tools as ct
import col_dbtools as cdb


maMaison = ct.PointGPS()
maMaison.lat = 43.76666689338895
maMaison.lon = 7.219108651604221
	
conn = cdb.create_connection('db.sqlite3')
myListeCols =  cdb.select_all_cols06(conn)
conn.close()