import React, { useState } from "react";
import styled from "styled-components";


const Form = styled.form`
  margin: 2rem 0;
`;

const Input = styled.input`
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 0.5rem;
  width: 300px;
`;

const Button = styled.button`
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  &:hover {
    background-color: #0056b3;
  }
`;

function MemeInput({ onSuggest }) {
  const [memeIdea, setMemeIdea] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSuggest(memeIdea);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter a meme idea (e.g., funny relationship meme)"
        value={memeIdea}
        onChange={(e) => setMemeIdea(e.target.value)}
      />
      <button type="submit">Suggest Memes</button>
    </form>
  );
}

export default MemeInput;