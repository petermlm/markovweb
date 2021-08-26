const PLAIN_TEXT = 0;
const REDDIT = 1;
var Current = {};

function make_url(url) {
  if(ENV == "PROD") {
    return BASE_URL + url;
  }
  return url;
}

function hide(element) {
  element.classList.add('hide');
}

function show(element) {
  element.classList.remove('hide');
}

function clear(event) {
  var store = window.sessionStorage;
  event.preventDefault();
  store.setItem('results', JSON.stringify([]));
  while(Current['results_table'].rows.length > 1) {
    Current['results_table'].deleteRow(-1);
  }
  hide(Current['results']);
  hide(Current['clear']);
}

function format_timestamp(ts) {
  dt = new Date(ts);
  return dt.toISOString()
}

function plain_text_submit(event) {
  event.preventDefault();
  var url = make_url('/plain_text');
  var data = {
    'text': Current['text'].value,
    'output_size': parseInt(Current['output_size'].value, 10),
  };
  request(url, data);
}

function reddit_submit(event) {
  event.preventDefault();
  var url = make_url('/reddit');
  var data = {
    'username': Current['text'].value,
    'output_size': parseInt(Current['output_size'].value, 10),
  };
  request(url, data);
}

function getStoredResults() {
  var store = window.sessionStorage;
  var stored_results = store.getItem('results');
  var results = [];
  if(stored_results != null) {
    results = JSON.parse(stored_results);
  }
  return results;
}

function writeAllResults() {
  results = getStoredResults();

  if(results.length == 0) {
    return;
  }

  var i = 1;
  results.forEach(element => {
    addRow(i, element)
    i++;
  });
}

function addRow(index, entry) {
  var row = Current['results_table'].insertRow(index);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  cell1.innerHTML = format_timestamp(entry['timestamp']);
  cell2.innerHTML = entry['text'];
  show(Current['results']);
  show(Current['clear']);
}

function addResultsEntry(new_text) {
  var store = window.sessionStorage;

  // Get stored results
  results = getStoredResults();

  // Remove entry from table and results if necessary
  while(results.length >= 11) {
    results.pop();
    Current['results_table'].deleteRow(-1);
  }

  entry = {
    'timestamp': Date.now(),
    'text': new_text,
  }

  // Add entry and store
  results = [entry].concat(results);
  store.setItem('results', JSON.stringify(results));

  // Display in table
  addRow(1, entry)
}

function request(url, data) {
  var xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
      addResultsEntry(this.responseText);
    }
  };

  xmlhttp.open("POST", url);
  xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlhttp.send(JSON.stringify(data));
}

function setCurrent() {
  var path = window.location.pathname;
  if(path.includes('reddit')) {
    Current['page'] = REDDIT;
  } else {
    Current['page'] = PLAIN_TEXT;
  }

  Current['text'] = document.querySelector('#text');
  Current['output_size'] = document.querySelector('#output_size');
  Current['results'] = document.querySelector('#results');
  Current['results_table'] = document.querySelector('#results table');
  Current['clear'] = document.querySelector('#btn-clear');
  Current['submit'] = document.querySelector('#btn-submit');

  writeAllResults();
}

function setActiveTab() {
  var ele = null;
  switch(Current['page']) {
    case PLAIN_TEXT:
      ele = document.querySelector('#nav-plain_text');
      break;
    case REDDIT:
      ele = document.querySelector('#nav-reddit');
      break;
  }
  ele.classList.add('active');
}

function setEvents() {
  Current['clear'].addEventListener('click', clear)

  switch(Current['page']) {
    case PLAIN_TEXT:
      Current['submit'].addEventListener('click', plain_text_submit)
      break;
    case REDDIT:
      Current['submit'].addEventListener('click', reddit_submit)
      break;
  }
}

window.onload = function() {
  setCurrent();
  setActiveTab();
  setEvents();
};
