from resemblyzer import VoiceEncoder, preprocess_wav
from scipy.spatial.distance import cosine

def is_admin_voice(admin_audio_path: str, test_audio_path: str, threshold: float = 0.75) -> bool:
    """
    Сравнивает голос из test_audio_path с голосом администратора из admin_audio_path.
    Возвращает True, если голоса совпадают (т.е. говорит админ), иначе False.
    """
    encoder = VoiceEncoder()
    
    # Получаем эмбеддинги для обоих файлов
    admin_embedding = encoder.embed_utterance(preprocess_wav(admin_audio_path))
    test_embedding = encoder.embed_utterance(preprocess_wav(test_audio_path))
    
    # Вычисляем косинусное сходство через scipy
    similarity = 1 - cosine(admin_embedding, test_embedding)
    
    print(f"Косинусное сходство: {similarity:.3f}")
    
    return similarity
