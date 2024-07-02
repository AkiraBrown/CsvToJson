import csv
import json

##This converts csv to JSON assuming an object

print("This is the csv to json converter")
def make_json(csvFilePath, rowName,jsonName="Data"):
    data ={}
    with open(csvFilePath,encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows[rowName]
            data[key] = rows
    with open(f"./results/{jsonName}.json", 'w', encoding="utf-8") as jsonf:
        jsonString = json.dumps(data,ensure_ascii=False, indent=4)
        print(jsonString)
        jsonf.write(jsonString)


print("Please provide the path for your csv file")
csvFilePathInput = input()
print("Please provide the new name for the json")
newFileName = input()
print("Provide the first rows name")
nameOfRows = input()
make_json(csvFilePathInput,nameOfRows,newFileName)
print("Done 👍🏿 | File is available in results folder")
