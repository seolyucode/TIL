class A {
    hello1() {
        console.log('hello1', this);
    }
    hello2 = () => {
        console.log('hello2', this);
    };
}

new A().hello1();
new A().hello2();