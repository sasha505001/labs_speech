// ModelSelect.js
import React from 'react';
import './common.css';
import './ModelSelect.css';
import axios from 'axios';


function ModelSelect({ models, selectedModel, setSelectedModel, setSupportedLang }) {
  const onChangeModelName = (e) => {

    setSelectedModel(e.target.value);
    try {
      axios.get(`http://127.0.0.1:5000/apis/get_supported_languages/${e.target.value}`)
      .then(res => {
        console.log(res.data.languages);
        setSupportedLang(res.data.languages);
      });
    } catch (error) {
      console.error(error);
    }
    
    console.log(e.target.value);
  }
  return (
    <select id="model-select" name="model" className="all_doc" defaultValue={selectedModel} onChange={onChangeModelName}>
      {models.map((model) => (
        <option key={model} value={model}>
          {model}
        </option>
      ))}
    </select>
  );
}

export default ModelSelect;