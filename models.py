from utils import MCESException
from dateutil.parser import parse
import uuid


class Unit(object):
    """This is a model to represent a [Fire,EMS,Rescue,Etc.] Unit

    Attributes:
        name: Name of the unit
        stationNumber: int containing Station Number that the unit belongs to.

    """

    def __init__(self, unitShortCode, name=None, stationNumber=None):
        self.name = name
        self.stationNumber = stationNumber
        self.uShort = unitShortCode
        if (self.__validateShortCode__()):
            self.__setVariables__()

    def __setVariables__(self):
        varSet = {
            "CMD": ("Command", 99),
            "ALL": ("ALL", 0),
            "E1": ("Engine 1", 1),
            "E2": ("Engine 2", 2),
            "E3": ("Engine 3", 3),
            "E4": ("Engine 4", 4),
            "E5": ("Engine 5", 5),
            "E6": ("Engine 6", 6),
            "E7": ("Engine 7", 7),
            "E8": ("Engine 8", 8),
            "E9": ("Engine 9", 9),
            "E10": ("Engine 10", 10),
            "E11": ("Engine 11", 11),
            "E12": ("Engine 12", 12),
            "E14": ("Engine 14", 14),
            "Sq1": ("Squad 1", 1),
            "SQ1": ("Squad 1", 1),
            "SQ4": ("Squad 4", 4),
            "SQ12": ("Squad 12", 12)

        }
        self.name = varSet[self.uShort][0]
        self.stationNumber = varSet[self.uShort][1]

    def __validateShortCode__(self):
        if self.uShort.startswith(("E", "SQ", "ALL", "CMD","Sq")):
            return True
        else:
            raise MCESException("Unit Short Code is Invalid")
            return False


class Call(object):
    """This object represents a 'Call' such as when units get paged out it is called a Call."""
    def __init__(self, mp3File):
        self.mFile = mp3File
        self.__parse__()

    def __parse__(self):
        mString = self.mFile.name
        rawArray1 = mString.split("_")
        if ("/" in rawArray1[0]):
            self.unit = Unit(rawArray1[0].split("/")[-1])
        dFormat = rawArray1[1][0:-2] + " " +rawArray1[1][-2::]+":"+rawArray1[2]+":"+rawArray1[3]
        self.date = parse(dFormat)
        self.uID = uuid.uuid4()







