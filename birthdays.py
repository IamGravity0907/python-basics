import json
# Load existing birthdays or start fresh
bds = json.load(open('bds.json','r')) if 'bds.json' else {}
def save(): json.dump(bds, open('bds.json','w'))

while True:
    # Show menu options
    print("\n1.Add 2.Show 3.Exit")
     # Get user choice
    c = input("Pick: ")
    # Add a new birthday
    if c=='1': bds[input("Name:")] = input("Date (YYYY-MM-DD): "); save()
    # Save to file
    elif c=='2': 
         # Show all birthdays
        print(bds)
    # Exit the loop
    elif c=='3': break
