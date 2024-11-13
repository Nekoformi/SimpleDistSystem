import json

from lib.distItem import DistItem

testDistItem = DistItem() # インスタンスを作成

def printDistItem(distItem: DistItem):
    print('ID: ' + distItem.getUUID()) # IDを取得
    print('Condition: ' + distItem.displayCondition()) # 条件項目を表示
    print('Expression: ' + distItem.displayExpression()) # 条件式を表示
    print('Value: "' + distItem.displayValue() + '"') # 条件内容を表示

print('- GET --------------------------------------------------------------------------')

printDistItem(testDistItem)

print('Condition dict: ' + json.dumps(testDistItem.conditionDict, indent=4, ensure_ascii=False)) # 条件項目の辞書を表示
print('Expression dict: ' + json.dumps(testDistItem.expressionDict, indent=4, ensure_ascii=False)) # 条件式の辞書を表示

print('- SET --------------------------------------------------------------------------')

TEST_CONDITION_INDEX = 0
TEST_EXPRESSION_INDEX = -1
TEST_VALUE = 'Alice, Bob, Carol,    Dave'

print('Condition index: ' + str(testDistItem.getConditionIndex()) + ' → ' + str(TEST_CONDITION_INDEX)) # 条件項目の番地を取得
print('Expression index: ' + str(testDistItem.getExpressionIndex()) + ' → ' + str(TEST_EXPRESSION_INDEX) + ' (Missing index)') # 条件式の番地を取得
print('Value: "' + testDistItem.displayValue() + '" → "' + TEST_VALUE + '"')

testDistItem.setConditionIndex(TEST_CONDITION_INDEX) # 条件項目を変更
testDistItem.setExpressionIndex(TEST_EXPRESSION_INDEX) # 条件式を変更
testDistItem.setValue(TEST_VALUE) # 条件内容を変更

print('- GET (RE) ---------------------------------------------------------------------')

printDistItem(testDistItem)
