from gtts import gTTS
from playsound import playsound

text = '''
Dryckeslista	Kan jag få se er dryckeslista?	
Reservation	Jag har en reservation på namnet Johansson.	
Räkor	Jag skulle vilja ha räkor till förrätt.	
Grilla	Kan ni grilla köttet medium rare, tack?	
Specialerbjudande	Vilket är ert specialerbjudande för dagen?	

'''

# text = '''
# Äta	Jag gillar att äta fisk
# Beställa	Kan jag beställa en pizza
# Meny	Kan jag få en meny, tack?
# Kypare	Kyparen kommer snart
# Notan	Kan jag få notan, tack?
# '''

text = '''
Har ni några vegetariska varma rätter?
'''

language = "sv"

# Create gTTS object with the text and language
tts = gTTS(text, lang=language, slow=True)

# Save the audio file
tts.save("Varma rätter.mp3")

# Play the audio file
# playsound("bestalla.mp3")
