const MongoDB = require("mongodb").MongoClient, // 몽고DB 모듈의 요청
    dbURL = "mongodb://localhost:27017",
    dbName = "recipe_db";


MongoDB.connect(dbURL, (error, client) => { // 로컬 데이터베이스 서버 연결 설정
    if (error) throw error;
    let db = client.db(dbName); // 몽고DB 서버로의 recipe_db 데이터베이스 연결 취득
    db.collection("contacts")
        .insert( {
            name: "Freddi Mercury",
            email: "fred@queen.com"
        }, (error, db) => {
            if (error) throw error;
            console.log(db);
        })
    db.collection("contacts")
        .find()
        .toArray((error, data) => { // contacts 컬렉션 내 모든 레코드 찾기
            if (error) throw error;
            console.log(data);  // 콘솔에 결과 출력
        });
});