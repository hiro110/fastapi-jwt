# fastapi-jwt
JWT Auth program to build MySQL and Fast API environment with DockerCompose

# How to
Create and Running
```
docker-compose up -d --build

docker exec -it db /bin/bash

# mysql login
mysql -u user -p

# run to docker/mysql/initdb.d/testdata.sql

```

# Demo
## Document of API
http://localhost:8000/docs


# Todo
モジュールの読み込みを環境によって振り分ける処理を実装しているが、廃止できないか検討したい
