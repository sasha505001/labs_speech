import React, { useState, useRef } from 'react';
import axios from 'axios';
import './common.css';

function AudioRecorder(setAudioFile) {
    const [isRecording, setIsRecording] = useState(false);
    const [audioURL, setAudioURL] = useState('');
    const mediaRecorderRef = useRef(null);
    const chunksRef = useRef([]);

    const startRecording = async () => {
        try {
          // Запрашиваем доступ к микрофону
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          
          // Создаем MediaRecorder
          mediaRecorderRef.current = new MediaRecorder(stream);
    
          // Сохраняем записанные кусочки данных
          mediaRecorderRef.current.ondataavailable = (event) => {
            if (event.data.size > 0) {
              chunksRef.current.push(event.data);
            }
          };
    
          // Когда запись остановлена, формируем итоговый blob и URL для проигрывания
          mediaRecorderRef.current.onstop = () => {
            const blob = new Blob(chunksRef.current, { type: 'audio/webm' });
            const url = URL.createObjectURL(blob);
            setAudioURL(url);
            chunksRef.current = [];
          };
    
          mediaRecorderRef.current.start();
          setIsRecording(true);
        } catch (error) {
          console.error('Ошибка доступа к микрофону:', error);
        }
    };

    const stopRecording = () => {
        if (mediaRecorderRef.current && isRecording) {
          mediaRecorderRef.current.stop();
          setIsRecording(false);
        }
    };

    const handleButtonClick = () => {
        if (!isRecording) {
          startRecording();
        } else {
          stopRecording();
        }
    };

    return (
        <div>
          <button onClick={handleButtonClick}>
            {isRecording ? 'Остановить запись' : 'Начать запись'}
          </button>
    
          {/* Воспроизведение записанного звука */}
          {audioURL && (
            <div>
              <h4>Ваша запись:</h4>
              <audio src={audioURL} controls />
            </div>
          )}
        </div>
      );
    
}

export default AudioRecorder;