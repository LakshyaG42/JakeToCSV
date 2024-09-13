import re
import csv

data = """

"""
datePattern = r'(\d{1,2}/\d{1,2}/\d{2})'
companyPattern = r'\s*([\w\s]+)\s+\[\s*([\w@.]+)(?:\s*;\s*([\w$]+))?\s*\]\s*->\s*([\w\s]+)'

results = []
lines = data.splitlines()
currDate = None 
for line in lines:
    dateMatch = re.match(datePattern, line.strip())
    if dateMatch:
        currDate = dateMatch.group(1)
    else:
        companyMatch = re.search(companyPattern, line.strip())  
        print(companyMatch)
        if companyMatch and currDate:
            companyName, email, password, status = companyMatch.groups()
            results.append([currDate, companyName.strip(), email.strip(), password or '', status.strip()])

with open('applications.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date Applied', 'Company Name', 'Email', 'Password', 'Status']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(results)
print(results)
print("CSV file created successfully.")
