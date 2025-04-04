import { useState, useEffect } from "react";
import './App.css';
import ModelSelect from './components/ModelSelect';
import TextInput from './components/TextInput';
import ConvertButton from './components/ConvertButton';
import AudioPlayer from './components/AudioPlayer';
import SupportedLang from './components/SupportedLang';

function App() { 
  
  const [models, setModels] = useState([]); // список доступных моделей
  const [selectedModel, setSelectedModel] = useState(); // выбранная модель
  const [audioURL, setAudioURL] = useState(null); // URL до сгенерированного аудио
  const [text, setText] = useState('');
  const [supportedLang, setSupportedLang] = useState('');

  // стартовая фигня по крайней мере 
  useEffect(() => { 
    fetch("http://127.0.0.1:5000/apis/names")
    .then( response => response.json()) 
    .then(data => {
      setModels(data)
      setSelectedModel(data[0]) // выбираю первую модель 
      //console.log(data)
      //console.log(data[0])
      setAudioURL(null)
      setSupportedLang('en')
    })
    .catch(error => console.error(error))
    
  }, [])
  
  return (
    <div className="hell">
      <h1>Text-to-Speech Converter</h1>
      
      <ModelSelect 
        models={models} 
        selectedModel={selectedModel} 
        setSelectedModel={setSelectedModel} 
        setSupportedLang={setSupportedLang}
      />
      <SupportedLang SupportedLang={supportedLang} />
      <br />
      <TextInput text={text} setText={setText} />
      <br />
      <ConvertButton 
      selectedModel = {selectedModel} 
      text = {text}  
      audioURL={audioURL}
      setAudioURL={setAudioURL}/>
      
      <h2>Audio output</h2>
      <AudioPlayer audioURL={audioURL} setAudioURL={setAudioURL} />
    </div>
  );
}

export default App;
