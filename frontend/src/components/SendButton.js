// SendButton.js
import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import './SendButton.css';
import './common.css';

function SendButton({ audioBlob, setRequestText, setAnswerText, setURLs, setCenterOfMass }) {

  const [isLoading, setIsLoading] = useState(false);

  const handleClicked = async() => {

    if(!audioBlob){
      alert("Сначала сделайте запись!");
      return;
    }

    try{
      setIsLoading(true);

      // Формируем FormData для передачи файла
      let formData = new FormData();
      formData.append('file', audioBlob, 'recorded_audio.webm');

      // Отправляем аудио на сервер для распознавания речи + ответа бота
      let response = await axios.post('http://localhost:5000/process_audio', formData,{
         headers: {'Content-Type': 'multipart/form-data'}
      });

      if(response.status === 200){
        let my_request_text = response.data.text;
        setRequestText(my_request_text);
        let data = {"text": my_request_text};
        let bot_response = await axios.post('http://localhost:5000/write_chatbot', data);
        if(bot_response.status === 200){
          let bot_answer_text = bot_response.data.answer;
          
          setAnswerText(bot_answer_text);

          // Затем генерируем аудиофайлы из ответа бота:
          let data_for_tts= {"text": bot_answer_text};
          
          let res_audios=await axios.post('http://localhost:5000/generate/audios', data_for_tts);

          if(res_audios.status ===200){
            let audio_names=res_audios.data.names;

            let gtts=await axios.get(`http://localhost:5000/generated_audios/${audio_names[0]}`,{responseType:'blob'});
            let pyttsx3=await axios.get(`http://localhost:5000/generated_audios/${audio_names[1]}`,{responseType:'blob'});
            let mixed=await axios.get(`http://localhost:5000/generated_audios/${audio_names[2]}`,{responseType:'blob'});

            gtts= URL.createObjectURL(gtts.data);
            pyttsx3= URL.createObjectURL(pyttsx3.data);
            mixed= URL.createObjectURL(mixed.data);

            setURLs(gtts, pyttsx3,mixed);

            // Расчет центра масс:
            let gtts_centroid_resp=await axios.get(`http://localhost:5000/center_of_mass/${audio_names[0]}`);
            let pyttsx3_centroid_resp=await axios.get(`http://localhost:5000/center_of_mass/${audio_names[1]}`);
            let mixed_centroid_resp=await axios.get(`http://localhost:5000/center_of_mass/${audio_names[2]}`);

            console.log(gtts_centroid_resp,gtts_centroid_resp,mixed_centroid_resp)

            setCenterOfMass(
              gtts_centroid_resp.data.centroid,
              pyttsx3_centroid_resp.data.centroid,
              mixed_centroid_resp.data.centroid)
            }
          }
       }

     }catch(error){
       console.error(error)
     }finally{
       setIsLoading(false)
     }
    
  }


  return (
    <button className="all_doc" onClick={handleClicked} disabled={isLoading}>
       {isLoading? "In process..." : "Отправить"}
     </button>
  )
}

export default SendButton;