const axios = require('axios')

axios.get('http://jsonplaceholder.typicode.com/posts123')
    .then(response => {
        console.log(response)
    })
    .catch(err => {
        console.log(err)
    })