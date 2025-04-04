import React from 'react';
import axios from 'axios';
import './SupportedLang.css';
import './common.css';

function SupportedLang({SupportedLang}) {
    
    return (
        <div className="all_doc">
            <label>Supported languages: {SupportedLang}</label>
        </div>
    );
}

export default SupportedLang;