function add(one, two) {
    if(one > 0 || two > 0) {
        console.log(one + two);
    }else {
        if(one > two) {
            console.log(one - two)
        }else {
            console.log(two - one)
        }
    }
}
add(-2, -1)