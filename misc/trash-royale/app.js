var express = require('express');
var app = express();

const PORT = process.env.PORT || 3000;

const { readFile } = require('fs');
var path = require('path');

// path to where the files are stored on disk
var FILES_DIR = path.join(__dirname, 'downloads');

app.use(express.static('./public/imgs'));

app.get('/', function (req, res) {
    res.redirect('/home');
});

app.get('/home', (req, res) => {
    readFile('./public/home.html', 'utf8', (err, html) => {
        if (err) {
            res.status(500).send('Sorry! Server error.');
        }
        res.send(html);
    });
});

app.get('/3ar1y-4cc35s', (req, res) => {
    readFile('./secret.html', 'utf8', (err, html) => {
        if (err) {
            res.status(500).send('Sorry! Server error.');
        }
        res.send(html);
    });
});

app.get('/downloads/:file(*)', (req, res, next) => {
    res.download(req.params.file, { root: FILES_DIR }, function (err) {
        if (!err) return;
        if (err.status !== 404) return next(err);
        res.statusCode = 404;
        res.send("Can't find that file, sorry!");
    });
});

app.use((req, res, next) => {
    res.status(404).send('Sorry! This page does not exist!');
});

app.listen(PORT, () => {
    console.log(`App listening on port ${PORT}!`);
});
