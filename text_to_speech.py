from gtts import gTTS

text = input("Enter the text you want to convert to speech: ")
language = 'en'

obj = gTTS(text=text, lang=language, slow=False)
obj.save("sample.mp3")

print("The audio has been saved as 'sample.mp3'")
