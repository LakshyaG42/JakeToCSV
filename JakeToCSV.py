import re
import csv

data = """
9/11/24
    Pearson [ jaketduffy@comcast.net ] -> UNDER REVIEW (as of 9/11)
    Westfield [ jaketduffy@comcast.net ] -> UNDER REVIEW (as of 9/11)
    Wayfair [ jaketduffy@comcast.net ] -> UNDER REVIEW (as of 9/11) 
9/6/24
    Spectrum [ jaketduffy@comcast.net; eh73HU82H61$hi789 ] -> UNDER REVIEW (as of 9/11)
"""

datePattern = r'(\d{1,2}/\d{1,2}/\d{2})'

companyPattern = r'\s*([\w\s]+)\s+\[\s*([\w@.]+)(?:;\s*([\w$]+))?\s*\]\s*->\s*([\w\s]+)'
results = []
lines = data.splitlines()
currData = None 
for line in lines:
    dateMatch = re.match(datePattern, line.strip())
    if dateMatch:
        currDate = dateMatch.group(1)
    else:
        companyMatch = re.match(companyPattern, line.strip())
        if companyMatch and currDate:
            companyName, email, password, status = companyMatch.groups()
            results.append([currDate, companyName.strip(), email.strip(), password or '', status.strip()])

with open('applications.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date Applied', 'Company Name', 'Email', 'Password', 'Status']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(results)

print("CSV file created successfully.")
