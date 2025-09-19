class restrunt:
    restrunt_name="pista house"
    owner="ramu kaka"
    def _restrunt_details( self):
     print(f"restrunt name : {restrunt_name} \n owner : {owner}")
class loc1(restrunt):
   def __init__ (self,name,manager):
      self.name=name
      self.manager=manager
      def loc_details(self):
         self.restrunt_details()
         print(f"loc :{self.name} \n manaer : {self.manager}")
class loc2(restrunt):
   def __init__(self,name,manager):
      self.name=name
      self.manager=manager
      def loc2_details(self):
         self.restrunt_details()
         print(f"loc :{self.name} \n manaer : {self.manager}")
r=loc1("uppal","naveen")
r1=loc2("vanastalipuram","prashanth")
r1.loc2_details( )
    

     

    
