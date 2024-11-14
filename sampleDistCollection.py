import json

from lib.distCollection import DistCollection
from lib.distData import DistData

testDistCollection = DistCollection() # インスタンスを作成

def printDistCollection(distCollection: DistCollection):
    print('ID: ' + distCollection.getUUID()) # IDを取得
    print('Name: "' + distCollection.getName() + '"') # コレクション名を表示
    print('Folder path: "' + distCollection.getFolderPath() + '"') # フォルダーパスを表示
    print('Root: ' + json.dumps(distCollection.root.exportJson(), indent=4, ensure_ascii=False)) # RootDistGroupを表示

print('- GET --------------------------------------------------------------------------')

printDistCollection(testDistCollection)

print('- SET --------------------------------------------------------------------------')

TEST_NAME = 'HOGE FUGA FILE'
TEST_FOLDER_PATH = './HogeFugaFolder'

print('Name: "' + testDistCollection.getName() + '" → "' + TEST_NAME + '"')
print('Folder path: "' + testDistCollection.getFolderPath() + '" → "' + TEST_FOLDER_PATH + '"')

testDistCollection.setName(TEST_NAME) # コレクション名を変更
testDistCollection.setFolderPath(TEST_FOLDER_PATH) # フォルダーパスを変更

TEST_WEB_URL_VALUE = 'https://example.com'
TEST_FILE_NAME_VALUE = 'hoge,fuga'
TEST_FILE_CONTENT_VALUE = 'Hello, world!'

print('root.content[0]@distItem.value = "' + TEST_WEB_URL_VALUE + '"')
print('root.content[1]@distItem.value = "' + TEST_FILE_NAME_VALUE + '"')
print('root.content[2]@distItem.value = "' + TEST_FILE_CONTENT_VALUE + '"')

testDistCollection.root.content[0].setValue(TEST_WEB_URL_VALUE)
testDistCollection.root.content[1].setValue(TEST_FILE_NAME_VALUE)
testDistCollection.root.content[2].setValue(TEST_FILE_CONTENT_VALUE)

print('- GET (RE) ---------------------------------------------------------------------')

printDistCollection(testDistCollection)

print('- COPY -------------------------------------------------------------------------')

copyDistCollection = DistCollection()

copyDistCollection.deepCopy(testDistCollection) # オブジェクトをディープコピー

copyDistCollection.root.content = []

print('Original: ')
printDistCollection(testDistCollection)

print('Copy: ')
printDistCollection(copyDistCollection)

print('- SETUP ------------------------------------------------------------------------')

testData_A = DistData()
testData_B = DistData()
testData_C = DistData()

testData_A.setData({
    'webUrl': 'https://example.com',
    'webContent': '<html>...</html>',
    'fileName': 'hoge',
    'fileExtension': 'txt',
    'fileContent': 'Hello, world!',
}) # 情報を設定

testData_B.setData({
    'webUrl': 'https://another.example.com',
    'webContent': '<html>...</html>',
    'fileName': 'fuga',
    'fileExtension': 'txt',
    'fileContent': 'Hello, human!',
})

testData_C.setData({
    'webUrl': 'https://another.example.com',
    'webContent': '<html>...</html>',
    'fileName': 'piyo',
    'fileExtension': 'txt',
    'fileContent': 'Goodbye, human!',
})

print('Test Data A: ' + json.dumps(testData_A.getData(), indent=4, ensure_ascii=False)) # 情報を表示
print('Test Data B: ' + json.dumps(testData_B.getData(), indent=4, ensure_ascii=False))
print('Test Data C: ' + json.dumps(testData_C.getData(), indent=4, ensure_ascii=False))

print('- EXE 1 ------------------------------------------------------------------------')

print('Root operation index: 0')

testDistCollection.root.setOperationIndex(0)

print('Test Data A - Result: ' + str(testDistCollection.root.match(testData_A))) # 結果を表示 (1: 一致, 0: 不一致)
print('Test Data B - Result: ' + str(testDistCollection.root.match(testData_B)))
print('Test Data C - Result: ' + str(testDistCollection.root.match(testData_C)))

print('Test Data A - Trace: ' + json.dumps(testDistCollection.root.trace(testData_A), indent=4, ensure_ascii=False)) # 結果の詳細を表示
print('Test Data B - Trace: ' + json.dumps(testDistCollection.root.trace(testData_B), indent=4, ensure_ascii=False))
print('Test Data C - Trace: ' + json.dumps(testDistCollection.root.trace(testData_C), indent=4, ensure_ascii=False))

print('- EXE 2 ------------------------------------------------------------------------')

print('Root operation index: 1')

testDistCollection.root.setOperationIndex(1)

print('Test Data A - Result: ' + str(testDistCollection.root.match(testData_A)))
print('Test Data B - Result: ' + str(testDistCollection.root.match(testData_B)))
print('Test Data C - Result: ' + str(testDistCollection.root.match(testData_C)))

print('Test Data A - Trace: ' + json.dumps(testDistCollection.root.trace(testData_A), indent=4, ensure_ascii=False))
print('Test Data B - Trace: ' + json.dumps(testDistCollection.root.trace(testData_B), indent=4, ensure_ascii=False))
print('Test Data C - Trace: ' + json.dumps(testDistCollection.root.trace(testData_C), indent=4, ensure_ascii=False))
