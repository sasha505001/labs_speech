// ConvertButton.js
import React from 'react';
import axios from 'axios';
import './ConvertButton.css';
import './common.css';

function ConvertButton({selectedModel, text, audioURL,setAudioURL}) {
  const handleClicked = async() => {
    try {
      let data = {"model": selectedModel, "text": text}
      //console.log(data);
      const response = await axios.post('http://localhost:5000/api/convert', data);
      if(response.status === 200){
        let path = 'http://localhost:5000/generated_audios/' + response.data.path
        console.log(path)
        await axios.get(path,
          {responseType: 'blob'} 
        ).then(res => {
          const audioBLob = res.data;
          setAudioURL(audioBLob)
        })
      }
      else if(response.status === 500){
        console.log("не получилось преобразовать");
      }
      else 
      {
        console.log("не принял запрос");
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