class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} no. of times"

class Grandson(Son):

    dance = 6

    def isdance(self):
        return f"Jackson yeh!" \
         f"Yes I dance very awsomely {self.dance} no. of times"

darry = Dad()
larry = Son()
Maulik = Grandson()

print(Maulik.isdance())