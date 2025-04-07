// AudioPlayer.js
import React from 'react';
import { useState, useEffect } from 'react';
import './common.css';
import './AudioPlayer.css';

function AudioPlayer({ audioURLRef }) {
  return <audio id="player_audio" 
  className="all_doc" 
  src={audioURLRef} 
  controls>Ваш браузер не поддерживает элемент audio.</audio>
}

export default AudioPlayer;
