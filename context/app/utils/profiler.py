import cProfile
import pstats
import contextlib


@contextlib.contextmanager
def profile():
    # Inspired by https://gist.github.com/davesque/6644474
    p = cProfile.Profile()

    p.enable()
    yield
    p.disable()

    stats = pstats.Stats(p).sort_stats('cumulative')
    stats.print_stats(r'context/app')
