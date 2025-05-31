class Lock:
    def __init__(
        self,
        object_name: str,
        lock_name: str = "lock",
    ):
        self.object_name = object_name
        self.lock_name = lock_name
