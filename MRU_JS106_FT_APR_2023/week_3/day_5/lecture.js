let hello_timeout = setTimeout(sayHi, 1000, "Hello", "John"); //  calls sayHi() after one second --> Hello, John
hello_timeout.clearTimeout();
