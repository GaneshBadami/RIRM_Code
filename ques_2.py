class Url:
    def getUrlDetails(self):
        self.social=" Social Links :https://www.facebook.com/fulioTech/\n\t\t https://www.linkedin.com/company/ful-io/\n"
        self.email = " Email : support@ful.io\n"
        self.contact = " Contact : +1 343 303 6668"

    def printResult(self):
        print(self.social,self.email, self.contact)
url = input("Enter website url : ")

S1=Url()
S1.getUrlDetails()
if url == "https://ful.io" :
    print("Output : ")
    S1.printResult()
else :
    print("Invalid Input")
        
