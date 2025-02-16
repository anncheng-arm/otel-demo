# Prerequisite
1. Install Docker Engine
```
$ sudo apt install docker.io -y
```
2. Install standalone docker-compse
```
$ sudo curl -SL https://github.com/docker/compose/releases/download/v2.33.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```
```
$ sudo chmod +x /usr/local/bin/docker-compose

$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
3. Run docker without sudo
```
$ sudo usermod -aG docker $USER`
$ sudo systemctl restart docker`
$ newgrp docker
```

# Run/Stop Opentelemetry MicroServices Cheat Sheet
| **Command** | **Description** |
|------------|---------------|
| `docker-compose up -d` | **Run `docker-compose` in the background (detached mode)** |
| `docker-compose ps` | **Check running containers** |
| `docker-compose logs -f` | **View real-time logs of all containers** |
| `docker-compose logs -f otel-collector` | **View logs of a specific service (`otel-collector`)** |
| `docker-compose down` | **Stop and remove all containers** |
| `docker-compose stop` | **Stop containers without removing them** |
| `docker-compose restart` | **Restart all containers** |
| `docker-compose restart grafana` | **Restart a specific container (`grafana`)** |

* Prometheus: http://[server_ip]::9090/
* Grafana: http://[server_ip]::3000/ (default username/password: admin/admin)

# Run the BMC sensor reading demo
`python3 bmc_query_temp_otlp_demo.py`



