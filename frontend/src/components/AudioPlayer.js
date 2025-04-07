// AudioPlayer.js
import React from 'react';
import { useState, useEffect } from 'react';
import './common.css';
import './AudioPlayer.css';

function AudioPlayer({ audioUrlRef }) {
  const [label, setLabel] = useState('Аудиофайл не выбран');

  useEffect(() => {
    console.log("audioPl:");
    if (audioUrlRef) {
      console.log("audioPl:"+ audioUrlRef.current);
      setLabel(`Аудиофайл: ${audioUrlRef.current.name}`);
    } else {
      setLabel('Аудиофайл не выбран');
    }
  }, [audioUrlRef]);

  
  return (
    // <audio id="player_audio" className="all_doc" controls>
    //   {audioBlob && (
    //     <source src={audioBlob}/>
    //   )}
    //   Ваш браузер не поддерживает элемент audio.
    // </audio>
    <label id = "player_audio" className="all_doc">{label}</label>
);
}

export default AudioPlayer;
