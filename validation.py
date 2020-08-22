import re
class validation:
 
    def validatemob(self,mob):
        pattern =re.compile(r'\d[10]')
        if(pattern.match(mob)):
            return True
        else:
            print("Re-enter Valid mobile number")
            return False
    
    def validateemail(self,eml):
        pattern =re.compile(r'\d[10]')
        if(pattern.match(mob)):
            return True
        else:
            print("Re-enter Valid Email Id")
            return False