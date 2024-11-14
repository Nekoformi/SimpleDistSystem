import json

from lib.distGroup import DistGroup
from lib.distItem import DistItem

testDistGroup = DistGroup() # インスタンスを作成

def printDistGroup(distGroup: DistGroup):
    print('ID: ' + distGroup.getUUID()) # IDを取得
    print('Operation: ' + distGroup.displayOperation()) # 条件演算を表示
    print('Content: ' + json.dumps(distGroup.exportContent(), indent=4, ensure_ascii=False)) # 条件一覧を表示

print('- GET --------------------------------------------------------------------------')

printDistGroup(testDistGroup)

print('Operation dict: ' + json.dumps(testDistGroup.operationDict, indent=4, ensure_ascii=False)) # 条件演算の辞書を表示

print('- SET --------------------------------------------------------------------------')

TEST_OPERATION_INDEX = 1

print('Operation index: ' + str(testDistGroup.getOperationIndex()) + ' → ' + str(TEST_OPERATION_INDEX)) # 条件演算の番地を取得
print('Content: ...')

testDistGroup.setOperationIndex(TEST_OPERATION_INDEX) # 条件演算を変更

newDistGroupId_A = testDistGroup.addNewDistItem() # 新しいDistItemを追加
newDistGroupId_B = testDistGroup.addNewDistItem()
newDistGroupId_C = testDistGroup.addNewDistItem()
newDistGroupId_D = testDistGroup.addNewDistItem()
newDistGroupId_E = testDistGroup.addNewDistItem()

testDistGroup.setDistItemConditionIndex(newDistGroupId_A, 0) # IDを基にDistItemを編集
testDistGroup.setDistItemExpressionIndex(newDistGroupId_A, 2)
testDistGroup.setDistItemValue(newDistGroupId_A, 'hoge')

testDistGroup.setDistItemConditionIndex(newDistGroupId_B, 1)
testDistGroup.setDistItemExpressionIndex(newDistGroupId_B, 2)
testDistGroup.setDistItemValue(newDistGroupId_B, 'fuga')

testDistGroup.setDistItemConditionIndex(newDistGroupId_C, 2)
testDistGroup.setDistItemExpressionIndex(newDistGroupId_C, 2)
testDistGroup.setDistItemValue(newDistGroupId_C, 'piyo')

testDistGroup.setDistItemConditionIndex(newDistGroupId_D, 3)
testDistGroup.setDistItemExpressionIndex(newDistGroupId_D, 2)
testDistGroup.setDistItemValue(newDistGroupId_D, 'nube')

testDistGroup.setDistItemConditionIndex(newDistGroupId_E, 4)
testDistGroup.setDistItemExpressionIndex(newDistGroupId_E, 2)
testDistGroup.setDistItemValue(newDistGroupId_E, 'hoyo')

testDistGroup.moveContentIndex(newDistGroupId_B, -1) # 条件一覧を移動
testDistGroup.moveContentIndex(newDistGroupId_A, +1)
testDistGroup.removeContentIndex(newDistGroupId_E) # 条件一覧を削除

newDistGroupId = testDistGroup.addNewDistGroup() # 新しいDistGroupを追加

newDistGroup = testDistGroup.getDistContent(newDistGroupId) # IDを基にDistGroupやDistItemを取得

newDistItem = DistItem()

newDistGroup.addDistItem(newDistItem) # 引数からオブジェクトを条件一覧に追加することも可能

testDistGroup.pullContentLayer(newDistItem.getUUID()) # 特定のオブジェクトを親の階層へ移動

print('- GET (RE) ---------------------------------------------------------------------')

printDistGroup(testDistGroup)
