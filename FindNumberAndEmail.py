import re, pyperclip

PhoneRegex = re.compile('''(
                (\d{3}|\(\d{3}\))?      # area code
                (\s|-|\.)?              # seperator
                (\d{3})                 # first 3 digits
                (\s|-|\.)               # seperator
                (\d{4})                 # last 4 digits
                (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''',re.VERBOSE)

EmailRegex = re.compile('''(
                [a-zA-Z0-9._%+-]+       # username
                @                       # @ symbol
                [a-zA-Z0-9.-]+          # domain name
                (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)


#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = PhoneRegex.findall(text)
extractedEmail = EmailRegex.findall(text)

matches = []
for groups in extractedPhone:
    matches.append(groups[0])
for groups in extractedEmail:
    matches.append(groups[0])


results = ('\n'.join(matches))
if len(results):
    # pyperclip.copy(results)
    print(results)
else:
    print("No found")