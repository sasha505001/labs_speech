// TextInput.js
import React from 'react';
import './TextInput.css';
import './common.css';

function TextInput({ text, setText }) {
  return (
    <textarea
      id="text-input"
      name="text"
      className="all_doc"
      value={text}
      onChange={(e) => setText(e.target.value)}
    />
  );
}

export default TextInput;