//function initBody() {
//    var PickActive = function() {
//        var cc = document.getElementById("tabList").children;
//        var i;
//        for (i = 0; i < cc.length; i++) {
//            cc[i].className = "";
//        }
//        this.handleEvent = function (event) {
//            event.srcElement.className = "active";
//            alert("HEHE");
//        }
//    };
//
//    var cc = document.getElementById("tabList").children;
//    for (i = 0; i < cc.length; i++) {
//        cc[i].addEventListener('click',PickActive, false);
//    }
//
//}

var currentNum = 0;

function initBody() {
    var PickActive = function (element) {
        this.handleEvent = function (event) {
            var cc = document.getElementById("tabList").children;
            var i;
            for (i = 0; i < cc.length; i++) {
                cc[i].className = "";
            }
            event.srcElement.parentElement.className = "active";

        }

        element.addEventListener('click', this, false);
    };

    var s = new PickActive(document.getElementById("tabList"));


    var SetMenuButton = function(element, num) {

        this.handleEvent = function(event) {
            currentNum = num;
            var j;
            for(j = 0; j < 5; j++) {
                document.getElementById("bb" + j).className = "dropdown-toggle";
            }
            document.getElementById("bb" + num).className = "dropdown-toggle pickedButton";
        }
        element.addEventListener('click', this, false);
    }

    var s0 = new SetMenuButton(document.getElementById("bb0"),0);
    var s1 = new SetMenuButton(document.getElementById("bb1"),1);
    var s2 = new SetMenuButton(document.getElementById("bb2"),2);
    var s3 = new SetMenuButton(document.getElementById("bb3"),3);
    var s4 = new SetMenuButton(document.getElementById("bb4"),4);


    // var App = React.createClass({
    //    render: function(){
    //        return(React.createElement("h1", null, "Hello, world!"));
    //    }
    // });

    var App = React.createClass({
        render: function(){
            return <div>
                <h1>Hello, world!</h1>
                <p>Some text</p>
            </div>;
        }
    });

    React.render(React.createElement(App), document.getElementById("theContent"));

}



