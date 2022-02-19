# CSV Labs

```py
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # print(csv_reader) # object in memory

    # next(csv_reader)   # preskoci prvni radek

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

    # for line in csv_reader:
    #     print(line)  # vytiskne celou radu
    #     # print(line[2])   # vytiskne jen email
```

```py
import csv

with open('names.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter='\t')
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # print(line)
        print(line['email'])
```
