import web
from web import form
import sys
import urllib
import requests
import urllib2
import base64
from requests.auth import HTTPBasicAuth
import hmdappconfig
# THIS VERSION IS CURRENTLY DEPLOYED AT costofmoving.appspot.com
# MARCH 17 314 PM

def query_hmd(sex,country):
	inputstring = "http://www.mortality.org/hmd/"+ country+"/STATS/"+sex+"ltper_1x1.txt"
	filename = country + "_" + sex+ "ltper_1x1.txt"
	#print filename
	#print inputstring
	#This gets the file using urllib2, totally works
	request = urllib2.Request(inputstring)
	base64string = base64.encodestring('%s:%s' % (hmdappconfig.username, hmdappconfig.password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string) 
	result = urllib2.urlopen(request)
	localFile = open(filename, 'w')
	localFile.write(result.read())
	result.close()
	localFile.close()
	#textfile = open(inputstring,'r')
	
	
f = open('hmd_country_codes.txt','r')
country_code_dict={}
#March25 - edited countries list to read in from file instead of using subset
countries=[]
for i in range(37):
	boop = f.readline().split()
	country_code_dict[boop[0]]=boop[1]
	countries.append(boop[1])

ages=[]
for i in range (100):
	ages.append(i)
sexes =['m','f']


#countries = ["USA","CANADA","SWEDEN","JAPAN","NORWAY","AUSTRALIA","CHILE"]
user = hmdappconfig.username
pwd = hmdappconfig.password
                        
for country1 in countries:
	for sex in sexes:
		query_hmd(sex,country1)

	

