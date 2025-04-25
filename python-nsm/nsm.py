import libnsm


class NSMUtil:
    def __init__(self):
        self.fd = libnsm.nsm_lib_init()

    def get_random(self, length: int) -> bytes:
        return libnsm.nsm_get_random(self.fd, length)

    def get_attestation_doc(self, user_data: bytes, nonce: bytes, public_key: bytes) -> bytes:
        result = libnsm.nsm_get_attestation_doc(
            self.fd,
            user_data,
            len(user_data),
            nonce,
            len(nonce),
            public_key,
            len(public_key),
        )
        return result
