# README.md: DNS over TLS proxy [PROJECT HILDA]

- Listens for DNS queries on port 53/tcp
- Uses Cloudflare 1.1.1.1 over TCP/TLS 1.3 to resolve requests.
- TODO: 
    - add support for IP filtering
    - get advertisers IP list
    - list => hashmap => smart filtering

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

<p style="text-align:center;"><a href="https://raw.githubusercontent.com/Shokodemon/python-dns-over-tls/master/workspace.png"><img src="https://raw.githubusercontent.com/Shokodemon/python-dns-over-tls/master/workspace.png" align="center" height="600" width="800" ></a><p>
