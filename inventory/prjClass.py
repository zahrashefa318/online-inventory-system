
class PrjClass():
    def __init__(self):
         
         self. the_file=[]
         self.filename=""

    # A method for returning the file content:

    def tablemaker (self,filename):
        self.filename=filename 
        with open(self.filename, 'r') as file:
            self.the_file=file.readlines()   
            return self.the_file
                    
    # A method for adding user data in the file:
    def add (self,item,quantity,price ):
          item=item
          quantity=quantity
          price=price
          for line in self.the_file:
           if item in line:
                return "repeat"     
          with open(self.filename , 'a+') as file :
                    file.write(f'{item},')
                    file.write(f'{quantity},')
                    file.write(f'{price}\n')
                    
    # A method for deleting a chosen item by user in the file :          
    def delete(self , item):
          
          for line in self.the_file:
            if item.lower() in line.lower().strip():
                 self.the_file = [line for line in self.the_file if item.lower() not in line.lower().strip()]
              
                 with open(self.filename ,'w')as file:
                    file.writelines(self.the_file)
                 return "done" 
          
          return "Not"

         
     # A method for changing an item's price and quantity in the file:
    def change(self , item, quantity, price):
         
              for line in self.the_file:
                  if item.lower() in line.lower():
                     i=self.the_file.index(line)
                     line=line.split(',')
                     line[1]=quantity     
                     line[2]=price      
                     line=",".join(map(str,line))      
                     self.the_file[i]=line+'\n'
                                                          
                     with open(self.filename ,'w')as file:   
                         file.writelines(self.the_file)        
                     return "done"  
                         
              return "Not"          
                        
                                  
                         
                    
               

                   
                              
                    
                   