from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample hotel data for demonstratio
local_hotels = [
    # Tier 1 - Delhi
    {
        "name": "The Leela Palace",
        "address": "Diplomatic Enclave, Chanakyapuri",
        "city": "Delhi",
        "price": "₹14,500/night",
        "link": "https://www.booking.com/hotel/in/the-leela-palace-new-delhi.en-gb.html",
        "tier": "Tier 1",
        "rating": "9.1",
        "reviews": "500+"
    },
    # Tier 1 - Mumbai
    {
        "name": "The Taj Mahal Palace",
        "address": "Apollo Bunder, Colaba, Mumbai",
        "city": "Mumbai",
        "price": "₹16,000/night",
        "link": "https://www.booking.com/hotel/in/the-taj-mahal-palace.en-gb.html",
        "tier": "Tier 1",
        "rating": "9.2",
        "reviews": "1000+"
    },
    # Tier 2 - Bengaluru
    {
        "name": "The Oberoi",
        "address": "MG Road, Bengaluru",
        "city": "Bengaluru",
        "price": "₹8,500/night",
        "link": "https://www.booking.com/hotel/in/the-oberoi-bangalore.en-gb.html",
        "tier": "Tier 2",
        "rating": "8.9",
        "reviews": "300+"
    },
    # Tier 2 - Chennai
    {
        "name": "ITC Grand Chola",
        "address": "Guindy, Chennai",
        "city": "Chennai",
        "price": "₹10,000/night",
        "link": "https://www.booking.com/hotel/in/itc-grand-chola-chennai.en-gb.html",
        "tier": "Tier 2",
        "rating": "8.8",
        "reviews": "800+"
    },
    # Tier 3 - Hyderabad
    {
        "name": "Taj Krishna",
        "address": "Banjara Hills, Hyderabad",
        "city": "Hyderabad",
        "price": "₹7,000/night",
        "link": "https://www.booking.com/hotel/in/taj-krishna-hyderabad.en-gb.html",
        "tier": "Tier 3",
        "rating": "8.5",
        "reviews": "400+"
    },
    # Tier 3 - Jaipur
    {
        "name": "Rambagh Palace",
        "address": "Rambagh Palace, Jaipur",
        "city": "Jaipur",
        "price": "₹6,000/night",
        "link": "https://www.booking.com/hotel/in/rambagh-palace-jaipur.en-gb.html",
        "tier": "Tier 3",
        "rating": "8.7",
        "reviews": "350+"
    },
    # Tier 3 - Goa
    {
        "name": "The Leela Goa",
        "address": "Cavelossim, Goa",
        "city": "Goa",
        "price": "₹12,000/night",
        "link": "https://www.booking.com/hotel/in/the-leela-goa.en-gb.html",
        "tier": "Tier 3",
        "rating": "9.0",
        "reviews": "600+"
    },
    # Tier 4 - Amritsar
    {
        "name": "Taj Swarna",
        "address": "Amritsar, Punjab",
        "city": "Amritsar",
        "price": "₹5,500/night",
        "link": "https://www.booking.com/hotel/in/taj-swarna-amritsar.en-gb.html",
        "tier": "Tier 4",
        "rating": "8.6",
        "reviews": "250+"
    },
    # Tier 4 - Kochi
    {
        "name": "Le Meridien Kochi",
        "address": "Willingdon Island, Kochi",
        "city": "Kochi",
        "price": "₹7,200/night",
        "link": "https://www.booking.com/hotel/in/le-meridien-kochi.en-gb.html",
        "tier": "Tier 4",
        "rating": "8.4",
        "reviews": "450+"
    },
    # Tier 5 - Dharamshala
    {
        "name": "The Pavilion Dharamshala",
        "address": "Dharamshala, Himachal Pradesh",
        "city": "Dharamshala",
        "price": "₹4,500/night",
        "link": "https://www.booking.com/hotel/in/the-pavilion-dharamshala.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "200+"
    },
    # Tier 5 - Jammu
    {
        "name": "Radisson Blu Jammu",
        "address": "Jammu, J&K",
        "city": "Jammu",
        "price": "₹6,500/night",
        "link": "https://www.booking.com/hotel/in/radisson-blu-jammu.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.1",
        "reviews": "150+"
    },
    # Tier 5 - Jalandhar
    {
        "name": "The Maya Hotel",
        "address": "Jalandhar, Punjab",
        "city": "Jalandhar",
        "price": "₹3,500/night",
        "link": "https://www.booking.com/hotel/in/the-maya-jalandhar.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.9",
        "reviews": "180+"
    },
    # Tier 5 - Nawanshahr
    {
        "name": "Shah Hotel",
        "address": "Nawanshahr, Punjab",
        "city": "Nawanshahr",
        "price": "₹2,000/night",
        "link": "https://www.booking.com/hotel/in/shah-nawanshahr.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.8",
        "reviews": "120+"
    },
    # Tier 5 - Samastipur
    {
        "name": "Satyam Hotel",
        "address": "Samastipur, Bihar",
        "city": "Samastipur",
        "price": "₹1,800/night",
        "link": "https://www.booking.com/hotel/in/satyam-samastipur.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.6",
        "reviews": "80+"
    },
    # Tier 5 - Patiala
    {
        "name": "The Patiala Heritage",
        "address": "Patiala, Punjab",
        "city": "Patiala",
        "price": "₹3,000/night",
        "link": "https://www.booking.com/hotel/in/patiala-heritage.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.7",
        "reviews": "90+"
    },
     # Tier 5 - Agra
    {
        "name": "Tajview Agra",
        "address": "Taj Ganj, Agra",
        "city": "Agra",
        "price": "₹4,000/night",
        "link": "https://www.booking.com/hotel/in/tajview-agra.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "700+"
    },
    # Tier 5 - Varanasi
    {
        "name": "Hotel Surya, Kaiser Palace",
        "address": "Cantt Road, Varanasi",
        "city": "Varanasi",
        "price": "₹4,800/night",
        "link": "https://www.booking.com/hotel/in/surya-kaiser-palace-varanasi.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "400+"
    },
    # Tier 5 - Bhopal
    {
        "name": "Jehan Numa Palace Hotel",
        "address": "Shymala Hills, Bhopal",
        "city": "Bhopal",
        "price": "₹5,500/night",
        "link": "https://www.booking.com/hotel/in/jehan-numa-palace.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.8",
        "reviews": "350+"
    },
    # Tier 5 - Gaya
    {
        "name": "Hotel Siddhartha",
        "address": "Bodhgaya, Gaya",
        "city": "Gaya",
        "price": "₹2,200/night",
        "link": "https://www.booking.com/hotel/in/siddhartha-gaya.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.9",
        "reviews": "150+"
    },
    # Tier 5 - Jodhpur
    {
        "name": "Umaid Bhawan Palace",
        "address": "Umaid Bhawan Palace Road, Jodhpur",
        "city": "Jodhpur",
        "price": "₹6,200/night",
        "link": "https://www.booking.com/hotel/in/umaid-bhawan-palace.jodhpur.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.2",
        "reviews": "600+"
    },
    # Tier 5 - Lucknow
    {
        "name": "The Oberoi Lucknow",
        "address": "Lucknow, Uttar Pradesh",
        "city": "Lucknow",
        "price": "₹7,000/night",
        "link": "https://www.booking.com/hotel/in/oberoi-lucknow.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.9",
        "reviews": "500+"
    },
    # Tier 5 - Surat
    {
        "name": "The Gateway Hotel Surat",
        "address": "Surat, Gujarat",
        "city": "Surat",
        "price": "₹5,000/night",
        "link": "https://www.booking.com/hotel/in/gateway-suratt.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.7",
        "reviews": "400+"
    },
    # Tier 5 - Dehradun
    {
        "name": "The Amber - Vermont Estate",
        "address": "Dehradun, Uttarakhand",
        "city": "Dehradun",
        "price": "₹3,200/night",
        "link": "https://www.booking.com/hotel/in/the-amber-vermont-estate.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.1",
        "reviews": "200+"
    },
    # Tier 5 - Puri
    {
        "name": "Mayfair Waves Puri",
        "address": "Puri, Odisha",
        "city": "Puri",
        "price": "₹4,500/night",
        "link": "https://www.booking.com/hotel/in/mayfair-waves-puri.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "300+"
    },
    # Tier 5 - Khajuraho
    {
        "name": "The Lalit Temple View Khajuraho",
        "address": "Khajuraho, Madhya Pradesh",
        "city": "Khajuraho",
        "price": "₹5,000/night",
        "link": "https://www.booking.com/hotel/in/the-lalit-temple-view-khajuraho.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "250+"
    },
    # Tier 5 - Rishikesh
    {
        "name": "Aloha on the Ganges",
        "address": "Rishikesh, Uttarakhand",
        "city": "Rishikesh",
        "price": "₹6,000/night",
        "link": "https://www.booking.com/hotel/in/aloha-on-the-ganges-rishikesh.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.7",
        "reviews": "300+"
    },
    # Tier 5 - Kodaikanal
    {
        "name": "The Carlton",
        "address": "Lake Road, Kodaikanal",
        "city": "Kodaikanal",
        "price": "₹7,500/night",
        "link": "https://www.booking.com/hotel/in/the-carlton-kodaikanal.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.1",
        "reviews": "500+"
    },
    # Tier 5 - Ooty
    {
        "name": "Savoy Ooty",
        "address": "Ooty, Tamil Nadu",
        "city": "Ooty",
        "price": "₹5,200/night",
        "link": "https://www.booking.com/hotel/in/savoy-ooty.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.6",
        "reviews": "350+"
    },
    # Tier 5 - Nainital
    {
        "name": "The Naini Retreat",
        "address": "Nainital, Uttarakhand",
        "city": "Nainital",
        "price": "₹4,200/night",
        "link": "https://www.booking.com/hotel/in/the-naini-retreat.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.4",
        "reviews": "200+"
    },
    # Tier 5 - Bikaner
    {
        "name": "Lallgarh Palace Hotel",
        "address": "Bikaner, Rajasthan",
        "city": "Bikaner",
        "price": "₹6,000/night",
        "link": "https://www.booking.com/hotel/in/lallgarh-palace-bikaner.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "300+"
    },
    # Tier 5 - Chandigarh
    {
        "name": "JW Marriott Hotel Chandigarh",
        "address": "Sector 35B, Chandigarh",
        "city": "Chandigarh",
        "price": "₹6,000/night",
        "link": "https://www.booking.com/hotel/in/jw-marriott-chandigarh.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.9",
        "reviews": "500+"
    },
    # Tier 5 - Amritsar
    {
        "name": "Taj Swarna Amritsar",
        "address": "Ranjit Avenue, Amritsar",
        "city": "Amritsar",
        "price": "₹8,000/night",
        "link": "https://www.booking.com/hotel/in/taj-swarna-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.0",
        "reviews": "300+"
    },
    # Tier 5 - Ludhiana
    {
        "name": "Radisson Blu Hotel Ludhiana",
        "address": "Ferozepur Road, Ludhiana",
        "city": "Ludhiana",
        "price": "₹5,500/night",
        "link": "https://www.booking.com/hotel/in/radisson-blu-ludhiana.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "400+"
    },
    # Tier 5 - Patiala
    {
        "name": "The Royal Retreat",
        "address": "Patiala, Punjab",
        "city": "Patiala",
        "price": "₹3,800/night",
        "link": "https://www.booking.com/hotel/in/royal-retreat-patiala.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.2",
        "reviews": "200+"
    },
    # Tier 5 - Jalandhar
    {
        "name": "Ramada Encore by Wyndham Jalandhar",
        "address": "Jalandhar, Punjab",
        "city": "Jalandhar",
        "price": "₹4,500/night",
        "link": "https://www.booking.com/hotel/in/ramada-encore-jalandhar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "150+"
    },
    # Tier 5 - Srinagar
    {
        "name": "The Lalit Grand Palace Srinagar",
        "address": "Srinagar, Jammu and Kashmir",
        "city": "Srinagar",
        "price": "₹9,000/night",
        "link": "https://www.booking.com/hotel/in/the-lalit-grand-palace-srinagar.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.0",
        "reviews": "350+"
    },
    # Tier 5 - Manali
    {
        "name": "The Himalayan Resort & Spa",
        "address": "Manali, Himachal Pradesh",
        "city": "Manali",
        "price": "₹7,500/night",
        "link": "https://www.booking.com/hotel/in/the-himalayan-resort-spa.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.7",
        "reviews": "400+"
    },
    # Tier 5 - Dharamshala
    {
        "name": "The Dhauladhar View Hotel",
        "address": "Dharamshala, Himachal Pradesh",
        "city": "Dharamshala",
        "price": "₹4,500/night",
        "link": "https://www.booking.com/hotel/in/the-dhauladhar-view-dharamshala.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.2",
        "reviews": "180+"
    },
    # Tier 5 - Udaipur
    {
        "name": "The Oberoi Udaivilas",
        "address": "Udaipur, Rajasthan",
        "city": "Udaipur",
        "price": "₹20,000/night",
        "link": "https://www.booking.com/hotel/in/the-oberoi-udaivilas.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.5",
        "reviews": "800+"
    },
    # Tier 5 - Jaipur
    {
        "name": "Rambagh Palace",
        "address": "Jaipur, Rajasthan",
        "city": "Jaipur",
        "price": "₹15,000/night",
        "link": "https://www.booking.com/hotel/in/rambagh-palace-jaipur.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.3",
        "reviews": "1,000+"
    },
    # Tier 5 - Jaisalmer
    {
        "name": "Suryagarh Jaisalmer",
        "address": "Sam, Jaisalmer, Rajasthan",
        "city": "Jaisalmer",
        "price": "₹12,000/night",
        "link": "https://www.booking.com/hotel/in/suryagarh-jaisalmer.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.2",
        "reviews": "600+"
    },
    # Tier 5 - Cochin (Kochi)
    {
        "name": "Taj Malabar Resort & Spa",
        "address": "Willington Island, Kochi",
        "city": "Cochin",
        "price": "₹7,500/night",
        "link": "https://www.booking.com/hotel/in/taj-malabar-resort-spa-kochi.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.1",
        "reviews": "500+"
    },
    # Tier 5 - Munnar
    {
        "name": "The Wind Munnar",
        "address": "Munnar, Kerala",
        "city": "Munnar",
        "price": "₹5,200/night",
        "link": "https://www.booking.com/hotel/in/the-wind-munnar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.8",
        "reviews": "400+"
    },
    # Tier 5 - Kovalam
    {
        "name": "Turtle on the Beach",
        "address": "Kovalam, Kerala",
        "city": "Kovalam",
        "price": "₹6,000/night",
        "link": "https://www.booking.com/hotel/in/turtle-on-the-beach.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "300+"
    },
    # Tier 5 - Kolkata
    {
        "name": "The Oberoi Grand Kolkata",
        "address": "Kolkata, West Bengal",
        "city": "Kolkata",
        "price": "₹9,000/night",
        "link": "https://www.booking.com/hotel/in/the-oberoi-grand-kolkata.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.2",
        "reviews": "700+"
    },
    # Tier 5 - Pune
    {
        "name": "The Westin Pune Koregaon Park",
        "address": "Pune, Maharashtra",
        "city": "Pune",
        "price": "₹8,500/night",
        "link": "https://www.booking.com/hotel/in/the-westin-pune-koregaon-park.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.0",
        "reviews": "600+"
    },
      # Tier 5 - Chandigarh
    {
        "name": "JW Marriott Hotel Chandigarh",
        "address": "Sector 35B, Chandigarh",
        "city": "Chandigarh",
        "price": "₹6,000/night",
        "link": "https://www.booking.com/hotel/in/jw-marriott-chandigarh.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.9",
        "reviews": "500+"
    },
    {
        "name": "The Lalit Chandigarh",
        "address": "Rajiv Gandhi IT Park, Chandigarh",
        "city": "Chandigarh",
        "price": "₹5,200/night",
        "link": "https://www.booking.com/hotel/in/the-lalit-chandigarh.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.7",
        "reviews": "450+"
    },
    # Tier 5 - Amritsar
    {
        "name": "Taj Swarna Amritsar",
        "address": "Ranjit Avenue, Amritsar",
        "city": "Amritsar",
        "price": "₹8,000/night",
        "link": "https://www.booking.com/hotel/in/taj-swarna-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.0",
        "reviews": "300+"
    },
    {
        "name": "Radisson Blu Hotel Amritsar",
        "address": "Airport Road, Amritsar",
        "city": "Amritsar",
        "price": "₹5,000/night",
        "link": "https://www.booking.com/hotel/in/radisson-blu-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.8",
        "reviews": "200+"
    },
    # Tier 5 - Ludhiana
    {
        "name": "Radisson Blu Hotel Ludhiana",
        "address": "Ferozepur Road, Ludhiana",
        "city": "Ludhiana",
        "price": "₹5,500/night",
        "link": "https://www.booking.com/hotel/in/radisson-blu-ludhiana.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "400+"
    },
    {
        "name": "Park Plaza Ludhiana",
        "address": "Ferozepur Road, Ludhiana",
        "city": "Ludhiana",
        "price": "₹4,800/night",
        "link": "https://www.booking.com/hotel/in/park-plaza-ludhiana.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "250+"
    },
    # Tier 5 - Patiala
    {
        "name": "The Royal Retreat",
        "address": "Patiala, Punjab",
        "city": "Patiala",
        "price": "₹3,800/night",
        "link": "https://www.booking.com/hotel/in/royal-retreat-patiala.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.2",
        "reviews": "200+"
    },
    {
        "name": "Hotel Mohan Continental",
        "address": "Patiala, Punjab",
        "city": "Patiala",
        "price": "₹2,500/night",
        "link": "https://www.booking.com/hotel/in/mohan-continental-patiala.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.9",
        "reviews": "100+"
    },
    # Tier 5 - Jalandhar
    {
        "name": "Ramada Encore by Wyndham Jalandhar",
        "address": "Jalandhar, Punjab",
        "city": "Jalandhar",
        "price": "₹4,500/night",
        "link": "https://www.booking.com/hotel/in/ramada-encore-jalandhar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "150+"
    },
    {
        "name": "Country Inn & Suites by Radisson",
        "address": "Jalandhar, Punjab",
        "city": "Jalandhar",
        "price": "₹3,800/night",
        "link": "https://www.booking.com/hotel/in/country-inn-suites-by-radisson-jalandhar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.1",
        "reviews": "180+"
    },
    # Tier 5 - Srinagar
    {
        "name": "The Lalit Grand Palace Srinagar",
        "address": "Srinagar, Jammu and Kashmir",
        "city": "Srinagar",
        "price": "₹9,000/night",
        "link": "https://www.booking.com/hotel/in/the-lalit-grand-palace-srinagar.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.0",
        "reviews": "350+"
    },
    {
        "name": "Vivanta Dal View Srinagar",
        "address": "Boulevard Road, Srinagar",
        "city": "Srinagar",
        "price": "₹6,500/night",
        "link": "https://www.booking.com/hotel/in/vivanta-dal-view-srinagar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.8",
        "reviews": "200+"
    },
    # Tier 5 - Manali
    {
        "name": "The Himalayan Resort & Spa",
        "address": "Manali, Himachal Pradesh",
        "city": "Manali",
        "price": "₹7,500/night",
        "link": "https://www.booking.com/hotel/in/the-himalayan-resort-spa.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.7",
        "reviews": "400+"
    },
    {
        "name": "Manali Heights",
        "address": "Manali, Himachal Pradesh",
        "city": "Manali",
        "price": "₹5,200/night",
        "link": "https://www.booking.com/hotel/in/manali-heights.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "300+"
    },
    # Tier 5 - Dharamshala
    {
        "name": "The Dhauladhar View Hotel",
        "address": "Dharamshala, Himachal Pradesh",
        "city": "Dharamshala",
        "price": "₹4,500/night",
        "link": "https://www.booking.com/hotel/in/the-dhauladhar-view-dharamshala.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.2",
        "reviews": "180+"
    },
    {
        "name": "Hotel Norbu House",
        "address": "Dharamshala, Himachal Pradesh",
        "city": "Dharamshala",
        "price": "₹3,000/night",
        "link": "https://www.booking.com/hotel/in/norbu-house-dharamshala.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.9",
        "reviews": "120+"
    },
    # Tier 5 - Udaipur
    {
        "name": "The Oberoi Udaivilas",
        "address": "Udaipur, Rajasthan",
        "city": "Udaipur",
        "price": "₹20,000/night",
        "link": "https://www.booking.com/hotel/in/the-oberoi-udaivilas.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.5",
        "reviews": "800+"
    },
    {
        "name": "Leela Palace Udaipur",
        "address": "Lake Pichola, Udaipur",
        "city": "Udaipur",
        "price": "₹18,000/night",
        "link": "https://www.booking.com/hotel/in/the-leela-udaipur.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.3",
        "reviews": "1,200+"
    },
    # Tier 5 - Jaipur
    {
        "name": "Rambagh Palace",
        "address": "Jaipur, Rajasthan",
        "city": "Jaipur",
        "price": "₹15,000/night",
        "link": "https://www.booking.com/hotel/in/rambagh-palace-jaipur.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.3",
        "reviews": "1,000+"
    },
    {
        "name": "Jaipur Marriott Hotel",
        "address": "Ashram Marg, Jaipur",
        "city": "Jaipur",
        "price": "₹7,500/night",
        "link": "https://www.booking.com/hotel/in/marriott-jaipur.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.7",
        "reviews": "800+"
    },
    # Tier 5 - Jaisalmer
    {
        "name": "Suryagarh Jaisalmer",
        "address": "Sam, Jaisalmer, Rajasthan",
        "city": "Jaisalmer",
        "price": "₹12,000/night",
        "link": "https://www.booking.com/hotel/in/suryagarh-jaisalmer.en-gb.html",
        "tier": "Tier 5",
        "rating": "9.2",
        "reviews": "600+"
    },
    {
        "name": "The Golden House",
        "address": "Jaisalmer, Rajasthan",
        "city": "Jaisalmer",
        "price": "₹7,000/night",
        "link": "https://www.booking.com/hotel/in/the-golden-house-jaisalmer.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.4",
        "reviews": "250+"
    },
     {
        "name": "Hotel Regency",
        "address": "Nawanshahr, Punjab",
        "city": "Nawanshahr",
        "price": "₹2,000/night",
        "link": "https://www.booking.com/hotel/in/regency-nawanshahr.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.8",
        "reviews": "50+"
    },
    {
        "name": "The Royal Plaza",
        "address": "Nawanshahr, Punjab",
        "city": "Nawanshahr",
        "price": "₹2,500/night",
        "link": "https://www.booking.com/hotel/in/the-royal-plaza-nawanshahr.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.6",
        "reviews": "40+"
    }, {
        "name": "Holiday Inn Amritsar",
        "address": "Amritsar, Punjab",
        "city": "Amritsar",
        "price": "₹4,500/night",
        "link": "https://www.booking.com/hotel/in/holiday-inn-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.4",
        "reviews": "350+"
    },
    {
        "name": "Hotel Hayat Rabbani",
        "address": "Golden Temple Road, Amritsar",
        "city": "Amritsar",
        "price": "₹3,800/night",
        "link": "https://www.booking.com/hotel/in/hayat-rabbani-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.0",
        "reviews": "200+"
    },
    {
        "name": "Hampton by Hilton Amritsar",
        "address": "Amritsar, Punjab",
        "city": "Amritsar",
        "price": "₹5,000/night",
        "link": "https://www.booking.com/hotel/in/hampton-by-hilton-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "300+"
    },
     {
        "name": "Holiday Inn Chandigarh Zirakpur",
        "address": "Zirakpur, Chandigarh",
        "city": "Chandigarh",
        "price": "₹4,800/night",
        "link": "https://www.booking.com/hotel/in/holiday-inn-chandigarh-zirakpur.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.2",
        "reviews": "150+"
    },
    {
        "name": "The Pride Hotel Chandigarh",
        "address": "Chandigarh, Punjab",
        "city": "Chandigarh",
        "price": "₹5,500/night",
        "link": "https://www.booking.com/hotel/in/the-pride-chandigarh.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.4",
        "reviews": "120+"
    },
    {
        "name": "The Majestic Hotel Ludhiana",
        "address": "Ludhiana, Punjab",
        "city": "Ludhiana",
        "price": "₹4,200/night",
        "link": "https://www.booking.com/hotel/in/the-majestic-ludhiana.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "170+"
    },
    {
        "name": "Golden Tulip Ludhiana",
        "address": "Ludhiana, Punjab",
        "city": "Ludhiana",
        "price": "₹3,900/night",
        "link": "https://www.booking.com/hotel/in/golden-tulip-ludhiana.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.1",
        "reviews": "140+"
    },
     {
        "name": "Best Western Merrion",
        "address": "Amritsar, Punjab",
        "city": "Amritsar",
        "price": "₹4,300/night",
        "link": "https://www.booking.com/hotel/in/best-western-merrion-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.0",
        "reviews": "220+"
    },
    {
        "name": "Hotel Moon Star",
        "address": "Amritsar, Punjab",
        "city": "Amritsar",
        "price": "₹3,200/night",
        "link": "https://www.booking.com/hotel/in/moon-star-amritsar.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.9",
        "reviews": "150+"
    },
    {
        "name": "Shah Posh Houseboats",
        "address": "Srinagar, Jammu and Kashmir",
        "city": "Srinagar",
        "price": "₹7,500/night",
        "link": "https://www.booking.com/hotel/in/shah-posh-houseboats-srinagar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.6",
        "reviews": "220+"
    },
    {
        "name": "Lalit Grand Palace Srinagar",
        "address": "Srinagar, Jammu and Kashmir",
        "city": "Srinagar",
        "price": "₹8,500/night",
        "link": "https://www.booking.com/hotel/in/the-lalit-grand-palace-srinagar.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.9",
        "reviews": "300+"
    },
     {
        "name": "Holiday Inn Manali",
        "address": "Manali, Himachal Pradesh",
        "city": "Manali",
        "price": "₹6,000/night",
        "link": "https://www.booking.com/hotel/in/holiday-inn-manali.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "180+"
    },
    {
        "name": "Solang Valley Resort",
        "address": "Solang, Manali",
        "city": "Manali",
        "price": "₹5,500/night",
        "link": "https://www.booking.com/hotel/in/solang-valley-resort-manali.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "250+"
    },
    {
        "name": "The Norbulingka Institute",
        "address": "Dharamshala, Himachal Pradesh",
        "city": "Dharamshala",
        "price": "₹3,800/night",
        "link": "https://www.booking.com/hotel/in/norbulingka-institute-dharamshala.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.4",
        "reviews": "150+"
    },
    {
        "name": "Hotel Dharamshala Paradise",
        "address": "Dharamshala, Himachal Pradesh",
        "city": "Dharamshala",
        "price": "₹2,800/night",
        "link": "https://www.booking.com/hotel/in/dharamshala-paradise.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.9",
        "reviews": "100+"
    },
    # Tier 5 - Jammu
    {
        "name": "The Katra Hotel",
        "address": "Katra, Jammu & Kashmir",
        "city": "Jammu",
        "price": "₹3,500/night",
        "link": "https://www.booking.com/hotel/in/the-katra-hotel-jammu.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.2",
        "reviews": "180+"
    },
    {
        "name": "Vivanta Jammu",
        "address": "Jammu, Jammu & Kashmir",
        "city": "Jammu",
        "price": "₹4,200/night",
        "link": "https://www.booking.com/hotel/in/vivanta-jammu.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.3",
        "reviews": "220+"
    },
    {
        "name": "Hotel Prem Singh",
        "address": "Jammu, Jammu & Kashmir",
        "city": "Jammu",
        "price": "₹2,800/night",
        "link": "https://www.booking.com/hotel/in/prem-singh-jammu.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.8",
        "reviews": "150+"
    },
    {
        "name": "Radisson Blu Jammu",
        "address": "Jammu, Jammu & Kashmir",
        "city": "Jammu",
        "price": "₹6,500/night",
        "link": "https://www.booking.com/hotel/in/radisson-blu-jammu.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.5",
        "reviews": "300+"
    },
    {
        "name": "Hotel Jammu Ashok",
        "address": "Jammu, Jammu & Kashmir",
        "city": "Jammu",
        "price": "₹3,000/night",
        "link": "https://www.booking.com/hotel/in/jammu-ashok.en-gb.html",
        "tier": "Tier 5",
        "rating": "7.9",
        "reviews": "120+"
    },
    {
        "name": "Kashmir Regent",
        "address": "Jammu, Jammu & Kashmir",
        "city": "Jammu",
        "price": "₹4,000/night",
        "link": "https://www.booking.com/hotel/in/kashmir-regent-jammu.en-gb.html",
        "tier": "Tier 5",
        "rating": "8.1",
        "reviews": "180+"
    }

]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_hotels", methods=["POST"])
def get_hotels():
    city = request.json.get("city")
    if not city:
        return jsonify([])

    # Filter hotels based on the city provided
    filtered_hotels = [hotel for hotel in local_hotels if hotel["city"].lower() == city.lower()]
    return jsonify(filtered_hotels)

if __name__ == "__main__":
    app.run(debug=True)
