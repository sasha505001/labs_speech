# тестируемые API
from tts_apis.tts_espeakng import create_espeakng_audio
from tts_apis.tts_google import create_gtts_audio
from tts_apis.tts_microsoft import crate_microsoft_audio
from tts_apis.tts_pyttsx3 import create_pyttsx3_audio
from tts_apis.tts_silero import create_selero_audio
from tts_apis.tts_vosk import create_vosktts_audio



# todo неправильные тесты
# когда вводится неверный язык

# tts_espeakng
create_espeakng_audio("hello world")
create_espeakng_audio("hi")

# tts_google
create_gtts_audio("серьёзные дела")
create_gtts_audio("how it's sounds in english")
create_gtts_audio("hi")

# tts_microsoft
crate_microsoft_audio("today i work on full day")

# tts_pyttsx3
create_pyttsx3_audio("нежданно негаданно")
create_pyttsx3_audio("english text sounds")
create_pyttsx3_audio("hi")

# tts_silero
create_selero_audio("привет жестокий мир")

# tts_vosk
create_vosktts_audio("ну работаем что делать")