dic = {}
dic["aaa"] = "bb"
print(dic.get("aaa")) # output:bb
dic["aaa"] = 6
print(dic.get("aaa")) # output:6
del dic["aaa"]
print(dic.get("aaa")) # output:None