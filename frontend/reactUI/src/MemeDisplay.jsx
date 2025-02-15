import React from "react";
import styled from "styled-components";

const MemeGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
`;

const MemeCard = styled.div`
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s;

  &:hover {
    transform: scale(1.05);
  }
     img {
    width: 100%;
    height: auto;
  }

  p {
    padding: 0.5rem;
    text-align: center;
    background-color: #f9f9f9;
  }
`;

function MemeDisplay({ suggestions, onSelect }) {
  return (
    <div>
      <h2>Suggested Memes</h2>
      <MemeGrid>
  {suggestions.map((meme) => (
    <MemeCard key={meme.name} onClick={() => onSelect(meme)}>
      <img src={meme.base_img} alt={meme.name} />
      <p>{meme.name}</p>
    </MemeCard>
  ))}
</MemeGrid>
    </div>
  );
}

export default MemeDisplay;