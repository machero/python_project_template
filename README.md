# python_project_template

Python 项目常用模块的模板集合，当前包含一个 Flask + Redis 的 Web 服务示例，可通过 Docker Compose 一键启动。

## 目录结构

```
.
├── python_web/            # Flask + Redis 示例
│   ├── app.py             # 应用入口
│   ├── requirements.txt   # 依赖
│   ├── Dockerfile         # 镜像构建
│   └── docker-compose.yml
├── .gitignore
├── .dockerignore
└── README.md
```

## 快速开始

### 使用 Docker Compose（推荐）

```bash
cd python_web
docker compose up --build
```

启动后访问 http://localhost:8000 ，页面会显示累计访问次数。

### 本地运行

```bash
cd python_web
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 需要本地可用的 Redis，默认连接 localhost:6379
python app.py
```

## 环境变量

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `REDIS_HOST` | `localhost` | Redis 地址 |
| `REDIS_PORT` | `6379` | Redis 端口 |
