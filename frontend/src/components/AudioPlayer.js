// AudioPlayer.js
import React from 'react';
import './common.css';
import './AudioPlayer.css';

function AudioPlayer({ audioURL }) {
  return (
    <audio id="player_audio" className="all_doc" controls>
      <source src={audioURL} type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  );
}

export default AudioPlayer;
