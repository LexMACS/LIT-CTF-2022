require("dotenv").config();

const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();
const ejs = require("ejs");

var flag = (process.env.FLAG ?? "ctf{flag}");

app.set('view engine', 'ejs');

app.use(cookieParser());

app.use(function (req, res, next) {
	var likeCookie = req.cookies.likeCookie;
	if(likeCookie === undefined) {
	    res.cookie('likeCookie',false, { maxAge: 900000});
	}
	next()
});

app.get('/', (req, res) => {
	res.render("index",{likeCookie: req.cookies.likeCookie,flag: flag});
});

app.listen(8080, () => {
	console.log("BDIMENSION OTZ OTZ OTZ OTZ!!!");
});