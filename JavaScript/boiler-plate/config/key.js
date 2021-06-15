/*
    process.env.NODE_ENV - local에서 하면 development로
    배포 된 상태에서는 production으로 나온다.
*/
if (process.env.NODE_ENV === 'production') {
    module.exports = require('./prod')
} else {
    module.exports = require('./dev')
}