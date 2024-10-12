#removeprefix()用于从字符串的开头移除指定的前缀.
nostarch_url='https://nostarch.com'
nostarch_url=nostarch_url.removeprefix('https://')#删除前缀https://
print(nostarch_url)