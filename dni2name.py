
import sys
from GoogleSearchAPI.google import Google

'''
	dni2name
	@author github.com/julian3833
	uses 
		a google result contains: link, title, description and other values of 
		the ranked page usually accessed humanly through google.com	

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
			buscardatos.com returns a title like this: "Garcia Minzoni Schmid Belen, DNI 33.779.880"
			we take here the part before the comma (",")
		'''

		if "buscardatos.com" in result.link:
			return result.name[0:result.name.find(",")]
		'''
			www.dateas.com returns a title like this: "Esteban Roitberg - CUIT 20-33779884-6"
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
    
