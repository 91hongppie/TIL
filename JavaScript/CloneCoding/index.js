const title = document.querySelector("#title");

const CLICKED_CLASS = "clicked";

function handleClick() {
    title.classList.toggle(CLICKED_CLASS); // title의 클래스에 CLICKED_CLASS가 있는지 체크해서 없으면 add 있으면 remove
    // const hasClass = title.classList.contains(CLICKED_CLASS); // classList = 클래스 목록, contains(CLICKED_CLASS) = CLICKED_CLASS 포함하는지 확인
    // if (hasClass) {
    //     title.classList.remove(CLICKED_CLASS); // title의 클래스 목록에서 CLICKED_CLASS를 뺀다.
    // } else {
    //     title.classList.add(CLICKED_CLASS); // title의 클래스 목록에 CLICKED_CLASS를 더한다.
    // }
    
}

function init() {
    title.addEventListener("click", handleClick);
}
init()
