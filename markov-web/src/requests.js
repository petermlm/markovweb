import axios from 'axios'

let BaseUrl = process.env.NODE_ENV === 'production'
  ? 'https://pedromelgueira.com/markov/'
  : 'http://localhost:5000/';


function url(endpoint) {
  return BaseUrl + endpoint
}

export function request_plain_text (text, output_size) {
  return new Promise (function (resolve, reject) {
    console.log(output_size);
    console.log(typeof(output_size));
    axios.post(url('plain_text'), {'text': text, 'output_size': output_size})
      .then(response => {
        var res_text = response['data']
        resolve(res_text);
      })
      .catch(() => {
        reject();
      })
  });
}

export function request_reddit (text, output_size) {
  return new Promise (function (resolve, reject) {
    axios.post(url('reddit'), {'username': text, 'output_size': output_size})
      .then(response => {
        var res_text = response['data']
        resolve(res_text);
      })
      .catch(() => {
        reject();
      })
  });
}
