// ConvertButton.js
import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import './ConvertButton.css';
import './common.css';


function ConvertButton({selectedModel, text, onConvertClick}) {
  const [isLoading, setIsLoading] = useState(false);
  // что должно быть при нажатии кнопки: генерация аудио и подстановка его в плеер
  const handleClicked = async() => {
    setIsLoading(true);
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
          let audioBlob = res.data;
          //console.log('audioBlob:', audioBlob);
          const audioUrl = URL.createObjectURL(audioBlob);
          //console.log('audioUrl:', audioUrl);
          console.log("передал данные")
          onConvertClick(audioUrl);
        })
      }
    } catch (error) {
      console.error(error);
    } finally
    {
      setIsLoading(false);
    }
  }

  return (
    <button 
    id="convert-btn" 
    className="all_doc" 
    onClick={handleClicked}
    disabled={isLoading}>
      {isLoading ? 'Генерация файла...' : 'Convert Text to Speech'}
    </button>
  );
}

export default ConvertButton;