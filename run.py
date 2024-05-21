from jinja2 import Environment, FileSystemLoader
import os

# Define the directory contents
files = [
    'C0/a0.0__c0.mp3', 'C0/a0.5__c0.mp3', 'C0/a0.7__c0.mp3', 'C0/a1.0__c0.mp3',
    'C0/a1.8__c0.mp3', 'C0/a2.3__c0.mp3', 'C0/a3__c0.mp3', 'C0/a4__c0.mp3',
    'C0/a5__c0.mp3', 'C5/a1.5__c5.mp3', 'C5/a2.3__c5.mp3', 'C5/a2.9__c5.mp3',
    'C5/a3__c5.mp3', 'C5/a4__c5.mp3', 'C5/a7.5__c5.mp3'
]

# Extract values of A and C from filenames
file_info = {'C0': [], 'C5': []}
for file in files:
    parts = file.split('/')
    A_value = parts[1].split('__')[0][1:]
    C_value = parts[0][1:]
    file_info[f'C{C_value}'].append({'A': A_value, 'C': C_value, 'file': file})

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(searchpath='.'))
template = env.get_template('template.html')

# Render the template with the file information
output = template.render(file_info=file_info)

# Save the output to an HTML file
with open('index.html', 'w') as f:
    f.write(output)

print("HTML file generated successfully.")

