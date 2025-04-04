// ConvertButton.js
import React, { useEffect } from 'react';
import axios from 'axios';
import './ConvertButton.css';
import './common.css';


function ConvertButton({selectedModel, text, audioBLob, setAudioBLob}) {
  // что должно быть при нажатии кнопки: генерация аудио и подстановка его в плеер
  const handleClicked = async() => {
    try {
      // данные для запроса: модель - текст
      let data = {"model": selectedModel, "text": text}
      // запрос для конвертации текста в речь
      const response = await axios.post('http://localhost:5000/api/convert', data);
      // обрабатываю результат запроса
      if(response.status === 200){
        // если преобразование прошло успешно
        let path = 'http://localhost:5000/generated_audios/' + response.data.path
        console.log(path) // Путь к файлу на сервере
        await axios.get(path,
          {responseType: 'blob'} 
        ).then(res => {
          let audioBLob = res.data;
          setAudioBLob(audioBLob)
        })
      }
    } catch (error) {
      console.error(error);
    }
  }

  

  return (
    <button id="convert-btn" className="all_doc" onClick={handleClicked}>
      Convert Text to Speech
    </button>
  );
}

export default ConvertButton;