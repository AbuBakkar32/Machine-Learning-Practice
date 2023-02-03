const axios = require("axios");
const crypto = require("crypto-js/enc-hex");
const SHA256 = require("crypto-js/sha256");

const apiKey = "ff81875fcd84aeeb4324d40d5a90a594";
const apiSecret = "c83578204d";
const url = "https://api.test.hotelbeds.com/activity-content-api/3.0/countries/en";
const utcDate = Math.floor(new Date().getTime() / 1000);
const assemble = (apiKey + apiSecret + utcDate);

//Begin SHA-256 Encryption
const hash = SHA256(assemble).toString();
const encryption = (hash.toString(crypto));

const headers = {
    "Api-Key": apiKey,
    "X-Signature": encryption,
};

axios
    .get(url, {headers})
    .then((response) => {
        console.log(response.data);
    })
    .catch((error) => {
        console.error(error);
    });
