
import sys
from GoogleSearchAPI.google import Google

'''
	dni2name: returns a name given a dni number using google and two simple extraction rules. 
	
	@author julian3833 github.com/julian3833
	
	Includes GoogleSearchAPI, a library that request and process google search result pages. 
	(It's a git project, see the readme for the link).
	
	Google.search() returns a list of google results, each of which contains the link, title, description and other values of 
	the ranked pages that we usually access through www.google.com	

	dni2name.extractName(): applies over this pages two simple rules based on two human trivial observations:
	
	* if the site is 'buscardatos.com' then the title has the form "Peller Julian , D.N.I. 1234567890"
	* if the site is 'dateas.com  then the title has the form "Julian Peller - CUIT 20-1234567890-4"  
	
	In the first case the code returns the text before the "," (i.e: "Peller Julian") and in the second it returns the 
	part before the "-". In other case it does nothing and return no full name.

	Despite this simplicity, the density of results seems high in some regions of the id numbers.
	I think using this a lot is not legal, so, you know, don't use it a lot. 

	(Really, Google will ban your I.P. Making a huge human db is not trivial, not legal and not cheap.)	

'''


class dni2name:

	'''
		base method: searchs for a DNI in google and try to extract a full name
	'''
	def checkDNI(self, id):
		
		google_results = Google.search("DNI "+str(id))

		#check all the pages returned by google and try to extract full names with simple rules
		for result in google_results:
			name = self.extractName(result)
			if name is not False:
				print id, name
				return name
		
		return False

	'''
		two simple rules to extract fullnames from a given google ranked page
	'''
	def extractName(self, result):
		
		'''
			buscardatos.com returns a title like this: "Julian Peller, DNI 12345678"
			we take here the part before the comma (",")
		'''

		if "buscardatos.com" in result.link:
			return result.name[0:result.name.find(",")]
		'''
			www.dateas.com returns a title like this: "Julian Peller - CUIT 20-123456789-6"
			we take here the part before the "-"
		'''
		if "www.dateas.com" in result.link:
			return result.name[0:result.name.find(" -")]
		

		return False
		

	'''
		searchs for names for the dnis between min and max
	'''
	def checkRange(self, min, max):
		return [self.checkDNI(id) for id in range(int(min), int(max))]

	'''
		a simple use case
		>>> python dni2name.py
		33779884 Esteban Roitberg
	'''
	def runExample(self):
		self.checkDNI("33779884") #Loi's ID number



if __name__ == "__main__":
    ans = dni2name()

    if len(sys.argv) == 1:
    	ans.runExample()
    elif len(sys.argv) == 2:
    	ans.checkDNI(sys.argv[1])
    elif len(sys.argv) == 3:
    	ans.checkRange(sys.argv[1], sys.argv[2])
    
