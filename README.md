# Domains-API

## Endpoints

## '/'
    Methods ['GET']
    Parameters [str:'domain']

    Example :
    localhost/?domain=noop.pt

    Output : 
    {
    "data": {
        "results": {
            "address": [
                "DomainsByProxy.com",
                "2155 E Warner Rd"
            ],
            "city": "Tempe",
            "country": "US",
            "creation_date": [
                "Sat, 27 Nov 1999 12:57:39 GMT",
                "Sat, 27 Nov 1999 07:57:39 GMT"
            ],
            "dnssec": "unsigned",
            "domain_name": [
                "NOOP.COM",
                "noop.com"
            ],
            "emails": "abuse@uniregistry.com",
            "expiration_date": [
                "Wed, 27 Nov 2030 12:57:38 GMT",
                "Wed, 27 Nov 2030 07:57:38 GMT"
            ],
            "name": "Registration Private",
            "name_servers": [
                "NS1.MYTRAFFICMANAGEMENT.COM",
                "NS2.MYTRAFFICMANAGEMENT.COM"
            ],
            "org": "Domains By Proxy, LLC",
            "referral_url": null,
            "registrant_postal_code": "85284",
            "registrar": "GoDaddy Online Services Cayman Islands Ltd.",
            "state": "Arizona",
            "status": [
                "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
                "clientRenewProhibited https://icann.org/epp#clientRenewProhibited",
                "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
                "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited"
            ],
            "updated_date": [
                "Thu, 13 Apr 2023 03:48:45 GMT",
                "Wed, 12 Apr 2023 22:48:45 GMT"
            ],
            "whois_server": "whois.uniregistrar.com"
        }
    },
    "is_available": false,
    "success": true
    }

# Docker 
## Usage 
```docker run -p 5000:5000 quanilo/domains-api:production```

## Development 
**After working on the project build docker with**   
    ```docker build -t [image_name]:[tagname] .  ```  
    ```docker push [image_name]:[tagname]```
