import json

class DistData(object):
    webUrl: str
    webContent: str
    fileName: str
    fileExtension: str
    fileContent: str

    # 内部関数

    def match(self, target: str, expression: str, value: list[str]) -> int:
        if expression == 'eq':
            for item in value:
                if (target == item):
                    return 1

            return 0
        elif expression == 'ne':
            for item in value:
                if (target == item):
                    return 0

            return 1
        elif expression == 'ss':
            count = 0

            for item in value:
                count += target.count(item)

            return count
        elif expression == 'ns':
            for item in value:
                if target.count(item) > 0:
                    return 0

            return 1
        else:
            return -1

    # 公開関数

    def getData(self) -> json:
        return {
            'webUrl': self.webUrl,
            'webContent': self.webContent,
            'fileName': self.fileName,
            'fileExtension': self.fileExtension,
            'fileContent': self.fileContent,
        }

    def setData(self, data: json):
        if 'webUrl' in data:
            self.webUrl = data['webUrl']
        if 'webContent' in data:
            self.webContent = data['webContent']
        if 'fileName' in data:
            self.fileName = data['fileName']
        if 'fileExtension' in data:
            self.fileExtension = data['fileExtension']
        if 'fileContent' in data:
            self.fileContent = data['fileContent']

    def matchWebUrl(self, expression: str, value: list[str]) -> int:
        return self.match(self.webUrl, expression, value)

    def matchWebContent(self, expression: str, value: list[str]) -> int:
        return self.match(self.webContent, expression, value)

    def matchFileName(self, expression: str, value: list[str]) -> int:
        return self.match(self.fileName, expression, value)

    def matchFileExtension(self, expression: str, value: list[str]) -> int:
        return self.match(self.fileExtension, expression, value)

    def matchFileContent(self, expression: str, value: list[str]) -> int:
        return self.match(self.fileContent, expression, value)
