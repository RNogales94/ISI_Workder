const infojobs = require('infojobs')

const search = infojobs({
  id: 'cbbb268e3ae74f2b833efcf354c8eb62',
  secret: 'zUvMo29uTptnuw7mUTZ1OXnPSHEWnjCM9KG/JKWXK1CHl9Y2HB'
})

async t => {
  const res = await search()
    .offer({ q: 'java' })
    .run()

  t.deepEqual(res, require('./data/hola.json'))
}

const Busqueda=search()
  .offer({
    title: 'java',
    province: 'Madrid'
  })
  .run()
  .then( response => {
      console.log(response)
  }).catch(console.log)
