# Protocol Overview

MAVLink is a binary serialisation format and the reference library comes with convenience functions to make this serialization easy.

{% method %}
## Packet Serialization

My first method exposes how to print a message in JavaScript and Go.

{% sample lang="js" %}
Here is how to print a message to `stdout` using JavaScript.

```js
console.log('My first method');
```

{% sample lang="go" %}
Here is how to print a message to `stdout` using Go.

```go
fmt.Println("My first method")
```

{% common %}
Whatever language you are using, the resulting binary data will be the same:

```bash
0xFF 0xABC
```
{% endmethod %}
