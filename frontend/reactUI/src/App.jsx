import React, { useState } from "react";
import MemeInput from "./MemeInput";
import MemeDisplay from "./MemeDisplay";
import styled from "styled-components";
import GlobalStyles from "./GlobalStyles/globalStyles";

const AppContainer = styled.div`
   max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
`;

function App() {
  const [suggestions, setSuggestions] = useState([]);
  const [selectedMeme, setSelectedMeme] = useState(null);

  const handleMemeSuggestions = async (memeIdea) => {
    // Call Spring Boot backend to get meme suggestions
    const response = await fetch("http://localhost:8080/api/suggest-memes", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ idea: memeIdea }),
    });
    const data = await response.json();
    setSuggestions(data);
  };

  const handleMemeSelection = (meme) => {
    setSelectedMeme(meme);
  };

  return (
    <>
    <GlobalStyles/>
    <AppContainer>
    
      <h1>AI-Powered Meme Generator</h1>
      <MemeInput onSuggest={handleMemeSuggestions} />
      <MemeDisplay suggestions={suggestions} onSelect={handleMemeSelection} />
      {selectedMeme && (
        <div>
          <h2>Selected Meme: {selectedMeme.name}</h2>
          <img src={selectedMeme.base_img} alt={selectedMeme.name} />
        </div>
      )}
    
    </AppContainer>
    </>
  );
}

export default App;