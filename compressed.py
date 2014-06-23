
import sys
from GoogleSearchAPI.google import Google
class dni2name:
	def checkDNI(self, id):
		results = Google.search("DNI "+str(id))
		name = self.findName(results)

		if name:
			print id, name
		return name
	def checkRange(self, min, max):
		return [self.checkDNI(id) for id in range(int(min), int(max))]
	def extractName(self, result):
		if "www.dateas.com" in result.link:
			return result.name[0:result.name.find(" -")]
		
		if "buscardatos.com" in result.link:
			return result.name[0:result.name.find(",")]
		return False
	def findName(self, google_results):
		for result in google_results:
			name = self.extractName(result)
			if name is not False:
				return name
		return False
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