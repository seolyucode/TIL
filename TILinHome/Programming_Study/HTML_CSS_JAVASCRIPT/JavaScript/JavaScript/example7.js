function p() {
    return new Promise((resolve, reject) => {
        /* pending */
        setTimeout(() => {
            resolve();  /* fulfilled */
        }, 1000);
    });
}

p().then(() => {
    console.log('1000ms 후에 fulfilled 됩니다.');
});