from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")
def read_root():
    return """Welcome to the Sina Hosseini FastAPI application! This is a simple API built with FastAPI to show some
    information about solar system star, planets and moons. You can use the following endpoints to get information:
    1. /star - Get information about the star (Sun) 
    2. /planets - Get a list of all planets in the solar system 
    3. /planets/{planet_name} - Get information about a specific planet by name 
    4. /moons - Get a list of all moons in the solar system """

@app.get("/star")
def get_star_info():
    return {
        "name": "Sun",
        "type": "G-type main-sequence star (G dwarf)",
        "mass": "1.989 x 10^30 kg",
        "diameter": "1.3927 million km",
        "age": "4.6 billion years"
    }

@app.get("/planets")
def get_planets():
    return [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

@app.get("/planets/{planet_name}")
def get_planet_info(planet_name: str):
    planets_info = {
        "Mercury": {"diameter": "4,880 km", "orbital_period": "88 days"},
        "Venus": {"diameter": "12,104 km", "orbital_period": "225 days"},
        "Earth": {"diameter": "12,742 km", "orbital_period": "365.25 days"},
        "Mars": {"diameter": "6,779 km", "orbital_period": "687 days"},
        "Jupiter": {"diameter": "139,820 km", "orbital_period": "12 years"},
        "Saturn": {"diameter": "116,460 km", "orbital_period": "29 years"},
        "Uranus": {"diameter": "50,724 km", "orbital_period": "84 years"},
        "Neptune": {"diameter": "49,244 km", "orbital_period": "165 years"}
    }
    planet_info = planets_info.get(planet_name.capitalize())

    if planet_info:
        return {planet_name.capitalize(): planet_info}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Planet not found")
    
@app.get("/moons")
def get_moons():
    return [
        "Moon (Earth)",
        "Phobos (Mars)",
        "Deimos (Mars)",
        "Io (Jupiter)",
        "Europa (Jupiter)",
        "Ganymede (Jupiter)",
        "Callisto (Jupiter)",
        "Titan (Saturn)",
        "Enceladus (Saturn)",
        "Triton (Neptune)"
    ]
