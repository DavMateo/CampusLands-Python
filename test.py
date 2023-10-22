dictTest = {"123": {"1": "ABC", "2": "DEF"}}
dictTest2 = {"456": {"DEF"}}
lstTest = []
lstTest.append(dictTest)
lstTest.append(dictTest2)

print(lstTest, len(lstTest))
print(lstTest[0])
print("")
cod = "123"


print(dict(lstTest))