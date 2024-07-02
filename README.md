# The CSV TO JSON converter

There are two commands to be mindful of in this project.

1. Convert csv to json using a dictionary

```bash
sh cnvDict
```

2. Convert csv to json using list (Best Way)

```bash
sh cnvList
```

The cnvList method is better simply because it returns json in an array rather than an object like cnvDict does. This makes it easier to iterate through the data. With `sh cnvList` it
prompts for the location of the csv file and the new name of the file. It then takes parses the csv file into json and creates that file in the results folder.
