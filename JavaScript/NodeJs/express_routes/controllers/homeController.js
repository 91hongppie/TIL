const express = require("express");

exports.sendReqParam = (req, res) => {
    let veg = req.params.vegetable;
    res.send(`This is the page for ${veg}`);
}

exports.logRequestPaths = express.urlencoded({
    extended: false
})

exports.userSignUpProcessor = (req, res) => {
    console.log(req.params);
    console.log(req.body);
    console.log(req.body.firstname);
    console.log(req.body.lastname);
    res.send("POST Successful!!");
}