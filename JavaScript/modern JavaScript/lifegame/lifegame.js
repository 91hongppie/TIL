"use strict";
var state = Object.create(null); //    M: 생명 게임의 상태를 저장하는 객체
var view = Object.create(null); //     V: 상태를 그래픽으로 표시하는 객체
var controls = Object.create(null); // C: 컨트롤러 객체

window.onload = function() {
    readFile("./patterns.json", function(jsonObj, error) {
        if (error) {
            delete controls.pattern;
        } else {
            state.patterns = jsonObj;
        }
        createLifeGame(document.body, 78, 60, 780, 600);
    });
};

function readFile(filename, callback) {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            if (req.status == 200) {
                callback(req.response, false/* no error */);
            }
            else {
                callback(null, true/* error */);
            }
        }
    };
    req.open("GET", filename, true);
    req.responseType = "json";
    req.send(null);
}

function createLifeGame(parent, nx, ny, width, height) {
    var title = elt("h1", {class: "title"}, "Life Game");
    var viewpanel = view.create(nx, ny, width, height);
    state.create(nx, ny);
    var toolbar = elt("div", {class: "toolbar"});
    for (let name in controls) {
        toolbar.appendChild(controls[name](state));
    }
    parent.appendChild(elt("div", null, title, toolbar, viewpanel));
}

state.create = function(nx, ny) {
    state.nx = nx;
    state.ny = ny;
    state.cells = new Array(ny);
    for (var ix=0; ix<nx; ix++) {
        state.cells[ix] = new Array(ny);
        for (var iy=0; iy<ny; iy++) {
            state.cells[ix][iy] = 0
        }
    }
    document.addEventListener("clickview", function(e) {
        state.setLife(e.detail.ix, e.detail.iy, e.detail.life);
    }, false);

    state.changeCellEvent = document.createEvent("HTMLEvents");
    state.changeGenerationEvent = document.createEvent("HTMLEvents");
    state.generation = 0;
    state.tellGenerationChange(0);
    state.playing = false;
    state.timer = null;
};

state.tellCellChange = function(ix, iy, life) {
    state.changeCellEvent.initEvent("changecell", false, false);
    state.changeCellEvent.detail = {ix, iy, life};
    document.dispatchEvent(state.changeCellEvent);
}

state.tellGenerationChange = function(generation) {
    state.changeGenerationEvent.initEvent("changegeneration", false, false);
    state.changeGenerationEvent.detail = {generaion};
    document.dispatchEvent(state.changeGenerationEvent);

}

state.getSumAround = function(ix, iy) {
    var dx = [0, 1, 1, 1, 0, -1, -1, -1];
    var dy = [1, 1, 0, -1, -1, -1, 0, 1];

    for (var k=0, sum=0; k<dx.length; k++) {
        if (state.cells[(ix+dx[k]+state.nx)%state.nx][(iy+dy[k]+state.ny)%state.ny]) {
            sum++;
        }
    }
    return sum;
};