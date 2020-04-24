from addressing import addresser
from protobuf import user_pb2


class SupplyState(object):
    def __init__(self, context, timeout=2):
        self._context = context
        self._timeout = timeout

    def set_user(self, username, public_key):
        user_address = addresser.get_user_address(public_key)

        user = user_pb2.User(
            username=username,
            public_key=public_key
        )
        container = user_pb2.UserContainer()
        state_entries = self._context.get_state(
            addresses=[user_address],
            timeout=self._timeout
        )

        if state_entries:
            container.ParseFromString(state_entries[0].data)

        container.entries.extend([user])
        data = container.SerializeToString()

        updated_state ={}
        updated_state[user_address] = data
        self._context.set_state(updated_state, timeout=self._timeout)

    def get_user(self, public_key):
        user_address = addresser.get_user_address(public_key)
        state_entries = self._context.get_state(
            addresses=[user_address],
            timeout=self._timeout
        )
        if state_entries:
            container = user_pb2.UserContainer()
            container.ParseFromString(state_entries[0].data)
            for user in container.entries:
                if user.public_key == public_key:
                    return user
        return None
