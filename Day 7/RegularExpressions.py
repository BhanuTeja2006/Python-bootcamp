import re 

data = "sample 9876543210 20/06/2024"
pattern = re.compile(r"\d")
pattern = re.compile(r"\D")
pattern = re.compile(r"\w")
pattern = re.compile(r"\W")
pattern = re.compile(r"\W+")
pattern = re.compile(r"\s")
pattern = re.compile(r"\S")
pattern = re.compile(r"\b")
pattern = re.compile(r"a\b")
pattern = re.compile(r'[ab]')
pattern = re.compile(r'[a-z]')
pattern = re.compile(r'[A-Z]')
pattern = re.compile(r'\d{10}')

res = re.finditer(pattern, data)

for row in res:
    print(row)
