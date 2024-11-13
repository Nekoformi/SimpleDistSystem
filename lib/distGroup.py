from __future__ import annotations

from typing import Union, Literal

import uuid

from lib.distData import DistData
from lib.distItem import DistItem

class DistGroup(object):
    id: uuid
    operation: Literal['and', 'or']
    content: list[Union[DistGroup, DistItem]]

    operationDict: dict[str, str] = {
        'and': '全てに一致',
        'or': '何れに一致',
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
        self.operation = 'and'
        self.content = []

    def getUUID(self) -> str:
        return str(self.id)

    def getOperationIndex(self) -> int:
        return self.findDictIndex(self.operationDict, self.operation)

    def getDistContent(self, targetId: str) -> Union[DistGroup, DistItem, None]:
        if self.getUUID() == targetId:
            return self
        else:
            for item in self.content:
                if type(item) is DistGroup:
                    buf = item.getDistContent(targetId)

                    if buf != None:
                        return buf

                if type(item) is DistItem:
                    if item.getUUID() == targetId:
                        return item

        return None

    def setOperationIndex(self, index: int):
        buf = self.getItemFromDictIndex(self.operationDict, index)

        if buf != None:
            self.operation = buf

    def addNewDistGroup(self) -> str:
        new = DistGroup()

        self.content.append(new)

        return new.getUUID()

    def addNewDistItem(self) -> str:
        new = DistItem()

        self.content.append(new)

        return new.getUUID()

    def addDistGroup(self, distGroup: DistGroup) -> str:
        self.content.append(distGroup)

        return distGroup.getUUID()

    def addDistItem(self, distItem: DistItem) -> str:
        self.content.append(distItem)

        return distItem.getUUID()

    def getDistGroupOperationIndex(self, targetId: str) -> int:
        buf = self.getDistContent(targetId)

        if type(buf) is DistGroup:
            return buf.getOperationIndex()
        else:
            return -1

    def getDistItemConditionIndex(self, targetId: str) -> int:
        buf = self.getDistContent(targetId)

        if type(buf) is DistItem:
            return buf.getConditionIndex()
        else:
            return -1

    def getDistItemExpressionIndex(self, targetId: str) -> int:
        buf = self.getDistContent(targetId)

        if type(buf) is DistItem:
            return buf.getExpressionIndex()
        else:
            return -1

    def getDistItemValue(self, targetId: str) -> Union[list[str], None]:
        buf = self.getDistContent(targetId)

        if type(buf) is DistItem:
            return buf.getValue()
        else:
            return None

    def setDistGroupOperationIndex(self, targetId: str, index: int):
        buf = self.getDistContent(targetId)

        if type(buf) is DistGroup:
            buf.setOperationIndex(index)

    def setDistItemConditionIndex(self, targetId: str, index: int):
        buf = self.getDistContent(targetId)

        if type(buf) is DistItem:
            buf.setConditionIndex(index)

    def setDistItemExpressionIndex(self, targetId: str, index: int):
        buf = self.getDistContent(targetId)

        if type(buf) is DistItem:
            buf.setExpressionIndex(index)

    def setDistItemValue(self, targetId: str, value: str):
        buf = self.getDistContent(targetId)

        if type(buf) is DistItem:
            buf.setValue(value)

    def displayOperation(self) -> str:
        return self.operationDict.get(self.operation, '')

    def exportContent(self) -> list[dict]:
        content = []

        for item in self.content:
            content.append(item.exportJson())

        return content

    def exportJson(self) -> dict:
        return {
            'id': str(self.id),
            'operation': self.operation,
            'content': self.exportContent(),
        }

    def match(self, distData: DistData) -> int:
        for item in self.content:
            buf = item.match(distData)

            if self.operation == 'and' and buf <= 0:
                return 0

            if self.operation == 'or' and buf > 0:
                return 1

        if self.operation == 'and':
            return 1
        elif self.operation == 'or':
            return 0
        else:
            return -1

    def trace(self, distData: DistData) -> dict:
        content = []

        for item in self.content:
            content.append(item.trace(distData))

        return {
            'id': str(self.id),
            'operation': self.operation,
            'match': self.match(distData),
            'content': content,
        }
