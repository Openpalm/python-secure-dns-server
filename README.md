# README.md: DNS over TLS proxy

- Listens for DNS queries on port 53/tcp
- Uses Cloudflare 1.1.1.1 over TCP/TLS 1.3 to resolve requests.

### APP VARS

using the .env file under ./

    - RESOLVER_HOSTNAME
    - RESOLVER_IP
    - RESOLVER_PORT
    - APP_BIND_HOST
    - APP_BIND_PORT
    - THREAD_TIMEOUT

## security

- does not use DNSSEC. Resolved Addresses may be altered by privileged attacker.
- does not use blacklists/whitelists

## future-work

- Add Caching
- Add Proper logging
- Add Error handelling
- Add Sane tests

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
