# import class Country for use in class Country atalogue
from country import Country

# A country catalogue that stores country objects in a catalogue list and stores country and continent pairs in a dictionary
class CountryCatalogue:

    # Constructs a country catalogue
    # @param firstfile is file that contains data in the format Country|Population|Area
    # @param secondfile is file that contains data in the format Country,Continent
    # self._countryCat is a list of country objects
    # self._cDictionary is a dictionary with key:country and value: continent
    def __init__(self, firstfile, secondfile):
        self._countryCat = []
        self._cDictionary = {}
        self._secondfile = open(secondfile, "r")
        self._secondfile.readline()
        for line in self._secondfile:
            line = line.strip()
            words = line.split(",")
            self._cDictionary[words[0]] = words[1]
        self._firstfile = open(firstfile, "r")
        self._firstfile.readline()
        for line in self._firstfile:
            line = line.strip()
            words = line.split("|")
            name = words[0]
            pop = words[1].replace(",","")
            area = words[2].replace(",","")
            continent = self._cDictionary[words[0]]
            countryObject = Country(name, pop, area, continent)
            self._countryCat.append(countryObject)

    # Looks up information about a country
    # @param name the country name
    # @return the country object if country exists in the catalogue or none if it doesn't exist
    def findCountry(self, name):
        for countryObject in self._countryCat:
            if countryObject.getName() == name:
                return countryObject
        return None

    # Sets the population of a country
    # @param name is the country name
    # @param pop is the new population
    # @return True if country exits and method is successful, and false if unsuccessful
    def setPopulationOfCountry(self, name, pop):
        for countryObject in self._countryCat:
            if countryObject.getName() == name:
                countryObject._population = pop
                return True
        return False

    # Sets the area of a country
    # @param name is the country name
    # @param area is the new area
    # @return True if country exits and method is successful, and false if unsuccessful
    def setAreaOfCountry(self, name, area):
        for countryObject in self._countryCat:
            if countryObject.getName() == name:
                countryObject._area = float(area)
                return True
        return False

    # Adds a new country to the dictionary of countries and country catalogue
    # @param name is the country name
    # @param pop is the population
    # @param area is the area
    # @param continent is the continent name
    # @return True if method is successful, and False if the country already exits and method is unsuccessful
    def addCountry(self, name, pop, area, continent):
        for countryObject in self._countryCat:
            if countryObject.getName() == name:
                return False
        newCountry = Country(name, pop, area, continent)
        self._countryCat.append(newCountry)
        self._cDictionary[name] = continent
        return True

    # Deletes a country from the catalogue and cDictionary if it exists
    # @param name is the country name
    def deleteCountry(self, name):
        for countryObject in self._countryCat:
            if countryObject.getName() == name:
                self._countryCat.remove(countryObject)
                del self._cDictionary[name]

    # Displays the whole catalogue to the screen, using the default string representation for the Country objects
    def printCountryCatalogue(self):
        print(self._countryCat)

    # Generates a list of countries on a specific continent
    # @param continent is the continent name
    # @return list of country objects
    def getCountriesByContinent(self, continent):
        continentList = []
        for countryObject in self._countryCat:
            if countryObject.getContinent() == continent:
                continentList.append(countryObject)
        return continentList

    # Generates a list of countries on a continent in descending order by population
    # @param continent is the continent name
    # @return a list of only the countries and their population on that continent (if valid continent name), list of all the countries and their population in the catalogue (if continent name is empty string), empty list (if continent is invalid)
    def getCountriesByPopulation(self, continent=""):
        populationList = []
        masterContinent = continent
        if masterContinent == "":
            for countryObject in self._countryCat:
                pair = (countryObject.getName(), countryObject.getPopulation())
                populationList.append(pair)
                populationList.sort(key=lambda tup: tup[1], reverse=True)
            return populationList
        else:
            for countryObject in self._countryCat:
                if countryObject.getContinent() == continent:
                    pair = (countryObject.getName(), countryObject.getPopulation())
                    populationList.append(pair)
                    populationList.sort(key=lambda tup: tup[1], reverse=True)
            return populationList

    # Generates a list of countries on a continent in descending order by area
    # @param continent is the continent name
    # @return a list of only the countries and their area on that continent (if valid continent name), list of all the countries and their area in the catalogue (if continent name is empty string), empty list (if continent is invalid)
    def getCountriesByArea(self, continent=""):
        areaList = []
        masterContinent = continent
        if masterContinent == "":
            for countryObject in self._countryCat:
                pair = (countryObject.getName(), countryObject.getArea())
                areaList.append(pair)
                areaList.sort(key=lambda tup: tup[1], reverse=True)
            return areaList
        else:
            for countryObject in self._countryCat:
                if countryObject.getContinent() == continent:
                    pair = (countryObject.getName(), countryObject.getArea())
                    areaList.append(pair)
                    areaList.sort(key=lambda tup: tup[1], reverse=True)
            return areaList

    # Find the name of the continent with the most number of people living in it and the number of people living in the continent
    # @return name of continent with the most people living in it and the number of people living in it
    def findMostPopulousContinent(self):
        continents = set()
        continentPopulations = []
        for countryObject in self._countryCat:
            continents.add(countryObject.getContinent())
        for continent in continents:
            continentPop = 0
            for countryObject in self._countryCat:
                if countryObject.getContinent() == continent:
                    continentPop = continentPop + countryObject.getPopulation()
            pair = (continent, continentPop)
            continentPopulations.append(pair)
        continentPopulations.sort(key=lambda tup: tup[1], reverse=True)
        maxPop = continentPopulations[0]
        return maxPop

    # Generate list of countries that have a population density that falls within a certain range (inclusive of the endpoints)
    # @param lowerBound is the lower bound of the range
    # @param upperBound is the upper bound of the range
    # @return list of country names and their densities in descending order
    def filterCountriesByPopDensity(self, lowerBound, upperBound):
        densityList = []
        for countryObject in self._countryCat:
            popDensity = countryObject.getPopDensity()
            if popDensity >= lowerBound and popDensity <= upperBound:
                pair = (countryObject.getName(), popDensity)
                densityList.append(pair)
                densityList.sort(key=lambda tup: tup[1], reverse=True)
        return densityList

    # Saves all country information in the catalogue to a file where they are displayed as Name|Continent|Population|AreaSize|PopulationDensity in alphabetical order
    # @param filename is the name of the output file
    # @return number of items written to the file is the method is successful, -1 if the method is unsuccessful
    def saveCountryCatalogue(self, filename):
        outFile = open(filename, "w")
        sortedCat = sorted(self._countryCat, key=lambda x: x.getName())
        countList = []
        for countryObject in sortedCat:
            name = countryObject.getName()
            continent = countryObject.getContinent()
            population = str(countryObject.getPopulation())
            area = "{0:.2f}".format(round(countryObject.getArea(), 2))
            popDensity = "{0:.2f}".format(countryObject.getPopDensity())
            outFile.write(name + "|" + continent + "|" + population + "|" + area + "|" + popDensity + "\n")
            countList.append(1)
        if not countList:
            return -1
        else:
            return (len(countList))
