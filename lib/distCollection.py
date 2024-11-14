from __future__ import annotations

import uuid

from lib.distGroup import DistGroup
from lib.distItem import DistItem

class DistCollection(object):
    type = 'DistCollection'
    id: uuid
    name: str
    folderPath: str
    root: DistGroup

    # 内部関数

    def addInitialDistItemToRoot(self, condition: str, expression: str):
        distItem = DistItem()

        distItem.condition = condition
        distItem.expression = expression
        distItem.value = []

        self.root.addDistGroup(distItem)

    # 公開関数

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = 'New Item'
        self.folderPath = ''
        self.root = DistGroup()

        self.addInitialDistItemToRoot('webUrl', 'eq')
        self.addInitialDistItemToRoot('fileName', 'ss')
        self.addInitialDistItemToRoot('fileContent', 'ss')

    def getUUID(self) -> str:
        return str(self.id)

    def getName(self) -> str:
        return self.name

    def getFolderPath(self) -> str:
        return self.folderPath

    def setName(self, name: str):
        self.name = name

    def setFolderPath(self, folderPath: str):
        self.folderPath = folderPath

    def importJson(self, data: dict):
        if data['type'] != 'DistCollection':
            return

        self.id = data['id']
        self.name = data['name']
        self.folderPath = data['folderPath']

        buf = DistGroup()

        buf.importJson(data['root'])

        self.root = buf

    def exportJson(self) -> dict:
        return {
            'type': self.type,
            'id': str(self.id),
            'name': self.name,
            'folderPath': self.folderPath,
            'root': self.root.exportJson(),
        }

    def deepCopy(self, distCollection: DistCollection):
        self.importJson(distCollection.exportJson())
