import axios from 'axios'

let BaseUrl = process.env.NODE_ENV === 'production'
  ? 'https://pedromelgueira.com/markov/'
  : 'http://localhost:5000/';


function url(endpoint) {
  return BaseUrl + endpoint
}

export function request_plain_text (text) {
  return new Promise (function (resolve, reject) {
    axios.post(url('plain_text'), {'text': text})
      .then(response => {
        var res_text = response['data']
        resolve(res_text);
      })
      .catch(() => {
        reject();
      })
  });
}

export function request_reddit (text) {
  return new Promise (function (resolve, reject) {
    axios.post(url('reddit'), {'username': text})
      .then(response => {
        var res_text = response['data']
        resolve(res_text);
      })
      .catch(() => {
        reject();
      })
  });
}
