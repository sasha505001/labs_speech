import { useCallback, useState, useMemo } from "react";
import './App.css';
import TextInput from './components/TextInput';
import SendButton from './components/SendButton';
import AudioPlayer from './components/AudioPlayer';
import AudioRecorder from "./components/AudioRecorder";

function App() { 

  // файл аудиозаписи с запросом
  const [audioFile, setAudioFile] = useState(null);
  
  const [requestText, setRequestText] = useState(''); // Текст запроса
  const [answerText, setAnswerText] = useState(''); // Текст ответа
  // URLs до сгенерированного аудио
  const [gttsURL, setGttsURL] = useState(null); // URL до сгенерированного аудио
  const [pyttsx3URL, setPyttsx3URL] = useState(null); // URL до сгенерированного аудио
  const [mixedURL, setMixedURL] = useState(null); // URL до сгенерированного аудио
  
  // Расчет центра масс
  const [centerOfMassGtts, setCenterOfMassGtts] = useState("");
  const [centerOfMassPyttsx3, setCenterOfMassPyttsx3] = useState("");
  const [centerOfMassMixed, setCenterOfMassMixed] = useState("");

  async function setCenterOfMass(centerOfMassGtts, centerOfMassPyttsx3, centerOfMassMixed){
    setCenterOfMassGtts(centerOfMassGtts);
    setCenterOfMassPyttsx3(centerOfMassPyttsx3);
    setCenterOfMassMixed(centerOfMassMixed);
  }

  const recivedBotAnswer = useCallback((answer) => {
    setAnswerText(answer);
  });
  
  async function setURLs(gttsURL, pyttsx3URL, mixedURL){
    if(gttsURL){
      setGttsURL(gttsURL);
    }
    if(pyttsx3URL){
      setPyttsx3URL(pyttsx3URL);
    }
    if(mixedURL){
      setMixedURL(mixedURL);
    }
  }
  
  return (
    <div className="hell">
      <h1>Your Asistent</h1>

      // кнопка записи
      <AudioRecorder setAudioFile = {setAudioFile}/>

      <h2>Ваш запрос</h2>
      <TextInput text={requestText} setText={setRequestText} isReadOnly={true}/>
      <h2>Ответ бота</h2>

      
      <TextInput text={answerText ? answerText : 'собщений не было или произошла ошибка'} setText={setRequestText} isReadOnly={true}/>
      <br />
      <h1>Audio output</h1>  
      <h2>Google TTS</h2>
      <label className="all_doc">{"центр масс: " + centerOfMassGtts}</label>
      <AudioPlayer audioURLRef={gttsURL} />
      <h2>Pyttsx3</h2>
      <label className="all_doc">{"центр масс: " + centerOfMassPyttsx3}</label>
      <AudioPlayer audioURLRef={pyttsx3URL} />
      <h2>Mixed</h2>
      <label className="all_doc">{"центр масс: " + centerOfMassMixed}</label>
      <AudioPlayer audioURLRef={mixedURL} />
    </div>
  );
}

export default App;
