import { useCallback, useState, useEffect, useMemo } from "react";
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
  const audioURLRef = useMemo(() =>  audioURL, [audioURL])
  const [text, setText] = useState('');
  const [supportedLang, setSupportedLang] = useState('');

  const handleConvertClick = useCallback(async (AudioURL) =>  {
    if(AudioURL){
      setAudioURL(AudioURL);
    }
    else
      console.log('AudioURL  is null');
  });


  // стартовая фигня по крайней мере 
  useEffect(() => { 
    fetch("http://127.0.0.1:5000/apis/names")
    .then( response => response.json()) 
    .then(data => {
      setModels(data)
      setSelectedModel(data[0]) // выбираю первую модель 

      //----
      fetch(`http://127.0.0.1:5000/apis/get_supported_languages/${data[0]}`)
      .then( response => response.json()) 
      .then(data => {
        setSupportedLang(data.languages)
      })
    })
    .catch(error => console.error(error))
    
  }, [])
  useEffect(() => {
    console.log('audioURLRef updated in app.js:', audioURLRef);
    console.log('audioURL updated in app.js:', audioURL); 
    setAudioURL(audioURLRef)
  }, [audioURLRef]);
  
  
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
      onConvertClick={handleConvertClick}/>
      
      <h2>Audio output</h2>
      {audioURLRef!==null && <AudioPlayer audioURLRef={audioURLRef} />}
      {/* {audioURL && <audio id="player_audio" className="all_doc" source src={audioURL} controls>Ваш браузер не поддерживает элемент audio.</audio>} */}
      {audioURL && (
      <a
        id="download-link"
        className="all_doc"
        href={audioURL}
        download="audio_file.mp3"
      >
        Скачать файл
      </a>
    )}
    </div>
  );
}

export default App;
