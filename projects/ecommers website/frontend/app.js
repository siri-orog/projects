import React, { useState, useEffect } from 'react';

function App() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/api/products")
            .then(res => res.json())
            .then(data => setProducts(data));
    }, []);

    return (
        <div>
            <h1>E-Commerce Store</h1>
            <div>
                {products.map(product => (
                    <div key={product._id}>
                        <h3>{product.name}</h3>
                        <p>{product.description}</p>
                        <p>${product.price}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;