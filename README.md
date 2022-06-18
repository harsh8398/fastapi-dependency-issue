# Running application
```sh
docker-compose up --build
```

# ApacheBench Command
```sh
ab -n 1000 -c 500 http://localhost:80/items
```

# Custom Configurations
```
GUNICORN WORKERS = 4
```
_Note: All other settings are default_

# Test #1

```sh
git checkout test#1
```

## Code for `get_db`
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Result
```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            80

Document Path:          /items
Document Length:        2 bytes

Concurrency Level:      500
Time taken for tests:   120.800 seconds
Complete requests:      1000
Failed requests:        139
   (Connect: 0, Receive: 0, Length: 139, Exceptions: 0)
Non-2xx responses:      139
Total transferred:      132672 bytes
HTML transferred:       4641 bytes
Requests per second:    8.28 [#/sec] (mean)
Time per request:       60399.853 [ms] (mean)
Time per request:       120.800 [ms] (mean, across all concurrent requests)
Transfer rate:          1.07 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    6   6.4      3      17
Processing:    11 25561 44981.3    600  120771
Waiting:        9 25560 44981.5    597  120771
Total:         27 25567 44978.8    604  120785

Percentage of the requests served within a certain time (ms)
  50%    604
  66%    882
  75%  30101
  80%  59858
  90%  120053
  95%  120597
  98%  120700
  99%  120752
 100%  120785 (longest request)
```

## Failed Requests Reason
```
api       |     raise exc.TimeoutError(
api       | sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30.00 (Background on this error at: https://sqlalche.me/e/14/3o7r)
```

# Test #2

```sh
git checkout test#2
```

## Code for `get_db`
```python
def get_db():
    with SessionLocal() as db:
        yield db
```

## Result
```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            80

Document Path:          /items
Document Length:        2 bytes

Concurrency Level:      500
Time taken for tests:   150.338 seconds
Complete requests:      1000
Failed requests:        176
   (Connect: 0, Receive: 0, Length: 176, Exceptions: 0)
Non-2xx responses:      176
Total transferred:      134448 bytes
HTML transferred:       5344 bytes
Requests per second:    6.65 [#/sec] (mean)
Time per request:       75169.209 [ms] (mean)
Time per request:       150.338 [ms] (mean, across all concurrent requests)
Transfer rate:          0.87 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    4   3.5      5       9
Processing:     3 29030 52551.7    457  150318
Waiting:        3 29029 52552.1    455  150318
Total:          3 29033 52550.4    463  150326

Percentage of the requests served within a certain time (ms)
  50%    463
  66%    684
  75%  30085
  80%  59782
  90%  149841
  95%  150044
  98%  150297
  99%  150309
 100%  150326 (longest request)
```

## Failed Requests Reason
```
api       |     raise exc.TimeoutError(
api       | sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30.00 (Background on this error at: https://sqlalche.me/e/14/3o7r)
```

# Test #3

```sh
git checkout test#3
```

## Code for GET `items`
```python
@app.get("/items", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100):
    with SessionLocal() as db:
        items = crud.get_items(db, skip=skip, limit=limit)
        return items
```

## Result
```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            80

Document Path:          /items
Document Length:        2 bytes

Concurrency Level:      500
Time taken for tests:   0.886 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      126000 bytes
HTML transferred:       2000 bytes
Requests per second:    1128.10 [#/sec] (mean)
Time per request:       443.224 [ms] (mean)
Time per request:       0.886 [ms] (mean, across all concurrent requests)
Transfer rate:          138.81 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    4   4.3      5      12
Processing:    22  371 195.3    300     863
Waiting:       10  360 198.0    277     863
Total:         22  376 196.7    300     872

Percentage of the requests served within a certain time (ms)
  50%    300
  66%    371
  75%    456
  80%    528
  90%    757
  95%    835
  98%    867
  99%    868
 100%    872 (longest request)
```

## Failed Requests Reason
0 failed requests