const port = 3000,
    express = require("express"),
    homeController = require("./controllers/homeControllers"),
    layouts = require("express-ejs-layouts"),
    app = express();

app.use(layouts);
app.set("view engine", "ejs");

app.get('/name/:myName', homeController.respondWithName);
    

app.listen(port, () => {
    console.log(`Server running on port: ${port}`)
})
