text = "abcdefghijklmop"
print(dir(text))
help(text.isupper)
print(text.isupper())        # is the text all uppercase
print("ABC".isupper())       # is the text all uppercase
print(text.upper())          # convert the text to uppercase
print(text.upper().isupper())    # is the text all uppercase? YES

new_text = text.upper()
print(text, new_text)
print("bannannnana" .count("n"))
print("bannannnana" . replace("n", "d"))
print("banabababnan" .index("b"))

sentence = "Hello, kind sir; how may! i be of serice today?"
print(sentence.replace(",", "").replace(";","").replace("!","").replace("?",""))

punctuation = ".,;!?-"
for p in punctuation:
    sentencce = sentence.replace(p,"")

print(sentence)


print("This is a sentence and I want the words".split("  "))
text = "Bob goes to schol. Bob like to play tennis and he is also a very good runner. Bob has not many friend," \
       " His best friend is Tom"

print(text.find("Bob"))

print(text.rfind("Bob"))

i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1

name = input("whats your name? ")
print(f"hello, {name}!")



