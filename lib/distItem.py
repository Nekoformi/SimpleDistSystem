from typing import Literal

import re
import uuid

from lib.distData import DistData

class DistItem(object):
    type = 'DistItem'
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

    def getDictIndexFromKey(self, dict: dict, key) -> int:
        if key in dict:
            return list(dict.keys()).index(key)
        else:
            return -1

    def getDictIndexFromValue(self, dict: dict, value) -> int:
        if value in dict:
            return list(dict.values()).index(value)
        else:
            return -1

    def getDictKeyFromValue(self, dict: dict, value):
        return next((item["key"] for item in dict if item["value"] == value), None)

    def getDictKeyFromIndex(self, dict: dict, index: int):
        if index >= 0 and index < len(dict):
            return list(dict.keys())[index]
        else:
            return None

    def getDictValueFromKey(self, dict: dict, key):
        return next((item["value"] for item in dict if item["key"] == key), None)

    def getDictValueFromIndex(self, dict: dict, index: int):
        if index >= 0 and index < len(dict):
            return list(dict.values())[index]
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

    def getConditionValue(self) -> str:
        return self.getDictValueFromKey(self.conditionDict, self.condition)

    def getConditionIndex(self) -> int:
        return self.getDictIndexFromKey(self.conditionDict, self.condition)

    def getExpressionValue(self) -> str:
        return self.getDictValueFromKey(self.expressionDict, self.expression)

    def getExpressionIndex(self) -> int:
        return self.getDictIndexFromKey(self.expressionDict, self.expression)

    def getValue(self) -> list[str]:
        return self.value

    def setConditionFromDictValue(self, value: str):
        buf = self.getDictKeyFromValue(self.conditionDict, value)

        if buf != None:
            self.condition = buf

    def setConditionFromDictIndex(self, index: int):
        buf = self.getDictKeyFromIndex(self.conditionDict, index)

        if buf != None:
            self.condition = buf

    def setExpressionFromDictValue(self, value: str):
        buf = self.getDictKeyFromValue(self.expressionDict, value)

        if buf != None:
            self.expression = buf

    def setExpressionFromDictIndex(self, index: int):
        buf = self.getDictKeyFromIndex(self.expressionDict, index)

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

    def importJson(self, data: dict):
        if data['type'] != 'DistItem':
            return

        self.id = data['id']
        self.condition = data['condition']
        self.expression = data['expression']
        self.value = data['value']

    def exportJson(self) -> dict:
        return {
            'type': self.type,
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
