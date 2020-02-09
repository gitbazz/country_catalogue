# Student Name: Bazillah Zargar, Student ID: 250611535

# A simulated country that consists of a name, population, area, and continent
class Country:

    # Constructs a country
    # @param name is the country name, default value is an empty string
    # @param pop is the population, default value is 0
    # @param area is the area, default value is 0
    # @param continent is the continent name, default value is an empty string
    def __init__(self, name="", pop=0, area=0, continent=""):
        self._name = name
        self._population = int(pop)
        self._area = float(area)
        self._continent = continent

    # Gets the name of the country
    # @return the country name
    def getName(self):
        return self._name

    # Gets the population of the country
    # @return the population
    def getPopulation(self):
        return self._population

    # Gets the area of the country
    # @return the area
    def getArea(self):
        return self._area

    # Gets the continent name of the country
    # @return the continent name
    def getContinent(self):
        return self._continent

    # Sets the population of the country
    # @param pop is the population
    def setPopulation(self, pop):
        self._population = pop

    # Sets the area of the country
    # @param area is the area
    def setArea(self, area):
        self._area = area

    # Sets the continent name of the country
    # @param continent is the continent
    def setContinent(self, continent):
        self._continent = continent

    # Calcultes the population density of the country
    # @return the population density
    def getPopDensity(self):
        popDensity = round((self._population/self._area), 2)
        return popDensity

    # Constructs the string representation of the country
    # @return string representation
    def __repr__(self):
        output = self._name + " (pop: " + str(self._population) + ", size: " + str(self._area) + ") in " + self._continent
        return output
