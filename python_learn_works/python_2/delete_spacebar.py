#strip（）可用于删除str两端的空格或特定字符，当括号内无内容时，默认删除空格。rstrip、lstrip分别对应删除右侧（左侧）空格特定字符。
favarite_language=" python "
print(favarite_language.rstrip())
print(favarite_language.lstrip())
print(favarite_language.strip())
favarite_language=favarite_language.strip()
print(favarite_language)