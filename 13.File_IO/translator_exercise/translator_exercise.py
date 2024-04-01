# File IO
# Translator Exercise
# Build an offline translator service using Python module and files.

from translate import Translator
translator = Translator(to_lang='ja')

try:
    with open("test.txt", mode='r') as source:
        text = source.read()
        print(text)
        translation = translator.translate(text)
        print('\n', translation)
        # getting UnicodeEncodeError
        # with open('test_ja.txt', mode='w') as result:
        #     result.write(translation)

except FileNotFoundError as err:
    print("Please check your file path.")
