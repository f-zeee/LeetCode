class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        finalEmails=[]
        for email in emails:
            a="@"
            email=email.split("@",1)
            if "." in email[0]:
                email[0]=email[0].replace(".","")
            
            if "+" in email[0]:
                email1=email[0].split("+",1)
                email[0]=email1[0]
            email="@".join(email)
            finalEmails.append(email)
            
        finalEmails=list(set(finalEmails))
        return len(finalEmails)