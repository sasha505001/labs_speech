import React, { useState, useRef } from 'react';
import SendButton from './SendButton';
import './common.css';

function AudioRecorder({setRequestText, setAnswerText, setURLs, setCenterOfMass }) {
    const [isRecording, setIsRecording] = useState(false);
    const [audioURL, setAudioURL] = useState('');
    const [audioBlob, setAudioBlob] = useState(null);   // <--- сохраняем blob
    const mediaRecorderRef = useRef(null);
    const chunksRef = useRef([]);

    const startRecording = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorderRef.current = new MediaRecorder(stream);

            mediaRecorderRef.current.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    chunksRef.current.push(event.data);
                }
            };

            mediaRecorderRef.current.onstop = () => {
                const blob = new Blob(chunksRef.current, { type: 'audio/webm' });
                setAudioBlob(blob);   // save blob
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

    const handleRecordClick = () => {
        if (!isRecording) startRecording();
        else stopRecording();
    };

    return (
        <div className="all_doc">
            <button class="record-button" onClick={handleRecordClick}>
                {isRecording ? 'Остановить запись' : 'Начать запись'}
            </button>

            {audioURL && (
                <div>
                    <br />
                    <label id='audio_label'>Ваша запись:</label>
                    <br />
                    <br />
                    <audio src={audioURL} controls />
                </div>
            )}
            <br />
            {/* Кнопка Отправить */}
            {audioBlob && 
                <SendButton 
                    audioBlob={audioBlob}
                    setRequestText={setRequestText}
                    setAnswerText={setAnswerText}
                    setURLs={setURLs}
                    setCenterOfMass={setCenterOfMass}
                />
            }
      </div>
  );
}

export default AudioRecorder;