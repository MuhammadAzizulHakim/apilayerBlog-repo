const axios = require('axios');
const params = {
  access_key: 'afa4899f8e81f951909ef6227a3b4967',
  query: '38.897675, -77.036547'
}

axios.get('http://api.positionstack.com/v1/reverse', {params})
  .then(response => {
    console.log(response.data);
  }).catch(error => {
    console.log(error);
  });
