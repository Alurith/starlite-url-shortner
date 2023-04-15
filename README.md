# Starlite URL Shortner
This is a demo project to test the [litestar framework](https://litestar.dev/).

| Packages  | Version |
| --------- | ------- |
| starlite  | 1.51.10 |
| uvicorn   | 0.21.1  |
| shortuuid | 1.0.11  |
| htmx      | 1.9.0   |
| picocss   | 1.5.9   |
## Run the project:
Rename ```proto.env``` to ```.env``` and set the ```REDIS_URL```

Run the project via 
```
starlite run --debug --reload
```

The ```docker-compose``` is just to start redis
