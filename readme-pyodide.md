
```
python -m http.server
```

```
// example on how to run python and access variable from javascript
pyodide.runPython(`
    #import js
    products = [
    {
        "id": 1,
        "name": "new name 1",
        "price": 100,
        "votes": 2
    },
    {
        "id": 2,
        "name": "new name 2",
        "price": 300,
        "votes": 3
    }
    ]
`);

let products = pyodide.globals.get("products");
console.log('products from python is:');
console.log(products.toJs({ dict_converter: Object.fromEntries }));
```