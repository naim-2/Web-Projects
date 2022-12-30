const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();
const port = 3000;
const jsonParser = bodyParser.json();
const fileName = 'students.json';

// Load data from file
let rawData = fs.readFileSync(fileName);
let data = JSON.parse(rawData);

app.set('views', 'views');
app.set('view engine', 'hbs');
app.use(express.static('public'));


app.get('/', (request, response) => {
    response.render('home');
});

// This is a RESTful GET web service
app.get('/students', (request, response) => {
    data.sort((a, b) => (b.year > a.year) ? 1: -1);
    data.sort((a, b) => (a.product > b.product) ? 1 : -1 );
    response.send(data);
});

// This is a RESTful POST web service
app.post('/students', jsonParser, (request, response) => {
    if(Number.isInteger(request.body.price)){
        if(Number.isInteger(request.body.year)){
            data.push(request.body);
            fs.writeFileSync(fileName, JSON.stringify(data, null, 2));
            response.end();
        }
    }
});

//for editing
app.put('/students', jsonParser, (request, response) => {
    const jsonData = fs.readFileSync(dataPath)
    var existStudents = JSON.parse(jsonData)
    fs.readFile(dataPath, 'utf8', (err, data) => {
      const studentPY = request.params['product'] && request.params['year'];
      existStudents[studentPY] = request.body;
      const stringifyData = JSON.stringify(existStudents)
      fs.writeFileSync(dataPath, stringifyData)
      res.send(`accounts with id ${studentPY} has been updated`)
    }, true);
  });

  //for deleting
app.delete('/students', jsonParser, (request, response) => {
    fs.readFile(dataPath, 'utf8', (err, data) => {
        const jsonData = fs.readFileSync(dataPath)
        var existStudents = JSON.parse(jsonData)
        const studentId = request.params['product'] && request.params['year'];
        delete existStudents[studentId]; 
        const stringifyData = JSON.stringify(existStudents)
        fs.writeFileSync(dataPath, stringifyData)
        result.send(`accounts with id ${studentId} has been deleted`)
    },  true);
  })
app.listen(port);
console.log('server listening on port 3000');