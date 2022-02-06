const axios = require('axios');
const params = {
  access_key: 'afa4899f8e81f951909ef6227a3b4967',
  query: '1600 Pennsylvania Ave NW, Washington DC'
}

axios.get('http://api.positionstack.com/v1/forward', {params})
  .then(response => {
    console.log(response.data);
  }).catch(error => {
    console.log(error);
  });
