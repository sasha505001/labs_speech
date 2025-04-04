// AudioPlayer.js
import React from 'react';
import './common.css';
import './AudioPlayer.css';

function AudioPlayer({ audioURL, setAudioURL }) {
  return (
    audioURL && (
      <audio id="player_audio" className="all_doc" controls>
        <source src={URL.createObjectURL(audioURL)}/>
        Your browser does not support the audio element.
      </audio>
    )
  );
}

export default AudioPlayer;
