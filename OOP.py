class Car(object):
  num_of_wheels=4
  num_of_doors=4
  def _init_(self,type="honda",name="general",model="GM"):
    self.type=type
    self.name=name
    self.model=model
    if self.name=='Koenigsegg' or self.name=='Porsche':
      self.num_of_doors=2
    elif:
      self.car_type=='trailer':
      self.num_of_wheels==8
    else:
      self.car_type=="Salon"

  def is_saloon(self):
	  if self.car_type is not'trailer':
	    return True
	    return False
  def drive(self,speed):
    if self.car_type is 'trailer':
      self.speed==77
    else:
      self.speed==1000