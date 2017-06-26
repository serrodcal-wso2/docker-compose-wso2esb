# docker-compose-wso2esb

Docker compose for CI in WSO2 ESB 5.0.0 using WireMock.

# Description

* Easy definition of services using WireMock.
* Start up WSO2 ESB 5.0.0 server deploying Carbon Aplications and mediators.
* OSGi Console enabled.
* Expose Web Admin Console of WSO2 ESB by port 9443.

# Usage

1. Clone this repo in your local.
2. Use internal script, `$ ./scripts/build.sh` at first. Next one uses `$ ./scripts/up.sh`.

Use `Ctrl + C` to stop docker-compose.

Check permission of scripts or make `$ chmod 755 *` in `scripts/` directory.

# Test integration

Run following request:

```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"sergio":"example"}' \
 'http://localhost:8280/echo/wiremock'
```
