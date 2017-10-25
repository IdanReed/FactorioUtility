import base64
import zlib

class entity(object):
    number = 2
    def testFunction(self):
        self.number = 7
        print(self.number)

def decodeExchangeString(exchangeString):
    decoded = base64.b64decode(exchangeString[1:])
    decompressed = zlib.decompress(decoded)
    return str(decompressed)

def entityBreak(decodedString):
    entityString = "entity_number"
    curIndex = 0
    entityList = []
    while curIndex < len(decodedString):
        findVal = decodedString.find(curIndex)
        if findVal == -1:
            print("adf")

def fileDecode(filenameString):
    text_file = open(filenameString)
    print(decodeExchangeString(text_file.readlines()))

def hello():
    return "word"
