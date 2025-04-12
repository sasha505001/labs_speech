// SendButton.js
import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import './SendButton.css';
import './common.css';


function SendButton({isLoading, setIsLoading,requestText, recivedBotAnswer, setURLs, setCenterOfMass}) {
  
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
    if(requestText===""){
      alert("Введите текст запроса!");
      return;
    }
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
        let res_audios = await axios.post('http://localhost:5000/generate/audios', data);
        if(res_audios.status === 200){
          // получаю пути к аудиофайлам
          let audio_names = res_audios.data.names;
          console.log(audio_names);
          let gtts = await axios.get('http://localhost:5000/generated_audios/' + audio_names[0],
             {responseType: 'blob'});
          let pyttsx3 = await axios.get('http://localhost:5000/generated_audios/' + audio_names[1], 
            {responseType: 'blob'});
          let mixed = await axios.get('http://localhost:5000/generated_audios/' + audio_names[2], 
            {responseType: 'blob'});
          gtts = URL.createObjectURL(gtts.data);
          pyttsx3 = URL.createObjectURL(pyttsx3.data);
          mixed = URL.createObjectURL(mixed.data);
          setURLs(gtts, pyttsx3, mixed);
          // расчёт центра масс
          gtts = await axios.get('http://localhost:5000/center_of_mass/' + audio_names[0]);
          pyttsx3 = await axios.get('http://localhost:5000/center_of_mass/' + audio_names[1]);
          mixed = await axios.get('http://localhost:5000/center_of_mass/' + audio_names[2]);
          console.log(gtts, pyttsx3, mixed);
          gtts = gtts.data.centroid;
          pyttsx3 = pyttsx3.data.centroid;
          mixed = mixed.data.centroid;
          setCenterOfMass(gtts, pyttsx3, mixed);
        }
      }
      else{
        console.log('Ошибка при получении ответа от бота:', response.status);
        return;
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
      {isLoading ? 'In process...' : 'Отправить запрос'}
    </button>
  );
}

export default SendButton;