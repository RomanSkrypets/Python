favourive_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    'roman' : 'python',
    'oleg' : 'security',
}

for people, lang in favourive_languages.items():
    print(f"Hello {people.title()} thank you for the choise language {lang.title()}")

print("\n")

coders = ['jen', 'edward', 'olga', 'vlad', 'john']
for coder in coders:
    if coder not in favourive_languages:
        print(f"Please, {coder.title()} take a survey!")
    else:
        print(f"Thank you. {coder.title()} you have already taken the survey!")