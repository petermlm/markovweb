import axios from 'axios'

let BaseUrl = process.env.NODE_ENV === 'production'
  ? 'https://pedromelgueira.com/markov/'
  : 'http://localhost:5000/'

function url (endpoint) {
  return BaseUrl + endpoint
}

export function requestPlainText (text, outputSize) {
  return new Promise(function (resolve, reject) {
    axios.post(url('plain_text'), {'text': text, 'output_size': outputSize})
      .then(response => {
        var resText = response['data']
        resolve(resText)
      })
      .catch(() => {
        reject()
      })
  })
}

export function requestReddit (text, outputSize) {
  return new Promise(function (resolve, reject) {
    axios.post(url('reddit'), {'username': text, 'output_size': outputSize})
      .then(response => {
        var resText = response['data']
        resolve(resText)
      })
      .catch(() => {
        reject()
      })
  })
}
