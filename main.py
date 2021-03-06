import web
from web import form
import sys
import urllib
import requests
import urllib2
import base64
import os
from requests.auth import HTTPBasicAuth
#

render = web.template.render('templates/')

urls = ('/', 'index')
application = web.application(urls, globals())
#app = app.gaerun()


f = open('hmd_country_codes.txt','r')
country_code_dict={}
#March25 - edited countries list to read in from file instead of using subset
countries=[]
for i in range(37):
	boop = f.readline().split()
	country_code_dict[boop[0]]=boop[1]
	countries.append(boop[0])

ages=[]
for i in range (100):
	ages.append(i)
sexes =['M','F']


#countries = ["USA","CANADA","SWEDEN","JAPAN","NORWAY","AUSTRALIA","CHILE"]
user = "mtrotter@stanford.edu"
pwd = "1t_only_adds"
                        

	
myform = form.Form(  
	form.Dropdown('Your current age', ages),
	form.Dropdown('Your gender', sexes),
	form.Dropdown('Your current country of residence', countries),
	form.Dropdown('Your preferred country of residence', countries)) 
	
class index: 
    def GET(self): 
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtest(form)
        else:
            user_age = form["Your current age"].value
            user_sex = form["Your gender"].value
            user_sex = user_sex.lower()
            country1 = form["Your current country of residence"].value
            country2 = form["Your preferred country of residence"].value
            
            #figure out how to calculate the lifespan stuff in here!
            
	    user_country1 = translate_country(country1,country_code_dict)
	    #print "User country: " + user_country1
	    user_country2 = translate_country(country2,country_code_dict)
	    #print "User country2: " + user_country2
		
		
	    (ages_Can,lx_Can, cap_Lx_Can)=query_hmd(user_age,user_sex,user_country1)
	    (ages_Swe,lx_Swe, cap_Lx_Swe)=query_hmd(user_age,user_sex,user_country2)
	    old_life = remaining_years(lx_Can,cap_Lx_Can)
	    new_life = remaining_years(lx_Swe,cap_Lx_Swe)
		
	    life_change = new_life - old_life
            #life_change = old_life
            # return "Old lifespan: %s, new lifespan: %s, age: %s, sex: %s, country1: %s, country2: %s : Your lifespan changes by %s years!" % (old_life, new_life, user_age, user_sex, user_country1, user_country2, life_change)
        return render.index(old_life=old_life, new_life=new_life, country1=country1,country2=country2, change = life_change)
#if __name__=="__main__":
#   web.internalerror = web.debugerror
#    app.run()
    


def translate_country(user_country,country_code_dict):
	for code in country_code_dict:
		#print code.lower()
		#print country_code_dict[code]
		#print user_country.lower()
		if user_country.lower()==code.lower():
			user_country = country_code_dict[code]
			#print user_country
			#print country_code_dict[code]
			break
		else:
			user_country=user_country
	#print user_country		
	return user_country

def query_hmd(user_age,sex,country):
	
	inputstring = "countrydata/"+country + "_"+sex+"ltper_1x1.txt"
	lx = []
	cap_Lx=[]
	ages=[]
	year = "2009"
	if country == "CHL":
		year = "2005"
	if country == "NZL_NP":
        year = "2008"

	#for i in range(total_size):
	
	with open(inputstring, 'r') as result:
		for line in result:
			line = line.split()
			if len(line)>0: #if it's not an empty line
				if line[1]!="110+": #if age isn't the last one
					if line[0]==year and float(line[1])>= float(user_age): 
					#if data is from 2010 and age >= user age
						ages.append(float(line[1]))
						lx.append(float(line[5]))
						cap_Lx.append(float(line[7]))
				else: #if age IS the last age class 110+
					if line[0]=="2009":
					#if data is from 2010 and age >= user age
						ages.append(110.0)
						lx.append(float(line[5]))
						cap_Lx.append(float(line[7]))
	result.close()				
	return (ages,lx, cap_Lx)

def remaining_years(lx, Lx):
	e_x=0;
	#lx[0]
	for i in range(len(lx)+1):
		e_x+= sum(Lx[:i:])
		e_x = e_x/lx[0]
	return e_x

#app = application.gaerun()
app = application.wsgifunc() 

#if __name__ == "__main__":
#    app = web.application(urls, globals())
#    app.run()

