
let userKey = prompt("Enter your four digit pin: ");
let userKeys = [];

for (let index = 0; index < 4; index++) {
    userKeys[index] = (parseInt(userKey[index]) + 7) % 10;
}

let numberSwap = userKeys[0];
userKeys[0] = userKeys[2];
userKeys[2] = numberSwap;

numberSwap = userKeys[1];
userKeys[1] = userKeys[3];
userKeys[3] = numberSwap;

let encrypted = "";
for (let index = 0; index < 4; index++) {
    encrypted += userKeys[index];
}
console.log("Encrypted key: " + encrypted);

numberSwap = userKeys[0];
userKeys[0] = userKeys[2];
userKeys[2] = numberSwap;

numberSwap = userKeys[1];
userKeys[1] = userKeys[3];
userKeys[3] = numberSwap;

let decrypted = "";
for (let index = 0; index < 4; index++) {
    let value = (userKeys[index] - 7 + 10) % 10;
    decrypted += value;
}
console.log("Decrypted key: " + decrypted);
