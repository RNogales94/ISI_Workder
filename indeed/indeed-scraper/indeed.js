const indeed = require('./lib/scraper.js');

const queryOptions = {
  query: '',
  city: 'Granada, España',
  radius: '25',
  level: '',
  jobType: 'fulltime',
  maxAge: '7',
  sort: 'date',
  limit: '100'
};

indeed.query(queryOptions).then(res => {
    console.log(res); // An array of Job objects
});
