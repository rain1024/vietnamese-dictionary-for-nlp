Build Image

```
docker build -t service .
```

Run Image

```
docker run -p 8000:8000 -v ~/data/app:/app service
```