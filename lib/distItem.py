from typing import Literal

import re
import uuid

from lib.distData import DistData

class DistItem(object):
    id: uuid
    condition: Literal['webUrl', 'webContent', 'fileName', 'fileExtension', 'fileContent']
    expression: Literal['eq', 'ne', 'ss', 'ns']
    value: list[str]

    conditionDict: dict[str, str] = {
        'webUrl': 'ウェブサイトのURL',
        'webContent': 'ウェブサイトの内容',
        'fileName': 'ファイルの名前',
        'fileExtension': 'ファイルの拡張子',
        'fileContent': 'ファイルの内容',
    }

    expressionDict: dict[str, str] = {
        'eq': 'と等しい',
        'ne': 'と等しくない',
        'ss': 'を含む',
        'ns': 'を含まない',
    }

    # 内部関数

    def findDictIndex(self, dict: dict, item) -> int:
        if item in dict:
            return list(dict.keys()).index(item)
        else:
            return -1

    def getItemFromDictIndex(self, dict: dict, index: int):
        if index >= 0 and index < len(dict):
            return list(dict.keys())[index]
        else:
            return None

    # 公開関数

    def __init__(self):
        self.id = uuid.uuid4()
        self.condition = 'fileContent'
        self.expression = 'ss'
        self.value = []

    def getUUID(self) -> str:
        return str(self.id)

    def getConditionIndex(self) -> int:
        return self.findDictIndex(self.conditionDict, self.condition)

    def getExpressionIndex(self) -> int:
        return self.findDictIndex(self.expressionDict, self.expression)

    def getValue(self) -> list[str]:
        return self.value

    def setConditionIndex(self, index: int):
        buf = self.getItemFromDictIndex(self.conditionDict, index)

        if buf != None:
            self.condition = buf

    def setExpressionIndex(self, index: int):
        buf = self.getItemFromDictIndex(self.expressionDict, index)

        if buf != None:
            self.expression = buf

    def setValue(self, value: str):
        self.value = re.split(r',\s*', value)

    def displayCondition(self) -> str:
        return self.conditionDict.get(self.condition, '')

    def displayExpression(self) -> str:
        return self.expressionDict.get(self.expression, '')

    def displayValue(self) -> str:
        return ','.join(self.value)

    def exportJson(self) -> dict:
        return {
            'id': str(self.id),
            'condition': self.condition,
            'expression': self.expression,
            'value': self.value,
        }

    def match(self, distData: DistData) -> int:
        if self.condition == 'webUrl':
            return distData.matchWebUrl(self.expression, self.value)
        elif self.condition == 'webContent':
            return distData.matchWebContent(self.expression, self.value)
        elif self.condition == 'fileName':
            return distData.matchFileName(self.expression, self.value)
        elif self.condition == 'fileExtension':
            return distData.matchFileExtension(self.expression, self.value)
        elif self.condition == 'fileContent':
            return distData.matchFileContent(self.expression, self.value)
        else:
            return -1

    def trace(self, distData: DistData) -> dict:
        buf = self.exportJson()

        buf.update({ 'match': self.match(distData) })

        return buf
