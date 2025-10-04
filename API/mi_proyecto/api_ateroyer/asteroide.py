import numpy as np

class Asteroid:
    def __init__(self, name, id, absolute_magnitude, estimated_diameter, is_potentially_hazardous, close_aproach_data, velocity, is_sentry_object, x, y, z, mass):
        self.name= name
        self.id= id
        self.absolute_magnitude= absolute_magnitude
        self.estimated_diameter= estimated_diameter
        self.is_potentially_hazardous= is_potentially_hazardous
        self.close_aproach_data= close_aproach_data
        self.velocity= velocity
        self.is_sentry_object= is_sentry_object
        self.x=x
        self.y=y
        self.z=z
        self.latitude= calculateLatitude(x, y, z)
        self.altitude= calculateAltitude(x, y, z)
        self.mass= mass

        # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # absolute_magnitude
    @property
    def absolute_magnitude(self):
        return self._absolute_magnitude

    @absolute_magnitude.setter
    def absolute_magnitude(self, value):
        self._absolute_magnitude = value

    # estimated_diameter
    @property
    def estimated_diameter(self):
        return self._estimated_diameter

    @estimated_diameter.setter
    def estimated_diameter(self, value):
        self._estimated_diameter = value

    # is_potentially_hazardous
    @property
    def is_potentially_hazardous(self):
        return self._is_potentially_hazardous

    @is_potentially_hazardous.setter
    def is_potentially_hazardous(self, value):
        self._is_potentially_hazardous = value

    # close_aproach_data
    @property
    def close_aproach_data(self):
        return self._close_aproach_data

    @close_aproach_data.setter
    def close_aproach_data(self, value):
        self._close_aproach_data = value

    # velocity
    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    # is_sentry_object
    @property
    def is_sentry_object(self):
        return self._is_sentry_object

    @is_sentry_object.setter
    def is_sentry_object(self, value):
        self._is_sentry_object = value

    # x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # z
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    # latitude
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    # altitude
    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        self._altitude = value

    # mass
    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value
    
def calculateLatitude(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    return np.arcsin(z / r)  # En radianes
def calculateAltitude(x, y, z):
    R_earth = 6371  # Radio promedio de la Tierra en km
    r = np.sqrt(x**2 + y**2 + z**2)
    return r - R_earth