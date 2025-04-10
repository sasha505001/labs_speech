import { useCallback, useState, useMemo } from "react";
import './App.css';
import TextInput from './components/TextInput';
import SendButton from './components/SendButton';
import AudioPlayer from './components/AudioPlayer';

function App() { 
  // Текст запроса
  const [requestText, setRequestText] = useState('');
  const [answerText, setAnswerText] = useState(''); // Текст ответа
  // URLs до сгенерированного аудио
  const [gttsURL, setGttsURL] = useState(null); // URL до сгенерированного аудио
  const [pyttsx3URL, setPyttsx3URL] = useState(null); // URL до сгенерированного аудио
  const [mixedURL, setMixedURL] = useState(null); // URL до сгенерированного аудио
  
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

      <TextInput text={requestText} setText={setRequestText} isReadOnly={false}/>
      <SendButton 
      requestText = {requestText}  
      recivedBotAnswer = {recivedBotAnswer}
      setURLs = {setURLs}
      />
      <h2>Ответ бота</h2>

      
      <TextInput text={answerText ? answerText : 'собщений не было или произошла ошибка'} setText={setRequestText} isReadOnly={true}/>
      <br />
      <h1>Audio output</h1>  
      <h2>Google TTS</h2>
      <AudioPlayer audioURLRef={gttsURL} />
      <h2>Pyttsx3</h2>
      <AudioPlayer audioURLRef={pyttsx3URL} />
      <h2>Mixed</h2>
      <AudioPlayer audioURLRef={mixedURL} />
    </div>
  );
}

export default App;
