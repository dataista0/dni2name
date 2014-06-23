
import sys
from GoogleSearchAPI.google import Google



class dni2name:

	'''
		searchs for a DNI in google and try to extract a full name
	'''
	def checkDNI(self, id):
		results = Google.search("DNI "+str(id))
		name = self.findName(results)

		if name:
			print id, name
		return name

	'''
		a simple use case
		>>> python dni2name.py test
		33779884 Esteban Roitberg
	'''
	def runTest(self):
		self.checkDNI("33779884") #Loi's ID number

	'''
		check for a list of DNIs
	'''
	def run(self):
		some_ids = range(33779884, 33779910)
		names = [self.checkDNI(id) for id in some_ids]


	'''
		use heuristics to extract name from the given google result (link, title and description of a webpage)
		this is a example, it could be as complex as you wish
	'''
	def extractName(self, result):
		if "www.dateas.com" in result.link:
			return result.name[0:result.name.find(" -")]
		
		if "buscardatos.com" in result.link:
			return result.name[0:result.name.find(",")]
		return False

	'''
		check all google results and return the first name found
		the algorithm is an iteration for pedagogical reasons
		it could be like: 'next( (self.extractName(results) for results in google_results if self.extractName(result) is not False), False)'
	'''
	def findName(self, google_results):
		for result in google_results:
			name = self.extractName(result)
			if name is not False:
				return name
		return False


33799335 Angeletti Julieta Belen

if __name__ == "__main__":
    ans = dni2name()

    if len(sys.argv) == 1:
    	ans.runTest()
    elif len(sys.argv) > 1 and sys.argv[1] == "run":
    	ans.run()
    else:
    	ans.checkDNI(sys.argv[1])
