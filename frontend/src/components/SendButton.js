// SendButton.js
import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import './SendButton.css';
import './common.css';


function SendButton({requestText, recivedBotAnswer}) {
  const [isLoading, setIsLoading] = useState(false);
  // принажатии кнопки :
  // отправляю сообщение боту+
  // получаю ответ от бота+
  // ответ бота отправляю на сервер
  // сервер генерирует 3 аудиофайла
  // шаблон для названия файла
  // получаю каждый файл по отдельности
  // закидываю каждый файл в плееры
  //
  const handleClicked = async() => {
    setIsLoading(true);
    try {      
      // пишу боту
      let bot_mes = {"text": requestText}
      let response = await axios.post('http://localhost:5000/write_chatbot', bot_mes);
      let bot_answer = ""
      // получаю ответ от бота
      if(response.status === 200){
        bot_answer = response.data.answer;
        recivedBotAnswer(bot_answer);
        console.log(bot_answer)
        // отправляю ответ бота на сервер
        let data = {"text": bot_answer}
        response = await axios.post('http://localhost:5000/generate/audios', data);
      }
      else{
        console.log('Ошибка при получении ответа от бота:', response.status);
        return;
      }
      
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