
__all__ = ["Repository"]


class Repository(object):
    def __init__(self, cls):
        self.cls = cls

    def __enter__(self):
        super(Repository, self).__enter__()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        super(Repository, self).__exit__(exc_type, exc_value, exc_tb)
