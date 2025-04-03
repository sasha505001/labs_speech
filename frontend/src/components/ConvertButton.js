// ConvertButton.js
import React from 'react';
import './ConvertButton.css';
import './common.css';

function ConvertButton({ handleClicked }) {
  return (
    <button id="convert-btn" className="all_doc" onClick={handleClicked}>
      Convert Text to Speech
    </button>
  );
}

export default ConvertButton;