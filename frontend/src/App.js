import './App.css';
import { useState, useEffect } from "react";


function App() {
  
  const [models, setModels] = useState([]); // список доступных моделей
  const [selectedModel, setSelectedModel] = useState("Espeak NG"); // выбранная модель
  const [audioURL, setAudioURL] = useState(''); // URL до сгенерированного аудио

  // стартовая фигня по крайней мере 
  useEffect(() => { 
    fetch("http://127.0.0.1:5000/apis/names")
    .then( response => response.json()) 
    .then(data => {
      setModels(data)
      setSelectedModel(data[0]) // выбираю первую модель 
      console.log(data)
      console.log(data[0])
    })
    .catch(error => console.error(error))
  }, [])
  
  return (
    <div className="hell">
      <h1>Text-to-Speech Converter</h1>
      <p>
        <select id="model-select" name= "model" className="all_doc" defaultValue="Espeak NG">
          <option value="ESpeak NG">ESpeak NG</option>
          <option value="Google TTS">Google TTS</option>
          <option value="Pyttsx3">Pyttsx3</option>
          <option value="Silero">Silero</option>
          <option value="Vosk TTS">Vosk TTS</option>
        </select>
        <br />
        <textarea
          id = "text-to-convert"
          className="all_doc"
          rows="4"
          placeholder="Enter your text here..."
        ></textarea>
        <br />
        <button id = "convert-button" className="all_doc">Convert to Speech</button>
      </p>
      <h2>Audio output</h2>
        <audio id='player_audio' className="all_doc" controls>
          <source src={audioURL || null} type="audio/mpeg" />
          Ваш браузер не поддерживает аудио.
        </audio>
    </div>
  );
}

export default App;
