

if __name__ == "__main__":
    addressBook = {"David": {"address": "555 Home St", "phone": "4045551234", "email": "david@david.com"},
                   "Lucy": {"address": "555 Home St", "phone": "4045555678", "email": "lucy@lucy.com"},
                   "Dana": {"address": "123 Here Rd", "phone": "4045559101", "email": "dana@dana.net"}}
    print(addressBook["Lucy"])
    print(addressBook["Dana"]["email"])
