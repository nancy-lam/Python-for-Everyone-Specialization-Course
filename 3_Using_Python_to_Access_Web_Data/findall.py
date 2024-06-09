import re

# Find all number in the x text
x = '27 February, 1965 - Beatles For Sale Reaches No.1 In UK Record Retailer Chart'
y = re.findall('[0-9]+', x)
print(y)

# Find and extract email
text = 'I don\'t like the \'name with numbers\'. Like first.last_123@mail.com'
email = re.findall('\S+@\S+', text)
print(email)

# Parentheses tell where to start and stop what string to extract
tx = 'From carlscoffee@shared1.ccsend.com to all the customers in the Glendale, Arizona'
em = re.findall('^From (\S+@\S+)', tx)
print(em)

# Match non-blank charector [^ ]
ed = re.findall('@([^ ]*)', tx)
print(ed)