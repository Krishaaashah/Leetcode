class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.space = [0,big,medium,small]
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.space[carType] > 0:
            self.space[carType] -= 1
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)