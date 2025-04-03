// ModelSelect.js
import React from 'react';
import './common.css';
import './ModelSelect.css';


function ModelSelect({ models, selectedModel, setSelectedModel }) {
  const onChangeModelName = (e) => {
    setSelectedModel(e.target.value);
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