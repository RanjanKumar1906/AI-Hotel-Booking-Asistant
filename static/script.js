function searchHotels() {
    const city = document.getElementById("cityInput").value.trim();
    if (!city) return;
  
    fetch("/get_hotels", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ city: city })
    })
      .then(res => res.json())
      .then(data => {
        const results = document.getElementById("results");
        results.innerHTML = "";
        if (data.length === 0) {
          results.innerHTML = "<p>❌ No hotels found for this city.</p>";
          return;
        }
  
        data.forEach(hotel => {
          const div = document.createElement("div");
          div.className = "hotel";
          div.innerHTML = `
            <h3>🏨 ${hotel.name}</h3>
            <p><strong>📍 Address:</strong> ${hotel.address}</p>
            <p><strong>💰 Price:</strong> ${hotel.price}</p>
            <p><strong>⭐ Rating:</strong> ${hotel.rating} (${hotel.reviews} reviews)</p>
            <a class="book-btn" href="${hotel.link}" target="_blank">🔗 Book Now</a>
          `;
          results.appendChild(div);
        });
      });
  }
  
  function toggleTheme() {
    document.body.classList.toggle("light");
  }
  