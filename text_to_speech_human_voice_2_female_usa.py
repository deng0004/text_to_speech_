import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the speech
engine.setProperty('rate', 200)  # Increased rate for faster speech
engine.setProperty('volume', 1.0)  # Set the volume level (0.0 to 1.0)

# Set the voice to a female American sweet voice
voices = engine.getProperty('voices')
# Find the desired voice by iterating through available voices
for voice in voices:
    if 'TTS_MS_EN-US_ZIRA_11.0' in voice.id:
        engine.setProperty('voice', voice.id)
        break

# Set the path to save the generated audio file
audio_path = 'output.mp3'

# Text to be converted to speech
text = '''
I sat behind the wheel of my car, gazing into the inky blackness that stretched out before me. It was well past midnight, and the night held an eerie stillness. The road seemed to disappear into the darkness, with only the feeble glow of my headlights illuminating the way ahead. I was alone, my only companion the haunting sound of my own breath.

I had always been an adventurous soul, but that night, a sense of unease lingered in the pit of my stomach. It was a feeling that something wasn't quite right, as if the very air was thick with a hidden menace. Ignoring my instincts, I tightened my grip on the steering wheel and pressed on, my destination miles away.

As I ventured deeper into the night, the road became increasingly desolate. Shadows danced and flickered at the edge of my vision, playing tricks on my tired mind. The occasional hoot of an owl or the rustling of leaves in the wind sent shivers down my spine. Each passing mile only heightened the growing sense of dread that clung to me like a second skin.

Then, it happened. A flicker of movement caught my eye in the rearview mirror. I glanced back and gasped. Behind me, a pair of headlights pierced the darkness, closing in fast. Panic gripped my heart as I realized there was nowhere to escape. The road stretched out before me like an endless, nightmarish path.

The vehicle behind me drew nearer, its headlights blinding and relentless. I could feel its presence, a malevolent force that threatened to swallow me whole. I sped up, hoping to outrun the pursuer, but it matched my pace effortlessly. The sound of the engine roared in my ears, drowning out all other noise.

As I glanced back again, a face appeared in the rearview mirror. Pale and distorted, its eyes burned with an unholy intensity. It was a face twisted by torment, a visage that sent a jolt of terror coursing through my veins. My heart raced, pounding against my chest like a caged animal.

In a desperate attempt to escape, I swerved onto a narrow side road. The pursuing vehicle followed suit, its relentless pursuit unyielding. Panic consumed me, blurring my vision and clouding my judgment. Fear and adrenaline merged into a lethal cocktail, driving me to the brink of madness.

Minutes turned into hours as the chase continued, the darkness around me seemingly endless. My mind became a chaotic mess, fragments of thoughts and prayers jumbled together. The road ahead seemed to twist and warp, mocking my attempts at escape. It felt as if I had entered a nightmarish labyrinth with no exit.

Suddenly, I noticed a faint glimmer of light in the distance, like a beacon of hope...
'''

# Save the speech to an audio file
engine.save_to_file(text, audio_path)

# Run the speech synthesis
engine.runAndWait()

print(f"Speech saved to: {audio_path}")
