#write a program to fill in letter template given below with name and date.
letter = '''Dear <|Name|>,

                You are selected!
                Date: <|Date|>'''
print(letter.replace("<|Name|>","Suresh".replace("<|Date|>","27/10/2026")))