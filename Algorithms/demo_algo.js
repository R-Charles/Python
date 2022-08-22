

function rotateStr(str, amnt) {
    var result = '';
    var num = amnt%str.length;
    result = str.slice(str.length-num, str.length) + str.slice(0, str.length-num);
    return result;
  }
  