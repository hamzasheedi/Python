# Simple dict overwrite example
tools = {
    "weather": "Sunny ☀️",
    "weather": "Rainy 🌧️"  # same key overwrites previous one
}

print(tools)  
# Output: {'weather': 'Rainy 🌧️'}

print(tools["weather"])  
# Output: Rainy 🌧️
