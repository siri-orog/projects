const productRoutes = require('./routes/productRoutes');
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/ecommerceDB', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("Connected to MongoDB"))
    .catch(err => console.log(err));


    // Import and link routes
const productRoutes = require('./routes/productRoutes');
app.use('/api', productRoutes);
   

// Start Server
app.listen(5000, () => {
    console.log("Server running on port 5000");
});