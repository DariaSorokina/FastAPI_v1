

Copy
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [posters, setPosters] = useState([]);
  const [shows, setShows] = useState([]);
  const [acters, setActers] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/v1/products/').then(response => setPosters(response.data));
    axios.get('http://127.0.0.1:8000/api/v1/show/').then(response => setShows(response.data));
    axios.get('http://127.0.0.1:8000/api/v1/acters/').then(response => setActers(response.data));
    axios.get('http://127.0.0.1:8000/api/v1/products/').then(response => setProducts(response.data));
  }, []);


  return (
    <div className="App">
      <h1>Афиши</h1>
      <ul>
        {posters.map(poster => (
          <li key={poster.id}>{poster.name_poster}</li>
        ))}
      </ul>

      <h2>Спектакли</h2>
      <ul>
        {shows.map(show => (
          <li key={show.id}>{show.name_show}</li>
        ))}
      </ul>

      <h2>Актеры</h2>
      <ul>
        {acters.map(acter => (
          <li key={acter.id}>{acter.name}</li>
        ))}
      </ul>

      <h2>Цены на билеты</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>{product.name_show} - {product.price} руб.</li>
        ))}
      </ul>

      <div>
        <input type="number" placeholder="ID спектакля" id="showId" />
        <input type="number" placeholder="Цена" id="price" />
        <input type="number" placeholder="ID актера" id="acterId" />
        <button onClick={() => handleBuyTicket(
          document.getElementById('showId').value,
          document.getElementById('price').value,
          document.getElementById('acterId').value
        )}>Купить билет</button>
      </div>
    </div>
  );
}

export default App;