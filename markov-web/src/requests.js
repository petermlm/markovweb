import axios from 'axios'

let MarkovUrl = 'http://localhost:5000'

export function request (text) {
  return new Promise (function (resolve, reject) {
    if(process.env.NODE_ENV == 'development') {
      resolve(text);
      return;
    }

    axios.post(MarkovUrl, {'text': text})
      .then(response => {
        var res_text = response['data']
        resolve(res_text);
      })
      .catch(() => {
        reject();
      })
  });
}
