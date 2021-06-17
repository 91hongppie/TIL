const port = 3000,
    express = require("express"),
    homeController = require("./controllers/homeControllers"),
    errorController = require("./controllers/errorController"),
    layouts = require("express-ejs-layouts"),
    app = express();

app.use(layouts);
app.set("view engine", "ejs");

app.get('/name/:myName', homeController.respondWithName);


app.use(errorController.respondNoResouceFound);
app.use(errorController.respondInternalError);
app.listen(port, () => {
    console.log(`Server running on port: ${port}`)
})
