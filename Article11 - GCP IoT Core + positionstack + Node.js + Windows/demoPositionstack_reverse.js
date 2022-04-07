const axios = require('axios');
const params = {
  access_key: 'YOUR_ACCESS_KEY',
  query: '38.897675, -77.036547'
}
 
axios.get('http://api.positionstack.com/v1/reverse', {params})
  .then(response => {
    console.log(response.data);
  }).catch(error => {
    console.log(error);
  });