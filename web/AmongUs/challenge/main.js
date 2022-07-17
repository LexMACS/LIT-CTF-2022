// No source challenge

require("dotenv").config();

const express = require('express');
const app = express();

app.get('/', (req, res) => {
	res.sendFile(__dirname + "/index.html");
});

app.get('/sussy-yellow-amogus', (req, res) => {
	res.set("sussyFlag","LITCTF{mr_r4y_h4n_m4y_b3_su55y_bu7_4t_l3ast_h3s_OTZOTZOTZ}")
	res.sendFile(__dirname + "/amongus.gif");
});

app.listen(8080, () => {
	console.log("POLOPOPY OTZ OTZ OTZ OTZ!!!");
});