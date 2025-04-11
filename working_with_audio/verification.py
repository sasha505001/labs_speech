import torchaudio
from speechbrain.pretrained import SpeakerRecognition


# Загружаем модель speaker verification
verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-xvect",
    savedir="pretrained_models/spkrec-xvect"
)   

# Путь к эталонной записи администратора
signal1, fs1 = torchaudio.load("admin.wav")
# Путь к новой проверяемой записи
signal2, fs2 = torchaudio.load("test_sample.wav")

# Считаем вероятность того что обе записи принадлежат одному человеку
score, prediction = verification.verify_batch(signal1.unsqueeze(0), signal2.unsqueeze(0))

print(f"Similarity score: {score.item():.2f}")
print(f"Same person? {'Yes' if prediction else 'No'}")