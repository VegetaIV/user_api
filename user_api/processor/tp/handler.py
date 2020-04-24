from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction

from addressing import addresser
from protobuf import payload_pb2

from tp.payload import SupplyPayload
from tp.state import SupplyState


class SupplyHandler(TransactionHandler):

    @property
    def family_name(self):
        return addresser.FAMILY_NAME

    @property
    def family_versions(self):
        return [addresser.FAMILY_VERSION]

    @property
    def namespace(self):
        return [addresser.NAMESPACE]

    def apply(self, transaction, context):
        header = transaction.header
        payload = SupplyPayload(transaction.payload)
        state = SupplyState(context)

        if payload.action == payload_pb2.SimpleSupplyPayload.CREATE_USER:
            _create_user(
                state=state,
                public_key=header.signer_public_key,
                payload=payload
            )


def _create_user(state, public_key, payload):
    if state.get_user(public_key):
        raise InvalidTransaction('User with the public key {} already exists'.format(public_key))

    state.set_user(
        username=payload.data.username,
        public_key=public_key
    )
