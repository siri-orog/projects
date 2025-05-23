async function getWeather() {
    const city = document.getElementById("city").value;
    const apiKey = "f57c129246f17dbf2c3ced68bf23f769"; // Replace with your actual API key
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        document.getElementById("weather-info").innerHTML =
            `<p>Temperature: ${data.main.temp}°C</p>
             <p>Weather: ${data.weather[0].description}</p>`;
    } catch (error) {
        document.getElementById("weather-info").innerHTML = `<p>City not found.</p>`;
    }
}

