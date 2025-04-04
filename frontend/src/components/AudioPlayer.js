// AudioPlayer.js
import React from 'react';
import { useEffect } from 'react';
import './common.css';
import './AudioPlayer.css';

function AudioPlayer({ audioBLob, setAudioBLob }) {
  
  return (
    <audio id="player_audio" className="all_doc" controls>
      {audioBLob && (
        <source src={URL.createObjectURL(audioBLob)}/>
      )}
      Ваш браузер не поддерживает элемент audio.
    </audio>
);
}

export default AudioPlayer;
