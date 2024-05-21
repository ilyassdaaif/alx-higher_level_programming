#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.error('Usage: node 101-starwars_characters.js <Movie ID>');
    process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Failed to get a valid response. Status code:', response.statusCode);
    } else {
        try {
            const film = JSON.parse(body);
            const characterUrls = film.characters;

            // Function to fetch character names in order
            const fetchCharacterName = (url) => {
                return new Promise((resolve, reject) => {
                    request(url, (charError, charResponse, charBody) => {
                        if (charError) {
                            reject(charError);
                        } else if (charResponse.statusCode !== 200) {
                            reject(new Error(`Failed to get a valid response for character. Status code: ${charResponse.statusCode}`));
                        } else {
                            const character = JSON.parse(charBody);
                            resolve(character.name);
                        }
                    });
                });
            };

            // Fetch all character names in order
            const fetchAllCharacters = async () => {
                for (const url of characterUrls) {
                    try {
                        const name = await fetchCharacterName(url);
                        console.log(name);
                    } catch (err) {
                        console.error('Error:', err);
                    }
                }
            };

            fetchAllCharacters();
        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
        }
    }
});
