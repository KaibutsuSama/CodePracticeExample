domains = {"de": "Germany", "sk": "Slovakia", "hu": "Hungary",
           "us": "United States", "no": "Norway"}

for key in domains:
    print(key)

for val in domains:
    print(val)

for k, v in domains.items():
    print(": ".join((k,v)))
