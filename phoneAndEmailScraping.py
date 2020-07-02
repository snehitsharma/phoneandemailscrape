import re,pyperclip

phoneReex = re.compile('''
[+]\d\d 
-?
\d\d\d\d\d\d\d\d''',re.VERBOSE)



emailReex = re.compile('''
[a-zA-Z0-9._]+
@
[a-zA-Z0-9._]+
''',re.VERBOSE)

text = pyperclip.paste()

phoneNumbers = phoneReex.findall(text)
emailId =  emailReex.findall(text)
print(phoneNumbers)
print(emailId)

#results = '\n'.join(phoneNumbers) + '\n' +'\n'.join(emailId)
#pyperclip.copy(results)
