class Lock:
    def __init__(
        self,
        object_name: str,
        lock_name: str = "lock",
        timeout: int = -1,
        verbose: bool = False,
    ):
        self.object_name = object_name
        self.lock_name = lock_name
        self.timeout = timeout
        self.verbose = verbose
