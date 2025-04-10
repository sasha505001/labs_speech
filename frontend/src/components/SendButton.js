// SendButton.js
import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import './SendButton.css';
import './common.css';


function SendButton({text, onConvertClick}) {
  const [isLoading, setIsLoading] = useState(false);
  // принажатии кнопки :
  // отправляю сообщение боту
  // получаю ответ от бота
  // ответ бота отправляю на сервер
  // сервер генерирует 3 аудиофайла
  // шаблон для названия файла
  // получаю каждый файл по отдельности
  // закидываю каждый файл в плееры
  //
  const handleClicked = async() => {
    setIsLoading(true);
    try {
      // отправляю сообщение боту
      let bot_mes = {"text": text}
      // получаю ответ от бота
      
      // данные для запроса: модель - текст
      let data = {"model": selectedModel, "text": text}
      // // запрос для конвертации текста в речь
      // const response = await axios.post('http://localhost:5000/api/generate', data);
      // // обрабатываю результат запроса
      // if(response.status === 200){
      //   // если преобразование прошло успешно
      //   let path = 'http://localhost:5000/generated_audios/' + response.data.path
      //   console.log(path) // Путь к файлу на сервере
      //   await axios.get(path,
      //     {responseType: 'blob'} 
      //   ).then(res => {
      //     let audioBlob = res.data;
      //     const audioUrl = URL.createObjectURL(audioBlob);
      //     onConvertClick(audioUrl);
      //   })
      // }
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

export default SendButton;