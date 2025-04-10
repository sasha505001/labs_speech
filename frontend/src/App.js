import { useCallback, useState, useEffect, useMemo } from "react";
import './App.css';
import TextInput from './components/TextInput';
import SendButton from './components/SendButton';


function App() { 
  // Текст запроса
  const [requestText, setRequestText] = useState('');
  const [answerText, setAnswerText] = useState(''); // Текст ответа
  const [gttsURL, setGttsURL] = useState(""); // URL до сгенерированного аудио
  const [pyttsx3URL, setPyttsx3URL] = useState(""); // URL до сгенерированного аудио
  const [mixedURL, setMixedURL] = useState(""); // URL до сгенерированного аудио

  const [audioURL, setAudioURL] = useState(null); // URL до сгенерированного аудио
  const audioURLRef = useMemo(() =>  audioURL, [audioURL])
  
  const recivedBotAnswer = useCallback((answer) => {
    setAnswerText(answer);
  });
  
  const handleConvertClick = useCallback(async (AudioURL) =>  {
    if(AudioURL){
      setAudioURL(AudioURL);
    }
    else
      console.log('AudioURL  is null');
  });
  useEffect(() => {
    // console.log('audioURLRef updated in app.js:', audioURLRef);
    // console.log('audioURL updated in app.js:', audioURL); 
    setAudioURL(audioURLRef)
  }, [audioURLRef]);
  
  return (
    <div className="hell">
      <h1>Your Asistent</h1>

      <TextInput text={requestText} setText={setRequestText} />
      <SendButton 
      requestText = {requestText}  
      recivedBotAnswer = {recivedBotAnswer}/>
      <h2>Ответ бота</h2>
      <label className="all_doc">{answerText ? answerText : 'собщений не было или произошла ошибка'}</label>
      
      <br />
      <h1>Audio output</h1>  
      <br />
      
      <h2>Google TTS</h2>
      <h2>Pyttsx3</h2>
      <h2>Mixed</h2>
    </div>
  );
}

export default App;
