class DistanceConversion:
    def __init__(self,distance):
        self.__distance = distance

    def m_to_cm(self):
        return self.__distance * 100

    def m_to_km(self):
        return self.__distance / 1000

    def m_to_inch(self):
        return self.__distance * 39.37

distance = float(input("Enter a distance in meter: "))
obj= DistanceConversion(distance)

print("Distance in cm: ", obj.m_to_cm())
print("Distance in km: ", obj.m_to_km())
print("Distance in inch: ", obj.m_to_inch())