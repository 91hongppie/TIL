const express = require("express"),
    app = express(),
    port = 3000,
    mongoose = require("mongoose"),
    admin = require("./admin");

mongoose.connect(`mongodb+srv://${admin.USERNAME}:${admin.PASSWORD}@boiler-plate.v1suj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`, {
    useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
}).then(() => console.log("MongoDB Connected..."))
  .catch(err => console.log(err));

app.get("/", (req, res) => res.send("Hello World!~~~~~안녕하세요"))

app.listen(port, () => console.log(`Example app listening on port: ${port}`));