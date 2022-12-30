const server = 'http://localhost:3000';
var product;
var price;
var year;
var gProduct = [];
var gPrice = [];
var gYear = [];

async function fetchStudents() {
    const url = server + '/students';
    const options = {
        method: 'GET',
        headers: {
            'Accept' : 'application/json'
        }
    }
    const response = await fetch(url, options);
    const students = await response.json();
    console.log(students)
    populateContent(students);
    var gLabels = ['2010', '2011', '2012', '2013', '2014', '2015','2016','2017','2018','2019','2020','2021','2022'];
    plotgraph(gLabels, students)
    populateCheckboxes(store(students))
}

async function editStudents() {
    const url = server + '/students';
    const options = {
        method: 'PUT',
        headers: {
            'Accept' : 'application/json'
        }
    }
    const response = await fetch(url, options);
    const students = await response.json();
    console.log(students)
}

function store(students){
    for (let i = 0; i < students.length; i++) { //loop used to store all items into the gProduct array without duplication
        if (students[i].product) { 
            if (gProduct.length == 0){
                gProduct.push(students[i].product)
            }
            else{
                for (let j = 0; j < gProduct.length; j++){
                    if (gProduct[j]==students[i].product){
                        j = gProduct.length - 1
                    }
                    else if (j+1 == gProduct.length && gProduct[j]!=students[i].product){
                        gProduct.push(students[i].product)
                    }
                }
            }
        }
    }
    return gProduct
}

async function deleteStudent() {
    const url = server + '/students';
    const options = {
        method: 'DELETE',
    }
    const response = await fetch(url, options);
    const students = await response.json();
    console.log(students)
}

function getDatasets(students){
    gProduct = store(students);
    var label = []
    for (let i = 0; i < gProduct.length; i++) {
        label.push("# of "+gProduct[i])
    }
    var data = []
    var dataChild = []
    for (let i = 0; i < gProduct.length; i++) {
        for (let k = 2010; k <= 2022; k++){
            let count = 0
            for (let j = 0; j < students.length; j++) {
                if(gProduct[i] == students[j].product && students[j].year == k){
                    gPrice.push(students[j].price)
                    gYear.push(students[j].year)
                    count = 20
                }
            }
            if(count != 20){
                gPrice.push(NaN)
                gYear.push(k.year-1)
            }
        }
        for (let p = 0; p < 13; p++){
            dataChild.push(parseInt(gPrice[p+(13*i)]))
        }
        data.push(dataChild)
        var dataChild = []
    }
    var backgroundColor = [['red'], ['blue'], ['green'], ['purple'], ['maroon'], ['fuchsia'], ['lime'], ['olive'], ['yellow'], ['navy'], ['teal'], ['aqua'], ['black']]
    var borderColor = backgroundColor
    var myList = []
    for (let j = 0; j < gProduct.length; j++){
        myList.push({label: label[j], data: data[j], backgroundColor: backgroundColor[j], borderColor: borderColor[j], borderWidth: 1})
    }
    return myList
}

const plotgraph = (gLabels, students) => {
    const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: gLabels,
        datasets: getDatasets(students)
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
}

async function addStudent() {
    const url = server + '/students';
    const student = {"product": product, "price": price, "year": year};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(student)
    }
    const response = await fetch(url, options);
}

function populateContent(students) {
    var table = document.getElementById('content');
    table.innerHTML = "<tr><th>Product</th><th>Price</th><th>Year</th></tr>";
    students.forEach(student => {
        var row = document.createElement('tr');
        var dataProduct = document.createElement('td');
        var textProduct = document.createTextNode(student.product);
        dataProduct.appendChild(textProduct);
        var dataPrice = document.createElement('td');
        var textPrice = document.createTextNode(student.price);
        dataPrice.appendChild(textPrice);
        var dataYear = document.createElement('td');
        var textYear = document.createTextNode(student.year);
        dataYear.appendChild(textYear);
        var edit1 = document.createElement('td');
        edit1.innerHTML = '<button onClick="onEdit(this)">EDIT</button>'
        var delete1 = document.createElement('td');
        delete1.innerHTML = '<button onClick="onDelete(this)">DELETE</button>'
        row.appendChild(dataProduct);
        row.appendChild(dataPrice);
        row.appendChild(dataYear);
        row.append(edit1)
        row.append(delete1)
        table.appendChild(row);
    });
}

//function populateCheckboxes(students) {
//    var list = []
//    var label = document.getElementById('cb');
//    for(let i = 0; i< students.length; i++) {
//        var row = document.createElement('tr');
//        var check = document.createElement('td');
//        check.innerHTML = "<input type=checkbox>"
//        var textCheck = document.createTextNode(students[i]);
//        check.appendChild(textCheck);
//        row.appendChild(check);
//        label.appendChild(row);
//    };
//}

document.querySelector('#add').addEventListener('click', (e) => {
    product = document.getElementById('product').value;
    product = product.toLowerCase();
    price = document.getElementById('price').value;
    year = document.getElementById('year').value;
    //conditions = (product && (price>0 && isNaN(price)==false) && (year>2009 && year<2023 && year==parseInt(year)) )
    if (true) { //conditions
        addStudent();
        fetchStudents();
        getDatasets(students);
        plotgraph();
    }
    e.preventDefault();
});

function onEdit(td){
    selectedRow = td.parentElement.parentElement;
    selectedRow.cells[0].innerHTML = document.getElementById('product').value;
    selectedRow.cells[1].innerHTML = document.getElementById('price').value;
    selectedRow.cells[2].innerHTML = document.getElementById('year').value;
}

function onDelete(td){
    if(confirm('Do you want to delete this record?')){
        row = td.parentElement.parentElement;
        document.getElementById('content').deleteRow(row.rowIndex); 
    }
    document.getElementById('product').value = '';
    document.getElementById('price').value = '';
    document.getElementById('year').value = '';
}