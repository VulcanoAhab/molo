import re

class Extractor:
    """
    """
    _text=""
    _parsers={}

    @classmethod
    def setCut(cls, fieldName, fieldPattern, flag=0):
        """
        """
        cls._parsers[fieldName]=re.compile(r"{}".format(fieldPattern),
                                                                flag)

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
        for field,rexFunc in self._parsers.items():
            valueContainer=rexFunc.findall(self._t)
            if not len(valueContainer):
                self._results[field]=None
                continue
            if onlyFirst:
                self._results[field]=valueContainer[0]
            else:
                self._results[field]=valueContainer
