# README.md: DNS over TLS proxy [PROJECT HILDA]

- Listens for DNS queries on port 53/tcp
- Uses Cloudflare 1.1.1.1 over TCP/TLS 1.3 to resolve requests.
- TODO: 
    - add support for IP filtering
    - get advertisers IP list
    - list from file => hashmap => efficient filtering

### APP VARS

using the .env file under ./

    - RESOLVER_HOSTNAME
    - RESOLVER_IP
    - RESOLVER_PORT
    - APP_BIND_HOST
    - APP_BIND_PORT
    - THREAD_TIMEOUT

## run // build // deploy

```
docker-compose up
```

## see if it works

```
watch dig +tcp @localhost example.com
```
& 


```
watch dig @localhost example.com
```
