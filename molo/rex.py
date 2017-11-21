import re

class Extractor:
    """
    """
    _text=""
    _parsers={}

    @classmethod
    def setCut(cls, fieldName, fieldPattern, flag=0, groupName=None):
        """
        """
        rex=re.compile(r"{}".format(fieldPattern),flag)
        cls._parsers[fieldName]={
            "rex":rex,
            "groupName":groupName,
        }

    @classmethod
    def cleanParsers(cls):
        """
        """
        cls._parsers={}

    def __init__(self, textIn):
        """
        """
        self._t=textIn
        self._results={}

    def __getattr__(self, attr):
        """
        """
        if not attr in self._results:return None
        return self._results[attr]

    def toDict(self):
        """
        """
        return self._results

    def run(self, onlyFirst=True):
        """
        """
        for field,rexDict in self._parsers.items():
            rexFunc=rexDict["rex"]
            groupName=rexDict["groupName"]
            #-- by Group Name
            if groupName:
                valueContainer=rexFunc.search(self._t)
                if not valueContainer:
                    self._results[field]=None
                    continue
                self._results[field]=valueContainer.group(groupName).strip()
            #-- by Index
            else:
                valueContainer=rexFunc.findall(self._t)
                if not len(valueContainer):
                    self._results[field]=None
                    continue
                if onlyFirst:
                    self._results[field]=valueContainer[0].strip()
                else:
                    self._results[field]=[r.strip() for in valueContainer]
