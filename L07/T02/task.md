Python scripts often work with data from the internet. One common way to get such data is the `requests` module. It allows a program to send an HTTP request to a server and receive a response object in return. For example, `requests.get(...)` sends a GET request to the given URL.

The returned response object contains useful information about the server reply. Its `status_code` attribute stores the HTTP status code, which shows whether the request was successful. For example, status code `200` usually means that the server processed the request correctly. The same response object also has a `text` attribute, which stores the response body as a string.

Other commonly used parts of `requests` are `requests.post(...)`, which sends data to a server, and `response.json()`, which converts a JSON response into Python data.

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
print(response.text)

api_response = requests.post("https://example.com/login", data={"name": "Alex"})
print(api_response.status_code)
```

### Working with hashes

Hashing is the process of turning data into a fixed-size value called a **hash**. The same input always produces the same hash, but even a small change in the input leads to a different result. Hashing is often used to compare data, check integrity, or work with sensitive information such as passwords without storing or sending the original text directly.

In Python, hashes can be created with the `hashlib` module. It contains several hashing algorithms, including SHA-1, which can be created with `hashlib.sha1(...)`.

Hashing functions work with bytes, not regular strings, so text usually has to be converted first. This can be done with `.encode('utf-8')`, which turns a string into a sequence of bytes using UTF-8 encoding. Other common encodings include UTF-16 and ASCII, but UTF-8 is the most widely used.

```python
text = "Hello!"
data = text.encode('utf-8')
print(data)
```

### Converting a hash to text

After a hash object is created, it can be converted into a readable hexadecimal string with `.hexdigest()`. This is useful when a program needs to compare or send the hash as text instead of working with the raw bytes.

Another common method is `.digest()`, which returns the raw bytes of the hash instead of a hexadecimal string. In practice, `.hexdigest()` is often more convenient when the result should be printed, stored, or compared as text.

```python
import hashlib

result = hashlib.sha1(b"data")
print(result.hexdigest())
print(result.digest())
```

Many hashing algorithms in `hashlib` are used in the same way. For example, `hashlib.md5(...)` and `hashlib.sha256(...)` also create hash objects, but they produce different hash values.

### Running the script with command-line arguments

To run this script, open the terminal in the bottom-left corner and pass one or more passwords as command-line arguments:

```bash
python L07/T02/task.py password123 qwerty M8#vQ2zLp7@Ks4
```

<img src="images/password.gif" width="800">

The script will check each password and print whether it was found in known data leaks.
